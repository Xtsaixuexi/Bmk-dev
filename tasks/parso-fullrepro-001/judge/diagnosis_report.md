# parso-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-parso-fullrepro-001-20260702T035140Z/output/parso/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-parso-fullrepro-001-20260702T035227Z/output/parso/__init__.py
```

## Reference

- Passed: 90/90
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 41; total 41; integration: passed 49; total 49

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-parso-fullrepro-001-20260702T035140Z`
- Score: 14/90
- Summary: passed 14; failed 18; collection_error 58; total 90
- By layer: atomic: passed 10; failed 14; collection_error 17; total 41; integration: passed 4; failed 4; collection_error 41; total 49
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-parso-fullrepro-001-20260702T035227Z`
- Score: 0/90
- Summary: error 40; collection_error 50; total 90
- By layer: atomic: error 24; collection_error 17; total 41; integration: error 16; collection_error 33; total 49
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 90; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
