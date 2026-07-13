# Stage 3 Test Filter Alignment

## Inputs Checked

- Read `github_alignment/raw_main/skills/test-filter/SKILL.md` and `github_alignment/raw_main/skills/task-synthesizer/SKILL.md` before filtering.
- Verified `PIPELINE_STATE.md` entry state was `S3_FILTER_IN_PROGRESS`.
- Source repo: `/root/autodl-tmp/new-e2e/jsonpickle__jsonpickle` at commit `4bdc0d6`.
- Spec: `spec.md`, matching `spec/spec_v1.md` with the Stage 2 corrections for reserved wire tags and `v1_decode`.

## Upstream Accounting

- Collected all 784 upstream nodeid rows into `filter/collected_nodeids.txt`.
- Accounted for every row in `filter/candidate_filter_map.md`.
- Retained 12 clean public upstream nodeids in `filter/kept_upstream.txt`.
- Excluded 772 upstream rows because they were duplicate collection artifacts, helper/setup nodeids, optional-extension tests, out-of-scope `jsonpickle.util`/`tags` tests, exact backend formatting checks, or fixtures replaced by public generated coverage.
- Accounting gate passed: `functions_kept + functions_excluded = 12 + 772 = 784`.

## Track B And Coverage Floor

- Used `filter/generated_tests.py` for 64 generated public-behavior tests.
- Final oracle has 76 scoreable nodeids: 12 upstream + 64 generated.
- `filter/spec_test_map.md` contains the 784 upstream decisions plus the 64 generated covered rows. Root copy: `spec_test_map.md`.
- Section coverage floor passed; details are in `filter/coverage_floor.json`.
- Branch coverage artifact generated at `filter/coverage.json`; optional extension modules are included in its denominator but are non-goals for this task.

## Gates

- Dummy gate: `filter/dummy_score.json` -> 0/76 passed.
- Reference gate: `reference_score.json` -> 76/76 passed.
- Taxonomy gate: `taxonomy.jsonl` produced nonzero `atomic`, `integration`, and `system_e2e` counts and no `unknown` layer in the scorer output.
- Scorer isolation: both scorer gates used `--remove-path jsonpickle`; reference preflight resolved to `/root/autodl-tmp/new-e2e/jsonpickle__jsonpickle/jsonpickle/__init__.py`.

## Artifacts

- Filter artifacts: `filter/spec_test_map.md`, `filter/kept_nodeids.txt`, `filter/taxonomy.jsonl`, `filter/candidate_filter_map.md`, `filter/rewrite_audit.md`, `filter/generated_tests.py`, `filter/coverage_floor.json`.
- Root copies: `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `reference_score.json`, `reference_validation.md`, `test_taxonomy_score.csv`, `MANIFEST.json`.
- No external review models were called.
