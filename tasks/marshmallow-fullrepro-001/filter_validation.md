# Step 4 Filter Validation

## Structural Checks

- all_nodeids count: 1178
- unique all_nodeids: True
- kept_nodeids count: 832
- kept subset of all: True
- taxonomy rows: 832
- taxonomy rows equal kept count: True
- score CSV rows: 832
- taxonomy key rule: matches `harness/score_pytest_original.py` (`tests/file.py::Class::test[param]` -> `file::Class.test`)

## Filter Counts

- covered / kept: 832
- source-only: 305
- excluded: 41
- spec_gap: 0

## Kept Layer Counts

- atomic: 292
- integration: 481
- system_e2e: 59

## Notes

The active environment lacks pytest/uv, so collection was validated by matching the clean source commit against the prior builder collection and removing the pytest summary line. Scoring/oracle validation in Step 5 must install or activate pytest-capable dependencies before running the kept set.
