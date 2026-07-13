# Filter Validation: diskcache-fullrepro-001

Authority: GitHub accelerated snapshot `github_alignment/raw_main/skills/test-filter/SKILL.md`.

## Oracle Source

`oracle_source: generated_only`.

Upstream collection audit found 179 collectable non-Django upstream tests, but the suite contains implementation-shaped assertions and optional environment dependencies. The scoreable oracle uses generated public-API tests in `filter/oracle_repo/tests/test_generated_diskcache.py`.

## Fairness Correction

After the first candidate scoring pass, Stage 5 audit removed over-specific generated assertions about `fromcache()` object identity, `Index(directory, pairs)` constructor shape, and extra `release()` exception details that were not explicit in the spec. `kept_nodeids.txt`, `taxonomy.jsonl`, `spec_test_map.md`, dummy score, reference score, and candidate score were regenerated from the corrected oracle.

## Required Artifacts

- PASS: `filter/rewrite_audit.md`
- PASS: `filter/kept_nodeids.txt` (63 nodeids)
- PASS: `filter/taxonomy.jsonl`
- PASS: `filter/spec_test_map.md`
- PASS: `filter/test_taxonomy_score.csv`
- PASS: `reference_score.json`
- PASS: `filter/dummy_score.json`

## Count Verification

- functions_in_scope: 63
- functions_kept: 63
- functions_excluded: 0
- oracle_count: 63
- Check: functions_kept + functions_excluded = functions_in_scope -> PASS
- Check: oracle_count >= 50 -> PASS

## Dummy Gate

- Result: 0/63 passed
- Pass rate excluding skips: 0.0
- Import preflight stdout: `/root/autodl-tmp/Bmk-Lizhiqian/wip/diskcache-fullrepro-001/filter/dummy_solution/diskcache/__init__.py`
- Verdict: PASS. No oracle test passed the dummy implementation.

## Reference Gate

- Result: 63/63 passed
- Pass rate excluding skips: 1.0
- Import preflight stdout: `/root/autodl-tmp/new-e2e/grantjenks__python-diskcache/diskcache/__init__.py`
- Verdict: PASS.

## Section Coverage Counts

```json
{
  "Cache": 28,
  "Error Semantics": 8,
  "Cross-View Invariants": 26,
  "Representative Workflows": 9,
  "Disk and JSONDisk": 1,
  "FanoutCache": 11,
  "Deque": 8,
  "Index": 7,
  "Recipes": 7,
  "Installable Surface": 1
}
```

Below minimum sections:

```json
[]
```

Verdict: PASS.
