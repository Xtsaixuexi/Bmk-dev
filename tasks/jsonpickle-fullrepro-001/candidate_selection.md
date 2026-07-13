# Candidate Selection: jsonpickle-fullrepro-001

## Decision

- repo: `jsonpickle__jsonpickle`
- source_repo: `jsonpickle/jsonpickle`
- source_path: `/root/autodl-tmp/new-e2e/jsonpickle__jsonpickle`
- task_id: `jsonpickle-fullrepro-001`
- decision: keep
- selected_at: 2026-07-09

This repository is selected from `/root/autodl-tmp/new-e2e` after logical de-duplication, existing-task exclusion, mechanical audit, and clean pytest collection pre-screen.

## Evidence

- commit: `4bdc0d60779b8dac952b46788b5b858223a24674`
- remote: `https://github.com/jsonpickle/jsonpickle.git`
- source LOC: 4128
- source Python files: 28
- test files: 20
- rough test functions: 336
- docs files rough: 17
- private import file rate: 0.0
- network marker file rate: 0.15
- snapshot marker file rate: 0.0
- pytest collect pre-screen: `COLLECT_OK` with 784 nodeids and 0 error markers

## Gate Review

### Hard Gates

- Pure Python package source LOC >= 3,000: pass.
- Not a single-file task: pass, source spans 28 Python files.
- Test suite present and scoreable floor plausible: pass, rough test count is 336 and collect pre-screen found 784 nodeids.
- Documentation/public usage signal present: pass, docs rough count is 17.
- Private import risk acceptable for Stage 1: pass, private import file rate is 0.0.
- Environment/snapshot risk acceptable for Stage 1: pass with filtering note; network marker rate is 0.15 and snapshot marker rate is 0.0.

### Soft Signals

- Initial product signal: Python object graph to JSON encode/decode behavior.
- Clean collection pre-screen reduces collection-error risk in downstream scoring.
- Docs and examples should support a candidate-visible spec written as library documentation rather than benchmark scaffolding.

## Risks

- Stage 3 must still audit each retained test for spec traceability and behavioral fairness.
- Tests that depend on helper modules, private internals, exact strings, snapshots, external processes, or optional dependencies must be excluded or rewritten.
- Stage 2 should avoid copying upstream implementation structure into the public spec.

## Batch Context

Batch artifacts are recorded under `batch-runs/new-e2e-20260709/`.

## Conclusion

Proceed with `jsonpickle-fullrepro-001` to Stage 2 after Stage 1 model review.
