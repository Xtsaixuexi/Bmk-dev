# Filter Correction Request: Step 7 Judge

Verdict: filter correction applied.

The first Step 6 candidate scores exposed collection carrier failures in three upstream test modules. The candidate-visible spec v1 does not require `cerberus.utils.validator_factory`, `cerberus.schema.UnvalidatedSchema`, or `cerberus.utils.compare_paths_lt`, but selected kept nodeids lived in modules that import these helpers at collection time. This makes undocumented helper imports a hard scoring prerequisite.

Correction: mark the 11 affected kept nodeids as `source-only` and reduce final scoreable set from 115 to 104.

Affected groups:

- `cerberus/tests/test_assorted.py::test_dynamic_types`
- all 9 previously kept `cerberus/tests/test_schema.py::*` nodeids
- `cerberus/tests/test_utils.py::test_compare_paths`

Downstream actions required:

1. Re-run reference oracle on the 104-nodeid set.
2. Re-score available candidates with overlay scorer and corrected nodeids/taxonomy.
3. Re-run Step 7 judge on corrected scores.

## v3 Additional Fairness Correction

Removed 21 more nodeids after failure-pattern audit showed dependence on spec-v1-absent error constants/ErrorList internals, exact BasicErrorHandler message templates, deprecation warnings, internal/context validator attrs, docstring-derived `validation_rules`, or the `contains` rule. Corrected kept set is now 83.

## v4 Final Fairness Correction

Removed 2 final nodeids: `test_readonly_field_first_rule` for exact default error-message wording and `test_float` for requiring integer acceptance by the `float` type despite spec v1 only documenting that behavior for `number`. Corrected kept set is now 81.
