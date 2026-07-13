# Stage 2 Spec Validation: jsonpickle-fullrepro-001

validated_at: 2026-07-09
spec_version: v1
result: PASS

## Public API Surface Processed

Top-level `jsonpickle` exports and documented public modules were reviewed before writing:

- `jsonpickle.encode`, `decode`, `dumps`, `loads`
- `jsonpickle.Pickler`, `jsonpickle.pickler.Pickler`, `jsonpickle.pickler.encode`
- `jsonpickle.Unpickler`, `jsonpickle.unpickler.Unpickler`, `jsonpickle.unpickler.decode`
- `jsonpickle.JSONBackend`, `jsonpickle.backend.JSONBackend`, shared backend `jsonpickle.json`
- top-level backend helpers: `set_preferred_backend`, `set_encoder_options`, `set_decoder_options`, `load_backend`, `remove_backend`, `enable_fallthrough`
- handler surface: `jsonpickle.register`, `jsonpickle.unregister`, `jsonpickle.handlers.BaseHandler`, `Registry`, `register`, `unregister`
- public error catch point: `jsonpickle.errors.ClassNotFoundError`

Names present only as private helpers, backend internals, test helper classes, or optional dependency internals were excluded from the candidate-visible contract.

## Reference Checks For Priority And Override Claims

The following priority/override statements were checked against the reference implementation with concrete conflicting inputs:

- `set_preferred_backend` puts a loaded backend first: verified by loading `os.path` with `split`/`join` and observing `encode("/hello/world")` use that backend.
- `classes` mapping overrides the serialized class path: verified by encoding an `OldThing` and decoding it as `NewThing` through a name mapping.
- a direct subclass handler overrides an ancestor `base=True` handler: verified with separate base and child handlers.
- `__getnewargs_ex__` takes precedence over `__getnewargs__`: verified with a class whose `__getnewargs__` raises if used.
- backend fallthrough raises the last backend exception when enabled and the first selected backend exception when disabled: verified with two in-memory failing backend modules.

## Required Validation Checklist

1. Public traceability: PASS. Each covered feature maps to README/docs public API, top-level exports, documented modules, or public test-observable behavior.
2. Internal names: PASS. Candidate-visible spec excludes private helpers and internal registry storage. Public metadata tag names are described only semantically, not as an implementation blueprint.
3. Behavioral language: PASS. Contract sections use `must`, `returns`, and `raises`; no `can`, `may`, `might`, or `should` wording remains in candidate-visible text.
4. Non-goals: PASS. Non-goals explicitly exclude exact JSON formatting/order, private internals, optional dependency internals, fixture shapes, cross-operation identity, unsafe decoding claims, and undocumented historical formats.
5. Hidden fixture assumptions: PASS. Workflows use generic examples, not upstream test helper classes or fixture modules.
6. Strong conditionals: PASS. Conditional behavior names the option or input condition, such as `keys=True`, `unpicklable=False`, `make_refs=False`, `warn=True`, `safe=False`, or missing class metadata.
7. Failure paths: PASS. Error Semantics covers backend failures, missing classes, invalid JSON, malformed byte payloads, invalid handler registration, base handler methods, unloaded/no backend, warnings, and fail-safe.
8. Product State Model: PASS. The spec defines original, flattened, encoded, and restored projections before per-domain sections.
9. Cross-view invariants: PASS. The spec includes 12 invariants spanning encode/decode, flatten/restore, references, keys, classes, handlers, backends, aliases, custom-handler context, and formatting.
10. No escape hatches: PASS. The scope and non-goals set explicit included/excluded behavior; optional dependency internals are routed out rather than left ambiguous.
11. Priority/override verification: PASS. All priority or override rules included in the spec were verified against reference behavior with concrete conflicting inputs or were omitted.

## Candidate Packet Consistency

- `spec/spec_v1.md` contains an INTERNAL header plus the candidate-visible body.
- `spec/spec_v1_candidate.md` contains only the candidate-visible body.
- root `spec.md` is byte-identical to `spec/spec_v1_candidate.md`.
- Candidate-visible required headings are present: Product Overview, Scope, Installable Surface, Product State Model, Public API, Error Semantics, Cross-View Invariants, Representative Workflows, Non-Goals, and Evaluation Notes.

## Known Uncertainties Routed To Later Stages

- Stage 3 should filter tests that assert exact JSON object member order, whitespace, or backend-specific escaping outside explicitly requested formatting options.
- Stage 3 should filter optional dependency internals for numpy, pandas, sklearn, bson, sqlalchemy, yaml, ecdsa, gmpy2, and feedparser unless a test maps only to generic public handler behavior.
- Stage 3 should filter tests that inspect private backend fields or private helper functions rather than observable backend manager behavior.

## Review Correction

DeepSeek v4 Pro Stage 2 review requested two explicit public wire-format details. The candidate spec was patched to enumerate jsonpickle wire tags such as `py/object`, `py/type`, `py/state`, `py/id`, `py/ref`, `py/tuple`, `py/set`, `py/b64`, `py/b85`, and the `json://` key escape prefix, and to define `v1_decode=True` as legacy v1 reference-number decoding for plain dictionaries. The patch keeps candidate-visible text as public API documentation and does not add benchmark metadata.
