# Filter Validation: lark-fullrepro-001

- total collected nodeids: 1273
- kept covered nodeids: 792
- source-only: 422
- excluded: 59
- spec_gap: 0
- by layer: atomic=394, integration=248, system_e2e=150

## Checks

- Every kept row maps to an existing spec heading or combined existing headings.
- No tests requiring optional unavailable dependencies were kept.
- `tests.test_tree_templates`, Python grammar conformance details, standalone tooling, exact logging, exact repr/message/cache naming and old custom lexer protocols were excluded or marked source-only.
- Taxonomy keys follow `__main__::Class.test` because pytest collection routes all upstream unittest cases through `tests/__main__.py`.

## Next Required Check

- Run the kept set against the reference implementation and require >=95% pass rate before packaging.
