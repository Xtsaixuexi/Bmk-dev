# Filter Correction Request: Formatter Token Private Entrypoint

Task: `arrow-fullrepro-001`  
Date: 2026-07-12  
Affected source area: `tests/test_formatter.py::TestFormatterFormatToken`

## Problem

Most `TestFormatterFormatToken` tests call the private helper `DateTimeFormatter._format_token(...)` directly. The behavior being checked is valuable, but `_format_token` is not part of the candidate-visible public API contract.

Under the Bmk-dev test-filter rules, a correct reimplementation with different internals should not fail only because it lacks a private helper with the same name. These tests therefore need a public-entrypoint rewrite before they can be treated as strict current-main `covered` oracle rows.

## Affected Rows

Rows that require rewrite to a public entrypoint:

- `tests/test_formatter.py::TestFormatterFormatToken::test_year`
- `tests/test_formatter.py::TestFormatterFormatToken::test_month`
- `tests/test_formatter.py::TestFormatterFormatToken::test_day`
- `tests/test_formatter.py::TestFormatterFormatToken::test_hour`
- `tests/test_formatter.py::TestFormatterFormatToken::test_minute`
- `tests/test_formatter.py::TestFormatterFormatToken::test_second`
- `tests/test_formatter.py::TestFormatterFormatToken::test_sub_second`
- `tests/test_formatter.py::TestFormatterFormatToken::test_timestamp`
- `tests/test_formatter.py::TestFormatterFormatToken::test_timezone`
- `tests/test_formatter.py::TestFormatterFormatToken::test_timezone_formatter[US/Alaska]`
- `tests/test_formatter.py::TestFormatterFormatToken::test_timezone_formatter[UTC]`
- `tests/test_formatter.py::TestFormatterFormatToken::test_timezone_formatter[Europe/Mariehamn]`
- `tests/test_formatter.py::TestFormatterFormatToken::test_am_pm`
- `tests/test_formatter.py::TestFormatterFormatToken::test_week`
- `tests/test_formatter.py::TestFormatterFormatToken::test_nonsense`

Rows already using a public entrypoint and can remain covered:

- `tests/test_formatter.py::TestFormatterFormatToken::test_format`
- `tests/test_formatter.py::TestFormatterFormatToken::test_escape`

## Rewrite Strategy

Preferred public entrypoints:

- `DateTimeFormatter.format(dt, token_or_format_string)`
- `Arrow.format(token_or_format_string)` when an Arrow value is already the public object under test

For simple single-token tests, replace:

```python
self.formatter._format_token(dt, "YYYY") == "2013"
```

with:

```python
self.formatter.format(dt, "YYYY") == "2013"
```

This preserves the public formatting behavior while removing the private method requirement.

For timezone tokens, rewrite `ZZ`, `Z`, and `ZZZ` through `formatter.format(...)` and keep the existing expected offset or timezone abbreviation logic.

For `test_nonsense`, do not preserve the private-helper assertion that `_format_token(..., "NONSENSE") is None`. Public `format(...)` scans recognized token sequences inside a format string; for example, `S` remains a fractional-second token even inside ordinary text. The public rewrite should test one of these public contracts instead:

- bracket-escaped literal text remains literal, or
- mixed literal/token strings format recognized tokens and emit non-token characters literally.

## Spec Update Made

The spec wording was tightened from a broad literal-text statement to:

```text
Format strings are scanned for recognized Arrow token sequences wherever they appear. Characters that are not part of a recognized token are emitted literally, and bracket-escaped text remains literal.
```

## Required Downstream Action

Before final strict qualification:

1. Rewrite the affected `_format_token` tests to public `format(...)` entrypoints.
2. Run the rewritten tests against the reference implementation.
3. Re-run dummy gate if the rewritten tests are included in oracle.
4. Update `spec_test_map.md` rows to reflect the rewritten public-entrypoint oracle.
5. Recompute reference score and Gate D if nodeids or assertions change.

Until that is done, these rows should be described as:

```text
behavior valuable, but current oracle entrypoint requires rewrite before strict current-main covered status.
```
