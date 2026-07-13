# Step 4 Filter Validation v4

## Structural Checks

- all_nodeids count: 247
- unique all_nodeids: True
- kept_nodeids count: 81
- kept subset of all: True
- taxonomy rows: 81
- taxonomy rows equal kept count: True

## Filter Counts

- covered / kept: 81
- source-only: 155
- excluded: 11
- spec_gap: 0

## Kept Layer Counts

- atomic: 25
- integration: 46
- system_e2e: 10

## Corrections

- v2 removed 11 top-level import carrier nodeids whose modules required helper APIs absent from candidate-visible spec v1.
- v3 removed 21 additional nodeids that relied on error constants/ErrorList internals, exact BasicErrorHandler message templates, deprecation warnings, internal/context validator attrs, docstring-derived `validation_rules`, or the `contains` rule absent from spec v1.
- v4 removed 2 final fairness outliers: one exact default error-message assertion and one `float`-accepts-`int` expectation not stated by spec v1.

The corrected scoreable set is spec-driven and behavioral against spec v1.
