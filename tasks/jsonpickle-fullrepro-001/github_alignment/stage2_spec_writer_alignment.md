# Stage 2 Spec Writer Alignment: jsonpickle-fullrepro-001

date: 2026-07-09
stage: 2
status: S2_SPEC_DONE_PENDING_REVIEW

## Workflow Inputs

Read and followed:

- `github_alignment/raw_main/skills/spec-writer/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- `PIPELINE_STATE.md`
- `candidate_selection.md`
- `filter_notes.md`
- `source_audit.json`

The local state was `S2_SPEC_IN_PROGRESS`. The requested user exit state for this run is `S2_SPEC_DONE_PENDING_REVIEW`, so this stage stops at review handoff and does not advance to Stage 3.

## Source Boundary

Repository inspected: `/root/autodl-tmp/new-e2e/jsonpickle__jsonpickle`

Public documentation and package metadata:

- `README.rst`
- `pyproject.toml`
- `docs/api.rst`
- `docs/examples.rst`
- `docs/extensions.rst`
- `examples/custom_handler_context.py`
- `examples/changing_class_path.py`

Public package and behavior sources:

- `jsonpickle/__init__.py`
- `jsonpickle/pickler.py`
- `jsonpickle/unpickler.py`
- `jsonpickle/handlers.py`
- `jsonpickle/backend.py`
- `jsonpickle/errors.py`
- `jsonpickle/tags.py`
- `jsonpickle/util.py`

Representative public behavior tests sampled:

- `tests/jsonpickle_test.py`
- `tests/object_test.py`
- `tests/handler_test.py`
- `tests/backend_test.py`
- `tests/collections_test.py`
- `tests/datetime_test.py`
- `tests/stdlib_test.py`
- `tests/zoneinfo_test.py`

## Inclusion Decisions

Included public contract areas:

- high-level `encode`/`decode` and `dumps`/`loads` aliases;
- low-level `Pickler.flatten` and `Unpickler.restore`;
- `unpicklable`, `make_refs`, `keys`, `numeric_keys`, references, cycles, class metadata, missing class behavior, and trusted decode warnings;
- custom handler registration, base handler behavior, handler context, and handler precedence;
- public backend loading, preferred backend selection, backend options, removal, and fallthrough behavior;
- fail-safe, warning, readonly, property, depth, iterator, bytes/base85/base64, and pickle protocol state behavior where user-visible.

Excluded from candidate-visible scope:

- optional dependency internals and extension-specific data formats;
- exact JSON member order, whitespace, and backend escaping outside requested formatting options;
- private helper functions, private fields, and internal registry/list shapes;
- upstream test helper class names and fixture module shapes.

## Verification Performed

Text checks:

- root `spec.md` is byte-identical to `spec/spec_v1_candidate.md`;
- candidate spec contains no INTERNAL header;
- required headings are present;
- no `can`, `may`, `might`, `should`, `possibly`, or `when applicable` wording remains in candidate-visible text.

Reference checks with concrete conflicting inputs:

- preferred backend order;
- `classes` mapping override;
- direct handler over base handler;
- `__getnewargs_ex__` over `__getnewargs__`;
- backend fallthrough enabled/disabled exception behavior.

## Outputs

Created:

- `spec/spec_v1.md`
- `spec/spec_v1_candidate.md`
- `spec/spec_validation.md`
- `spec.md`
- `github_alignment/stage2_spec_writer_alignment.md`

Updated:

- `PIPELINE_STATE.md`

## Review Notes

The candidate-visible spec is intentionally focused on jsonpickle core public behavior. It does not attempt to document every optional extension or private helper because those are expected Stage 3 filter exclusions unless a test maps cleanly to the public behavior described in the spec.

After DeepSeek v4 Pro review, the spec explicitly documents jsonpickle wire tags and `v1_decode` behavior while preserving the candidate-visible/public-doc style required by the current Bmk-dev spec-writer workflow.
