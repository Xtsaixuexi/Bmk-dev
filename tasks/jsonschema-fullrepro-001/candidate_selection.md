# Candidate Selection: jsonschema

repo: jsonschema
source_path: /root/autodl-tmp/e2e/jsonschema
commit: 97c044c
src_loc: 4142
test_functions/nodeids collected: 8337
test_files_considered: 5
public_docs: README / public package exports
core_fact_source: public `jsonschema` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled during collection
private/import risk: 2 test files with package-private imports in rough scan; retained set reviewed by nodeid/file theme
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: validator/API/CLI package with large cleanly collected suite; retained subset avoids full saturation where possible.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases and will be audited after reference/candidate scoring.
