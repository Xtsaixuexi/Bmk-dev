# arrow-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-arrow-fullrepro-001-20260702T035140Z/output/arrow/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-arrow-fullrepro-001-20260702T035227Z/output/arrow/__init__.py
```

## Reference

- Passed: 87/87
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 14; total 14; integration: passed 73; total 73

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-arrow-fullrepro-001-20260702T035140Z`
- Score: 24/87
- Summary: passed 24; failed 33; error 30; total 87
- By layer: atomic: passed 9; failed 5; total 14; integration: passed 15; failed 28; error 30; total 73
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-arrow-fullrepro-001-20260702T035227Z`
- Score: 27/87
- Summary: passed 27; failed 30; error 30; total 87
- By layer: atomic: passed 11; failed 3; total 14; integration: passed 16; failed 27; error 30; total 73
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 87; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
