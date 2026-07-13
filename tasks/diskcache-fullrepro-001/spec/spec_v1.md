<!-- INTERNAL
task_id: diskcache-fullrepro-001
spec_version: v1
delta: Initial developer-facing behavioral specification for DiskCache based on Stage 2 GitHub spec-writer workflow; recipe contracts corrected against reference behavior before Stage 3.
source_boundary: /root/autodl-tmp/new-e2e/grantjenks__python-diskcache/diskcache/__init__.py; diskcache/core.py; diskcache/fanout.py; diskcache/persistent.py; diskcache/recipes.py; diskcache/djangocache.py; README.rst; docs/tutorial.rst; docs/api.rst; tests/test_core.py; tests/test_fanout.py; tests/test_deque.py; tests/test_index.py; tests/test_recipes.py; tests/test_djangocache.py; GitHub workflow snapshot under wip/diskcache-fullrepro-001/github_alignment/raw_main
-->

# DiskCache Specification

## Product Overview

DiskCache is a pure-Python disk and file backed cache library. It provides a dictionary-like cache whose contents live in a directory, plus higher-level containers and synchronization helpers built on top of that persistent cache state. A cache must work safely across threads, and multiple cache objects that point at the same directory must observe the same stored entries.

DiskCache is designed for local storage. It uses the local filesystem and SQLite as persistence mechanisms, but callers interact with public Python objects such as `Cache`, `FanoutCache`, `Deque`, `Index`, and recipe helpers rather than with database tables or file layouts.

## Scope

This specification covers:

- Core `Cache` behavior for setting, reading, deleting, expiring, evicting, iterating, and inspecting cache entries.
- File-like values, tag metadata, expiration metadata, queue-like `push`/`pull`/`peek` operations, statistics, settings, and transactions.
- `FanoutCache` sharding behavior and its child `cache()`, `deque()`, and `index()` views.
- Persistent `Deque` and `Index` containers backed by cache directories.
- Public recipe helpers: `Averager`, `Lock`, `RLock`, `BoundedSemaphore`, `throttle`, `barrier`, and `memoize_stampede`.
- Optional `DjangoCache` compatibility behavior when Django is installed and configured.
- Public serialization hooks through `Disk` and `JSONDisk`.

The specification does not require any particular SQLite schema, file naming layout, trigger implementation, lock primitive, or internal class hierarchy.

## Installable Surface

The package import name is `diskcache`. The following names are part of the public import surface:

```python
from diskcache import (
    Averager,
    BoundedSemaphore,
    Cache,
    DEFAULT_SETTINGS,
    Deque,
    Disk,
    ENOVAL,
    EVICTION_POLICY,
    EmptyDirWarning,
    FanoutCache,
    Index,
    JSONDisk,
    Lock,
    RLock,
    Timeout,
    UNKNOWN,
    UnknownFileWarning,
    barrier,
    memoize_stampede,
    throttle,
)
```

`DjangoCache` is public when Django imports successfully:

```python
from diskcache import DjangoCache
```

The package exposes version metadata including `__title__`, `__version__`, `__build__`, `__author__`, `__license__`, and `__copyright__`.

## Product State Model

DiskCache's core state is a collection of cache entries in a directory. Each entry has a key, a value, optional expiration time, optional tag metadata, and accounting metadata used for size, statistics, and eviction. Values are observable only through the public API; the implementation is free to store them in metadata, separate files, or another local representation that preserves the same behavior.

The same state has these public projections:

- A mapping projection: `cache[key]`, `key in cache`, `len(cache)`, `iter(cache)`, `reversed(cache)`, and `del cache[key]`.
- A method projection: `set`, `get`, `add`, `touch`, `pop`, `delete`, `incr`, `decr`, `expire`, `evict`, `cull`, `clear`, `stats`, `volume`, and `reset`.
- Container projections: `Deque`, `Index`, and child objects returned by `FanoutCache.cache()`, `FanoutCache.deque()`, and `FanoutCache.index()`.
- Metadata projections: tag, expiration time, settings, hit/miss statistics, and approximate volume.

State invariants:

- A value written through `Cache.set()` or `cache[key] = value` must be returned by `Cache.get()` and `cache[key]` for the same key while the entry is present and unexpired.
- Deleting an entry through `delete()`, `pop()`, or `del cache[key]` must remove it from membership tests, mapping access, and method access.
- Entries written by one `Cache` object must be visible to another `Cache` object opened on the same directory after the write succeeds.
- Tag and expiration metadata returned by `get(..., expire_time=True, tag=True)` or `pop(..., expire_time=True, tag=True)` must describe the same entry value returned by the operation.
- A `FanoutCache` must route all operations for a particular key to a stable shard so that set/get/delete/incr/decr operations agree for that key.
- `Deque` and `Index` objects opened on an existing directory must observe the persistent contents previously written to that directory.

## Public API

### Cache

```python
Cache(directory=None, timeout=60, disk=Disk, **settings)
```

A `Cache` represents one local cache directory. When `directory` is omitted, the object must create and use a temporary directory. When a path is supplied and it does not exist, initialization must create it. The `directory` property returns the cache directory as a string path. `close()` releases open resources. Closing an already closed cache must be harmless, and a closed cache must reopen itself when a later operation needs access.

`Cache` supports context-manager use. Entering returns the cache; exiting must close it. Cache objects must be pickleable enough that the unpickled object refers to the same directory and must reopen its resources on later access.

Mapping operations:

```python
cache[key] = value
value = cache[key]
del cache[key]
key in cache
len(cache)
iter(cache)
reversed(cache)
```

- `cache[key] = value` must store the value without expiration metadata and must behave like `set(key, value)` for public retrieval.
- `cache[key]` must return the stored value when the key is present and unexpired; it must raise `KeyError` when the key is missing or expired.
- `del cache[key]` must remove the key and must raise `KeyError` when the key is missing.
- `key in cache` returns `True` only when the key is present and unexpired.
- `len(cache)` returns the cache's stored count before explicit expiration cleanup; expired entries remain eligible to be counted until `expire()` or a writing operation removes them.
- Iteration returns keys in the cache's stored key order. `iterkeys(reverse=True)` and `reversed(cache)` return the reverse key order.

Core methods:

```python
set(key, value, expire=None, read=False, tag=None, retry=False) -> bool
touch(key, expire=None, retry=False) -> bool
add(key, value, expire=None, read=False, tag=None, retry=False) -> bool
get(key, default=None, read=False, expire_time=False, tag=False, retry=False)
read(key, retry=False)
pop(key, default=None, expire_time=False, tag=False, retry=False)
delete(key, retry=False) -> bool
incr(key, delta=1, default=0, retry=False)
decr(key, delta=1, default=0, retry=False)
```

- `set()` must store or replace a key and return `True` when the write succeeds. `expire` is a relative lifetime in seconds; `None` means the entry does not expire. `tag` stores caller-provided metadata. When `read=True`, `value` is a file-like object and the cache must store the bytes read from it.
- `touch()` must update the expiration time of an existing key and return `True`; it must return `False` when the key is absent.
- `add()` must store the value only when the key is not already present. It returns `True` when it inserts and `False` when the key already exists.
- `get()` must return `default` when the key is missing or expired. With `read=True`, the returned value must be a readable file-like object for file-backed content. With `expire_time=True` and/or `tag=True`, the return value must be a tuple beginning with the value and followed by the requested metadata in that order.
- `read()` must return a readable file-like object for a present key and must raise `KeyError` when the key is missing or expired.
- `pop()` must atomically remove a key and return its value, or `default` when the key is missing. With metadata flags, it must return the same tuple shape as `get()` and then remove the entry.
- `delete()` must remove a key and return `True` when an entry was removed; it must return `False` when the key was missing.
- `incr()` and `decr()` must atomically add or subtract numeric deltas. When the key is missing and `default` is not `None`, the operation must create the key using `default + delta` for `incr()` or `default - delta` for `decr()`. When the key is missing and `default is None`, the operation must raise `KeyError`.

Queue methods:

```python
push(value, prefix=None, side="back", expire=None, read=False, tag=None, retry=False) -> key
pull(prefix=None, default=(None, None), side="front", expire_time=False, tag=False, retry=False)
peek(prefix=None, default=(None, None), side="front", expire_time=False, tag=False, retry=False)
peekitem(last=True, expire_time=False, tag=False, retry=False)
```

`push()` stores a value under a generated integer-like key, optionally namespaced by `prefix`. Without a prefix, queue keys are integers between `0` and `999999999999999`; with a prefix, queue keys are strings formatted as `"prefix-000000000000000"` through `"prefix-999999999999999"`. A new empty queue starts at `500000000000000`. Back pushes choose one greater than the current largest key in the queue; front pushes choose one less than the current smallest key. Existing gaps are not filled unless they are at the selected edge. `side` must be `"back"` or `"front"`; invalid side names raise `KeyError` from the side lookup.

`pull()` removes and returns a `(key, value)` pair from the front or back side. `peek()` returns the same pair without removing it. Expired queue items must be deleted and skipped while searching for a returnable item. If the selected value file disappears before it is fetched, `pull()` and `peek()` must continue searching rather than returning a broken value. When no item is available, `pull()` and `peek()` return `default`. With `expire_time=True` and/or `tag=True`, the returned shape is `((key, value), expire_time, tag)` or the corresponding shorter metadata tuple. `peekitem(last=True)` returns the last key/value pair; `last=False` returns the first pair. Missing items must return the requested default or raise `KeyError` according to the method's documented mapping semantics.

Maintenance and metadata methods:

```python
expire(now=None, retry=False) -> int
evict(tag, retry=False) -> int
cull(retry=False) -> int
clear(retry=False) -> int
create_tag_index() -> None
drop_tag_index() -> None
stats(enable=True, reset=False) -> tuple[int, int]
volume() -> int
check(fix=False, retry=False) -> list
reset(key, value=ENOVAL, update=True)
transact(retry=False)
memoize(name=None, typed=False, expire=None, tag=None, ignore=())
```

- `expire()` removes expired keys and returns the number removed. `now` supplies an absolute timestamp cutoff when provided. An entry is expired for this method when its expiration time is not `None`, is greater than zero, and is strictly less than `now`. Entries whose expiration time equals `now` remain until a later cutoff.
- `evict(tag)` removes keys whose tag equals `tag` and returns the number removed.
- `cull()` first removes expired items and then removes entries according to the configured eviction policy until the cache is under its size limit or no more culling is required.
- `clear()` removes all cache entries and returns the number removed.
- `create_tag_index()` and `drop_tag_index()` change whether tag eviction is indexed; the observable `tag_index` setting must reflect the change.
- `stats(enable=True, reset=False)` returns `(hits, misses)`. When enabled, successful and failed reads must update those counters. `reset=True` must reset the returned counters after reading them. Disabled statistics must not accumulate new read counts.
- `volume()` returns the approximate total size of the metadata database plus files that hold values; it does not need to include filesystem directory metadata.
- `check()` returns warnings or integrity findings and must not corrupt valid entries. With `fix=True`, it is allowed to remove orphaned or inconsistent cache artifacts when doing so restores public cache consistency; it must not remove entries that remain valid through public cache operations.
- `reset()` with both key and value must update a setting; with only key it must return the current database setting and refresh the matching public attribute. Settings in `DEFAULT_SETTINGS` are public settings. Keys with `disk_` prefix map to the associated `Disk` object's unprefixed attributes such as `min_file_size` and `pickle_protocol`. Keys with `sqlite_` prefix map to SQLite pragmas after removing the prefix. Arbitrary setting names outside these public setting families are not part of the durable settings contract.
- `transact()` is a context manager. Operations inside it must be committed atomically. Nested transactions must be allowed. While a transaction is active, concurrent writes are allowed to block until it exits.
- `memoize()` returns a decorator. Calling the decorated function with the same effective arguments must reuse a cached return value until expiration. The cache key is a tuple made from the explicit `name` or fully qualified function name, positional arguments not ignored by index, a `None` separator, sorted keyword pairs not ignored by name, and, when `typed=True`, the argument value types. `ignore` entries remove positional indexes or keyword names from that key. The wrapper must expose `__wrapped__` and `__cache_key__(*args, **kwargs)`. `tag` and `expire` are applied to stored results.

### FanoutCache

```python
FanoutCache(directory=None, shards=8, timeout=0.01, disk=Disk, **settings)
```

`FanoutCache` spreads keys across multiple `Cache` shards under one directory. It supports the same main key/value methods as `Cache`: `set`, item assignment, `touch`, `add`, `incr`, `decr`, `get`, item access, `read`, membership, `pop`, `delete`, item deletion, `expire`, tag index management, `evict`, `cull`, `clear`, `stats`, `volume`, `close`, iteration, reverse iteration, length, and `reset`.

`FanoutCache.transact(retry=True)` is a context manager that acquires transactions on all shards and blocks until they are held. The method must require `retry=True`; calling it with `retry=False` must fail with an assertion error. While the context is active, writes through the fanout cache are covered by the shard transactions. A caller needing a single named transactional store must request a child `Cache` view with `cache(name)`.

Timeout behavior is different from `Cache`: `FanoutCache` methods that write through a shard must return the documented failure value on timeout when `retry=False`, such as `False`, `0`, an empty warning list, or the caller's default. With `retry=True`, they must retry through the underlying shard operation. Item assignment, item access, and item deletion call the corresponding fanout method with `retry=True`.

Child views:

```python
cache(name, timeout=60, disk=None, **settings) -> Cache
deque(name, maxlen=None) -> Deque
index(name) -> Index
```

These methods return persistent child objects stored below the fanout directory. The same child name must reopen the same child state across calls and across processes.

### Deque

```python
Deque(iterable=(), directory=None, maxlen=None)
Deque.fromcache(cache, iterable=(), maxlen=None)
```

`Deque` provides a persistent double-ended queue compatible with the main behavior of `collections.deque`. It supports indexing, assignment, deletion, iteration, reverse iteration, `append`, `appendleft`, `clear`, `copy`, `count`, `extend`, `extendleft`, `peek`, `peekleft`, `pop`, `popleft`, `remove`, `reverse`, `rotate`, and `transact`.

- A deque initialized with an iterable must contain those items in order.
- A deque initialized with `maxlen` must keep at most that many items; appending beyond `maxlen` must discard items from the opposite side as Python's `collections.deque` does.
- `pop()` and `popleft()` must remove and return values from the right and left side respectively; they must raise `IndexError` when the deque is empty.
- `peek()` and `peekleft()` must return the rightmost or leftmost value without removing it; they must raise `IndexError` when the deque is empty.
- Opening `Deque(directory=existing_directory)` must observe the persistent contents already stored in that directory.
- `Deque` entries must not expire or be evicted by normal cache eviction policy.

### Index

```python
Index(*args, **kwargs)
Index.fromcache(cache, *args, **kwargs)
```

`Index` provides a persistent mutable mapping with ordered-dictionary behavior. It supports item access, assignment, deletion, membership, iteration, reverse iteration, `keys`, `values`, `items`, `setdefault`, `peekitem`, `pop`, `popitem`, `push`, `pull`, `clear`, `memoize`, and `transact`.

- Initialization from a mapping or iterable of pairs must store those key/value pairs.
- `index[key]` must return the stored value or raise `KeyError` when missing.
- `pop(key)` must remove and return the key's value. If the key is missing and no default is supplied, it must raise `KeyError`; with a default, it must return that default.
- `popitem(last=True)` removes and returns the last key/value pair; `last=False` removes and returns the first pair. It must raise `KeyError` when empty.
- Opening `Index(existing_directory)` must observe the persistent contents already stored in that directory.
- `Index` entries must not expire or be evicted by normal cache eviction policy.

### Disk and JSONDisk

```python
Disk(directory, min_file_size=0, pickle_protocol=0)
JSONDisk(directory, compress_level=1, **kwargs)
```

`Disk` controls serialization for keys and values. Keys are always stored in cache metadata. Values are stored and returned according to public serialization behavior; the implementation is free to choose metadata or separate-file storage based on size and `read` mode. Native key/value types include integers, floats, strings, and bytes; other data types are serialized. Cache lookup uses the serialized form, not Python's `hash()` protocol. Equal Python objects whose serialized forms differ are allowed to be distinct cache keys.

A custom `Disk` subclass is allowed to override serialization methods. All clients sharing a cache directory must use compatible serialization. `JSONDisk` serializes JSON-compatible values using compressed JSON and is suitable when callers need more consistent cross-process key serialization for JSON data.

### Recipes

`Averager(cache, key, expire=None, tag=None)` maintains a running average in a cache. `add(value)` records a value in the stored total/count state. `get()` returns the current average or `None` when no values have been recorded. `pop()` returns the current average and clears the stored total/count state.

`Lock(cache, key, expire=None, tag=None)` provides a non-reentrant cache-backed lock. `acquire()` blocks until it acquires the lock, `release()` releases it by deleting the lock key, `locked()` reports whether it is held, and context-manager use must acquire on entry and release on exit. Calling `release()` while the lock key is absent must leave the cache unlocked.

`RLock(cache, key, expire=None, tag=None)` provides a reentrant lock for repeated acquisition by the same execution context. Context-manager use must balance acquisition and release.

`BoundedSemaphore(cache, key, value=1, expire=None, tag=None)` provides a cache-backed semaphore. `acquire()` must decrement available capacity or wait until capacity exists. `release()` must increment capacity and must not allow the counter to exceed the initial bound.

`throttle(cache, count, seconds, name=None, expire=None, tag=None, time_func=time.time, sleep_func=time.sleep)` returns a decorator that limits calls to at most `count` executions per `seconds` window for the decorated function identity or `name`.

`barrier(cache, lock_factory, name=None, expire=None, tag=None)` returns a decorator that serializes calls using locks created by `lock_factory`.

`memoize_stampede(cache, expire, name=None, typed=False, tag=None, beta=1, ignore=())` returns a decorator that caches function return values together with the time taken to compute them. A cache hit returns the stored result. Before expiration, the wrapper must probabilistically decide whether to trigger early recomputation using the stored computation time, remaining TTL, and `beta`; when early recomputation is triggered, at most one caller must start a background recomputation marker for that cache key while all callers continue receiving the old result. A cache miss computes synchronously, stores `(result, computation_time)` with `expire` and `tag`, and returns the result. The wrapper must expose `__wrapped__` and `__cache_key__(*args, **kwargs)`. It must use the same effective argument-key semantics as cache memoization for `name`, `typed`, and `ignore`.

### DjangoCache

When Django is installed, `DjangoCache(directory, params)` provides a Django-compatible cache backend built on `FanoutCache`. It supports Django-style `add`, `get`, `set`, `touch`, `pop`, `delete`, `incr`, `decr`, `has_key`, `get_or_set`, versioned keys, timeout conversion, `clear`, `close`, and the DiskCache-specific helper views `cache()`, `deque()`, `index()`, and `memoize()`.

Django-style timeouts must follow Django cache conventions: default timeout uses the backend default, `None` stores without expiration, and zero or negative timeout makes the value immediately unavailable. Version parameters must create distinct logical keys. Methods whose Django contract returns booleans or defaults must return those values rather than exposing shard timeouts.

## Error Semantics

- `Timeout` is raised by `Cache` operations when a database transaction cannot be obtained within the configured timeout and `retry=False`. With `retry=True`, cache transaction acquisition must keep retrying until it succeeds. For iterative removals such as `expire()`, `cull()`, and `clear()`, a `Timeout` must carry the number of items removed before failure as its first argument. `FanoutCache` and `DjangoCache` ordinary write methods must avoid raising `Timeout` for documented retrying or silent-failure operations.
- `cache[key]`, `read()`, `del cache[key]`, `Deque.pop()`, `Deque.popleft()`, `Deque.peek()`, `Deque.peekleft()`, `Index.__getitem__()`, `Index.pop()` without a default, and `Index.popitem()` must raise the standard missing/empty exception (`KeyError` or `IndexError`) when their precondition is not satisfied.
- `incr()` and `decr()` must raise `KeyError` when the key is missing and `default is None`.
- Invalid cache directories, unwritable directories, invalid disk configuration, SQLite operational failures, or full disks must raise the relevant Python filesystem or `sqlite3.OperationalError` exceptions from the operation that detects the failure.
- `memoize` methods must be called as decorators. Passing a callable directly where a decorator option is expected must raise `TypeError` rather than silently wrapping it with ambiguous semantics.
- Arbitrary setting names outside `DEFAULT_SETTINGS`, `disk_` attributes, and `sqlite_` pragmas are outside the public settings contract.
- `UnknownFileWarning` and `EmptyDirWarning` are warning classes for cache integrity checks involving unexpected files or empty directories.

## Cross-View Invariants

- A key stored with `cache[key] = value` must be visible through `cache.get(key)`, `key in cache`, and iteration until it is deleted or expired.
- A key removed through `delete(key)` must be absent from `key in cache`, `cache.get(key, default)`, and `cache[key]`.
- A value stored with `read=True` must be retrievable as bytes through ordinary value access and as a readable object through `get(..., read=True)` or `read()`.
- An entry stored with `tag=t` must be removed by `evict(t)` and must not be removed by `evict(other_tag)`.
- A key with expiration metadata must remain available before expiration and must become unavailable through membership and `get()` after expiration cleanup or an operation observes it as expired.
- Statistics returned by `stats()` must reflect the same successful and failed reads observed through `get()` and item access while statistics are enabled.
- `FanoutCache.get(key)` must return values written by `FanoutCache.set(key, value)` for the same key regardless of the shard chosen internally.
- `FanoutCache.cache(name)`, `FanoutCache.deque(name)`, and `FanoutCache.index(name)` must reopen persistent child state when called again with the same name.
- `Deque(directory=d)` must see the same sequence previously written by another `Deque` using directory `d`.
- `Index(directory)` or `Index(existing_directory)` must see the same mapping previously written by another `Index` using that directory.
- `Cache.volume()` must change in the same direction as public writes and removals for sufficiently large values, even though exact byte accounting is approximate.
- `reset(setting, value)` must update both the durable setting and the matching public attribute visible from compatible cache objects.

## Representative Workflows

### Persistent Cache Lifecycle

```python
from io import BytesIO
from diskcache import Cache

with Cache() as cache:
    assert cache.set("avatar", BytesIO(b"image-bytes"), read=True, tag="media")
    reader, expire_time, tag = cache.get("avatar", read=True, expire_time=True, tag=True)
    assert reader.read() == b"image-bytes"
    assert tag == "media"
    assert expire_time is None
    assert "avatar" in cache
    assert cache.evict("media") == 1
    assert cache.get("avatar") is None
```

The stored value, tag metadata, membership check, file-like read path, and tag eviction all describe the same cache entry.

### Shared Persistent Container State

```python
from diskcache import Deque, Index

queue = Deque(["first", "second"])
queue.appendleft("zero")
again = Deque(directory=queue.directory)
assert list(again) == ["zero", "first", "second"]
assert again.popleft() == "zero"

index = Index([("a", 1)])
index["b"] = 2
same_index = Index(index.directory)
assert list(same_index.items()) == [("a", 1), ("b", 2)]
```

Both containers persist their public state through their directories.

### Fanout Child Views

```python
from diskcache import FanoutCache

fanout = FanoutCache(shards=4)
fanout.set("answer", 42)
assert fanout.get("answer") == 42

jobs = fanout.deque("jobs")
jobs.append("compile")
assert fanout.deque("jobs").pop() == "compile"

results = fanout.index("results")
results["compile"] = "ok"
assert fanout.index("results")["compile"] == "ok"
```

The parent fanout cache and named child views must preserve state across repeated access.

## Non-Goals

- The public contract does not require a specific SQLite schema, trigger design, SQL query text, file naming algorithm, or internal directory layout.
- The public contract does not require private attributes such as internal disk objects, SQL connections, shard lists, or local thread state.
- Exact `repr()` strings are not part of the behavioral contract except where Python container conventions require a standard exception or value behavior.
- Benchmark, stress, plotting, and performance report scripts are not part of the installable library contract.
- Network filesystem performance, NFS locking behavior, and asynchronous SQLite integration are outside the required behavior.
- A reimplementation does not need to match undocumented warning message wording or exception message text.
- Optional Django behavior is required only when Django is installed and the backend is configured through Django-compatible settings.

## Evaluation Notes

Evaluation focuses on public behavior across atomic API calls, integration between cache state and metadata views, and end-to-end workflows that reopen or project the same persistent state through multiple public surfaces. Tests exercise cache lifecycle operations, file-like values, expiration and tag behavior, statistics, settings, fanout sharding behavior, persistent `Deque` and `Index` state, recipe helpers, and optional Django compatibility when the environment provides Django.

The scoring suite is expected to use only public imports and observable outcomes. It must not require a specific SQLite schema, private attributes, internal helper names, exact SQL, exact file names, or exact exception message text. Implementations are judged by whether their public behavior matches the contract above in a clean environment.
