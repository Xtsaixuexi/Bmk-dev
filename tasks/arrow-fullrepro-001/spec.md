<!-- INTERNAL
task_id: arrow-fullrepro-001
spec_version: v2
delta: rewrote the candidate-visible body to remove copied README markup, audit language, duplicated symbol lists, and test-list wording; clarified Arrow's public date/time construction, formatting, representation, and error contracts in developer-documentation style.
source_boundary: README.rst summary, public package exports, public module/class/function names, and retained public behavior areas recorded in the task artifacts
-->

# Arrow Specification

## Product Overview

Arrow is a Python library for creating, parsing, formatting, converting, and comparing dates and times through a small public API. It wraps the standard `datetime` model with an `Arrow` object and factory helpers that make common timezone-aware workflows concise.

Arrow values represent a single point in time together with timezone information. Public constructors and factory functions should preserve the same observable date, time, timezone, and timestamp semantics that callers would expect from a user-facing date/time library. UTC is the default timezone for UTC-oriented helpers, while caller-provided timezone objects and timezone names are respected where accepted.

## Scope

This specification covers the public Python API for:

- importing the `arrow` package and its documented top-level exports;
- constructing `Arrow` values from date/time components, timestamps, `datetime`, `date`, `struct_time`, ISO-like strings, ISO calendar triples, existing `Arrow` values, and timezone inputs;
- creating current-time values with `now`, `utcnow`, and factory methods;
- preserving timezone behavior for `datetime.tzinfo`, `dateutil`, `pytz`, `zoneinfo`, and timezone-name inputs;
- representing Arrow values through public string, repr, hash, equality, and attribute access behavior;
- formatting Arrow values with token-based format strings and built-in date/time format constants;
- raising public user-level exceptions for invalid parse and construction inputs.

Out of scope: private modules, private attributes, repository tooling, release scripts, network access, internal caches, and implementation layout. Exact exception message text is not part of the public contract unless a public API explicitly documents it.

## Installable Surface

A solution provides an importable `arrow` package from the solution root. It must not rely on another installed distribution of `arrow` to satisfy imports.

The top-level package exposes these user-facing names:

- `arrow.get`
- `arrow.now`
- `arrow.utcnow`
- `arrow.Arrow`
- `arrow.ArrowFactory`
- `arrow.ParserError`
- `arrow.FORMAT_ATOM`
- `arrow.FORMAT_COOKIE`
- `arrow.FORMAT_RFC822`
- `arrow.FORMAT_RFC850`
- `arrow.FORMAT_RFC1036`
- `arrow.FORMAT_RFC1123`
- `arrow.FORMAT_RFC2822`
- `arrow.FORMAT_RFC3339`
- `arrow.FORMAT_RFC3339_STRICT`
- `arrow.FORMAT_RSS`
- `arrow.FORMAT_W3C`

The public module paths below are part of the import surface for normal user code:

- `arrow.api.get`, `arrow.api.now`, `arrow.api.utcnow`, and `arrow.api.factory`
- `arrow.arrow.Arrow`
- `arrow.factory.ArrowFactory`
- `arrow.formatter.DateTimeFormatter`
- `arrow.locales.get_locale`, `arrow.locales.get_locale_by_class_name`, and public locale classes used by formatting and human-facing date/time text

## Public API Behavior

### Module-Level Factories

`arrow.get(*args, **kwargs)` is the general construction entry point. It dispatches by public input shape:

- no arguments, or `None`, returns an `Arrow` for the current UTC time;
- an existing `Arrow` returns an equivalent Arrow value;
- a `datetime.datetime` preserves its date/time fields and timezone unless an explicit timezone argument is supplied;
- a `datetime.date` creates a value at midnight on that date;
- a `time.struct_time` creates a value from the contained calendar fields;
- an integer, float, or decimal value creates a value from a Unix timestamp;
- public timestamp inputs may use second, millisecond, or microsecond precision, and Arrow normalizes them to the represented instant;
- a numeric-looking string is not treated as a Unix timestamp by the single-argument parser; parse timestamp strings with an explicit timestamp format token such as X;
- a string without an explicit format is parsed as a supported date/time string;
- a string with a format string is parsed according to Arrow's formatting tokens;
- a `tzinfo` object or supported timezone name can be used where the factory accepts timezone input;
- an ISO calendar triple is interpreted consistently with Python's ISO calendar date rules.

`arrow.now(tz=None)` returns the current local time in the requested timezone. If `tz` is omitted, it uses the process-local timezone behavior. `arrow.utcnow()` returns the current UTC time.

Keyword options that affect parsing or timezone selection are part of the public call contract when documented by Arrow, including whitespace normalization for string parsing and explicit `tzinfo` arguments.

### Arrow Values

`Arrow(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, **kwargs)` constructs an Arrow value from date/time components. Missing time components default to zero. `tzinfo` may be omitted, may be a `datetime.tzinfo` object, or may be a supported timezone name. Ambiguous local times preserve a supplied `fold` value where Python's datetime model supports it.

An `Arrow` value exposes public date/time attributes and derived views consistent with the underlying instant, including calendar fields, `tzinfo`, a naive datetime view, Unix timestamp behavior, week-related values, and quarter-related values. Attribute access for public datetime-like properties should match the value represented by the Arrow object.

`Arrow.now`, `Arrow.utcnow`, `Arrow.fromtimestamp`, `Arrow.utcfromtimestamp`, `Arrow.fromdatetime`, `Arrow.fromdate`, `Arrow.strptime`, and `Arrow.fromordinal` create Arrow values using the same public semantics as the module-level factory helpers. Factory and constructor routes that represent the same instant must agree on the resulting public value.

### Formatting And Built-In Formats

`Arrow.format(fmt=None, locale='en-us')` returns a string representation using Arrow format tokens. When no explicit format is provided, Arrow uses its documented default date/time format.

Supported token families include:

- year tokens such as full and short year forms;
- month tokens for numeric and textual month output;
- day tokens for day-of-month output;
- hour, minute, and second tokens;
- fractional second tokens;
- Unix timestamp tokens;
- timezone offset and timezone name tokens;
- AM/PM tokens;
- ISO week-related tokens;
- bracket escaping for literal text.

Format strings are scanned for recognized Arrow token sequences wherever they appear. Characters that are not part of a recognized token are emitted literally, and bracket-escaped text remains literal. Timezone formatting reflects the Arrow value's timezone, including named timezones and UTC offsets.

The built-in format constants represent common internet and HTTP date/time formats, including Atom, Cookie, RFC 822, RFC 850, RFC 1036, RFC 1123, RFC 2822, RFC 3339, strict RFC 3339, RSS, and W3C. Passing one of these constants to `format` produces output for that public standard.

`arrow.formatter.DateTimeFormatter` provides the public formatter implementation used by Arrow formatting workflows. Its observable behavior should match `Arrow.format` for the same value, format string, and locale.

### Representation, Equality, And Hashing

`str(arrow_value)` returns a user-facing ISO-style date/time string for the represented value. `repr(arrow_value)` returns an Arrow-specific representation that includes the formatted value inside an `Arrow` wrapper. Equivalent Arrow values compare and hash consistently so they can be used in equality checks and hash-based containers.

### Locales

Locale helpers and public locale classes support user-facing localized date/time text. Formatting behavior that accepts a locale should carry the selected locale through to all public text projections that depend on it. Locale internals, registry implementation, and private lookup state are not part of the contract.

## Error Semantics

Invalid user input should fail with public, user-level exceptions rather than private implementation exceptions.

- Invalid parse input for Arrow's parser-facing APIs raises `arrow.ParserError` when the failure is a parse failure.
- Invalid component values follow Python date/time construction semantics for impossible calendar values.
- Unsupported input shapes or unsupported timezone arguments raise an appropriate public exception type such as `TypeError`, `ValueError`, or `ParserError`, depending on whether the problem is type mismatch, invalid value, or parse failure.
- Boolean values are not accepted as numeric timestamps even though bool is a Python subclass of int.
- Error message wording is not part of the contract unless explicitly documented as exact public output.

## Cross-View Invariants

- `arrow.get`, `ArrowFactory`, module-level helpers, and `Arrow` class methods must agree when they are given equivalent public inputs.
- A value parsed from a supported string or timestamp must preserve the same instant when formatted, converted, compared, or inspected through public attributes.
- Timezone inputs supplied as `tzinfo` objects, supported timezone names, or timezone-aware datetimes must produce consistent public timezone projections.
- `str`, `repr`, `format`, timestamp conversion, and public date/time attributes must describe the same represented value.
- Equality and hashing must be stable for equivalent Arrow values and must not depend on private object identity.
- Repeated operations on an immutable Arrow value must produce the same observable result.
- Locale and formatting options must affect only the documented text projections and must not change the represented instant.

## Representative Workflow

A typical Arrow workflow is:

1. Import `arrow`.
2. Create an Arrow value with `arrow.get`, `arrow.utcnow`, `arrow.now`, or an `Arrow` class method.
3. Provide input as a timestamp, string, `datetime`, `date`, `struct_time`, ISO calendar tuple, or explicit date/time components.
4. Inspect public attributes such as calendar fields, timezone information, naive datetime view, or timestamp behavior.
5. Format the value with a token string or a built-in format constant.
6. Compare, hash, or convert the value while preserving the same public instant and timezone semantics.
7. Handle invalid input using Arrow's public exception behavior.

## Non-Goals

Do not reproduce Arrow's private helper modules, source-code layout, release tooling, test utilities, coverage configuration, or internal caches. Do not depend on network resources. Do not expose private attributes or require callers to match internal implementation structures. Do not treat arbitrary exception message wording as a required behavior.

## Evaluation Notes

Validation focuses on public behavior described in this document. Checks may cover individual APIs, combinations of parsing/formatting/conversion behavior, timezone consistency, and representative user workflows. A correct implementation should satisfy these public contracts without matching Arrow's internal source layout or private helper structure.
