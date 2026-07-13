# hy-fullrepro-001 Gate Report

Date: 2026-07-05
Status: QUALIFIED
Judge verdict: 通过

## Scope

- Repository: [hy](https://github.com/hylang/hy)
- Source path: `/root/autodl-tmp/e2e/hy`
- Commit: `5369306`
- Task directory: `wip/hy-fullrepro-001`
- Candidate-visible packet: `spec.md` plus generic implementation instructions only.

## Required Bmk-dev Checks

### 1. Anti-cheat / Import Provenance

Preflight output:

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e-remaining-opencode/opencode-gpt-5.5-hy-fullrepro-001-20260705T000000Z-smoke/output/hy/__init__.py
```

Verdict: PASS.

The import path points into the generated candidate run directory, not the upstream e2e source checkout or a globally installed target package.

### 2. Solvability / Reference Oracle

Reference result: 64 passed + 0 skipped / 64 retained nodeids; pass_rate_excluding_skips=1.0.

Layer summary: {"atomic": {"passed": 37, "total": 37}, "integration": {"passed": 15, "total": 15}, "system_e2e": {"passed": 12, "total": 12}}.

The retained oracle is solvable by the reference implementation under the recorded dependency/profile settings.

### 3. Fairness / Spec-driven Behavioral Scope

The task package contains `spec.md`, `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `test_taxonomy_score.csv`, `reference_score.json`, and `reference_validation.md`. The retained tests map to public behavior sections in the specification and the reference implementation passes them.

### 4. Candidate Evaluation

- `opencode + gpt-5.5`: 0/64 passed; summary={"collection_error": 64, "total": 64}; provenance=clean.

## Final Decision

QUALIFIED.

Promote this task to `tasks/hy-fullrepro-001/`.
