# pycparser-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-pycparser-fullrepro-001-20260702T035140Z/output/pycparser/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-pycparser-fullrepro-001-20260702T035227Z/output/pycparser/__init__.py
```

## Reference

- Passed: 90/90
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 60; total 60; integration: passed 30; total 30

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-pycparser-fullrepro-001-20260702T035140Z`
- Score: 27/90
- Summary: passed 27; failed 63; total 90
- By layer: atomic: passed 22; failed 38; total 60; integration: passed 5; failed 25; total 30
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-pycparser-fullrepro-001-20260702T035227Z`
- Score: 33/90
- Summary: passed 33; failed 57; total 90
- By layer: atomic: passed 31; failed 29; total 60; integration: passed 2; failed 28; total 30
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 90; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
