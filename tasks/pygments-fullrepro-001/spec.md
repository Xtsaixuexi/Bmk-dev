<!-- INTERNAL
task_id: pygments-fullrepro-001
spec_version: v1
delta: initial automated public-packet draft for e2e batch evaluation
source_boundary: README.rst, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# pygments Specification

## Product Overview

This document describes the public behavior of `pygments`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
Welcome to Pygments
===================

This is the source of Pygments.  It is a **generic syntax highlighter** written
in Python that supports over 500 languages and text formats, for use in code
hosting, forums, wikis or other applications that need to prettify source code.

Installing
----------

... works as usual, use ``pip install Pygments`` to get published versions,
or ``pip install -e .`` to install from a checkout in editable mode.

Documentation
-------------

... can be found online at https://pygments.org/ or created with Sphinx by ::

   tox -e doc

By default, the documentation does not include the demo page, as it requires
having Docker installed for building Pyodide. To build the documentation with
the demo page, use ::

   tox -e web-doc

The initial build might take some time, but subsequent ones should be instant
because of Docker caching.

To view the generated documentation, serve it using Python's ``http.server``
module (this step is required for the demo to work) ::

   python3 -m http.server --directory doc/_build/html

Development
-----------

... takes place on `GitHub <https://github.com/pygments/pygments>`_, where the
Git repository, tickets and pull requests can be viewed.

Continuous testing runs on GitHub workflows:

.. image:: https://github.com/pygments/pygments/workflows/Pygments/badge.svg
   :target: https://github.com/pygments/pygments/actions?query=workflow%3APygments

Please read our `Contributing instructions <https://pygments.org/docs/contributing>`_.

Security considerations
-----------------------

Pygments provides no guarantees on execution time, which needs to be taken
into consideration when using Pygments to process arbitrary user inputs. For
example, if you have a web service which uses Pygments for highlighting, there
may be inputs which will cause the Pygments process to run "forever" and/or use
significant amounts of memory. This can subsequently be used to perform a
remote denial-of-service attack on the server if the processes are not
terminated quickly.

Unfortunately, it's practically impossible to harden Pygments itself against
those issues: Some regular expressions can result in "catastrophic
backtracking", but other bugs like incorrect matchers can also
cause similar problems, and there is no way to find them in an automated fashion
(short of solving the halting problem.) Pygments has extensive unit tests,
automated randomized testing, and is also tested by `OSS-Fuzz <https://github.com/google/oss-fuzz/tree/master/projects/pygments>`_,
but we will never be able to eliminate all bugs in this area.

Our recommendations are:

* Ensure that the Pygments process is *terminated* after a reasonably short
  timeout. In general Pygments should take seconds at most for reasonably-sized
  input.
* *Limit* the number of concurrent Pygments processes to avoid oversubscription
  of resources.

The Pygments authors will treat any bug resulting in long processing times with
high priority -- it's one of those things that will be fixed in a patch release.
When reporting a bug where you suspect super-linear execution times, please make
sure to attach an input to reproduce it.

The authors
-----------

Pygments is maintained by **Georg Brandl**, e-mail address *georg*\ *@*\ *python.org*, **Matthäus Chajdas** and **Jean Abou-Samra**.

Many lexers and fixes have been contributed by **Armin Ronacher**, the rest of
the `Pocoo <https://www.pocoo.org/>`_ team and **Tim Hatch**.

The code is distributed 
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: lexer instantiate all; lexer classes; lexer metadata uniqueness; random input; lexer options; get lexers; formatter public api; formatter encodings; formatter unicode handling.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `pygments` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names observed from the package surface include:

- `pygments.lex`
- `pygments.format`
- `pygments.highlight`

Additional public module members observed in the package tree include:

- `pygments.cmdline.main_inner`
- `pygments.cmdline.HelpFormatter`
- `pygments.cmdline.main`
- `pygments.console.reset_color`
- `pygments.console.colorize`
- `pygments.console.ansiformat`
- `pygments.filter.apply_filters`
- `pygments.filter.simplefilter`
- `pygments.filter.Filter`
- `pygments.filter.FunctionFilter`
- `pygments.formatter.Formatter`
- `pygments.lexer.LexerMeta`
- `pygments.lexer.Lexer`
- `pygments.lexer.DelegatingLexer`
- `pygments.lexer.include`
- `pygments.lexer.combined`
- `pygments.lexer.bygroups`
- `pygments.lexer.using`
- `pygments.lexer.default`
- `pygments.lexer.words`
- `pygments.lexer.RegexLexerMeta`
- `pygments.lexer.RegexLexer`
- `pygments.lexer.LexerContext`
- `pygments.lexer.ExtendedRegexLexer`
- `pygments.lexer.do_insertions`
- `pygments.lexer.ProfilingRegexLexerMeta`
- `pygments.lexer.ProfilingRegexLexer`
- `pygments.modeline.get_filetype_from_line`
- `pygments.modeline.get_filetype_from_buffer`
- `pygments.plugin.iter_entry_points`
- `pygments.plugin.find_plugin_lexers`
- `pygments.plugin.find_plugin_formatters`
- `pygments.plugin.find_plugin_styles`
- `pygments.plugin.find_plugin_filters`
- `pygments.regexopt.commonprefix`
- `pygments.regexopt.make_charset`
- `pygments.regexopt.regex_opt_inner`
- `pygments.regexopt.regex_opt`
- `pygments.scanner.EndOfText`
- `pygments.scanner.Scanner`
- `pygments.sphinxext.PygmentsDoc`
- `pygments.sphinxext.setup`
- `pygments.style.StyleMeta`
- `pygments.style.Style`
- `pygments.token.is_token_subtype`
- `pygments.token.string_to_tokentype`
- `pygments.unistring.combine`
- `pygments.unistring.allexcept`
- `pygments.util.ClassNotFound`
- `pygments.util.OptionError`
- `pygments.util.get_choice_opt`
- `pygments.util.get_bool_opt`
- `pygments.util.get_int_opt`
- `pygments.util.get_list_opt`
- `pygments.util.docstring_headline`
- `pygments.util.make_analysator`
- `pygments.util.shebang_matches`
- `pygments.util.doctype_matches`
- `pygments.util.html_doctype_matches`
- `pygments.util.looks_like_xml`
- `pygments.util.surrogatepair`
- `pygments.util.format_lines`
- `pygments.util.duplicates_removed`
- `pygments.util.Future`
- `pygments.util.guess_decode`
- `pygments.util.guess_decode_from_terminal`
- `pygments.util.terminal_encoding`
- `pygments.util.UnclosingTextIOWrapper`
- `pygments.util.html_escape`

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

1. Import `pygments` from the solution package.
2. Construct or parse representative public input values using documented functions/classes.
3. Inspect public properties or return values.
4. Convert, format, serialize, tokenize, or execute the corresponding public workflow.
5. Handle invalid input using documented public exception types.

## Non-Goals

Do not reproduce upstream private helper modules, source-code layout, project release tooling, coverage tooling, or network-bound data fetching. Private implementation details and repository maintenance artifacts are outside the public contract.

## Evaluation Notes

The evaluator uses a filtered subset of public behavior checks that already pass on the reference implementation in this environment. Tests are grouped as atomic, integration, and system_e2e. Atomic tests focus on individual public functions/classes. Integration tests combine parsing, formatting, conversion, construction, or public helpers. System_e2e tests cover command or full workflow behavior when present. A correct implementation should satisfy the public behavior in this specification without matching private internals.
