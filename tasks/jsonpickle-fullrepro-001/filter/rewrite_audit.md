# Stage 3 Rewrite Audit

State entry verified: `S3_FILTER_IN_PROGRESS`. `filter_iter` was 0, so no loop escalation was required.

## Shared Fixture And Import Audit

- `tests/helper.py` contains only a pytest skip wrapper and no private jsonpickle imports.
- Files importing out-of-scope helpers or optional extension modules were not retained directly. Their public core behaviors are represented by `filter/generated_tests.py`.
- Clean upstream files retained directly: `tests/collections_test.py`, `tests/document_test.py`, `tests/stdlib_test.py`, `tests/wizard_test.py` (`test_with_pickling` only), and `tests/zoneinfo_test.py`.

## Per-File Accounting

| file | collected rows | kept rows | excluded rows | decision |
|---|---:|---:|---:|---|
| `tests/backend_test.py` | 46 | 0 | 46 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/collections_test.py` | 14 | 6 | 8 | retain selected public nodeids |
| `tests/datetime_test.py` | 34 | 0 | 34 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/document_test.py` | 2 | 1 | 1 | retain selected public nodeids |
| `tests/ecdsa_test.py` | 4 | 0 | 4 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/feedparser_test.py` | 3 | 0 | 3 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/handler_test.py` | 11 | 0 | 11 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/helper.py` | 1 | 0 | 1 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/jsonpickle_test.py` | 393 | 0 | 393 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/numpy_test.py` | 50 | 0 | 50 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/object_test.py` | 152 | 0 | 152 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/sqlalchemy_test.py` | 5 | 0 | 5 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/stdlib_test.py` | 6 | 3 | 3 | retain selected public nodeids |
| `tests/util_test.py` | 55 | 0 | 55 | exclude from Track A; covered by generated/public oracle or out of scope |
| `tests/wizard_test.py` | 6 | 1 | 5 | retain selected public nodeids |
| `tests/zoneinfo_test.py` | 2 | 1 | 1 | retain selected public nodeids |

## Track A Result

- functions_in_scope: 784
- functions_kept: 12
- functions_excluded: 772
- Track B trigger: Track A retained fewer than 30 nodeids and several public behaviors in the upstream unit files required extraction from out-of-scope helper imports.
- `filter/rewritten_upstream_tests.py` is intentionally empty because no upstream function required a source-preserving rewrite; retained upstream tests run from their original files and generated tests live in `filter/generated_tests.py`.
