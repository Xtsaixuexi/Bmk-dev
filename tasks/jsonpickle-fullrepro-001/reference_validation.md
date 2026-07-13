# Reference Validation

## Collection

- Upstream test-suite collection: 784 nodeid rows from `pytest tests --collect-only -q`.
- Unique collected nodeids: 440. Duplicate rows are documented as collection artifacts in `filter/candidate_filter_map.md`.

## Track A

- Retained upstream nodeids: 12.
- Excluded upstream rows: 772.
- Accounting gate: 12 + 772 = 784.

## Track B

- Generated nodeids: 64 in `filter/generated_tests.py`.
- Oracle count: 76.
- Coverage floor: global floor passed (`76 >= 50`); no section below minimum in `filter/coverage_floor.json`.

## Dummy Gate

Command shape: `score_pytest_original.py --source-repo filter/oracle_source --solution-dir filter/dummy_solution --remove-path jsonpickle --package jsonpickle`.

Result: {'failed': 76, 'total': 76} with pass rate 0.0. No dummy test passed.

## Reference Gate

Command shape: `score_pytest_original.py --source-repo filter/oracle_source --solution-dir /root/autodl-tmp/new-e2e/jsonpickle__jsonpickle --remove-path jsonpickle --package jsonpickle`.

Result: {'passed': 76, 'total': 76} with pass rate 1.0.

Preflight import path:

```text
/root/autodl-tmp/new-e2e/jsonpickle__jsonpickle/jsonpickle/__init__.py
```

## Taxonomy Gate

Reference by-layer summary:

```json
{
  "atomic": {
    "passed": 13,
    "total": 13
  },
  "integration": {
    "passed": 53,
    "total": 53
  },
  "system_e2e": {
    "passed": 10,
    "total": 10
  }
}
```

No `unknown` layer appears in the reference score.

## Branch Coverage Artifact

`filter/coverage.json` was generated with WIP-local `coverage` installed under `filter/runtime/vendor`. Overall branch coverage is 51%; optional extension modules are included in the denominator but excluded from this task's core spec.
