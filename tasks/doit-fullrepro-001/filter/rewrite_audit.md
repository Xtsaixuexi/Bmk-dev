# Rewrite Audit: doit-fullrepro-001

## Track A Source

- upstream test root: `/root/autodl-tmp/new-e2e/pydoit__doit/tests`
- collected nodeids processed: 909
- upstream nodeids retained without rewrite: 438
- upstream nodeids excluded: 471
- rewritten upstream tests: 0
- generated tests: 0

## Shared Fixture Audit

Shared upstream fixture/support files were read for import risk. `tests/support.py` imports public `doit` modules and standard-library helpers. No candidate-visible oracle depends on private `doit._*` imports. Helper collection artifacts from support/sample files are excluded from scoring.

## Rewrite Decisions

No source tests were rewritten into a separate test module. The retained oracle uses original upstream nodeids only when the test body maps to a public behavior in `spec.md` and avoids private state, exact help/completion/traceback formatting, platform-specific strace details, optional auto-watch behavior, and DBM implementation file-extension assumptions.

## Exclusion Summary

- `excluded`: 436 nodeids. Reasons include helper/non-test collection artifacts, direct private method/state access, exact command transcript tests, shell completion exact script checks, platform-specific strace behavior, source-root optional backend skips, and dummy-gate passes.
- `source-only`: 35 nodeids. Reasons include repr/string-format assertions, helper stream internals, exact parser help formatting, exact exception string wording, and internal serialization shape.
- `spec_gap`: 0 nodeids. No spec patch was required.

## Retained Coverage Summary

- Actions: 65
- Command, Loader, Parser, Plugin, and Reporter APIs: 50
- Cross-View Invariants: 14
- Dependency State: 144
- Embedded Execution API: 3
- Error Semantics: 55
- Installable Surface: 1
- Task Loading: 37
- Task Object API: 48
- Top-Level API: 1
- Up-To-Date Helpers and Tools: 20

## Gate Results

- Reference gate: 438 passed / 438 collected.
- Dummy gate: 0 passed, 296 failed, 142 error / 438 collected.
