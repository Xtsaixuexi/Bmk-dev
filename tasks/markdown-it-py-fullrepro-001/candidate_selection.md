# Candidate Selection: markdown-it-py

repo: markdown-it-py
source_path: /root/autodl-tmp/e2e/markdown-it-py
commit: 2c3f71e
src_loc: 5221
test_functions/nodeids collected: 981
test_files_considered: 10
public_docs: README / public package exports
core_fact_source: public `markdown_it` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled during collection
private/import risk: 0 test files with package-private imports in rough scan; retained set reviewed by nodeid/file theme
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: Markdown parser/renderer with public API, CLI, plugin, token, and tree surfaces.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases and will be audited after reference/candidate scoring.
