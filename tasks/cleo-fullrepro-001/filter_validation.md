# Filter Validation: cleo-fullrepro-001

## Summary

- collected nodeids processed: 258
- retained upstream nodeids: 87
- generated nodeids: 0
- source-only exclusions: 105
- mechanical/protocol exclusions: 66
- spec gaps: 0
- oracle count: 87
- oracle source: upstream_only

## Layer Counts

- integration: 22
- atomic: 54
- system_e2e: 11

## Spec Section Counts

- Error Semantics: 6
- Command: 3
- Product State Model: 3
- Events, Loaders, and Testers: 12
- Arguments, Options, and Input Definitions: 16
- Input Parsing: 18
- Application: 8
- Output, Formatting, and IO: 5
- Cross-View Invariants: 5
- Representative Workflows: 2
- Command With Argument and Flag Option: 1
- Interactive Question: 3
- Formatting Styles and Helpers: 5

## Gates

- Reference gate: PASS. Direct upstream pytest and isolated scorer both passed 87 / 87 retained nodeids.
- Dummy gate: PASS. 0 passed / 87 retained nodeids against a local unimplemented dummy `cleo` package.
- Taxonomy gate: PASS. `taxonomy.jsonl` uses scorer-compatible dotted keys and the isolated scorer reported non-zero atomic, integration, and system_e2e buckets.
- Scorer isolation gate: PASS. `score_pytest_original.py` was run with `--remove-path src/cleo`; imports resolved to `/root/autodl-tmp/new-e2e/python-poetry__cleo/src/cleo/__init__.py` through the reference `solution_dir`.
- Spec map gate: PASS. All 258 collected nodeids are classified, and every covered row maps to a heading present in `spec.md`.
- Coverage floor: PASS for the primary behavioral sections used by the retained oracle. Error Semantics has 6 rows, Cross-View Invariants has 5, Output/Formatting/IO has 5, Formatting Styles and Helpers has 5, Application has 8, Command has 3, Input Parsing has 18, Arguments/Options has 16, and Events/Loaders/Testers has 12. Representative workflow behavior is covered by retained tester/application/question rows; the upstream suite has no fair reference-passing public single-command-application nodeid after exact snapshot and missing-reference-API gates.

## Exclusion Policy Applied

Excluded tests that assert exact shell completion scripts, help/list/version snapshots, ANSI byte sequences, table border/layout snapshots, traceback line rendering, exact exception-message wording, terminal/environment behavior, private `_utils` imports, private `_tokens` assertions, collected fixture helpers, and fixture-only Python inheritance that passed the dummy gate.

## Track B Decision

Track B was not triggered. Track A retained 87 scoreable reference-passing nodeids, above the 50-test global floor, with non-zero atomic, integration, and system_e2e coverage. Generating tests for the spec's single-command `Command.default()` example would not pass the current reference because the method is absent; this is recorded as a coverage caveat for review rather than patched in Stage 3.
