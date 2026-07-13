# Rewrite Audit: lark-fullrepro-001

## Import Audit

- Top-level private package import pre-screen: clean for `lark._*` imports.
- Upstream test aggregation uses relative imports in `tests/__main__.py`; this is upstream test infrastructure, not candidate-visible API.
- No Track A public-API rewrite was performed in Step 4 v1; filtering is nodeid-level and conservative.

## Module Counts

| module | total | kept |
|---|---:|---:|
| `tests.test_parser` | 1146 | 716 |
| `tests.test_grammar` | 26 | 25 |
| `tests.test_trees` | 22 | 16 |
| `tests.test_tree_templates` | 19 | 0 |
| `tests.test_tree_forest_transformer` | 12 | 12 |
| `tests.test_python_grammar` | 12 | 0 |
| `tests.test_cache` | 10 | 7 |
| `tests.test_reconstructor` | 8 | 8 |
| `tests.test_pattern_matching` | 6 | 6 |
| `tests.test_tools` | 5 | 0 |
| `tests.test_logger` | 5 | 0 |
| `tests.test_lexer` | 2 | 2 |

## Exclusion Reasons

| reason | count |
|---|---:|
| uses custom lexer compatibility protocol not specified as public contract | 412 |
| undocumented tree template helper API; not in spec scope | 19 |
| depends on optional regex/interegular dependency unavailable in baseline environment | 18 |
| built-in Python grammar language details are out of scope for Lark public API reconstruction | 12 |
| asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract | 9 |
| standalone tool executes generated module/subprocess-like tooling; environment-sensitive for hidden oracle | 5 |
| asserts logging/debug collision output and optional interegular behavior; environment/exact-output sensitive | 5 |
| pickle round-trip for Tree is not documented as public behavior | 1 |
