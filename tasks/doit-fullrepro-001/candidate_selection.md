# Candidate Selection: doit-fullrepro-001

## Decision

- repo: `pydoit__doit`
- source_repo: `pydoit/doit`
- source_path: `/root/autodl-tmp/new-e2e/pydoit__doit`
- task_id: `doit-fullrepro-001`
- decision: keep
- selected_at: 2026-07-09

This repository is selected from `/root/autodl-tmp/new-e2e` after logical de-duplication, existing-task exclusion, mechanical audit, and pytest collection pre-screen.

## Evidence

- commit: `1f9cbbce78a93f96a35abf2db5425361e2abf142`
- remote: `https://github.com/pydoit/doit.git`
- source LOC: 6669
- source Python files: 99
- test files: 34
- rough test functions: 545
- docs files rough: 97
- private import file rate: 0.0
- network marker file rate: 0.088
- snapshot marker file rate: 0.0
- pytest collect pre-screen: `COLLECT_OK` with 909 nodeids and 0 error markers

## Gate Review

### Hard Gates

- Pure Python package source LOC >= 3,000: pass.
- Not a single-file task: pass, source spans 99 Python files.
- Test suite present and scoreable floor plausible: pass, rough test count is 545 and collect pre-screen found 909 nodeids.
- Documentation/public usage signal present: pass, docs rough count is 97.
- Private import risk acceptable for Stage 1: pass, private import file rate is 0.0.
- Environment/snapshot risk acceptable for Stage 1: pass with filtering note; network marker rate is 0.088 and snapshot marker rate is 0.0.

### Soft Signals

- The project has enough public API surface and tests to support atomic, integration, and system-style oracle construction.
- Clean collection pre-screen reduces the chance of candidate collection failures caused by missing optional test-only dependencies.
- Docs and examples should support a candidate-visible spec written as library documentation rather than benchmark scaffolding.

## Risks

- Stage 3 must still audit each retained test for spec traceability and behavioral fairness.
- Tests that depend on helper modules, private internals, exact strings, snapshots, external processes, or optional dependencies must be excluded or rewritten.
- Stage 2 should avoid copying upstream implementation structure into the public spec.

## Batch Context

Batch artifacts are recorded under `batch-runs/new-e2e-20260709/`:

- `logical_stage1_queue.json`
- `logical_stage1_queue.csv`
- `logical_stage1_queue.md`
- `collect_results.json`
- `collect_results.csv`
- `collect_results.md`

## Conclusion

Proceed with `doit-fullrepro-001` to Stage 2.
