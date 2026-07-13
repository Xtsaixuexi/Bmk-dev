# click-fullrepro-001 Diagnosis Report

## Anti-cheat Scan

Preflight output:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/click-repair-opencode/opencode-gpt-5.5-click-fullrepro-001-20260705T-repair-provenance/output/click/__init__.py
```

Initial e2e10 runs were invalid because candidate import provenance was `None` or errored during import. The repaired opencode run created a normal `click/__init__.py` package and passes the preflight gate.

## Reference Validation

Reference passed 90/90 retained nodeids.

## Candidate Score

Runner/model: `opencode + gpt-5.5` repaired run.

Overall: 2/90 passed.

By layer:

```json
{
  "atomic": {
    "collection_error": 59,
    "failed": 11,
    "total": 71,
    "xfailed": 1
  },
  "system_e2e": {
    "collection_error": 1,
    "failed": 16,
    "passed": 2,
    "total": 19
  }
}
```

## Failure Interpretation

Remaining failures are candidate implementation gaps. The oracle is reference-solvable and the repaired candidate import path is clean.

## Judge Verdict

QUALIFIED.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 90; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
