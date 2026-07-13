# Candidate Selection: rich

repo: rich
source_path: /root/autodl-tmp/e2e/rich
commit: 9d8f9a3
src_loc: 35251
test_functions/nodeids collected: 981
test_files_considered: 9
public_docs: README / public package exports
core_fact_source: public `rich` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled during collection
private/import risk: 11 test files with package-private imports in rough scan; retained set reviewed by nodeid/file theme
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: large console rendering library with multiple public projections and clean collection after local markdown-it-py dependency is on PYTHONPATH.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases and will be audited after reference/candidate scoring.
