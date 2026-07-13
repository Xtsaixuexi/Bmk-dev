# Judge Diagnosis: diskcache-fullrepro-001

verdict: QUALIFIED
spec_version: v1
filter_version: generated_filter_v2
candidate_run: opencode-gpt-5.5-diskcache-fullrepro-001-20260709T-stage4-cleanroom

## Preflight output

Command:

```bash
python -c "import diskcache; print(diskcache.__file__)"
```

Output:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-diskcache-fullrepro-001-20260709T-stage4-cleanroom/output/diskcache/__init__.py
```

The path points into the candidate output directory, not the reference source tree or an installed package.

## Anti-Cheat Scan

No cheating evidence was found in the candidate implementation. A scan of candidate-visible files found only the prompt/metadata prohibition text for hidden-artifact terms; no candidate code references the source repository, oracle tests, kept nodeids, taxonomy, spec-test map, reference score, previous outputs, or API key file. The candidate run was executed in `/tmp` with only `prompt.md` and an empty `output/` directory, then persisted to `candidate-runs/` after generation.

## Solvability

Reference oracle passes the corrected final scoring set under scorer isolation:

- reference: 63/63
- pass_rate_excluding_skips: 1.0
- dummy gate: 0/63 passed

## Candidate Score

- score: 61/63
- pass_rate_excluding_skips: 0.9682539682539683

```json
{
  "atomic": {
    "passed": 22,
    "total": 22
  },
  "integration": {
    "failed": 2,
    "passed": 31,
    "total": 33
  },
  "system_e2e": {
    "passed": 8,
    "total": 8
  }
}
```

## Fairness Corrections

Initial scoring exposed generated-oracle overreach. The filter was corrected before final scoring by removing assertions about `fromcache()` object identity, `Index(directory, pairs)` positional constructor shape, and extra release exception details not explicit in the spec. After correction, dummy remains 0/63, reference remains 63/63, and candidate improves to 61/63. The two remaining failures are spec-driven and behavioral.

## Gate A - Spec Mapping Spot-Check

Sampled covered rows map to real spec sections and expected outcomes are derivable from the spec:

| test | mapped section | verdict |
|---|---|---|
| `test_cache_length_counts_expired_entries_until_cleanup` | Cache + Cross-View Invariants | PASS |
| `test_fanout_reset_updates_shard_settings` | FanoutCache + Cross-View Invariants | PASS |
| `test_cache_file_like_value_round_trip` | Cache + Cross-View Invariants + Representative Workflows | PASS |
| `test_fanout_child_deque_reopens_named_state` | FanoutCache + Cross-View Invariants + Representative Workflows | PASS |
| `test_memoize_stampede_caches_result_and_exposes_key` | Recipes | PASS |

## Gate B - Failure Pattern Audit

The remaining two failures check observable public behavior, not private fields, SQL, filenames, repr strings, or exception message text. Reference passes both failures. Candidate implementation diverges from the candidate-visible spec.

## Gate C - Generated-Only Oracle Spot-Check

The oracle is marked `generated_only`, so generated tests were manually spot-checked:

| test | spec-driven | behavioral | note |
|---|---|---|---|
| `test_cache_length_counts_expired_entries_until_cleanup` | yes | yes | Checks public `len(cache)` and `expire()` lifecycle. |
| `test_fanout_reset_updates_shard_settings` | yes | yes | Checks public `FanoutCache.reset()` and public setting attribute visibility. |
| `test_cache_file_like_value_round_trip` | yes | yes | Checks public read/write bytes behavior only. |
| `test_fanout_child_index_reopens_named_state` | yes | yes | Checks public child view persistence. |
| `test_index_persists_by_directory` | yes | yes | Checks public `Index` persistence through directory. |
| `test_public_constants_and_exports_are_available` | yes | yes | Checks installable surface and public exception/warning classes. |

Gate C verdict: PASS.

## Gate D - Coverage Gap Audit

| spec section | uncovered behaviors | impact | recommendation |
|---|---|---|---|
| none | none | none | no action required |

Coverage counts:

```json
{
  "Cache": 28,
  "Error Semantics": 8,
  "Cross-View Invariants": 26,
  "Representative Workflows": 9,
  "Disk and JSONDisk": 1,
  "FanoutCache": 11,
  "Deque": 8,
  "Index": 7,
  "Recipes": 7,
  "Installable Surface": 1
}
```

Coverage verdict: FULL.

## Real Failure Clusters

1. `state-management`: candidate treats an entry stored with `expire=0` as absent from `len(cache)` immediately. The spec states `len(cache)` returns stored count before explicit expiration cleanup and expired entries remain eligible to be counted until `expire()` or a writing operation removes them. Affected test: `test_cache_length_counts_expired_entries_until_cleanup`.
2. `cross-view-consistency`: candidate `FanoutCache.reset("size_limit", 2048)` returns `2048` but does not expose `fanout.size_limit`. The spec states `reset(setting, value)` updates both durable setting and matching public attribute visible from compatible cache objects. Affected test: `test_fanout_reset_updates_shard_settings`.

## Cascade Analysis

The failures are two independent integration-level root causes. There are no collection errors and no atomic/system cascade failures after fairness correction.

## Labels

- qualified
- generated-only-spotchecked
- high-candidate-score
- expiration-state-signal
- settings-cross-view-signal

## Verdict

QUALIFIED. Hard gates pass: clean import provenance, no cheat evidence, reference 63/63, dummy 0/63, oracle count 63, Gate C spot-check passed, and Gate D coverage verdict FULL. Remaining candidate failures are valid model capability signals.
