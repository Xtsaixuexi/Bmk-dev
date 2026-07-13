# Stage 2 Review: DeepSeek v4 Pro

## Review: diskcache-fullrepro-001

**Verdict**: FAIL  
**Continue**: **Do not continue** until critical missing description is completed.

### Findings

1. **Incomplete specification (CRITICAL)**: The `memoize_stampede` description is truncated mid-sentence. The spec does not define its full behavior, pre- stampede protection mechanism, or expected return‑value semantics. This gap will cause hidden tests that rely on this recipe to fail immediately.

2. **Ambiguity – expired items in pull/peek**  
   - `pull` and `peek` do not describe what happens when the next key is expired. Since expired keys are considered “missing”, `pull`/`peek` should skip them, but the spec does not state this. Tests that mix `push` with expiration and `pull` will be unpredictable.

3. **Undefined key generation for push**  
   - The spec mentions a default integer space starting near `500000000000000` but does not say how keys are generated (monotonically increasing? how are gaps handled?). This affects reproducibility across processes.

4. **Missing semantics for `retry` parameter**  
   - Many methods accept `retry=False` but the retry strategy (number of attempts, delay, retry-on‑which exceptions) is unspecified. Hidden tests exercising retry paths may fail if the implementation defaults to a different behaviour.

5. **`FanoutCache.transact` behaviour unclear**  
   - The spec says `transact()` “must be rejected or unavailable”, but does not list it as part of `FanoutCache`’s API nor specify what happens if a caller attempts `fanout.transact()`. A precise exception/error contract is needed.

6. **`expire(now=…)` cutoff ambiguous**  
   - The description does not specify whether expired keys are those with `timestamp <= now` or `timestamp < now`. This off‑by‑one can affect hidden tests that supply an explicit `now`.

7. **`reset` attribute refresh unspecified**  
   - “refresh the matching public attribute” is mentioned without defining which attributes map to which settings. Tests that verify side‑effects of `reset` will be unreliable.

8. **`memoize` argument equality undefined**  
   - “same effective arguments” is not defined. Hidden tests that rely on distinguishing equal-but-not‑identical objects or on `typed=True` may behave differently.

### Required Fixes

- **Complete the `memoize_stampede` specification** – define full behaviour, stampede protection mechanism, return value, and interaction with `expire`, `tag`, `beta`.
- **Clarify pull/peek expiration** – explicitly state that expired items are skipped and removed, similar to `get`.
- **Specify push key generation** – describe the key sequence and whether gaps are possible.
- **Document `retry` behaviour** – number of retries, delay, and which exceptions trigger a retry.
- **Define `FanoutCache.transact` error contract** – either remove it or state it raises `NotImplementedError` (or equivalent).
- **Define `expire(now)` cutoff semantics** – use unambiguous language (`<` vs `<=`).
- **Explicitly list `reset` attribute mappings** – map each known setting to its public attribute (e.g., `'size_limit'` → `cache.size_limit`).
- **Define argument equality for `memoize`** – reference the key‑generation algorithm used (e.g., `diskcache` default hashing, `typed` semantics).

Only after these clarifications should the task proceed to implementation.
