# lark-fullrepro-001

Reference-qualified Lark full-reconstruction benchmark task.

## Status

- Step 3 spec: complete, DeepSeek/GLM reviewed.
- Step 4 filter/taxonomy: complete, DeepSeek/GLM reviewed.
- Step 5 reference/oracle: complete, 710 passed, 82 skipped, 0 failed.
- Reference pass rate excluding skips: 1.0.

## Candidate Visibility

Candidates may receive only `spec.md` and generic implementation instructions. Do not expose source paths, upstream tests, kept node IDs, taxonomy, reference scores, review files, or prior candidate outputs.

## Scoring Inputs

- `kept_nodeids.txt`
- `kept_nodeids_direct.txt`
- `taxonomy.jsonl`
- `taxonomy_direct.jsonl`
- `test_taxonomy_score.csv`
- `spec_test_map.md`
- `reference_score.json`
- `reference_validation.md`

## Scoring Notes

The reference run reports 82 skipped tests. Candidate scoring must preserve the same environment profile and rely on the same upstream skip logic, so skipped tests are not counted as candidate failures when they match the reference skip conditions.

Use `kept_nodeids_direct.txt` and `taxonomy_direct.jsonl` for candidate scoring. The original `kept_nodeids.txt` preserves the Step 4/5 aggregate nodeids routed through `tests/__main__.py`; the direct files map those same test methods to their real test modules and reproduce the reference result exactly.
