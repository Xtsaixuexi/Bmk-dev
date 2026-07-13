# Spec Validation: pyyaml-fullrepro-001 v1

## Source Review

- Read Stage 1 artifacts: `PIPELINE_STATE.md`, `candidate_selection.md`, `filter_notes.md`, `source_audit.json`, Stage 1 alignment, and both Stage 1 reviews.
- Read workflow authorities: `github_alignment/raw_main/skills/spec-writer/SKILL.md` and `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`.
- Read source package public entry points and exports under `/root/autodl-tmp/new-e2e/yaml__pyyaml/lib/yaml`.
- Read source README and `pyproject.toml`.
- Read representative public-behavior tests for loading, dumping, type resolution, extension hooks, tokens/events/nodes, errors, marks, merge keys, Unicode streams, and sorting.
- Ran reference probes with `PYTHONPATH=/root/autodl-tmp/new-e2e/yaml__pyyaml/lib` to verify required `Loader` for `load`, single-document errors, `safe`/`full`/`unsafe` tag boundaries, dump return types under `encoding`, stream type errors, resolver scoping, `BaseLoader` scalar behavior, and invalid path resolver errors.

## Public API Surface List

Top-level `yaml`:

- Functions: `scan`, `parse`, `compose`, `compose_all`, `load`, `load_all`, `safe_load`, `safe_load_all`, `full_load`, `full_load_all`, `unsafe_load`, `unsafe_load_all`, `emit`, `serialize`, `serialize_all`, `dump`, `dump_all`, `safe_dump`, `safe_dump_all`, `add_constructor`, `add_multi_constructor`, `add_representer`, `add_multi_representer`, `add_implicit_resolver`, `add_path_resolver`, `warnings`.
- Classes: `BaseLoader`, `SafeLoader`, `FullLoader`, `Loader`, `UnsafeLoader`, `BaseDumper`, `SafeDumper`, `Dumper`, `YAMLObject`, `YAMLObjectMetaclass`, token classes, event classes, node classes, `Mark`, `YAMLError`, `MarkedYAMLError`.
- Optional classes: `CBaseLoader`, `CSafeLoader`, `CFullLoader`, `CUnsafeLoader`, `CLoader`, `CBaseDumper`, `CSafeDumper`, `CDumper` when LibYAML bindings are installed.

Public submodule exports:

- `yaml.constructor`: `BaseConstructor`, `SafeConstructor`, `FullConstructor`, `UnsafeConstructor`, `Constructor`, `ConstructorError`.
- `yaml.representer`: `BaseRepresenter`, `SafeRepresenter`, `Representer`, `RepresenterError`.
- `yaml.resolver`: `BaseResolver`, `Resolver`; `ResolverError` is included because public resolver calls raise it.
- Error-producing submodules export reader/scanner/parser/composer/emitter/serializer base classes and error classes; the spec names error classes because callers observe them through raised exceptions.

## Inclusion Decisions

- Included loading, dumping, and safe/full/unsafe loader boundaries because they are the primary documented API and contain PyYAML-specific security and tag behavior.
- Included YAML scalar and collection type mappings because they are library-specific and not fully derivable from general YAML knowledge.
- Included stream encoding and dump return-type semantics because tests and public behavior depend on them and they are not obvious.
- Included token, event, and node classes only as public data projections and constructor/attribute contracts; private scanner/parser implementation state is excluded.
- Included constructor, representer, resolver, and `YAMLObject` hooks because these are public extension APIs used by callers.
- Included `Mark` and `YAMLError` behavior because callers catch these errors and inspect marks.
- Included optional C-backed names only as availability and same-contract behavior; excluded C implementation details.
- Excluded exact byte-for-byte formatting for fixture files except where public options require observable behavior.
- Excluded private helper modules and test harness-created canonical helpers.

## Eleven Checks

1. Public docs/day-one knowledge traceability: PASS.
2. Internal class names or undocumented module paths: PASS.
3. Behavioral invariants: PASS.
4. Non-goals: PASS.
5. Hidden fixture shape assumptions: PASS.
6. Behavioral statements use `must` / `returns` / `raises`: PASS.
7. Conditional behavior states conditions: PASS.
8. Failure paths: PASS.
9. Product State Model: PASS.
10. Escape hatches: PASS.
11. Priority/override verification: PASS. Merge behavior, sort behavior, dump return types, required `Loader`, and resolver registration scope were verified from source/tests and targeted reference probes.

## Verdict

PASS. `spec/spec_v1.md`, `spec/spec_v1_candidate.md`, and root `spec.md` are ready for Stage 2 review.
