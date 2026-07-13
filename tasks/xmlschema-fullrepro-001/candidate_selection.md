# Candidate Selection: xmlschema

repo: xmlschema
source_path: /root/autodl-tmp/e2e/xmlschema
commit: 627c179
src_loc: 24391
test_functions/nodeids collected: 1542
test_files_considered: 9
public_docs: README / public package exports
core_fact_source: public `xmlschema` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled during collection
private/import risk: 0 test files with package-private imports in rough scan; retained set reviewed by nodeid/file theme
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: schema/resource/validation/conversion package with broad public behavior and clean collection.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases and will be audited after reference/candidate scoring.
