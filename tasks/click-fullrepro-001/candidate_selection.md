# Candidate Selection: click

repo: click
source_path: /root/autodl-tmp/e2e/click
commit: 679a7a0
src_loc: 9985
test_functions/nodeids collected: 32699
test_files_considered: 30
public_docs: README.md
core_fact_source: public `click` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled
private/import risk: filtered by nodeid/file heuristics; private/internal obvious tests excluded
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: source LOC and filtered reference-passing tests meet this batch's automated full-reconstruction criteria.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases.
