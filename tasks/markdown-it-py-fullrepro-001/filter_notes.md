repo: markdown-it-py
source_path: /root/autodl-tmp/e2e/markdown-it-py
commit: 2c3f71e
src_loc: 5221
test_functions: 91
test_files: 17
dominant_test_styles: unit / integration / command workflow / parser-renderer behavior depending on module
public_docs: README, package public exports, public module/class/function names
core_fact_source: public `markdown_it` API and user-visible command/workflow behavior
derived_views: Python API, CLI/command behavior when present, parse/render/validation/conversion outputs, public errors
external_deps: local Python dependencies only; no mandatory external service in retained subset
test_import_audit: clean — 0 rough private-import files
docs_test_alignment: aligned for retained subset; full upstream suite may include internal or standard-conformance stress tests
contamination_note: markdown-it-py@2c3f71e, relative to training cutoff: unknown
decision: keep
reason: Markdown parser/renderer with public API, CLI, plugin, token, and tree surfaces
risks: reference validation and candidate provenance must still pass before promotion
