# Candidate Selection: diskcache-fullrepro-001

## Decision

- repo: `grantjenks__python-diskcache`
- package: `diskcache`
- source_path: `/root/autodl-tmp/new-e2e/grantjenks__python-diskcache`
- task_id: `diskcache-fullrepro-001`
- decision: keep
- selected_at: 2026-07-09

`diskcache` is selected as the first candidate from the new source pool `/root/autodl-tmp/new-e2e`. This is an expansion line beyond the frozen 22-task meeting-aligned set recorded in `Bmk-Lizhiqian状态.md`; the existing freeze/P0 provenance work is left untouched.

## Evidence

- commit: `ebfa37cd99d7ef716ec452ad8af4b4276a8e2233`
- package source LOC: 4,150 across top-level `diskcache/*.py`
- implementation files: `__init__.py`, `cli.py`, `core.py`, `djangocache.py`, `fanout.py`, `persistent.py`, `recipes.py`
- regular test files: 7 `tests/test_*.py` files
- regular test functions: 253
- tests directory Python files: 27 files, including benchmarks, stress tests, settings, helper modules, and issue repro scripts
- module-level private import audit: 0 matches for `diskcache._*` imports in `tests/`
- public docs: `README.rst`, `docs/tutorial.rst`, `docs/api.rst`, `docs/index.rst`, `docs/development.rst`
- public import surface from `diskcache.__all__`: `Cache`, `FanoutCache`, `DjangoCache`, `Deque`, `Index`, `Disk`, `JSONDisk`, `Timeout`, `UnknownFileWarning`, `EmptyDirWarning`, `Averager`, `Lock`, `RLock`, `BoundedSemaphore`, `throttle`, `barrier`, `memoize_stampede`, constants
- external runtime dependency: none for core package install; optional Django behavior depends on Django

## Gate Review

### Hard Gates

- Pure Python package source LOC >= 3,000: pass, measured at 4,150 non-comment/nonblank LOC in top-level package files.
- Not a single-file task: pass, behavior spans cache storage, file-backed values, sharded fanout caches, persistent containers, Django cache adapter, and synchronization recipes.
- Shared fact source with multiple public projections: pass. Cache state is observable through mapping operations, method calls, iteration, expiration/eviction, volume/statistics, persistent `Deque`/`Index`, sharded `FanoutCache`, and optional Django-style cache APIs.
- Test suite present: pass, 253 regular test functions across 7 `test_*.py` files.
- Network/database/system-service dependency: pass with note. SQLite and filesystem are local standard-library dependencies; no mandatory external service is required. Some tests use subprocess, rsync, temporary directories, timing, or optional Django and must be filtered or isolated later.
- Closed standard/high-saturation pattern: pass. Although key-value cache behavior is familiar, disk-backed expiration, eviction, file value handling, sharding, memoization, persistent containers, and Django compatibility create library-specific contracts.
- Evaluator can avoid private implementation details: pass with filtering risk. Several upstream tests touch `_disk`, `_sql`, `_shards`, exact `repr`, Django private fields, or mocked internals; these must be excluded or rewritten during Stage 3.
- Docs-test projection mismatch: pass. Public docs cover the same projections tested by the suite: `Cache`, `FanoutCache`, `Deque`, `Index`, recipes, settings, expiration, eviction, tags, statistics, and optional Django integration.

### Soft Signals

- The library has a durable state source: a cache directory containing SQLite metadata plus value files.
- The same facts have multiple public views: mapping syntax, explicit methods, iteration, stats, volume, tag/expire metadata, container wrappers, and sharded fanout behavior.
- Official docs include tutorial and API reference with executable examples.
- Core behavior is pure Python and dependency-light, which lowers cleanroom scoring risk.
- The regular tests include enough behavioral coverage to support atomic, integration, and system-level oracle construction after filtering.

## Risks

- Some tests assert internal disk/cache structures (`_disk`, `_sql`, `_shards`) or exact representation; these are not behavioral and should not enter the scoring set.
- `tests/test_djangocache.py` depends on optional Django behavior. It is potentially valuable but requires a task-specific dependency environment or conservative filtering.
- Time, expiration, process safety, file IO, subprocess, and rsync-related tests may be flaky or environment-shaped. Stage 3 should prefer deterministic cache lifecycle tests and explicitly filter timing/utility-carrier tests.
- Doctest coverage may include examples that are useful as public behavior but can be brittle if exact transcript formatting is retained.
- A spec can easily become too broad because `diskcache` exposes many methods; Stage 2 should focus on non-derivable public contracts and cross-view invariants rather than listing every implementation detail.

## New Source Pool Notes

The mechanical audit for `/root/autodl-tmp/new-e2e` is recorded in:

- `logs/new_e2e_step1_mechanical_audit.json`
- `logs/new_e2e_step1_mechanical_audit.csv`
- `logs/new_e2e_step1_triage_summary.md`

High mechanical-score projects such as `gunicorn`, `Twisted`, `sqlfluff`, and `pex` were not selected first because they carry higher process/network/framework/environment risk. `cmd2`, `doit`, and `textX` remain good next candidates if `diskcache` is retired later.

## Conclusion

Proceed with `diskcache-fullrepro-001`. The project passes Stage 1 gates and has a clear full-reconstruction signal centered on persistent cache state and public cross-view behavior. Continue to Step 2 only after human confirmation.
