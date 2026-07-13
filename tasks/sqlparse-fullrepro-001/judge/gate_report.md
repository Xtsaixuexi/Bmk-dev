# sqlparse-fullrepro-001 Gate Report

Date: 2026-07-05
Status: QUALIFIED
Judge verdict: 通过

## Scope

- Repository: [sqlparse](https://github.com/andialbrecht/sqlparse)
- Source path: `/root/autodl-tmp/e2e/sqlparse`
- Commit: `f80af6a`
- Task directory: `wip/sqlparse-fullrepro-001`
- Candidate-visible packet: `spec.md` plus generic implementation instructions only.

## Required Bmk-dev Checks

### 1. Anti-cheat / Import Provenance

Preflight output:

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-sqlparse-fullrepro-001-20260702T035140Z/output/sqlparse/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-sqlparse-fullrepro-001-20260702T035227Z/output/sqlparse/__init__.py
```

Verdict: PASS.

Reference/oracle passes at 100%; candidate runs have clean import provenance; remaining failures are candidate implementation gaps.

### 2. Solvability / Reference Oracle

Reference result: 90/90 passed, pass_rate_excluding_skips=1.0.

Layer summary: atomic: passed 37; total 37; integration: passed 30; total 30; system_e2e: passed 23; total 23.

The retained oracle is solvable by the reference implementation under the recorded dependency/profile settings.

### 3. Fairness / Spec-driven Behavioral Scope

The task package contains `spec.md`, `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `test_taxonomy_score.csv`, `reference_score.json`, and `reference_validation.md`. The retained tests are treated as scoreable because they map to the public behavioral spec and the reference implementation passes them.

### 4. Candidate Evaluation

- `opencode + gpt-5.5`: 17/90 passed; passed 17; failed 73; total 90; provenance=clean
- `swe-agent + gpt-5.5`: 7/90 passed; passed 7; failed 83; total 90; provenance=clean

Best adopted candidate: `opencode + gpt-5.5`, 17/90.

## Final Decision

QUALIFIED.

Promote this task to `tasks/sqlparse-fullrepro-001/`.
