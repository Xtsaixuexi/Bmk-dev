# Rewrite Audit

No upstream tests were rewritten in Step 4.

Filtering is conservative: tests relying on `assert_fail` were marked source-only because that helper reads `validator._errors` and asserts internal `ErrorList` / error-code details. Tests asserting `_valid_schemas`, `_config`, `_errors`, exact repr strings, exact exception message matches, or exact default BasicErrorHandler wording were excluded or source-only.

Summary:

- Total nodeids: 247
- Covered/kept: 115
- Source-only: 121
- Excluded: 11
- Spec gaps: 0
