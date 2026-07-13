# Review Verdict
**Verdict:** NEEDS_CORRECTION
**Blockers:** None
**Required Corrections:**
1. **Missing reserved metadata keys.** The spec states “objects must carry class metadata using jsonpickle’s reserved metadata keys” and requires decode to recognise them but does not enumerate the keys (e.g., `py/object`, `py/type`, `py/tuple`, etc.). These are non‑derivable and essential for a candidate to produce a compatible implementation. Add the exact key names and their meaning.
2. **`v1_decode` behaviour undefined.** The option `v1_decode` appears in the public API signatures but is not described anywhere in the behavioural sections. A candidate cannot implement its effect. Specify the observable behaviour when `v1_decode=True` for both encoding and decoding.

**Proceed/Stop:** Stop. Apply the required corrections to the spec before advancing to Stage 3 test filtering.

## Rationale
The specification otherwise meets the gate requirements: it reads as public library documentation, contains no benchmark metadata, and includes all required sections (Product State Model, error semantics, invariants, workflows, non‑goals, evaluation notes). However, two critical gaps violate the principle that every non‑derivable contract detail must be explicit. The reserved metadata keys and the `v1_decode` behaviour are part of the library’s public wire format and API contract; omitting them could cause preventable test failures. Once these are added, the spec will satisfy all 11 validation checks and be ready for Stage 3.
