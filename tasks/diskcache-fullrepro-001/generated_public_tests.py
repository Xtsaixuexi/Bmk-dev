from __future__ import annotations

import pickle
from io import BytesIO

import pytest

import diskcache as dc


def test_cache_set_get_mapping_membership(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.set("alpha", {"n": 1}) is True
    assert cache.get("alpha") == {"n": 1}
    assert cache["alpha"] == {"n": 1}
    assert "alpha" in cache
    assert list(cache) == ["alpha"]
    cache.close()


def test_cache_missing_defaults_and_key_errors(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.get("missing", default="fallback") == "fallback"
    with pytest.raises(KeyError):
        cache["missing"]
    with pytest.raises(KeyError):
        cache.read("missing")
    cache.close()


def test_cache_delete_and_delitem_remove_all_views(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache["key"] = "value"
    assert cache.delete("key") is True
    assert "key" not in cache
    assert cache.get("key") is None
    cache["key"] = "value"
    del cache["key"]
    assert cache.delete("key") is False
    cache.close()


def test_cache_add_only_inserts_missing_key(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.add("k", "first") is True
    assert cache.add("k", "second") is False
    assert cache.get("k") == "first"
    cache.close()


def test_cache_touch_extends_and_can_expire_entry(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.set("k", "v", expire=60)
    assert cache.touch("k", expire=None) is True
    value, expire_time = cache.get("k", expire_time=True)
    assert value == "v"
    assert expire_time is None
    assert cache.touch("k", expire=0) is True
    assert cache.get("k", default="gone") == "gone"
    cache.close()


def test_cache_incr_and_decr_create_and_update_values(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.incr("count") == 1
    assert cache.incr("count", delta=4) == 5
    assert cache.decr("count", delta=2) == 3
    assert cache.get("count") == 3
    with pytest.raises(KeyError):
        cache.incr("missing", default=None)
    cache.close()


def test_cache_file_like_value_round_trip(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.set("blob", BytesIO(b"payload"), read=True, tag="media")
    assert cache.get("blob") == b"payload"
    reader = cache.get("blob", read=True)
    assert reader.read() == b"payload"
    reader.close()
    reader = cache.read("blob")
    assert reader.read() == b"payload"
    reader.close()
    cache.close()


def test_cache_get_metadata_tuple_order(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.set("k", "v", expire=60, tag="tag-a")
    value, expire_time, tag = cache.get("k", expire_time=True, tag=True)
    assert value == "v"
    assert expire_time is not None
    assert tag == "tag-a"
    cache.close()


def test_cache_pop_returns_metadata_and_removes_entry(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache.set("k", "v", tag="tag-a")
    (value, expire_time, tag) = cache.pop("k", expire_time=True, tag=True)
    assert value == "v"
    assert expire_time is None
    assert tag == "tag-a"
    assert "k" not in cache
    assert cache.pop("k", default="missing") == "missing"
    cache.close()


def test_cache_expire_uses_strict_cutoff(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache.set("older", "value", expire=1)
    _, expire_time = cache.get("older", expire_time=True)
    assert cache.expire(now=expire_time) == 0
    assert cache.get("older") == "value"
    assert cache.expire(now=expire_time + 0.001) == 1
    assert cache.get("older", default="gone") == "gone"
    cache.close()


def test_cache_tag_evict_removes_only_matching_tag(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache.set("a", 1, tag="group")
    cache.set("b", 2, tag="other")
    assert cache.evict("group") == 1
    assert cache.get("a") is None
    assert cache.get("b") == 2
    cache.close()


def test_cache_clear_returns_removed_count(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    for number in range(4):
        cache.set(number, str(number))
    assert cache.clear() == 4
    assert len(cache) == 0
    cache.close()


def test_cache_stats_track_hits_and_misses_when_enabled(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache.set("a", 1)
    assert cache.stats(enable=True, reset=True) == (0, 0)
    assert cache.get("a") == 1
    assert cache.get("missing") is None
    assert cache.stats(reset=True) == (1, 1)
    assert cache.stats(enable=False) == (0, 0)
    cache.get("a")
    cache.get("missing")
    assert cache.stats() == (0, 0)
    cache.close()


def test_cache_length_counts_expired_entries_until_cleanup(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache.set("k", "v", expire=0)
    assert len(cache) == 1
    assert cache.expire() == 1
    assert len(cache) == 0
    cache.close()


def test_cache_push_generates_documented_integer_edges(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.push("a") == 500000000000000
    assert cache.push("b") == 500000000000001
    assert cache.push("front", side="front") == 499999999999999
    assert cache.pull() == (499999999999999, "front")
    assert cache.pull(side="back") == (500000000000001, "b")
    cache.close()


def test_cache_push_generates_prefixed_keys(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.push("one", prefix="jobs") == "jobs-500000000000000"
    assert cache.push("two", prefix="jobs") == "jobs-500000000000001"
    assert cache.push("zero", prefix="jobs", side="front") == "jobs-499999999999999"
    assert cache.pull(prefix="jobs") == ("jobs-499999999999999", "zero")
    cache.close()


def test_cache_peek_does_not_remove_queue_item(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    key = cache.push("item")
    assert cache.peek() == (key, "item")
    assert cache.peek() == (key, "item")
    assert cache.pull() == (key, "item")
    assert cache.peek(default=("none", None)) == ("none", None)
    cache.close()


def test_cache_pull_and_peek_skip_expired_queue_items(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    expired_key = cache.push("old", expire=0)
    live_key = cache.push("new")
    assert cache.peek() == (live_key, "new")
    assert cache.pull() == (live_key, "new")
    assert expired_key not in cache
    cache.close()


def test_cache_queue_metadata_tuple_shape(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    key = cache.push("value", tag="queued")
    pair, expire_time, tag = cache.peek(expire_time=True, tag=True)
    assert pair == (key, "value")
    assert expire_time is None
    assert tag == "queued"
    pair, tag = cache.pull(tag=True)
    assert pair == (key, "value")
    assert tag == "queued"
    cache.close()


def test_cache_peekitem_returns_first_and_last_pairs(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    cache["a"] = 1
    cache["b"] = 2
    assert cache.peekitem(last=False) == ("a", 1)
    assert cache.peekitem(last=True) == ("b", 2)
    cache.close()


def test_cache_iteration_and_reversed_key_order(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    for key in ["a", "b", "c"]:
        cache[key] = key.upper()
    assert list(cache) == ["a", "b", "c"]
    assert list(reversed(cache)) == ["c", "b", "a"]
    assert list(cache.iterkeys(reverse=True)) == ["c", "b", "a"]
    cache.close()


def test_cache_reset_updates_setting_and_attribute(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    assert cache.reset("size_limit", 1000) == 1000
    assert cache.size_limit == 1000
    assert cache.reset("size_limit") == 1000
    cache.close()


def test_cache_volume_includes_database_and_value_files(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    before = cache.volume()
    cache.set("large", b"x" * 10000)
    after = cache.volume()
    assert after >= before
    cache.close()


def test_cache_context_manager_and_pickle_reopen_same_directory(tmp_path):
    directory = tmp_path / "cache"
    with dc.Cache(directory) as cache:
        cache["answer"] = 42
        payload = pickle.dumps(cache)
    restored = pickle.loads(payload)
    assert restored.get("answer") == 42
    reopened = dc.Cache(directory)
    assert reopened["answer"] == 42
    restored.close()
    reopened.close()


def test_cache_memoize_caches_results_and_exposes_key(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    calls = {"count": 0}

    @cache.memoize(name="double")
    def double(value):
        calls["count"] += 1
        return value * 2

    assert double(5) == 10
    assert double(5) == 10
    assert calls["count"] == 1
    assert cache[double.__cache_key__(5)] == 10
    assert double.__wrapped__(5) == 10
    cache.close()


def test_cache_memoize_ignore_removes_arguments_from_cache_key(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    calls = {"count": 0}

    @cache.memoize(name="ignore-demo", ignore=("noise",))
    def compute(value, noise=None):
        calls["count"] += 1
        return value * 10

    assert compute(3, noise="a") == 30
    assert compute(3, noise="b") == 30
    assert calls["count"] == 1
    cache.close()


def test_cache_memoize_typed_separates_equal_values_by_type(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    calls = {"count": 0}

    @cache.memoize(name="typed-demo", typed=True)
    def identify(value):
        calls["count"] += 1
        return type(value).__name__

    assert identify(3) == "int"
    assert identify(3.0) == "float"
    assert identify(3) == "int"
    assert calls["count"] == 2
    cache.close()


def test_cache_memoize_rejects_bare_decorator_use(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    with pytest.raises(TypeError):
        cache.memoize(lambda: None)
    cache.close()


def test_jsondisk_round_trips_json_compatible_values(tmp_path):
    cache = dc.Cache(tmp_path / "cache", disk=dc.JSONDisk)
    value = {"items": [1, 2, 3], "ok": True}
    assert cache.set("payload", value)
    assert cache.get("payload") == value
    cache.close()


def test_fanout_set_get_delete_membership(tmp_path):
    cache = dc.FanoutCache(tmp_path / "fanout", shards=4)
    assert cache.set("alpha", 1)
    assert cache.get("alpha") == 1
    assert cache["alpha"] == 1
    assert "alpha" in cache
    assert cache.delete("alpha") is True
    assert cache.get("alpha") is None
    cache.close()


def test_fanout_add_touch_incr_decr(tmp_path):
    cache = dc.FanoutCache(tmp_path / "fanout", shards=4)
    assert cache.add("k", 10) is True
    assert cache.add("k", 20) is False
    assert cache.touch("k", expire=None) is True
    assert cache.incr("k", delta=5) == 15
    assert cache.decr("k", delta=3) == 12
    assert cache.get("k") == 12
    cache.close()


def test_fanout_pop_and_default_values(tmp_path):
    cache = dc.FanoutCache(tmp_path / "fanout", shards=4)
    cache.set("k", "v")
    assert cache.pop("k") == "v"
    assert cache.pop("k", default="missing") == "missing"
    cache.close()


def test_fanout_stats_accumulate_across_shards(tmp_path):
    cache = dc.FanoutCache(tmp_path / "fanout", shards=4)
    cache.set("a", 1)
    cache.stats(enable=True, reset=True)
    assert cache.get("a") == 1
    assert cache.get("missing") is None
    hits, misses = cache.stats(reset=True)
    assert hits == 1
    assert misses == 1
    cache.close()


def test_fanout_clear_and_iteration(tmp_path):
    cache = dc.FanoutCache(tmp_path / "fanout", shards=4)
    for number in range(8):
        cache[number] = number
    assert set(cache) == set(range(8))
    assert len(cache) == 8
    assert cache.clear() == 8
    assert len(cache) == 0
    cache.close()


def test_fanout_child_cache_reopens_named_state(tmp_path):
    fanout = dc.FanoutCache(tmp_path / "fanout", shards=4)
    child = fanout.cache("settings")
    child.set("theme", "dark")
    again = fanout.cache("settings")
    assert again.get("theme") == "dark"
    fanout.close()


def test_fanout_child_deque_reopens_named_state(tmp_path):
    fanout = dc.FanoutCache(tmp_path / "fanout", shards=4)
    jobs = fanout.deque("jobs")
    jobs.append("compile")
    jobs.appendleft("lint")
    assert list(fanout.deque("jobs")) == ["lint", "compile"]
    fanout.close()


def test_fanout_child_index_reopens_named_state(tmp_path):
    fanout = dc.FanoutCache(tmp_path / "fanout", shards=4)
    results = fanout.index("results")
    results["compile"] = "ok"
    assert fanout.index("results")["compile"] == "ok"
    fanout.close()


def test_fanout_transact_requires_retry_true(tmp_path):
    fanout = dc.FanoutCache(tmp_path / "fanout", shards=4)
    with pytest.raises(AssertionError):
        with fanout.transact(retry=False):
            pass
    with fanout.transact(retry=True):
        fanout.set("a", 1)
        fanout.set("b", 2)
    assert fanout.get("a") == 1
    assert fanout.get("b") == 2
    fanout.close()


def test_fanout_reset_updates_shard_settings(tmp_path):
    fanout = dc.FanoutCache(tmp_path / "fanout", shards=4)
    assert fanout.reset("size_limit", 2048) == 2048
    assert fanout.size_limit == 2048
    fanout.close()


def test_fanout_file_like_read_round_trip(tmp_path):
    fanout = dc.FanoutCache(tmp_path / "fanout", shards=4)
    assert fanout.set("blob", BytesIO(b"fanout-bytes"), read=True)
    reader = fanout.get("blob", read=True)
    assert reader.read() == b"fanout-bytes"
    reader.close()
    assert fanout.get("blob") == b"fanout-bytes"
    fanout.close()


def test_deque_initialization_and_iteration(tmp_path):
    deque = dc.Deque(["a", "b"], directory=tmp_path / "deque")
    assert list(deque) == ["a", "b"]
    assert len(deque) == 2
    assert list(reversed(deque)) == ["b", "a"]


def test_deque_append_appendleft_pop_popleft(tmp_path):
    deque = dc.Deque(directory=tmp_path / "deque")
    deque.append("right")
    deque.appendleft("left")
    assert deque.peekleft() == "left"
    assert deque.peek() == "right"
    assert deque.popleft() == "left"
    assert deque.pop() == "right"
    with pytest.raises(IndexError):
        deque.pop()


def test_deque_maxlen_discards_from_opposite_side(tmp_path):
    deque = dc.Deque(directory=tmp_path / "deque", maxlen=3)
    deque.extend([1, 2, 3, 4])
    assert list(deque) == [2, 3, 4]
    deque.appendleft(1)
    assert list(deque) == [1, 2, 3]


def test_deque_index_assignment_and_deletion(tmp_path):
    deque = dc.Deque(["a", "b", "c"], directory=tmp_path / "deque")
    assert deque[1] == "b"
    deque[1] = "B"
    assert list(deque) == ["a", "B", "c"]
    del deque[-1]
    assert list(deque) == ["a", "B"]
    with pytest.raises(IndexError):
        deque[10]


def test_deque_extendleft_reverse_and_rotate(tmp_path):
    deque = dc.Deque(directory=tmp_path / "deque")
    deque.extendleft(["a", "b", "c"])
    assert list(deque) == ["c", "b", "a"]
    deque.reverse()
    assert list(deque) == ["a", "b", "c"]
    deque.rotate(1)
    assert list(deque) == ["c", "a", "b"]
    deque.rotate(-1)
    assert list(deque) == ["a", "b", "c"]


def test_deque_count_remove_and_missing_value(tmp_path):
    deque = dc.Deque(["a", "b", "a"], directory=tmp_path / "deque")
    assert deque.count("a") == 2
    deque.remove("a")
    assert list(deque) == ["b", "a"]
    with pytest.raises(ValueError):
        deque.remove("missing")


def test_deque_persists_by_directory(tmp_path):
    directory = tmp_path / "deque"
    first = dc.Deque(["first"], directory=directory)
    first.append("second")
    second = dc.Deque(directory=directory)
    assert list(second) == ["first", "second"]


def test_deque_fromcache_uses_supplied_cache_state(tmp_path):
    cache = dc.Cache(tmp_path / "deque-cache", eviction_policy="none")
    deque = dc.Deque.fromcache(cache, ["x", "y"])
    assert list(deque) == ["x", "y"]
    again = dc.Deque.fromcache(cache)
    assert list(again) == ["x", "y"]
    cache.close()


def test_index_initialization_order_and_views(tmp_path):
    index = dc.Index(str(tmp_path / "index"))
    index.update([("a", 1), ("b", 2)])
    assert list(index) == ["a", "b"]
    assert list(index.items()) == [("a", 1), ("b", 2)]
    assert list(index.values()) == [1, 2]
    assert "a" in index.keys()


def test_index_setdefault_pop_and_key_errors(tmp_path):
    index = dc.Index(str(tmp_path / "index"))
    assert index.setdefault("a", 1) == 1
    assert index.setdefault("a", 2) == 1
    assert index.pop("a") == 1
    assert index.pop("a", default="missing") == "missing"
    with pytest.raises(KeyError):
        index.pop("a")


def test_index_popitem_first_and_last(tmp_path):
    index = dc.Index(str(tmp_path / "index"))
    index.update([("a", 1), ("b", 2), ("c", 3)])
    assert index.popitem(last=False) == ("a", 1)
    assert index.popitem(last=True) == ("c", 3)
    assert index.popitem() == ("b", 2)
    with pytest.raises(KeyError):
        index.popitem()


def test_index_push_pull_queue_behavior(tmp_path):
    index = dc.Index(str(tmp_path / "index"))
    assert index.push("a") == 500000000000000
    assert index.push("b") == 500000000000001
    assert index.push("zero", side="front") == 499999999999999
    assert index.pull() == (499999999999999, "zero")
    assert index.pull(side="back") == (500000000000001, "b")
    assert index.push("job", prefix="jobs") == "jobs-500000000000000"
    assert index.pull(prefix="jobs") == ("jobs-500000000000000", "job")


def test_index_memoize_caches_results(tmp_path):
    index = dc.Index(str(tmp_path / "index"))
    calls = {"count": 0}

    @index.memoize(name="square")
    def square(value):
        calls["count"] += 1
        return value * value

    assert square(6) == 36
    assert square(6) == 36
    assert calls["count"] == 1
    assert index[square.__cache_key__(6)] == 36


def test_index_persists_by_directory(tmp_path):
    directory = tmp_path / "index"
    first = dc.Index(str(directory))
    first["a"] = 1
    first["b"] = 2
    second = dc.Index(str(directory))
    assert list(second.items()) == [("a", 1), ("b", 2)]


def test_index_fromcache_uses_supplied_cache_state(tmp_path):
    cache = dc.Cache(tmp_path / "index-cache", eviction_policy="none")
    index = dc.Index.fromcache(cache, {"a": 1})
    assert index["a"] == 1
    again = dc.Index.fromcache(cache)
    assert again["a"] == 1
    cache.close()


def test_averager_tracks_average_and_pop_clears_state(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    avg = dc.Averager(cache, "latency")
    avg.add(2)
    avg.add(4)
    assert avg.get() == 3
    assert avg.pop() == 3
    assert avg.get() is None
    cache.close()


def test_lock_context_sets_and_releases_lock_key(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    lock = dc.Lock(cache, "lock-key")
    assert not lock.locked()
    with lock:
        assert lock.locked()
        assert "lock-key" in cache
    assert not lock.locked()
    cache.close()


def test_rlock_allows_nested_acquire_and_balanced_release(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    lock = dc.RLock(cache, "rlock-key")
    lock.acquire()
    lock.acquire()
    lock.release()
    lock.release()
    with lock:
        with lock:
            cache.set("inside-rlock", True)
    assert cache.get("inside-rlock") is True
    cache.close()


def test_bounded_semaphore_allows_acquire_release_within_bound(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    sem = dc.BoundedSemaphore(cache, "sem-key", value=2)
    sem.acquire()
    sem.acquire()
    sem.release()
    sem.release()
    sem.acquire()
    sem.release()
    cache.close()


def test_throttle_uses_sleep_until_capacity_is_available(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    state = {"now": 0.0, "sleep": [], "calls": 0}

    def time_func():
        return state["now"]

    def sleep_func(delay):
        state["sleep"].append(delay)
        state["now"] += delay

    @dc.throttle(cache, count=1, seconds=10, name="throttled", time_func=time_func, sleep_func=sleep_func)
    def work():
        state["calls"] += 1
        return state["calls"]

    assert work() == 1
    assert work() == 2
    assert state["calls"] == 2
    assert state["sleep"] and state["sleep"][0] == pytest.approx(10.0)
    cache.close()


def test_barrier_decorator_returns_function_result(tmp_path):
    cache = dc.Cache(tmp_path / "cache")

    @dc.barrier(cache, dc.Lock, name="barrier-key")
    def work(value):
        assert "barrier-key" in cache
        return value + 1

    assert work(4) == 5
    assert "barrier-key" not in cache
    cache.close()


def test_memoize_stampede_caches_result_and_exposes_key(tmp_path):
    cache = dc.Cache(tmp_path / "cache")
    calls = {"count": 0}

    @dc.memoize_stampede(cache, expire=60, name="stampede-demo")
    def work(value):
        calls["count"] += 1
        return value * 3

    assert work(7) == 21
    assert work(7) == 21
    assert calls["count"] == 1
    result, computation_time = cache[work.__cache_key__(7)]
    assert result == 21
    assert computation_time >= 0
    assert work.__wrapped__(7) == 21
    cache.close()


def test_public_constants_and_exports_are_available():
    assert "size_limit" in dc.DEFAULT_SETTINGS
    assert "none" in dc.EVICTION_POLICY
    assert dc.ENOVAL is not dc.UNKNOWN
    assert issubclass(dc.Timeout, Exception)
    assert issubclass(dc.UnknownFileWarning, Warning)
    assert issubclass(dc.EmptyDirWarning, Warning)
