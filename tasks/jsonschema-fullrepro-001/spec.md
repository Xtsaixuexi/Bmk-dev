<!-- INTERNAL
task_id: jsonschema-fullrepro-001
spec_version: v1
delta: initial public-packet draft for remaining e2e project batch
source_boundary: README, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# jsonschema Specification

## Product Overview

This document describes the public behavior of `jsonschema`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
==========
jsonschema
==========

|PyPI| |Pythons| |CI| |ReadTheDocs| |Precommit| |Zenodo|

   :alt: PyPI version
   :target: https://pypi.org/project/jsonschema/

   :alt: Supported Python versions
   :target: https://pypi.org/project/jsonschema/

  :alt: Build status
  :target: https://github.com/python-jsonschema/jsonschema/actions?query=workflow%3ACI

.. |ReadTheDocs| image:: https://readthedocs.org/projects/python-jsonschema/badge/?version=stable&style=flat
   :alt: ReadTheDocs status
   :target: https://python-jsonschema.readthedocs.io/en/stable/

.. |Precommit| image:: https://results.pre-commit.ci/badge/github/python-jsonschema/jsonschema/main.svg
   :alt: pre-commit.ci status
   :target: https://results.pre-commit.ci/latest/github/python-jsonschema/jsonschema/main

.. |Zenodo| image:: https://zenodo.org/badge/3072629.svg
   :alt: Zenodo DOI
   :target: https://zenodo.org/badge/latestdoi/3072629


``jsonschema`` is an implementation of the `JSON Schema <https://json-schema.org>`_ specification for Python.

.. code:: python

    >>> from jsonschema import validate

    >>> # A sample schema, like what we'd get from json.load()
    >>> schema = {
    ...     "type" : "object",
    ...     "properties" : {
    ...         "price" : {"type" : "number"},
    ...         "name" : {"type" : "string"},
    ...     },
    ... }

    >>> # If no exception is raised by validate(), the instance is valid.
    >>> validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

    >>> validate(
    ...     instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema,
    ... )                                   # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValidationError: 'Invalid' is not of type 'number'

It can also be used from the command line by installing `check-jsonschema <https://github.com/python-jsonschema/check-jsonschema>`_.

Features
--------

* Full support for `Draft 2020-12 <https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft202012Validator>`_, `Draft 2019-09 <https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft201909Validator>`_, `Draft 7 <https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft7Validator>`_, `Draft 6 <https://python-jsonsche
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: format checkers come with defaults, format error causes become validation error causes, it can register checkers, it can register cls checkers, it can validate no formats, it catches registered errors, it raises a key error for unknown formats, repr, custom error format, custom error format applies to schema errors, instance does not exist, instance does not exist pretty output, instance is invalid JSON, instance is invalid JSON on stdin, instance is invalid JSON on stdin pretty output, instance is invalid JSON pretty output, invalid explicit base uri, invalid instance, invalid instance continues with the rest, invalid instance explicit plain output, invalid instance multiple errors, invalid instance multiple errors pretty output, invalid instance pretty output, invalid schema, invalid schema multiple errors, invalid schema multiple errors pretty output, invalid schema pretty output, invalid schema with invalid instance.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `jsonschema` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names and public module members observed from the package surface include:

- `jsonschema.FormatChecker`
- `jsonschema.TypeChecker`
- `jsonschema.SchemaError`
- `jsonschema.ValidationError`
- `jsonschema.Draft3Validator`
- `jsonschema.Draft4Validator`
- `jsonschema.Draft6Validator`
- `jsonschema.Draft7Validator`
- `jsonschema.Draft201909Validator`
- `jsonschema.Draft202012Validator`
- `jsonschema.validate`
- `jsonschema.cli.parse_args`
- `jsonschema.cli.main`
- `jsonschema.cli.run`
- `jsonschema.exceptions.ValidationError`
- `jsonschema.exceptions.SchemaError`
- `jsonschema.exceptions.UndefinedTypeCheck`
- `jsonschema.exceptions.UnknownType`
- `jsonschema.exceptions.FormatError`
- `jsonschema.exceptions.ErrorTree`
- `jsonschema.exceptions.by_relevance`
- `jsonschema.exceptions.best_match`
- `jsonschema.protocols.Validator`
- `jsonschema.validators.validates`
- `jsonschema.validators.create`
- `jsonschema.validators.extend`
- `jsonschema.validators.validate`
- `jsonschema.validators.validator_for`

## Public API Behavior

- Public constructors, functions, classes, exceptions, and constants must be importable from the paths shown above when those paths are part of the documented package surface.
- Functions and methods should accept the documented Python value types, preserve caller-visible return types, and raise the documented exception classes for invalid inputs.
- Mutable public objects should expose stable user-visible state through public methods, properties, iteration, conversion, or rendering APIs rather than through private fields.
- Public options, presets, flags, and mode selectors must affect output consistently across API calls and command-style workflows.

## Parsing, Validation, Rendering, and Conversion Behavior

- Text parsers should accept documented input strings, preserve meaningful whitespace and token boundaries where the public API exposes them, and reject malformed input with the package's public errors.
- Validators should distinguish valid and invalid inputs through public result values, exceptions, iterators, or CLI exit behavior as appropriate for the package.
- Renderers and converters should produce deterministic user-visible output for the same input and configuration. Formatting differences that are part of the public output contract must be reproduced.
- Public plugin, preset, extension, or rule registration APIs should update the same behavior observed by normal parse/render/validate calls.

## Command and Workflow Behavior

- CLI or command-style entry points should parse documented arguments, read files or standard input where supported, write user-visible output to the appropriate stream, and return documented success/failure status.
- File-based workflows should keep path handling, encoding, and error behavior consistent with the Python API view of the same underlying data.
- Import hooks, interactive helpers, or runtime integration points that are public must compose with the core package behavior rather than bypassing it.

## Error Semantics

- Invalid inputs should fail with the package's public exception classes or documented CLI status codes.
- Unknown names, unsupported formats, malformed documents, and invalid configuration should be distinguished when the public API exposes separate error types or outcomes.
- Exact exception message wording is not part of the public contract unless it is itself documented user-facing behavior.

## Cross-View Invariants

- API calls and CLI workflows must agree on whether the same input is accepted or rejected.
- Parser output consumed by renderer/converter APIs should round-trip user-visible content according to documented behavior.
- Configuration passed at construction time and configuration passed at call time should resolve with documented precedence.
- Public serialization, representation, or token views should describe the same logical data observed through direct API access.
- Errors raised during direct API use and errors surfaced through command workflows should describe the same invalid condition.
- Repeated calls with the same input and public configuration should be deterministic unless the API explicitly documents time-, environment-, or randomness-dependent behavior.

## Representative Workflow

A typical implementation should allow a caller to import `jsonschema`, construct or configure the main public object, process an input document/value/string through the documented API, inspect the returned Python object or rendered text, and receive the same observable result when the equivalent command/file workflow is supported.

## Non-Goals

The library contract does not include private helper modules, private test utilities, release automation, packaging metadata, repository-only files, unexposed network integrations, or internal caching and data-structure choices.

## Evaluation Notes

Evaluation runs a filtered subset of upstream pytest nodeids against the candidate package in an isolated oracle worktree. The retained tests are mapped to this specification and are intended to measure public import surface, atomic behavior, cross-component integration, and end-to-end workflows. Candidates receive this specification only; source code, tests, retained nodeids, taxonomy, private scoring artifacts, and prior attempts are not part of the candidate packet.
