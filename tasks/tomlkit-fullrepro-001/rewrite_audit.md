# Rewrite / Generation Audit: tomlkit-fullrepro-001

## Upstream Import Audit

Clean upstream modules retained:

- `tests/test_toml_file.py`
- `tests/test_write.py`

High-risk upstream modules excluded from direct scoring because they import private or implementation modules at module scope:

- `tests/test_api.py`: imports `tomlkit.parser.Parser`
- `tests/test_build.py`: imports `tomlkit._utils._utc`
- `tests/test_items.py`: imports `tomlkit.container.OutOfOrderTableProxy` and `tomlkit.parser.Parser`
- `tests/test_parser.py`: imports `tomlkit.parser.Parser`
- `tests/test_toml_document.py`: imports `tomlkit._utils._utc` and test helpers
- `tests/test_toml_tests.py`: imports `tomlkit._compat.decode`, `tomlkit._utils.parse_rfc3339`, and is dominated by external TOML compliance cases
- `tests/test_utils.py`: imports `tomlkit._utils.parse_rfc3339`

The direct upstream kept set is intentionally small because collection-carrier imports would force candidates to implement private modules that the spec explicitly excludes.

## Track B Public Test Generation

Track B was triggered because direct upstream cleanup left fewer than 30 safe scoreable nodeids.

Generated tests are in:

- `filter/generated_public_tests.py`

Generation constraints:

- import only public `tomlkit`, `tomlkit.toml_file`, `tomlkit.toml_document`, and `tomlkit.exceptions` names;
- assert public behavior mapped to `spec.md`;
- no private imports, no private attributes, no `repr()` checks, no exact exception-message checks;
- use exact serialized strings only where style-preserving serialization is part of the public contract.

Reference validation:

- first generated draft: 46/52 passed; six tests were corrected to avoid over-specific formatting or wrong exception category assumptions;
- final generated tests: 52/52 passed against reference.

## Oracle Merge

Final scoreable oracle:

- 12 upstream nodeids from clean public-import modules;
- 52 generated public behavior tests;
- 64 total scoreable tests.

Layer distribution:

- atomic: 25
- integration: 19
- system_e2e: 20
