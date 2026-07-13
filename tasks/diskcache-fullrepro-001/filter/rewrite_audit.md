# Rewrite Audit: diskcache-fullrepro-001

Authority: GitHub accelerated snapshot `github_alignment/raw_main/skills/test-filter/SKILL.md`.

## Track A Import Audit

- In-scope upstream files collected with `PYTEST_ADDOPTS='' python -m pytest --collect-only -q -o addopts='' tests/test_core.py tests/test_fanout.py tests/test_deque.py tests/test_index.py tests/test_recipes.py`.
- Collected upstream test functions: 179.
- Optional Django/doctest collection failed because Django is not installed; this is an optional-dependency environment issue, not part of the generated scoring oracle.
- Upstream tests contain a high concentration of implementation-shape checks: mocked shard internals, private state access, exact repr checks, rsync/subprocess environment dependencies, warning-message/details checks, benchmark/stress patterns, and optional Django test harness dependencies.
- No upstream test file was copied verbatim into the scoring oracle. This avoids carrying private implementation imports and fixture assumptions into candidate evaluation.

## Track B Trigger

Track B is used as the primary oracle because the public API surface is broad and the upstream suite is heavily implementation-shaped. The generated oracle uses only `import diskcache as dc`, `pytest`, `pickle`, and `io.BytesIO`; it does not import `diskcache.core`, `diskcache.fanout`, private helpers, or upstream fixtures.

## Generated Oracle

- File: `filter/oracle_repo/tests/test_generated_diskcache.py`
- Generated test functions: 63
- Layers: atomic=22, integration=33, system_e2e=8
- Reference direct pytest result: 63/63 passed.

## Count Accounting

functions_in_scope: 63
functions_kept: 63
functions_excluded: 0

For this generated-only oracle, count accounting applies to the scoreable generated test functions. Upstream functions were audited for suitability but not rewritten into the scoring set.

## Stage 5 fairness correction

2026-07-08T22:10:32Z: Removed over-specific generated assertions about `fromcache()` object identity, `Index(directory, pairs)` positional-constructor shape, and extra `release()` exception details that were not explicit in the spec. Regenerated map/taxonomy/nodeids and reran gates.
