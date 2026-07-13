# Stage 2 Review: GLM 5.2

# Spec Review: diskcache-fullrepro-001

## Verdict
**Do not continue** — the candidate fails the body-completeness check and contains a truncated Public API section, which will break hidden-test filtering and downstream reconstruction.

## Findings

1. **Truncated spec body (critical).** The Public API section ends mid-sentence in `memoize_stampede`:
   > "...protects concurrent callers from r"

   The Recipes subsection, `DjangoCache`, `Cross-View Invariants`, `Representative Workflows`, `Non-Goals`, and `Evaluation Notes` headings are absent from the candidate body, even though the local validator reports them as PASS. This indicates the validator summary is stale or was run against a different candidate.

2. **Validator/body mismatch.** The local summary claims PASS for `heading_Cross-View Invariants`, `heading_Representative Workflows`, `heading_Non-Goals`, and `heading_Evaluation Notes`, but none of these headings appear in the supplied body. Hidden-test filtering will reject the candidate on these checks alone.

3. **Cross-view invariants not present in body.** The State Model lists 6 invariants, but the required `Cross-View Invariants` section (which the validator counts) is missing. Risk: `cross_view_count_ge_6` will fail on re-validation.

4. **Non-Goals missing.** No `Non-Goals` heading in body; `non_goals_present` will fail.

5. **Evaluation Notes missing.** Hidden tests commonly check for evaluation/observability hooks; absence will fail `heading_Evaluation Notes`.

6. **DjangoCache behavior undescribed.** Scope mentions `DjangoCache` and the import surface lists it, but no behavioral contract is given. Risk: hidden tests for optional Django compatibility have no spec anchor.

7. **Recipe contracts incomplete.** `throttle`, `barrier`, and `memoize_stampede` are named but their behavioral contracts (return values, error cases, concurrency semantics) are not fully specified due to truncation.

8. **Minor spec-quality observations (non-blocking):**
   - `push()` key space "starts around 500000000000000" is loose; hidden tests may probe boundary behavior. Recommend stating the exact base or marking it implementation-defined.
   - `check(fix=True)` "allowed to remove orphaned or inconsistent cache artifacts" is permissive; consider stating whether valid entries may be removed (currently ambiguous vs. "must not corrupt valid entries").
   - `volume()` "does not need to include filesystem directory metadata" is acceptable but could be tightened to "must include database + value files, may omit directory metadata."

## Required Fixes

1. **Restore the full spec body** from the point of truncation, including:
   - Completion of `memoize_stampede` contract (return value, beta/lock semantics, error behavior).
   - Full `DjangoCache` behavioral subsection (or explicit Non-Goal statement if out of scope).
   - `Cross-View Invariants` section with ≥6 invariants (state model invariants may be promoted/repeated here).
   - `Representative Workflows` section with concrete end-to-end scenarios (set/get, push/pull, fanout shard routing, Deque/Index persistence, recipe usage).
   - `Non-Goals` section (e.g., no network/distributed cache, no cross-process locking guarantees beyond documented local-file semantics, no schema stability guarantees).
   - `Evaluation Notes` section describing how hidden tests should probe observable behavior (e.g., via public API only, no schema introspection).
2. **Re-run the local validator** against the restored body and confirm all 11+ checks genuinely PASS on the submitted candidate.
3. **Tighten** `push()` key-space wording, `check(fix=True)` semantics, and `volume()` wording per Finding 8.

## Continue / Do not continue
**Do not continue** to Stage 3 until the truncated body is restored and the local validator is re-run against the actual candidate.
