# Candidate Selection: pyyaml-fullrepro-001

## Decision

- repo: `yaml__pyyaml`
- source_repo: `yaml/pyyaml`
- source_path: `/root/autodl-tmp/new-e2e/yaml__pyyaml`
- task_id: `pyyaml-fullrepro-001`
- decision: keep
- selected_at: 2026-07-09

This repository is selected from `/root/autodl-tmp/new-e2e` after logical de-duplication, existing-task exclusion, mechanical audit, and clean pytest collection pre-screen.

## Evidence

- commit: `34a9bf82357f4952d8f194a5a31f1c39743652d0`
- remote: `https://github.com/yaml/pyyaml.git`
- source LOC: 5238
- source Python files: 23
- test files: 25
- rough test functions: 49
- docs files rough: 3
- private import file rate: 0.04
- network marker file rate: 0.04
- snapshot marker file rate: 0.0
- pytest collect pre-screen: `COLLECT_OK` with 2616 nodeids and 0 error markers

## Gate Review

### Hard Gates

- Pure Python package source LOC >= 3,000: pass.
- Not a single-file task: pass, source spans 23 Python files.
- Test suite present and scoreable floor plausible: pass, rough test count is 49 and collect pre-screen found 2616 nodeids.
- Documentation/public usage signal present: pass, docs rough count is 3.
- Private import risk acceptable for Stage 1: pass, private import file rate is 0.04.
- Environment/snapshot risk acceptable for Stage 1: pass with filtering note; network marker rate is 0.04 and snapshot marker rate is 0.0.

### Soft Signals

- Initial product signal: YAML parser/emitter with loader/dumper/resolver behavior.
- Clean collection pre-screen reduces collection-error risk in downstream scoring.
- Docs and examples should support a candidate-visible spec written as library documentation rather than benchmark scaffolding.

## Risks

- Stage 3 must still audit each retained test for spec traceability and behavioral fairness.
- Tests that depend on helper modules, private internals, exact strings, snapshots, external processes, or optional dependencies must be excluded or rewritten.
- Stage 2 should avoid copying upstream implementation structure into the public spec.

## Batch Context

Batch artifacts are recorded under `batch-runs/new-e2e-20260709/`.

## Conclusion

Proceed with `pyyaml-fullrepro-001` to Stage 2 after Stage 1 model review.
