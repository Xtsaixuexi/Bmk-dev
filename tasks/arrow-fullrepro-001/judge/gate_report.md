# arrow-fullrepro-001 Gate Report

Date: 2026-07-05
Status: QUALIFIED
Judge verdict: 通过

## Scope

- Repository: [arrow](https://github.com/arrow-py/arrow)
- Source path: `/root/autodl-tmp/e2e/arrow`
- Commit: `2224255`
- Task directory: `wip/arrow-fullrepro-001`
- Candidate-visible packet: `spec.md` plus generic implementation instructions only.

## Required Bmk-dev Checks

### 1. Anti-cheat / Import Provenance

Preflight output:

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-arrow-fullrepro-001-20260702T035140Z/output/arrow/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-arrow-fullrepro-001-20260702T035227Z/output/arrow/__init__.py
```

Verdict: PASS.

Reference/oracle passes at 100%; candidate runs have clean import provenance; remaining failures are candidate implementation gaps.

### 2. Solvability / Reference Oracle

Reference result: 87/87 passed, pass_rate_excluding_skips=1.0.

Layer summary: atomic: passed 14; total 14; integration: passed 73; total 73.

The retained oracle is solvable by the reference implementation under the recorded dependency/profile settings.

### 3. Fairness / Spec-driven Behavioral Scope

The task package contains `spec.md`, `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `test_taxonomy_score.csv`, `reference_score.json`, and `reference_validation.md`. The retained tests are treated as scoreable because they map to the public behavioral spec and the reference implementation passes them.

### 4. Candidate Evaluation

- `opencode + gpt-5.5`: 24/87 passed; passed 24; failed 33; error 30; total 87; provenance=clean
- `swe-agent + gpt-5.5`: 27/87 passed; passed 27; failed 30; error 30; total 87; provenance=clean

Best adopted candidate: `swe-agent + gpt-5.5`, 27/87.

## Final Decision

QUALIFIED.

Promote this task to `tasks/arrow-fullrepro-001/`.
