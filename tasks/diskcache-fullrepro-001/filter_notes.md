# Candidate Filter Notes: diskcache-fullrepro-001

repo: grantjenks__python-diskcache
source_path: /root/autodl-tmp/new-e2e/grantjenks__python-diskcache
commit: ebfa37cd99d7ef716ec452ad8af4b4276a8e2233
src_loc: 4150
test_functions: 253 regular `tests/test_*.py` functions
test_files: 7 regular test files under `tests/`
dominant_test_styles: unit and integration tests over persistent cache lifecycle, file-backed values, expiration, eviction, sharding, persistent containers, optional Django adapter, doctest examples
public_docs: README.rst; docs/tutorial.rst; docs/api.rst; docs/index.rst; docs/development.rst
core_fact_source: persistent cache entries in a cache directory backed by SQLite metadata and optional file-backed values
derived_views: Cache mapping/method API; FanoutCache sharded API; Deque sequence API; Index mapping API; recipes for locks/throttle/memoization; stats/volume/settings/tag/expiration projections; optional DjangoCache compatibility API
external_deps: standard-library sqlite3/filesystem/tempfile; optional Django; environment-sensitive subprocess/rsync tests to filter or isolate
test_import_audit: clean - no module-level `diskcache._*` private imports found; internal assertion risk remains in specific tests
docs_test_alignment: aligned - docs cover Cache, FanoutCache, Deque, Index, recipes, settings, expiration, eviction, tags, stats, and optional Django integration
contamination_note: grantjenks/python-diskcache@5.6.3-era checkout, commit ebfa37c; release/training cutoff relationship not independently verified in this local-only Step 1 audit
decision: keep
reason: durable local cache state with multiple public projections, docs-backed behavior, enough tests, and manageable dependency surface
risks: private attribute assertions, optional Django dependency, timing/expiration/subprocess/rsync sensitivity, doctest transcript brittleness

## Stage 3 Filter Priorities

- Exclude tests that assert `_disk`, `_sql`, `_shards`, Django private fields, exact `repr`, or mocked implementation internals.
- Treat optional Django tests as a separate filter track; keep only if the scoring environment can install Django and the tests check documented Django cache compatibility.
- Prefer deterministic public lifecycle tests: set/get/delete/add/pop, expiration when controllable, eviction policy effects, tag metadata, stats, file-backed values, Deque/Index workflows, FanoutCache behavior, memoization and lock semantics.
- Avoid rsync/subprocess and timing-heavy tests unless they are stable, public, and spec-derivable.
