# Stage 3 GitHub Alignment: pyyaml-fullrepro-001

Generated: 2026-07-09T10:53:42.629221Z

Authority files:

- `github_alignment/raw_main/skills/test-filter/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`

## Alignment Checks

- PASS: `PIPELINE_STATE.md` was verified as `S3_FILTER_IN_PROGRESS` before filtering.
- PASS: all 2616 collected nodeids are present in `filter/spec_test_map.md`.
- PASS: every covered row maps to headings present in `spec/spec_v1.md`.
- PASS: `filter/rewrite_audit.md` exists and records Track A file-level decisions before merge.
- PASS: original `test_yaml_ext.py` nodeids were excluded because they import private `yaml._yaml` and are optional C-extension wrapper tests under scorer isolation.
- PASS: original `test_merge.py` nodeids were excluded because they assert `Loader.flatten_mapping`/`MappingNode.value` implementation shape rather than public merge behavior.
- PASS: exact dump transcript, no-assertion scanner smoke, and test-added canonical helper rows were excluded.
- PASS: Track B was not triggered because Track A retained 889 public behavioral nodeids and all behavior coverage floors passed.
- PASS: `kept_nodeids.txt`, `taxonomy.jsonl`, `spec_test_map.md`, `candidate_filter_map.md`, `kept_upstream.txt`, and root copies were generated.
- PASS: scorer-compatible taxonomy produced non-zero by-layer counts and zero unknown cases.
- PASS: scorer isolation is recorded as `score_pytest_original.py --remove-path yaml`.
- PASS: reference gate passed 889/889 and dummy gate passed 0/889.
- PASS: no external review models were called in this Stage 3 run.
