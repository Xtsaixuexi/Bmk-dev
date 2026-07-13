# chardet-fullrepro-001 Gate Report

Date: 2026-07-05
Status: QUALIFIED
Judge verdict: 通过

## Scope

- Repository: [chardet](https://github.com/chardet/chardet)
- Source path: `/root/autodl-tmp/e2e/chardet`
- Commit: `b5b2aa5`
- Task directory: `wip/chardet-fullrepro-001`
- Candidate-visible packet: `spec.md` plus generic implementation instructions only.

## Required Bmk-dev Checks

### 1. Anti-cheat / Import Provenance

Preflight output:

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-chardet-fullrepro-001-20260702T035140Z/output/chardet/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-chardet-fullrepro-001-20260702T035227Z/output/chardet/__init__.py
```

Verdict: PASS.

Reference/oracle passes at 100%; candidate runs have clean import provenance; remaining failures are candidate implementation gaps.

### 2. Solvability / Reference Oracle

Reference result: 90/90 passed, pass_rate_excluding_skips=1.0.

Layer summary: atomic: passed 82; total 82; integration: passed 3; total 3; system_e2e: passed 5; total 5.

The retained oracle is solvable by the reference implementation under the recorded dependency/profile settings.

### 3. Fairness / Spec-driven Behavioral Scope

The task package contains `spec.md`, `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `test_taxonomy_score.csv`, `reference_score.json`, and `reference_validation.md`. The retained tests are treated as scoreable because they map to the public behavioral spec and the reference implementation passes them.

### 4. Candidate Evaluation

- `opencode + gpt-5.5`: 25/90 passed; passed 25; failed 10; collection_error 55; total 90; provenance=clean
- `swe-agent + gpt-5.5`: 22/90 passed; passed 22; failed 13; collection_error 55; total 90; provenance=clean

Best adopted candidate: `opencode + gpt-5.5`, 25/90.

## Final Decision

QUALIFIED.

Promote this task to `tasks/chardet-fullrepro-001/`.
