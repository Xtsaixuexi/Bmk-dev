# markdown-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-markdown-fullrepro-001-20260702T035140Z/output/markdown/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-markdown-fullrepro-001-20260702T035227Z/output/markdown/__init__.py
```

## Reference

- Passed: 90/90
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 81; total 81; integration: passed 9; total 9

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-markdown-fullrepro-001-20260702T035140Z`
- Score: 0/90
- Summary: failed 27; collection_error 62; skipped 1; total 90
- By layer: atomic: failed 27; collection_error 53; skipped 1; total 81; integration: collection_error 9; total 9
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-markdown-fullrepro-001-20260702T035227Z`
- Score: 0/90
- Summary: failed 27; collection_error 62; skipped 1; total 90
- By layer: atomic: failed 27; collection_error 53; skipped 1; total 81; integration: collection_error 9; total 9
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 90; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
