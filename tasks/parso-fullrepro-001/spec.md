<!-- INTERNAL
task_id: parso-fullrepro-001
spec_version: v1
delta: initial automated public-packet draft for e2e batch evaluation
source_boundary: README.rst, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# parso Specification

## Product Overview

This document describes the public behavior of `parso`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
###################################################################
parso - A Python Parser
###################################################################

.. image:: https://github.com/davidhalter/parso/workflows/Build/badge.svg?branch=master
    :target: https://github.com/davidhalter/parso/actions
    :alt: GitHub Actions build status

.. image:: https://coveralls.io/repos/github/davidhalter/parso/badge.svg?branch=master
    :target: https://coveralls.io/github/davidhalter/parso?branch=master
    :alt: Coverage Status

.. image:: https://pepy.tech/badge/parso
    :target: https://pepy.tech/project/parso
    :alt: PyPI Downloads

.. image:: https://raw.githubusercontent.com/davidhalter/parso/master/docs/_static/logo_characters.png

Parso is a Python parser that supports error recovery and round-trip parsing
for different Python versions (in multiple Python versions). Parso is also able
to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi_. It was pulled out of jedi to be useful
for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax tree.

A simple example:

.. code-block:: python

    >>> import parso
    >>> module = parso.parse('hello + 1', version="3.9")
    >>> expr = module.children[0]
    >>> expr
    PythonNode(arith_expr, [<Name: hello@1,0>, <Operator: +>, <Number: 1>])
    >>> print(expr.get_code())
    hello + 1
    >>> name = expr.children[0]
    >>> name
    <Name: hello@1,0>
    >>> name.end_pos
    (1, 5)
    >>> expr.end_pos
    (1, 9)

To list multiple issues:

.. code-block:: python

    >>> grammar = parso.load_grammar()
    >>> module = grammar.parse('foo +\nbar\ncontinue')
    >>> error1, error2 = grammar.iter_errors(module)
    >>> error1.message
    'SyntaxError: invalid syntax'
    >>> error2.message
    "SyntaxError: 'continue' not properly in loop"

Resources
=========

- `Testing <https://parso.readthedocs.io/en/latest/docs/development.html#testing>`_
- `PyPI <https://pypi.python.org/pypi/parso>`_
- `Docs <https://parso.readthedocs.org/en/latest/>`_
- Uses `semantic versioning <https://semver.org/>`_

Installation
============

.. code-block:: bash

    pip install parso

Future
======

- There will be better support for refactoring and comments. Stay tuned.
- There's a WIP PEP8 validator. It's however not in a good shape, yet.

Known Issues
============

- `async`/`await` are already used as keywords in Python3.6.
- `from __future__ import print_function` is not ignored.

Acknowledgements
================

- Guido van Rossum (@gvanrossum) for creating the parser generator pgen2
  (originally used in lib2to3).
- Salome Schneider for the extremely awesome parso logo.

.. _jedi: https://github.com/davidhalter/jedi
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: modulepickling change cache dir; modulepickling simulate deleted cache; cache limit; cache last used update; inactive cache; permission error; simple; change and undo; positions; if simple; func with for and comment; one statement func; for on one line; open parentheses; open parentheses at end; backslash; full copy; wrong whitespace.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `parso` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names observed from the package surface include:

- `parso.parse`

Additional public module members observed in the package tree include:

- `parso.cache.load_module`
- `parso.cache.try_to_save_module`
- `parso.cache.clear_cache`
- `parso.cache.clear_inactive_cache`
- `parso.file_io.FileIO`
- `parso.file_io.KnownContentFileIO`
- `parso.grammar.Grammar`
- `parso.grammar.PythonGrammar`
- `parso.grammar.load_grammar`
- `parso.normalizer.Normalizer`
- `parso.normalizer.NormalizerConfig`
- `parso.normalizer.Issue`
- `parso.normalizer.Rule`
- `parso.normalizer.RefactoringNormalizer`
- `parso.parser.ParserSyntaxError`
- `parso.parser.InternalParseError`
- `parso.parser.Stack`
- `parso.parser.StackNode`
- `parso.parser.BaseParser`
- `parso.tree.search_ancestor`
- `parso.tree.NodeOrLeaf`
- `parso.tree.Leaf`
- `parso.tree.TypedLeaf`
- `parso.tree.BaseNode`
- `parso.tree.Node`
- `parso.tree.ErrorNode`
- `parso.tree.ErrorLeaf`
- `parso.utils.Version`
- `parso.utils.split_lines`
- `parso.utils.python_bytes_to_unicode`
- `parso.utils.version_info`
- `parso.utils.PythonVersionInfo`
- `parso.utils.parse_version_string`

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

1. Import `parso` from the solution package.
2. Construct or parse representative public input values using documented functions/classes.
3. Inspect public properties or return values.
4. Convert, format, serialize, tokenize, or execute the corresponding public workflow.
5. Handle invalid input using documented public exception types.

## Non-Goals

Do not reproduce upstream private helper modules, source-code layout, project release tooling, coverage tooling, or network-bound data fetching. Private implementation details and repository maintenance artifacts are outside the public contract.

## Evaluation Notes

The evaluator uses a filtered subset of public behavior checks that already pass on the reference implementation in this environment. Tests are grouped as atomic, integration, and system_e2e. Atomic tests focus on individual public functions/classes. Integration tests combine parsing, formatting, conversion, construction, or public helpers. System_e2e tests cover command or full workflow behavior when present. A correct implementation should satisfy the public behavior in this specification without matching private internals.
