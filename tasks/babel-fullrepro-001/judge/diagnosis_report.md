# babel-fullrepro-001 Diagnosis Report

Date: 2026-07-05
Status: QUALIFIED

## Preflight output

```text
opencode + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-isolated/opencode-gpt-5.5-babel-fullrepro-001-20260702T035140Z/output/babel/__init__.py
swe-agent + gpt-5.5: /root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/e2e10-sweagent/swe-agent-gpt-5.5-babel-fullrepro-001-20260702T035227Z/output/babel/__init__.py
```

## Reference

- Passed: 63/63
- Pass rate excluding skips: 1.0
- By layer: atomic: passed 49; total 49; integration: passed 14; total 14

## Candidate Scores

### opencode + gpt-5.5

- Run: `opencode-gpt-5.5-babel-fullrepro-001-20260702T035140Z`
- Score: 0/63
- Summary: collection_error 63; total 63
- By layer: atomic: collection_error 49; total 49; integration: collection_error 14; total 14
- Import provenance: clean

### swe-agent + gpt-5.5

- Run: `swe-agent-gpt-5.5-babel-fullrepro-001-20260702T035227Z`
- Score: 0/63
- Summary: collection_error 63; total 63
- By layer: atomic: collection_error 49; total 49; integration: collection_error 14; total 14
- Import provenance: clean

## Diagnosis

The scoring instrument is valid for this batch: reference passes the retained oracle and candidate imports resolve from the candidate output directory. Candidate failures are recorded as implementation gaps, including collection errors caused by missing public import surface or incomplete package resources.

## Gate D - Coverage Gap Audit
Coverage verdict: **FULL**.

- Bmk-dev main basis: per-section minimums from `skills/test-filter/SKILL.md` (Cross-View Invariants >=5; Error Semantics >=3; workflow sections >=3; all other scored sections >=3) plus global floor >=50 scoreable tests.
- Scoreable tests: 63; global floor: PASS.
- All scored H2/H3 sections meet the current per-section minimums. Metadata/context sections with minimum 0 are not treated as score targets.

Gate D action: no coverage action required for current-main packaging.
