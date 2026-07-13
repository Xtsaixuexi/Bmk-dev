repo: hy
source_path: /root/autodl-tmp/e2e/hy
commit: 5369306
src_loc: 5929
test_functions: 208
test_files: 19
dominant_test_styles: unit / integration / command workflow / parser-renderer behavior depending on module
public_docs: README, package public exports, public module/class/function names
core_fact_source: public `hy` API and user-visible command/workflow behavior
derived_views: Python API, CLI/command behavior when present, parse/render/validation/conversion outputs, public errors
external_deps: local Python dependencies only; no mandatory external service in retained subset
test_import_audit: clean — 0 rough private-import files
docs_test_alignment: aligned for retained subset; full upstream suite may include internal or standard-conformance stress tests
contamination_note: hy@5369306, relative to training cutoff: unknown
decision: keep
reason: language/compiler package with public reader/compiler/importer workflows and clean collection
risks: reference validation and candidate provenance must still pass before promotion
