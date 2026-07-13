# lark-fullrepro-001 Diagnosis Report

## Reference

Reference result: 710 passed + 82 skipped / 792.

## Candidate

Best recorded candidate: opencode + gpt-5.5 scored 282/792.

## Verdict

QUALIFIED according to existing local task artifacts. Standardized diagnosis generated for e2e reporting compatibility.

## Preflight output

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/lark/opencode-gpt-5.5-lark-fullrepro-001-resourcepatch-20260701T224057Z/score_overlay_direct/overlay_worktree/lark/__init__.py
```

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 792; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
