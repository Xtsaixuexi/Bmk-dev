# Filter Validation: prompt-toolkit-fullrepro-001

## Verdict

PASS. Stage 3 produced a spec-mapped oracle with reference pass evidence and dummy-failure evidence.

## Artifact Checks

| check | result |
|---|---|
| `filter/rewrite_audit.md` exists | PASS |
| `filter/spec_test_map.md` exists and has one row per processed upstream/generated test | PASS |
| upstream rows accounted | 156 / 156 |
| generated rows accounted | 32 / 32 |
| covered rows | 100 |
| source-only rows | 28 |
| excluded rows | 60 |
| `filter/kept_nodeids.txt` line count | 100 |
| `filter/taxonomy.jsonl` line count | 100 |
| taxonomy layers non-zero | PASS: atomic 59, integration 33, system_e2e 8 |
| `filter/test_taxonomy_score.csv` exists | PASS |
| root copies exist for required public filter artifacts | PASS |

## Coverage Gate

The merged oracle has 100 scoreable tests, above the global floor of 50.

| spec section | covered tests |
|---|---:|
| Application, Prompt, and I/O | 3 |
| Completion | 18 |
| Cross-View Invariants | 5 |
| Document and Buffer | 13 |
| Error Semantics | 8 |
| Formatted Text | 16 |
| Formatted Text and Styles | 3 |
| Full-Screen Layout With a Buffer and Exit Binding | 3 |
| Installable Surface | 3 |
| Key Bindings | 6 |
| Layout Controls | 3 |
| Product State Model | 5 |
| Prompt With Completion and Validation | 3 |
| Styles | 7 |
| Validation | 4 |

Minimums are satisfied: Cross-View Invariants has 5, Error Semantics has 8, representative workflows have at least 3 each, and all executable public API sections have at least 3.

## Behavioral Filter Gate

Retained tests are mapped to public spec headings and avoid:

- terminal byte stream exactness
- snapshot exact rendering
- private renderer/parser internals
- contrib servers, dialogs, progress, widget visual polish
- platform-specific terminal behavior
- test helper fixtures

Kept upstream tests are from public behavior files for `Document`, `Buffer`, completion, formatted text, key bindings, layout, styles, and style transformations. Generated tests supplement public validation/error semantics, installable surface, application/session I/O, layout focus workflows, and cross-view invariants.

## Reference Gate

PASS.

- Upstream retained scorer gate: 68 passed / 68 total
- Generated public pytest gate: 32 passed / 32 total
- Merged aggregate: 100 passed / 100 total

See `filter/reference_validation.md` and `filter/reference_upstream_score.json`.

## Dummy Gate

PASS.

- Upstream retained scorer dummy gate: 0 passed / 68 total, all collection errors against the isolated dummy package
- Generated public pytest dummy gate: collection failed on public top-level import, 0 tests passed
- Merged dummy pass rate: 0.0

See `filter/dummy_score.json` and `filter/dummy_upstream_score.json`.

## Scorer Note

The upstream retained set was run through `score_pytest_original.py`. The generated tests are wip-local pytest tests, not original upstream nodeids, so they were validated by direct pytest reference/dummy gates. A unified scorer for both sources would require a runner mode that can merge upstream nodeids with generated pytest files.

## Aggregate Reference Score

Aggregate `filter/reference_score.json` records 100 passed / 100 total by combining the upstream isolated scorer gate with the generated public pytest reference gate. Taxonomy uses scorer-compatible dotted keys and has non-zero atomic, integration, and system_e2e layers.
