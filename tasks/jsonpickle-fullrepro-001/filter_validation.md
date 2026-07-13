# Filter Validation: jsonpickle-fullrepro-001

## Summary

- upstream collection rows processed: 784
- unique collected nodeids: 440
- retained upstream nodeids: 12
- generated nodeids: 64
- source/protocol exclusions: 772
- spec gaps: 0
- oracle count: 76
- oracle source: mixed upstream-filtered and generated tests

## Layer Counts

- atomic: 13
- integration: 53
- system_e2e: 10

## Spec Section Counts

- Installable Surface: 3
- Product State Model: 19
- Public API: 18
- Encoding And Decoding Behavior: 22
- References, Cycles, And Identity: 16
- Dictionary Key Semantics: 10
- Class Metadata And Missing Classes: 7
- Custom Handlers: 5
- JSON Backend Selection: 7
- Error Semantics: 7
- Cross-View Invariants: 24
- Representative Workflows: 5

## Gates

- Accounting gate: PASS. Track A accounts for all 784 upstream collection rows: 12 retained and 772 excluded.
- Reference gate: PASS. The isolated scorer passed 76 / 76 oracle nodeids with `--remove-path jsonpickle`.
- Dummy gate: PASS. 0 / 76 oracle nodeids passed against the local dummy `jsonpickle` package.
- Taxonomy gate: PASS. `taxonomy.jsonl` uses scorer-compatible keys and the reference score reports non-zero atomic, integration, and system_e2e buckets with no unknown layer.
- Scorer isolation gate: PASS. The scorer copies `filter/oracle_source`, removes the `jsonpickle` package, and imports the reference solution from `/root/autodl-tmp/new-e2e/jsonpickle__jsonpickle`.
- Spec map gate: PASS. `spec_test_map.md` classifies upstream rows and generated oracle rows, and every covered row maps to a public spec heading.
- Coverage floor: PASS. The final oracle has 76 scoreable nodeids, above the 50-test global floor, and every required behavior section meets its minimum in `filter/coverage_floor.json`.

## Track B Decision

Track B was triggered because Track A retained only 12 upstream public-behavior nodeids after excluding implementation-specific, protocol-specific, optional-backend, duplicate collection, and exact-format tests. The 64 generated tests fill public spec coverage without exposing source, upstream tests, kept nodeids, taxonomy, score reports, or other hidden artifacts to candidates.
