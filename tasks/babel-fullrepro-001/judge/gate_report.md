# babel-fullrepro-001 Gate Report

Date: 2026-07-05
Status: QUALIFIED
Judge verdict: 通过

## Scope

- Repository: [babel](https://github.com/python-babel/babel)
- Source path: `/root/autodl-tmp/e2e/babel`
- Commit: `baf9431`
- Task directory: `wip/babel-fullrepro-001`
- Candidate-visible packet: `spec.md` plus generic implementation instructions only.

## Required Bmk-dev Checks

### 1. Anti-cheat / Import Provenance

Preflight output:

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-babel-fullrepro-001-20260702T035140Z/output/babel/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-babel-fullrepro-001-20260702T035227Z/output/babel/__init__.py
```

Verdict: PASS.

Reference/oracle passes at 100%; candidate runs have clean import provenance; remaining failures are candidate implementation gaps.

### 2. Solvability / Reference Oracle

Reference result: 63/63 passed, pass_rate_excluding_skips=1.0.

Layer summary: atomic: passed 49; total 49; integration: passed 14; total 14.

The retained oracle is solvable by the reference implementation under the recorded dependency/profile settings.

### 3. Fairness / Spec-driven Behavioral Scope

The task package contains `spec.md`, `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `test_taxonomy_score.csv`, `reference_score.json`, and `reference_validation.md`. The retained tests are treated as scoreable because they map to the public behavioral spec and the reference implementation passes them.

### 4. Candidate Evaluation

- `opencode + gpt-5.5`: 0/63 passed; collection_error 63; total 63; provenance=clean
- `swe-agent + gpt-5.5`: 0/63 passed; collection_error 63; total 63; provenance=clean

Best adopted candidate: `swe-agent + gpt-5.5`, 0/63.

## Final Decision

QUALIFIED.

Promote this task to `tasks/babel-fullrepro-001/`.
