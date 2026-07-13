# Filter Validation: doit-fullrepro-001

## Summary

- collected nodeids processed: 909
- retained upstream nodeids: 438
- generated nodeids: 0
- source-only exclusions: 35
- mechanical/protocol exclusions: 436
- spec gaps: 0
- oracle count: 438
- oracle source: upstream_only

## Layer Counts

- atomic: 230
- integration: 207
- system_e2e: 1

## Spec Section Counts

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

## Gates

- Reference gate: PASS. Direct upstream pytest gate and isolated scorer gate both passed 438 / 438 retained nodeids; no skipped nodeids remain.
- Dummy gate: PASS. 0 passed / 438 retained nodeids against dummy implementation.
- Taxonomy gate: PASS. `taxonomy.jsonl` uses scorer-compatible dotted keys and has non-zero counts for atomic, integration, and system_e2e layers.
- Scorer isolation gate: PASS. `score_pytest_original.py` was run with `--remove-path doit` against an oracle worktree whose `doit` package directory was removed; `--rootdir` was pinned to the oracle worktree so pytest json nodeids match `kept_nodeids.txt`.
- Spec map gate: PASS. Every covered row maps to a heading present in `spec.md`.

## Exclusion Policy Applied

Excluded tests that assert exact help text, exact traceback or exception message wording, shell completion exact script content, DBM implementation-specific file extensions, private helper or private method access, optional auto-watch behavior, platform-specific strace details, internal runner/control scheduling, and tests that passed the dummy gate.

## Caveats

The retained set is upstream-only and strongly covers atomic and integration behavior. Only one upstream test qualifies as system_e2e under the strict taxonomy after excluding command transcript and private-runner tests. Track B was not used because the retained oracle is well above the 50-test floor and covers the public API, state, error, task loading, action, dependency, and tool surfaces.
