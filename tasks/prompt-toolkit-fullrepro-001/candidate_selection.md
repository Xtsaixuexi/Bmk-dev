# Candidate Selection: prompt-toolkit-fullrepro-001

## Decision

- repo: `prompt-toolkit__python-prompt-toolkit`
- source_repo: `prompt-toolkit/python-prompt-toolkit`
- source_path: `/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit`
- task_id: `prompt-toolkit-fullrepro-001`
- decision: keep
- selected_at: 2026-07-09

This repository is selected from `/root/autodl-tmp/new-e2e` after logical de-duplication, existing-task exclusion, mechanical audit, and pytest collection pre-screen.

## Evidence

- commit: `236bfb7c15c62e921dc81bac5aefcabb16450f0c`
- remote: `https://github.com/prompt-toolkit/python-prompt-toolkit.git`
- source LOC: 36892
- source Python files: 277
- test files: 21
- rough test functions: 156
- docs files rough: 159
- private import file rate: 0.0
- network marker file rate: 0.048
- snapshot marker file rate: 0.143
- pytest collect pre-screen: `COLLECT_OK` with 156 nodeids and 0 error markers

## Gate Review

### Hard Gates

- Pure Python package source LOC >= 3,000: pass.
- Not a single-file task: pass, source spans 277 Python files.
- Test suite present and scoreable floor plausible: pass, rough test count is 156 and collect pre-screen found 156 nodeids.
- Documentation/public usage signal present: pass, docs rough count is 159.
- Private import risk acceptable for Stage 1: pass, private import file rate is 0.0.
- Environment/snapshot risk acceptable for Stage 1: pass with filtering note; network marker rate is 0.048 and snapshot marker rate is 0.143.

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

Proceed with `prompt-toolkit-fullrepro-001` to Stage 2.
