# click-fullrepro-001

Broken click full-reconstruction benchmark task.

## Status

- Pipeline state: `BROKEN_PROVENANCE`
- Spec: complete (`spec.md` + `spec/spec_v1.md`)
- Filter/taxonomy: complete (`kept_nodeids.txt`, `taxonomy.jsonl`, `spec_test_map.md`)
- Reference/oracle: 90/90 passed
- Best adopted candidate: none; provenance gate failed

## Candidate Visibility

Candidates may receive only `spec.md` and generic implementation instructions. Do not expose source paths, upstream tests, kept node IDs, taxonomy, reference scores, review files, score reports, or prior candidate outputs.

## Scoring Inputs

- `kept_nodeids.txt`
- `taxonomy.jsonl`
- `test_taxonomy_score.csv`
- `spec_test_map.md`
- `reference_score.json`
- `reference_validation.md`

## Judge

- `judge/gate_report.md`
- `judge/diagnosis_report.md`
