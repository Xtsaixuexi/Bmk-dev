# Candidate Selection: dateutil

repo: dateutil
source_path: /root/autodl-tmp/e2e/dateutil
commit: 48bd1af
src_loc: 5950
test_functions/nodeids collected: 1517
test_files_considered: 10
public_docs: README.rst
core_fact_source: public `dateutil` package behavior and caller-visible values
external_deps: no external service required for retained tests; pytest plugin autoload disabled
private/import risk: filtered by nodeid/file heuristics; private/internal obvious tests excluded
docs_test_alignment: aligned enough for retained public API behavior subset
decision: keep
reason: source LOC and filtered reference-passing tests meet this batch's automated full-reconstruction criteria.
risks: automated spec is concise; some upstream tests may still encode package-specific edge cases.
