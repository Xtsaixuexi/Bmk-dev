# chardet-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-chardet-fullrepro-001-20260702T035140Z/output/chardet/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-chardet-fullrepro-001-20260702T035227Z/output/chardet/__init__.py
```

## Reference

- Passed: 90/90
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 82; total 82; integration: passed 3; total 3; system_e2e: passed 5; total 5

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-chardet-fullrepro-001-20260702T035140Z`
- Score: 25/90
- Summary: passed 25; failed 10; collection_error 55; total 90
- By layer: atomic: passed 22; failed 8; collection_error 52; total 82; integration: collection_error 3; total 3; system_e2e: passed 3; failed 2; total 5
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-chardet-fullrepro-001-20260702T035227Z`
- Score: 22/90
- Summary: passed 22; failed 13; collection_error 55; total 90
- By layer: atomic: passed 20; failed 10; collection_error 52; total 82; integration: collection_error 3; total 3; system_e2e: passed 2; failed 3; total 5
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 90; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
