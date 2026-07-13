# Spec Test Map: diskcache-fullrepro-001

oracle_source: generated_only
source_file: filter/oracle_repo/tests/test_generated_diskcache.py
authority: GitHub accelerated snapshot `github_alignment/raw_main/skills/test-filter/SKILL.md`

| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `tests/test_generated_diskcache.py::test_cache_set_get_mapping_membership` | atomic | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_missing_defaults_and_key_errors` | atomic | Cache + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_delete_and_delitem_remove_all_views` | atomic | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_add_only_inserts_missing_key` | atomic | Cache + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_touch_extends_and_can_expire_entry` | atomic | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_incr_and_decr_create_and_update_values` | atomic | Cache + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_file_like_value_round_trip` | integration | Cache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_get_metadata_tuple_order` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_pop_returns_metadata_and_removes_entry` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_expire_uses_strict_cutoff` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_tag_evict_removes_only_matching_tag` | integration | Cache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_clear_returns_removed_count` | atomic | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_stats_track_hits_and_misses_when_enabled` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_length_counts_expired_entries_until_cleanup` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_push_generates_documented_integer_edges` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_push_generates_prefixed_keys` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_peek_does_not_remove_queue_item` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_pull_and_peek_skip_expired_queue_items` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_queue_metadata_tuple_shape` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_peekitem_returns_first_and_last_pairs` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_iteration_and_reversed_key_order` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_reset_updates_setting_and_attribute` | integration | Cache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_volume_includes_database_and_value_files` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_context_manager_and_pickle_reopen_same_directory` | system_e2e | Cache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_memoize_caches_results_and_exposes_key` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_memoize_ignore_removes_arguments_from_cache_key` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_memoize_typed_separates_equal_values_by_type` | integration | Cache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_cache_memoize_rejects_bare_decorator_use` | integration | Cache + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_jsondisk_round_trips_json_compatible_values` | integration | Disk and JSONDisk | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_set_get_delete_membership` | integration | FanoutCache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_add_touch_incr_decr` | integration | FanoutCache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_pop_and_default_values` | integration | FanoutCache | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_stats_accumulate_across_shards` | integration | FanoutCache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_clear_and_iteration` | integration | FanoutCache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_child_cache_reopens_named_state` | system_e2e | FanoutCache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_child_deque_reopens_named_state` | system_e2e | FanoutCache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_child_index_reopens_named_state` | system_e2e | FanoutCache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_transact_requires_retry_true` | integration | FanoutCache + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_reset_updates_shard_settings` | integration | FanoutCache + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_fanout_file_like_read_round_trip` | integration | FanoutCache + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_initialization_and_iteration` | atomic | Deque + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_append_appendleft_pop_popleft` | atomic | Deque | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_maxlen_discards_from_opposite_side` | atomic | Deque | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_index_assignment_and_deletion` | atomic | Deque | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_extendleft_reverse_and_rotate` | atomic | Deque | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_count_remove_and_missing_value` | atomic | Deque + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_persists_by_directory` | system_e2e | Deque + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_deque_fromcache_uses_supplied_cache_state` | system_e2e | Deque + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_initialization_order_and_views` | atomic | Index | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_setdefault_pop_and_key_errors` | atomic | Index + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_popitem_first_and_last` | atomic | Index | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_push_pull_queue_behavior` | atomic | Index + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_memoize_caches_results` | integration | Index | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_persists_by_directory` | system_e2e | Index + Cross-View Invariants + Representative Workflows | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_index_fromcache_uses_supplied_cache_state` | system_e2e | Index + Cross-View Invariants | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_averager_tracks_average_and_pop_clears_state` | atomic | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_lock_context_sets_and_releases_lock_key` | atomic | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_rlock_allows_nested_acquire_and_balanced_release` | atomic | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_bounded_semaphore_allows_acquire_release_within_bound` | atomic | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_throttle_uses_sleep_until_capacity_is_available` | integration | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_barrier_decorator_returns_function_result` | integration | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_memoize_stampede_caches_result_and_exposes_key` | integration | Recipes | covered | generated public-API oracle; reference-observed and spec-derivable |
| `tests/test_generated_diskcache.py::test_public_constants_and_exports_are_available` | atomic | Installable Surface + Error Semantics | covered | generated public-API oracle; reference-observed and spec-derivable |

Total: 63 | kept (covered): 63 | spec_gap: 0 | source-only: 0 | excluded: 179 upstream + optional Django/doctest collection errors | final scoreable: 63
