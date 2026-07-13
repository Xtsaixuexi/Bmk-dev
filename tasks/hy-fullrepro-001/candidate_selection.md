# Candidate Selection: hy

repo: hy
source_path: /root/autodl-tmp/e2e/hy
commit: 5369306
src_loc: 5929
test_functions/nodeids collected: 636
test_files_considered: 8
public_docs: README / public package exports
core_fact_source: public `hy` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled during collection
private/import risk: 0 test files with package-private imports in rough scan; retained set reviewed by nodeid/file theme
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: language/compiler package with public reader/compiler/importer workflows and clean collection.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases and will be audited after reference/candidate scoring.
