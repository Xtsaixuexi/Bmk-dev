

# Stage 1 Review: new-e2e Batch 2

## Verdict: **PASS**

## Blockers: None

All five candidates meet Stage 1 hard gates and have complete handoff artifacts. No corrections required before Stage 2.

---

## Per-Task Assessment

| Task | LOC | Nodeids | Private Import | Network Risk | Snapshot Risk | Assessment |
|------|-----|---------|----------------|--------------|---------------|------------|
| `pyyaml-fullrepro-001` | 5238 | 2616 | 0.04 ✓ | 0.04 ✓ | 0.0 ✓ | Clean. Strong test coverage. Proceed. |
| `pgpy-fullrepro-001` | 7307 | 1114 | 0.083 ✓ | **0.333 ⚠️** | 0.167 ⚠️ | Network risk exceeds 30% threshold; snapshot rate elevated. Documented for Stage 3 filtering. Proceed with caution. |
| `jsonpickle-fullrepro-001` | 4128 | 784 | 0.0 ✓ | 0.15 ✓ | 0.0 ✓ | Clean. Zero private import risk. Proceed. |
| `cleo-fullrepro-001` | 6009 | 258 | 0.033 ✓ | 0.0 ✓ | 0.098 ✓ | Lowest nodeid count in batch (258). Adequate but verify scoreable floor after filtering. Proceed. |
| `watchdog-fullrepro-001` | 5427 | 199 | 0.0 ✓ | 0.077 ✓ | 0.038 ✓ | Lowest nodeid count (199). Timing/platform sensitivity noted. Proceed with caution. |

---

## Required Corrections: None

## Downstream Cautions (Stage 2/3)

1. **PGPy**: Network marker rate (33.3%) exceeds typical 30% threshold. Stage 3 must aggressively filter network-dependent tests or mock external dependencies. Snapshot rate (16.7%) also elevated—audit for brittleness.

2. **cleo**: Only 258 collected nodeids from 61 test files. Verify that post-filtering leaves sufficient scoreable tests. CLI exact-output assertions must be rewritten to behavioral checks.

3. **watchdog**: Only 199 collected nodeids. Filesystem observer tests are timing/platform-sensitive. Stage 3 should prioritize deterministic event/pattern behavior tests.

4. **All tasks**: Stage 3 must audit retained tests for spec traceability, private internal dependencies, and public contract alignment before finalizing the oracle.

---

## Stage 1 Gate Verification

| Gate | Status |
|------|--------|
| Logical de-duplication | ✓ Confirmed via `clone_manifest.json` queue |
| Existing task exclusion | ✓ First batch (`doit`, `pymdown-extensions`, `prompt-toolkit`) already in Stage 2 |
| LOC ≥ 3000 | ✓ All five pass (4128–7307) |
| Clean pytest collect | ✓ All `COLLECT_OK` with 0 error markers |
| Private import < 30% | ✓ All pass (0.0–0.083) |
| Handoff artifacts complete | ✓ All six required files present per task |

---

**Proceed to Stage 2.**