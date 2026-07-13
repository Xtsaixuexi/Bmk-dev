<!-- INTERNAL
task_id: babel-fullrepro-001
spec_version: v1
delta: initial automated public-packet draft for e2e batch evaluation
source_boundary: README.rst, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# babel Specification

## Product Overview

This document describes the public behavior of `babel`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
About Babel
===========

Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

Details can be found in the HTML files in the ``docs`` folder.

For more information please visit the Babel web site:

https://babel.pocoo.org/

Join the chat at https://gitter.im/python-babel/babel

Contributing to Babel
=====================

If you want to contribute code to Babel, please take a look at our
`CONTRIBUTING.md <https://github.com/python-babel/babel/blob/master/CONTRIBUTING.md>`__.

If you know your way around Babels codebase a bit and like to help
further, we would appreciate any help in reviewing pull requests. Please
contact us at https://gitter.im/python-babel/babel if you're interested!
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: message python format; message python brace format; message translator comments; message clone message object; catalog add returns message instance; catalog two messages with same singular; catalog duplicate auto comment; catalog duplicate user comment; catalog duplicate location; catalog update message updates comments; 2 num plurals checkers; python format invalid; python format valid;  validate format invalid.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `babel` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names observed from the package surface include:

- `babel.Locale`
- `babel.UnknownLocaleError`
- `babel.default_locale`
- `babel.get_locale_identifier`
- `babel.negotiate_locale`
- `babel.parse_locale`

Additional public module members observed in the package tree include:

- `babel.core.get_global`
- `babel.core.UnknownLocaleError`
- `babel.core.Locale`
- `babel.core.default_locale`
- `babel.core.negotiate_locale`
- `babel.core.parse_locale`
- `babel.core.get_locale_identifier`
- `babel.core.get_cldr_version`
- `babel.dates.get_timezone`
- `babel.dates.get_period_names`
- `babel.dates.get_day_names`
- `babel.dates.get_month_names`
- `babel.dates.get_quarter_names`
- `babel.dates.get_era_names`
- `babel.dates.get_date_format`
- `babel.dates.get_datetime_format`
- `babel.dates.get_time_format`
- `babel.dates.get_timezone_gmt`
- `babel.dates.get_timezone_location`
- `babel.dates.get_timezone_name`
- `babel.dates.format_date`
- `babel.dates.format_datetime`
- `babel.dates.format_time`
- `babel.dates.format_skeleton`
- `babel.dates.format_timedelta`
- `babel.dates.format_interval`
- `babel.dates.get_period_id`
- `babel.dates.ParseError`
- `babel.dates.parse_date`
- `babel.dates.parse_time`
- `babel.dates.DateTimePattern`
- `babel.dates.DateTimeFormat`
- `babel.dates.parse_pattern`
- `babel.dates.tokenize_pattern`
- `babel.dates.untokenize_pattern`
- `babel.dates.split_interval_pattern`
- `babel.dates.match_skeleton`
- `babel.languages.get_official_languages`
- `babel.languages.get_territory_language_info`
- `babel.lists.format_list`
- `babel.localedata.normalize_locale`
- `babel.localedata.resolve_locale_filename`
- `babel.localedata.exists`
- `babel.localedata.locale_identifiers`
- `babel.localedata.load`
- `babel.localedata.merge`
- `babel.localedata.Alias`
- `babel.localedata.LocaleDataDict`
- `babel.numbers.UnknownCurrencyError`
- `babel.numbers.list_currencies`
- `babel.numbers.validate_currency`
- `babel.numbers.is_currency`
- `babel.numbers.normalize_currency`
- `babel.numbers.get_currency_name`
- `babel.numbers.get_currency_symbol`
- `babel.numbers.get_currency_precision`
- `babel.numbers.get_currency_unit_pattern`
- `babel.numbers.get_territory_currencies`
- `babel.numbers.get_territory_currencies`
- `babel.numbers.get_territory_currencies`
- `babel.numbers.UnsupportedNumberingSystemError`
- `babel.numbers.get_decimal_symbol`
- `babel.numbers.get_plus_sign_symbol`
- `babel.numbers.get_minus_sign_symbol`
- `babel.numbers.get_exponential_symbol`
- `babel.numbers.get_group_symbol`
- `babel.numbers.get_infinity_symbol`
- `babel.numbers.format_number`
- `babel.numbers.get_decimal_precision`
- `babel.numbers.get_decimal_quantum`
- `babel.numbers.format_decimal`
- `babel.numbers.format_compact_decimal`
- `babel.numbers.UnknownCurrencyFormatError`
- `babel.numbers.format_currency`
- `babel.numbers.format_compact_currency`
- `babel.numbers.format_percent`
- `babel.numbers.format_scientific`
- `babel.numbers.NumberFormatError`
- `babel.numbers.parse_number`
- `babel.numbers.parse_decimal`

## Public API Behavior

Implement public functions, classes, constants, and exceptions so callers can use the package in normal documented workflows. Constructors should accept documented argument forms, preserve public attributes/properties, and raise the documented public exception types for invalid inputs. Parsing, formatting, conversion, tokenization, localization, CLI, or helper behavior should be deterministic and should not depend on hidden state outside caller-provided inputs and normal standard-library resources.

## Error Semantics

Invalid input should fail with the package's public exception types when such types are part of the public API. Do not expose private implementation exceptions for user-level errors. Error message text is not part of the public contract unless the public documentation specifies exact wording.

## Cross-View Invariants

- Public constructors and module-level factory functions must agree on the object values they create.
- A value parsed from a supported string/file/input form must format or serialize consistently through the documented output API.
- CLI-facing behavior, when in scope, must call the same public logic as Python API behavior.
- Equality, ordering, hashing, or containment behavior must be stable for equivalent public values.
- Locale, timezone, encoding, grammar, SQL, markup, token, or parser options must be carried through to all public projections that expose them.
- Repeated operations on the same immutable public value must produce the same observable result.

## Representative Workflow

1. Import `babel` from the solution package.
2. Construct or parse representative public input values using documented functions/classes.
3. Inspect public properties or return values.
4. Convert, format, serialize, tokenize, or execute the corresponding public workflow.
5. Handle invalid input using documented public exception types.

## Non-Goals

Do not reproduce upstream private helper modules, source-code layout, project release tooling, coverage tooling, or network-bound data fetching. Private implementation details and repository maintenance artifacts are outside the public contract.

## Evaluation Notes

The evaluator uses a filtered subset of public behavior checks that already pass on the reference implementation in this environment. Tests are grouped as atomic, integration, and system_e2e. Atomic tests focus on individual public functions/classes. Integration tests combine parsing, formatting, conversion, construction, or public helpers. System_e2e tests cover command or full workflow behavior when present. A correct implementation should satisfy the public behavior in this specification without matching private internals.
