# Bandit Filter Notes

## Oracle Composition

- Upstream public rewrites: 6 nodeids from `Issue` behavior.
- Generated public oracle: 84 nodeids.
- Final scoreable oracle: 90 nodeids.
- Reference gate: 100% pass.
- Dummy gate: 0% pass (all 90 tests failed the NotImplemented dummy).

## Filtering Decision

The upstream suite is saturated with bidirectional `bandit.core` manager, config,
metrics, formatter, extension-loader, source-tree fixture, and exact-output dependencies.
`filter/rewrite_audit.md` and `filter/candidate_filter_map.md` account for all 24 files
and 264 test functions. Six `Issue` tests were safely rewritten through top-level public
imports; Track B supplies the remaining behavior coverage.

## Fairness Boundaries

- No private import or private assertion is scoreable.
- No exact human diagnostic wording is scoreable.
- Detection assertions require public test IDs, not exact issue prose.
- Variable timestamps and path prefixes are not exact-matched.
- CLI tests use `python -m bandit` so candidate provenance can be isolated.
