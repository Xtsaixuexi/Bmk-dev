# markdown-it-py-fullrepro-001 Diagnosis Report

## Anti-cheat Scan

Preflight output:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e-remaining-opencode/opencode-gpt-5.5-markdown-it-py-fullrepro-001-20260705T000000Z/output/markdown_it/__init__.py
```

No source/test/reference artifact access is recorded in the retained score report. Candidate provenance is clean.

## Reference Validation

Reference passed 81 + 0 skipped / 81; pass rate excluding skips 1.0.

## Candidate Score

Runner/model: `opencode + gpt-5.5`.

Overall: 11/81 passed.

By layer:

```json
{
  "atomic": {
    "failed": 8,
    "total": 8
  },
  "integration": {
    "collection_error": 5,
    "failed": 49,
    "passed": 9,
    "total": 63
  },
  "system_e2e": {
    "failed": 8,
    "passed": 2,
    "total": 10
  }
}
```

## Failure Interpretation

Failures are treated as candidate implementation gaps because the same retained oracle passes on the reference implementation and the candidate import preflight points to candidate output. Collection errors generally indicate incomplete public package/module surface or missing public compatibility objects in the generated implementation.

## Judge Verdict

QUALIFIED: the task is solvable, candidate-isolated, and produces valid differentiating failure evidence.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 81; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
