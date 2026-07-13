# Candidate Selection: cleo-fullrepro-001

## Decision

- repo: `python-poetry__cleo`
- source_repo: `python-poetry/cleo`
- source_path: `/root/autodl-tmp/new-e2e/python-poetry__cleo`
- task_id: `cleo-fullrepro-001`
- decision: keep
- selected_at: 2026-07-09

This repository is selected from `/root/autodl-tmp/new-e2e` after logical de-duplication, existing-task exclusion, mechanical audit, and clean pytest collection pre-screen.

## Evidence

- commit: `8c3f1bbf82d918fc137ad40db65c446e14564aac`
- remote: `https://github.com/python-poetry/cleo.git`
- source LOC: 6009
- source Python files: 75
- test files: 61
- rough test functions: 159
- docs files rough: 12
- private import file rate: 0.033
- network marker file rate: 0.0
- snapshot marker file rate: 0.098
- pytest collect pre-screen: `COLLECT_OK` with 258 nodeids and 0 error markers

## Gate Review

### Hard Gates

- Pure Python package source LOC >= 3,000: pass.
- Not a single-file task: pass, source spans 75 Python files.
- Test suite present and scoreable floor plausible: pass, rough test count is 159 and collect pre-screen found 258 nodeids.
- Documentation/public usage signal present: pass, docs rough count is 12.
- Private import risk acceptable for Stage 1: pass, private import file rate is 0.033.
- Environment/snapshot risk acceptable for Stage 1: pass with filtering note; network marker rate is 0.0 and snapshot marker rate is 0.098.

### Soft Signals

- Initial product signal: command-line application, command, argument, option, IO behavior.
- Clean collection pre-screen reduces collection-error risk in downstream scoring.
- Docs and examples should support a candidate-visible spec written as library documentation rather than benchmark scaffolding.

## Risks

- Stage 3 must still audit each retained test for spec traceability and behavioral fairness.
- Tests that depend on helper modules, private internals, exact strings, snapshots, external processes, or optional dependencies must be excluded or rewritten.
- Stage 2 should avoid copying upstream implementation structure into the public spec.

## Batch Context

Batch artifacts are recorded under `batch-runs/new-e2e-20260709/`.

## Conclusion

Proceed with `cleo-fullrepro-001` to Stage 2 after Stage 1 model review.
