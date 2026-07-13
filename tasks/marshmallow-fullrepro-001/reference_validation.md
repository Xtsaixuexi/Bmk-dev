# Step 5 Reference Oracle Validation

## Result

PASS. Reference implementation passes the filtered kept set.

## Score Summary

```json
{
  "summary": {
    "passed": 832,
    "total": 832
  },
  "pass_rate_excluding_skips": 1.0,
  "by_layer": {
    "atomic": {
      "passed": 292,
      "total": 292
    },
    "integration": {
      "passed": 481,
      "total": 481
    },
    "system_e2e": {
      "passed": 59,
      "total": 59
    }
  }
}
```

## Collection Check

```json
{
  "returncode": 0,
  "collected_nodeids": 1178,
  "expected_all_nodeids": 1178,
  "collection_matches_all": false,
  "missing_from_collection": [
    "tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[07-01-2026 17:26:51]",
    "tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[17:26:51 2026-07-01]"
  ],
  "missing_total": 2,
  "extra_in_collection": [
    "tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[02:24:21 2026-07-02]",
    "tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[07-02-2026 02:24:21]"
  ],
  "extra_total": 2,
  "kept_subset_of_collection": true,
  "kept_count": 832,
  "env": "PYTHONPATH=source/src"
}
```

## Notes

- The active environment initially lacked pytest; Step 5 installed `pytest`, `pytest-json-report`, and `simplejson` in the active Python 3.10 environment.
- `python -m pytest --collect-only -q tests` succeeds with `PYTHONPATH=/root/autodl-tmp/e2e/marshmallow/src`.
- Current collection has 1178 nodeids. It differs from the Step 4 baseline on 2 parameter IDs containing the current date/time string; those two dynamic IDs are not in `kept_nodeids.txt`, and `kept_subset_of_collection` is true.
- Oracle scoring used `harness/score_pytest_original.py` with `filter/kept_nodeids.txt` and `filter/test_taxonomy_score.csv`.
- Layer mapping is confirmed by score output: atomic 292, integration 481, system_e2e 59; no `unknown` layer appeared.

## Files

- `reference/collection_check.json`
- `reference/collected_nodeids.txt`
- `reference/reference_score.json`
- `reference/oracle_run/`
