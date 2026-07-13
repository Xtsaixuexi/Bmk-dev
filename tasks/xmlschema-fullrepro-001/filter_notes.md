repo: xmlschema
source_path: /root/autodl-tmp/e2e/xmlschema
commit: 627c179
src_loc: 24391
test_functions: 915
test_files: 50
dominant_test_styles: unit / integration / command workflow / parser-renderer behavior depending on module
public_docs: README, package public exports, public module/class/function names
core_fact_source: public `xmlschema` API and user-visible command/workflow behavior
derived_views: Python API, CLI/command behavior when present, parse/render/validation/conversion outputs, public errors
external_deps: local Python dependencies only; no mandatory external service in retained subset
test_import_audit: clean — 0 rough private-import files
docs_test_alignment: aligned for retained subset; full upstream suite may include internal or standard-conformance stress tests
contamination_note: xmlschema@627c179, relative to training cutoff: unknown
decision: keep
reason: schema/resource/validation/conversion package with broad public behavior and clean collection
risks: reference validation and candidate provenance must still pass before promotion
