repo: rich
source_path: /root/autodl-tmp/e2e/rich
commit: 9d8f9a3
src_loc: 35251
test_functions: 721
test_files: 67
dominant_test_styles: unit / integration / command workflow / parser-renderer behavior depending on module
public_docs: README, package public exports, public module/class/function names
core_fact_source: public `rich` API and user-visible command/workflow behavior
derived_views: Python API, CLI/command behavior when present, parse/render/validation/conversion outputs, public errors
external_deps: local Python dependencies only; no mandatory external service in retained subset
test_import_audit: HIGH_RISK — 11 rough private-import files
docs_test_alignment: aligned for retained subset; full upstream suite may include internal or standard-conformance stress tests
contamination_note: rich@9d8f9a3, relative to training cutoff: unknown
decision: keep
reason: large console rendering library with multiple public projections and clean collection after local markdown-it-py dependency is on PYTHONPATH
risks: reference validation and candidate provenance must still pass before promotion
