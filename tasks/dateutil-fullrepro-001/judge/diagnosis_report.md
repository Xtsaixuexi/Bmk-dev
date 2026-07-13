# dateutil-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-dateutil-fullrepro-001-20260702T035140Z/output/dateutil/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-dateutil-fullrepro-001-20260702T035227Z/output/dateutil/__init__.py
```

## Reference

- Passed: 90/90
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 33; total 33; integration: passed 52; total 52; system_e2e: passed 5; total 5

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-dateutil-fullrepro-001-20260702T035140Z`
- Score: 27/90
- Summary: passed 27; failed 7; collection_error 53; skipped 3; total 90
- By layer: atomic: passed 24; failed 7; skipped 3; total 34; integration: passed 3; collection_error 50; total 53; system_e2e: collection_error 3; total 3
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-dateutil-fullrepro-001-20260702T035227Z`
- Score: 30/90
- Summary: passed 30; failed 4; collection_error 53; skipped 3; total 90
- By layer: atomic: passed 27; failed 4; skipped 3; total 34; integration: passed 3; collection_error 50; total 53; system_e2e: collection_error 3; total 3
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 90; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
