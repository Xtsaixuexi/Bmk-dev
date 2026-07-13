<!-- INTERNAL
task_id: sqlparse-fullrepro-001
spec_version: v1
delta: initial automated public-packet draft for e2e batch evaluation
source_boundary: README.rst, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# sqlparse Specification

## Product Overview

This document describes the public behavior of `sqlparse`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
python-sqlparse - Parse SQL statements
======================================

|buildstatus|_
|coverage|_
|docs|_
|packageversion|_

.. docincludebegin

sqlparse is a non-validating SQL parser for Python.
It provides support for parsing, splitting and formatting SQL statements.

The module is compatible with Python 3.8+ and released under the terms of the
`New BSD license <https://opensource.org/licenses/BSD-3-Clause>`_.

Visit the project page at https://github.com/andialbrecht/sqlparse for
further information about this project.

Quick Start
-----------

.. code-block:: sh

   $ pip install sqlparse

.. code-block:: python

   >>> import sqlparse

   >>> # Split a string containing two SQL statements:
   >>> raw = 'select * from foo; select * from bar;'
   >>> statements = sqlparse.split(raw)
   >>> statements
   ['select * from foo;', 'select * from bar;']

   >>> # Format the first statement and print it out:
   >>> first = statements[0]
   >>> print(sqlparse.format(first, reindent=True, keyword_case='upper'))
   SELECT *
   FROM foo;

   >>> # Parsing a SQL statement:
   >>> parsed = sqlparse.parse('select * from foo')[0]
   >>> parsed.tokens
   [<DML 'select' at 0x7f22c5e15368>, <Whitespace ' ' at 0x7f22c5e153b0>, <Wildcard '*' … ]
   >>>

Pre-commit Hook
---------------

sqlparse can be used as a `pre-commit <https://pre-commit.com/>`_ hook
to automatically format SQL files before committing:

.. code-block:: yaml

   repos:
     - repo: https://github.com/andialbrecht/sqlparse
       rev: 0.5.4  # Use the latest version
       hooks:
         - id: sqlformat
           # Optional: Add more formatting options
           # IMPORTANT: --in-place is required, already included by default
           args: [--in-place, --reindent, --keywords, upper]

Then install the hook:

.. code-block:: sh

   $ pre-commit install

Your SQL files will now be automatically formatted on each commit.

**Note**: The hook uses ``--in-place --reindent`` by default. If you override
the ``args``, you **must** include ``--in-place`` for the hook to work.

Links
-----

Project page
   https://github.com/andialbrecht/sqlparse

Bug tracker
   https://github.com/andialbrecht/sqlparse/issues

Documentation
   https://sqlparse.readthedocs.io/

Online Demo
   https://sqlformat.org/

sqlparse is licensed under the BSD license.

Parts of the code are based on pygments written by Georg Brandl and others.
pygments-Homepage: http://pygments.org/

.. |buildstatus| image:: https://github.com/andialbrecht/sqlparse/actions/workflows/python-app.yml/badge.svg
.. _buildstatus: https://github.com/andialbrecht/sqlparse/actions/workflows/python-app.yml
.. |coverage| image:: https://codecov.io/gh/andialbrecht/sqlparse/branch/master/graph/badge.svg
.. _coverage: https://codecov.io/gh/andialbrecht/sqlparse
.. |docs| image:: https://readthedocs.org/projects/sqlparse/badge/?version=latest
.. _docs: https://sqlparse.readthedocs.io/en/latest/?badge=latest
.. |packageversion| image:: https://img.shields.io/pypi/v/sqlparse?color=%2334D058&label=pypi%20package
.. _packageversion: https://pypi.org/project/sqlparse
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: cli main empty; parser empty; main help; valid args; invalid choice; invalid args; invalid infile; invalid outfile; stdout; script; encoding stdout; encoding output file; encoding stdin; encoding; cli multiple files with inplace; cli multiple files without inplace fails; cli inplace with stdin fails.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `sqlparse` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names observed from the package surface include:

- `sqlparse.cli`
- `sqlparse.engine`
- `sqlparse.filters`
- `sqlparse.formatter`
- `sqlparse.sql`
- `sqlparse.tokens`
- `sqlparse.parse`
- `sqlparse.parsestream`
- `sqlparse.format`
- `sqlparse.split`

Additional public module members observed in the package tree include:

- `sqlparse.cli.create_parser`
- `sqlparse.cli.main`
- `sqlparse.exceptions.SQLParseError`
- `sqlparse.formatter.validate_options`
- `sqlparse.formatter.build_filter_stack`
- `sqlparse.lexer.Lexer`
- `sqlparse.lexer.tokenize`
- `sqlparse.sql.NameAliasMixin`
- `sqlparse.sql.Token`
- `sqlparse.sql.TokenList`
- `sqlparse.sql.Statement`
- `sqlparse.sql.Identifier`
- `sqlparse.sql.IdentifierList`
- `sqlparse.sql.TypedLiteral`
- `sqlparse.sql.Parenthesis`
- `sqlparse.sql.SquareBrackets`
- `sqlparse.sql.Assignment`
- `sqlparse.sql.If`
- `sqlparse.sql.For`
- `sqlparse.sql.Comparison`
- `sqlparse.sql.Comment`
- `sqlparse.sql.Where`
- `sqlparse.sql.Over`
- `sqlparse.sql.Having`
- `sqlparse.sql.Case`
- `sqlparse.sql.Function`
- `sqlparse.sql.Begin`
- `sqlparse.sql.Operation`
- `sqlparse.sql.Values`
- `sqlparse.sql.Command`
- `sqlparse.utils.split_unquoted_newlines`
- `sqlparse.utils.remove_quotes`
- `sqlparse.utils.recurse`
- `sqlparse.utils.imt`
- `sqlparse.utils.consume`
- `sqlparse.utils.offset`
- `sqlparse.utils.indent`

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

1. Import `sqlparse` from the solution package.
2. Construct or parse representative public input values using documented functions/classes.
3. Inspect public properties or return values.
4. Convert, format, serialize, tokenize, or execute the corresponding public workflow.
5. Handle invalid input using documented public exception types.

## Non-Goals

Do not reproduce upstream private helper modules, source-code layout, project release tooling, coverage tooling, or network-bound data fetching. Private implementation details and repository maintenance artifacts are outside the public contract.

## Evaluation Notes

The evaluator uses a filtered subset of public behavior checks that already pass on the reference implementation in this environment. Tests are grouped as atomic, integration, and system_e2e. Atomic tests focus on individual public functions/classes. Integration tests combine parsing, formatting, conversion, construction, or public helpers. System_e2e tests cover command or full workflow behavior when present. A correct implementation should satisfy the public behavior in this specification without matching private internals.
