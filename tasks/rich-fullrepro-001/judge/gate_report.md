# rich-fullrepro-001 Gate Report

Date: 2026-07-05
Status: QUALIFIED
Judge verdict: 通过

## Scope

- Repository: [rich](https://github.com/Textualize/rich)
- Source path: `/root/autodl-tmp/e2e/rich`
- Commit: `9d8f9a3`
- Task directory: `wip/rich-fullrepro-001`
- Candidate-visible packet: `spec.md` plus generic implementation instructions only.

## Required Bmk-dev Checks

### 1. Anti-cheat / Import Provenance

Preflight output:

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e-remaining-opencode/opencode-gpt-5.5-rich-fullrepro-001-20260705T000000Z/output/rich/__init__.py
```

Verdict: PASS.

The import path points into the generated candidate run directory, not the upstream e2e source checkout or a globally installed target package.

### 2. Solvability / Reference Oracle

Reference result: 90 passed + 0 skipped / 90 retained nodeids; pass_rate_excluding_skips=1.0.

Layer summary: {"atomic": {"passed": 44, "total": 44}, "integration": {"passed": 46, "total": 46}}.

The retained oracle is solvable by the reference implementation under the recorded dependency/profile settings.

### 3. Fairness / Spec-driven Behavioral Scope

The task package contains `spec.md`, `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `test_taxonomy_score.csv`, `reference_score.json`, and `reference_validation.md`. The retained tests map to public behavior sections in the specification and the reference implementation passes them.

### 4. Candidate Evaluation

- `opencode + gpt-5.5`: 12/90 passed; summary={"collection_error": 59, "failed": 19, "passed": 12, "total": 90}; provenance=clean.

## Final Decision

QUALIFIED.

Promote this task to `tasks/rich-fullrepro-001/`.
