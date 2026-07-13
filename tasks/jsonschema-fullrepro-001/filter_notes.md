repo: jsonschema
source_path: /root/autodl-tmp/e2e/jsonschema
commit: 97c044c
src_loc: 4142
test_functions: 368
test_files: 13
dominant_test_styles: unit / integration / command workflow / parser-renderer behavior depending on module
public_docs: README, package public exports, public module/class/function names
core_fact_source: public `jsonschema` API and user-visible command/workflow behavior
derived_views: Python API, CLI/command behavior when present, parse/render/validation/conversion outputs, public errors
external_deps: local Python dependencies only; no mandatory external service in retained subset
test_import_audit: HIGH_RISK — 2 rough private-import files
docs_test_alignment: aligned for retained subset; full upstream suite may include internal or standard-conformance stress tests
contamination_note: jsonschema@97c044c, relative to training cutoff: unknown
decision: keep
reason: validator/API/CLI package with large cleanly collected suite; retained subset avoids full saturation where possible
risks: reference validation and candidate provenance must still pass before promotion
