# marshmallow-fullrepro-001 Diagnosis Report

## Reference

Reference result: 832 passed + 0 skipped / 832.

## Candidate

Best recorded candidate: opencode + gpt-5.5 scored 451/832.

## Verdict

QUALIFIED according to existing local task artifacts. Standardized diagnosis generated for e2e reporting compatibility.

## Preflight output

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-marshmallow-fullrepro-001-orderedsetfix-20260701T210138Z/output/marshmallow/__init__.py
```

## Gate D - Coverage Gap Audit
Coverage verdict: **GAP**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 832; global floor: PASS.

| spec section | covered/minimum | impact | recommendation |
|---|---:|---|---|
| Top-Level Names | 1/3 | below current per-section quota | Return to test-filter Track B generation or exclude this behavior from scored scope if fair tests would be circular/source-only. |
| OrderedSet | 2/3 | below current per-section quota | Return to test-filter Track B generation or exclude this behavior from scored scope if fair tests would be circular/source-only. |
| Utility Helpers | 0/3 | core zero-coverage section | Return to test-filter Track B generation or exclude this behavior from scored scope if fair tests would be circular/source-only. |
| Behavioral Sections | 0/3 | core zero-coverage section | Return to test-filter Track B generation or exclude this behavior from scored scope if fair tests would be circular/source-only. |

Gate D action: unresolved coverage gap remains; do not claim strict current-main qualification without Track B expansion or an explicit, evidence-backed caveat.
