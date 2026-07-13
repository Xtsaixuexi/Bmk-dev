<!-- INTERNAL
task_id: dateutil-fullrepro-001
spec_version: v1
delta: initial automated public-packet draft for e2e batch evaluation
source_boundary: README.rst, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# dateutil Specification

## Product Overview

This document describes the public behavior of `dateutil`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
dateutil - powerful extensions to datetime
==========================================

|pypi| |support| |licence|

|gitter| |readthedocs|

|appveyor| |gha| |coverage|

.. |pypi| image:: https://img.shields.io/pypi/v/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: pypi version

.. |support| image:: https://img.shields.io/pypi/pyversions/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: supported Python version

.. |appveyor| image:: https://img.shields.io/appveyor/ci/dateutil/dateutil/master.svg?style=flat-square&logo=appveyor
    :target: https://ci.appveyor.com/project/dateutil/dateutil
    :alt: appveyor build status

.. |gha| image:: https://github.com/dateutil/dateutil/actions/workflows/validate.yml/badge.svg
    :target: https://github.com/dateutil/dateutil/actions
    :alt: github actions build status

.. |coverage| image:: https://codecov.io/gh/dateutil/dateutil/branch/master/graphs/badge.svg?branch=master
    :target: https://codecov.io/gh/dateutil/dateutil?branch=master
    :alt: Code coverage

.. |gitter| image:: https://badges.gitter.im/dateutil/dateutil.svg
   :alt: Join the chat at https://gitter.im/dateutil/dateutil
   :target: https://gitter.im/dateutil/dateutil

.. |licence| image:: https://img.shields.io/pypi/l/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: licence

.. |readthedocs| image:: https://img.shields.io/readthedocs/dateutil/latest.svg?style=flat-square&label=Read%20the%20Docs
   :alt: Read the documentation at https://dateutil.readthedocs.io/en/latest/
   :target: https://dateutil.readthedocs.io/en/latest/

The `dateutil` module provides powerful extensions to
the standard `datetime` module, available in Python.

Installation
============
`dateutil` can be installed from PyPI using `pip` (note that the package name is
different from the importable name)::

    pip install python-dateutil

Download
========
dateutil is available on PyPI
https://pypi.org/project/python-dateutil/

The documentation is hosted at:
https://dateutil.readthedocs.io/en/stable/

Code
====
The code and issue tracker are hosted on GitHub:
https://github.com/dateutil/dateutil/

Features
========

* Computing of relative deltas (next month, next year,
  next Monday, last week of month, etc);
* Computing of relative deltas between two given
  date and/or datetime objects;
* Computing of dates based on very flexible recurrence rules,
  using a superset of the `iCalendar <https://www.ietf.org/rfc/rfc2445.txt>`_
  specification. Parsing of RFC strings is supported as well.
* Generic parsing of dates in almost any string format;
* Timezone (tzinfo) implementations for tzfile(5) format
  files (/etc/localtime, /usr/share/zoneinfo, etc), TZ
  environment string (in all known formats), iCalendar
  format files, given ranges (with help from relative deltas),
  local machine timezone, fixed offset timezone, UTC timezone,
  and Windows registry-based time zones.
* Internal up-to-date world timezone information based on
  Olson's database.
* Computing of Easter Sunday dates for any given year,
  using Western, Orthodox or Julian algorithms;
* A comprehensive test suite.

Quick example
=============
Here's a snapshot, just to give an idea about the power of the
package. For more examples, look at the documentation.

Suppose you want to know how much time is left, in
years/months/days/etc, bef
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: easter western; easter orthodox; easter julian; easter bad method; imported modules; lazy import; import version str; import version root; import easter direct; import easter from; import easter start; import parser direct.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `dateutil` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names observed from the package surface include:

- `dateutil.easter`
- `dateutil.parser`
- `dateutil.relativedelta`
- `dateutil.rrule`
- `dateutil.tz`
- `dateutil.utils`
- `dateutil.zoneinfo`

Additional public module members observed in the package tree include:

- `dateutil.easter.easter`
- `dateutil.relativedelta.relativedelta`
- `dateutil.rrule.weekday`
- `dateutil.rrule.rrulebase`
- `dateutil.rrule.rrule`
- `dateutil.rrule.rruleset`
- `dateutil.utils.today`
- `dateutil.utils.default_tzinfo`
- `dateutil.utils.within_delta`

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

1. Import `dateutil` from the solution package.
2. Construct or parse representative public input values using documented functions/classes.
3. Inspect public properties or return values.
4. Convert, format, serialize, tokenize, or execute the corresponding public workflow.
5. Handle invalid input using documented public exception types.

## Non-Goals

Do not reproduce upstream private helper modules, source-code layout, project release tooling, coverage tooling, or network-bound data fetching. Private implementation details and repository maintenance artifacts are outside the public contract.

## Evaluation Notes

The evaluator uses a filtered subset of public behavior checks that already pass on the reference implementation in this environment. Tests are grouped as atomic, integration, and system_e2e. Atomic tests focus on individual public functions/classes. Integration tests combine parsing, formatting, conversion, construction, or public helpers. System_e2e tests cover command or full workflow behavior when present. A correct implementation should satisfy the public behavior in this specification without matching private internals.
