# pyparsing-fullrepro-001

Qualified pyparsing full-reconstruction benchmark task.

## Status

- Spec: v4 complete after public helper and whitespace lifecycle patches.
- Filter/taxonomy: corrected 298-nodeid oracle.
- Reference/oracle: 298 passed, 0 failed.
- Best adopted candidate: `opencode + gpt-5.5`, 30/298.

## Candidate Visibility

Candidates may receive only `spec.md` and generic implementation instructions. Do not expose source paths, upstream tests, kept node IDs, taxonomy, reference scores, review files, or prior candidate outputs.

## Scoring Inputs

- `kept_nodeids.txt`
- `taxonomy.jsonl`
- `test_taxonomy_score.csv`
- `spec_test_map.md`
- `reference_score.json`
- `reference_validation.md`

## Scoring Notes

The final accepted OpenCode GPT v4 candidate imports from its own output package. Its timeout-labeled collection errors are candidate implementation/performance failures in `tests/test_unit.py`, not a remaining public-surface spec gap.
