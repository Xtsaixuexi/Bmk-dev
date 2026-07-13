# cookiecutter-fullrepro-001 Diagnosis Report

## Reference

Reference result: 0 passed + 0 skipped / 0.

## Candidate

Best recorded candidate: codex-subagent + gpt-5.5 scored 66/260.

## Verdict

QUALIFIED according to existing local task artifacts. Standardized diagnosis generated for e2e reporting compatibility.

## Preflight output

```text
Bmk-dev/results/codex-subagent/cookiecutter-fullrepro-001/specdelta-20260629-001/output/cookiecutter/__init__.py (reported in gate report, not locally verifiable)
```

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 213; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
