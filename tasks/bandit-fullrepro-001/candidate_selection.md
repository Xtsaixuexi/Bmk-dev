# Bandit Candidate Selection

repo: PyCQA/bandit
source_path: /root/autodl-tmp/new-e2e/PyCQA__bandit
commit: c45446eaa30c4f28289c3b8ba9a955e1d78ba715
src_loc: 17540
test_functions: 265 rough functions; 275 collected nodeids
test_files: 32
dominant_test_styles: source scanning, security plugins, configuration, issue filtering/baselines, CLI, and report formatters
public_docs: README plus 163 rough documentation files covering CLI, configuration, plugins, tests, issue taxonomy, baselines, and formats
core_fact_source: security findings produced by scanning a Python source tree
derived_views: CLI status/output, issue objects, severity/confidence filtering, profiles/config, baselines, metrics, and CSV/JSON/SARIF/XML/YAML/text/HTML reports
external_deps: local parser/plugin/formatter dependencies only for core tests; isolated install succeeded
test_import_audit: authoritative private import file rate 0.0
docs_test_alignment: aligned across scanner, CLI/config, findings, plugins, baselines, and report formats; AST/plugin internals require filtering
contamination_note: PyCQA/bandit at pinned commit; release timing relative to model training cutoff unknown
decision: proposed keep
reason: deterministic offline project scan with multiple public projections, substantial docs, and clean tests
risks: implementation-specific AST context, plugin manager registration shape, exact formatter whitespace/order, exact messages, and optional SARIF schema internals

## Collection Evidence

The isolated environment `/root/autodl-tmp/Bmk-Lizhiqian/envs/bandit-fullrepro-001` installed editable Bandit, test dependencies, and optional YAML/TOML/baseline/SARIF dependencies. Pytest collected 275 nodeids in 0.43 seconds with zero collection errors.

## Proposed Stage 1 Disposition

`S1_SELECTED_PENDING_REVIEW`, with implementation-shaped AST/plugin and exact-output checks routed to Stage 3 filtering.
