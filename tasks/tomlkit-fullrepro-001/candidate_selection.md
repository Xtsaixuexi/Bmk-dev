# Step 1 Candidate Selection: tomlkit-fullrepro-001

Date: 2026-07-02
Decision: KEEP
Primary candidate: `tomlkit`
Source path: `/root/autodl-tmp/e2e/tomlkit`
Commit: `43668ddebc3f082bf385d328aceed18d26976897`
Task id: `tomlkit-fullrepro-001`

## Selection Summary

`tomlkit` is selected as the new Bmk-Lizhiqian candidate. It is a pure-Python, style-preserving TOML library with a documented public API for parsing, loading, dumping, building, editing, and writing TOML documents.

The core benchmark signal is a shared TOML document fact source projected through multiple public surfaces: parsed mapping behavior, item helper constructors, style-preserving serialization, file read/write behavior, TOML document mutation, custom encoders, and documented exception classes.

## Hard Gate Audit

| Gate | Evidence | Result |
|---|---|---|
| Pure Python package LOC >= 3000 | estimated package LOC: 4597 | PASS |
| Not single-file reconstructable | 12 package Python files across parser, document, file, item, container, API and exceptions behavior | PASS |
| Shared fact source with >=2 public projections | TOML input/document state drives dict-style reads, item objects, dumps output, file writes, and mutation behavior | PASS |
| Test suite present and usable | 9 pytest test modules, 229 test functions, 1035 nodeids; full suite passed after initializing `tests/toml-test` | PASS |
| Network/service bound tests absent | no mandatory network, database, or service dependency | PASS |
| Private import saturation absent | 7/12 test files import private or non-top-level implementation modules in the pre-screen | HIGH_RISK |
| Docs-test alignment | README and docs cover parse/load/dump/build/edit APIs, TOMLDocument, TOMLFile, items, and exceptions | PASS |
| Not dominated by a closed standard | TOML syntax is standard, but the task focus is library-specific style preservation and editable document behavior | PASS |

## Soft Gate Evidence

- Durable/shared state: TOML document content, comments, whitespace, ordering, end-of-line style, table structure, and item formatting.
- Public projections:
  - `parse` / `loads` produce `TOMLDocument` mapping behavior.
  - `dumps` / `dump` serialize documents, mappings, and constructed items.
  - `TOMLFile` reads and writes files while preserving line-ending behavior.
  - Helper constructors create public item objects for strings, numbers, booleans, dates, arrays, tables, inline tables, comments, whitespace, and key/value pairs.
  - `TOMLDocument` mutation APIs preserve observable document structure.
  - Public exceptions expose parser error semantics.
- Public docs are sufficient for a traceable behavioral spec:
  - `README.md`
  - `docs/index.rst`
  - `docs/quickstart.rst`
  - `docs/api.rst`
- Runtime dependency risk is low: `pyproject.toml` lists no mandatory runtime dependency beyond Python >= 3.9.

## Public API Surface Seed

Top-level exports from `tomlkit/__init__.py`:

- `TOMLDocument`
- `aot`
- `array`
- `boolean`
- `comment`
- `date`
- `datetime`
- `document`
- `dump`
- `dumps`
- `float_`
- `inline_table`
- `integer`
- `item`
- `key`
- `key_value`
- `load`
- `loads`
- `nl`
- `parse`
- `register_encoder`
- `string`
- `table`
- `time`
- `unregister_encoder`
- `value`
- `ws`

Stage 2 must expand this seed by reading public docs, `tomlkit.api`, documented `TOMLDocument`, `TOMLFile`, public item classes, and exceptions. This Step 1 list is not the final spec surface.

## Risks to Carry Forward

1. Private/non-top-level imports are common in the upstream tests. Stage 3 must rewrite behavior through public APIs or exclude affected nodeids.
2. `tests/test_toml_tests.py` depends on the `toml-test` submodule. The submodule has been initialized at `08ed8697864548b3cdb4b8decbf496bef47e1c82`; full collection and test execution now pass locally.
3. Some tests assert exact serialized strings. These are acceptable only when the string format is part of documented style-preservation behavior and can be mapped to the spec.
4. TOML compliance cases must be separated from library-specific style preservation so the task does not become a closed-standard parser benchmark.
5. Exact `repr`, exception message text, internal proxy classes, and private utility parsing behavior must be filtered unless they are documented public contracts.

## Decision

Select `tomlkit-fullrepro-001` as the new Step 1 candidate. Do not proceed to Step 2 until Step 1 model review and human approval are complete.
