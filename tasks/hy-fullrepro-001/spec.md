<!-- INTERNAL
task_id: hy-fullrepro-001
spec_version: v1
delta: initial public-packet draft for remaining e2e project batch
source_boundary: README, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# hy Specification

## Product Overview

This document describes the public behavior of `hy`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
Hy
==

   :target: https://pypi.python.org/pypi/hy
   :alt: Version

.. image:: https://raw.github.com/hylang/shyte/18f6925e08684b0e1f52b2cc2c803989cd62cd91/imgs/xkcd.png
   :target: https://xkcd.com/224/
   :alt: XKCD #224

.. comment
   :title: We lost the documentation on quantum mechanics. You'll have to decode the regexes yourself.

Lisp and Python should love each other. Let's make it happen.

Hy is a Lisp dialect that's embedded in Python. Since Hy transforms its Lisp code into Python abstract syntax tree (AST) objects, you have the whole beautiful world of Python at your fingertips, in Lisp form.

To install the latest release of Hy, just use the command ``pip3 install --user hy``. Then you can start an interactive read-eval-print loop (REPL) with the command ``hy``, or run a Hy program with ``hy myprogram.hy``.

* `The Hy homepage <http://hylang.org>`__
* `Try Hy with a web console <http://hylang.org/try-hy>`__

Project
-------

* Code: https://github.com/hylang/hy
* Documentation: http://hylang.org/hy/doc
* Bug reports: We have no bugs! Your bugs are your own! (https://github.com/hylang/hy/issues)
* License: MIT (Expat)
* Community: Join us on `Github Discussions <https://github.com/hylang/hy/discussions>`__
* `Stack Overflow: The [hy] tag <https://stackoverflow.com/questions/tagged/hy>`__

Hy's current maintainer is `Kodi Arfer <https://github.com/Kodiologist>`__. He takes responsibility for answering user questions, which should primarily be asked on Stack Overflow or GitHub Discussions, but feel free to `poke him <http://arfer.net/elsewhere>`__ if he's missed a question or you've found a serious security issue.

.. image:: https://i.imgur.com/QbPMXTN.png
   :alt: Cuddles the Hacker

(fan art from the one and only `doctormo <http://doctormo.deviantart.com/art/Cuddles-the-Hacker-372184766>`__)
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: lex exception, unbalanced exception, lex single quote err, lex expression symbols, symbol and sugar, lex expression strings, lex expression integer, lex symbols, lex strings, lex strings exception, lex bracket strings, lex integers, lex expression float, lex big float, lex nan and inf, lex expression complex, lex digit separators, leading zero, dotted identifiers, lex bad attrs, lists, dicts, lex column counting, lex column counting with literal newline, lex line counting multi, symbol or keyword, wrap int, wrap tuple.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `hy` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names and public module members observed from the package surface include:

- `hy.nickname`
- `hy.last_version`
- `hy.I`
- `hy.cmdline.set_path`
- `hy.cmdline.run_command`
- `hy.cmdline.HyArgError`
- `hy.cmdline.cmdline_handler`
- `hy.cmdline.hy_main`
- `hy.cmdline.hyc_main`
- `hy.cmdline.hy2py_worker`
- `hy.cmdline.hy2py_main`
- `hy.compat.reu`
- `hy.compiler.calling_module`
- `hy.compiler.builds_model`
- `hy.compiler.Asty`
- `hy.compiler.Result`
- `hy.compiler.make_hy_model`
- `hy.compiler.mkexpr`
- `hy.compiler.is_annotate_expression`
- `hy.compiler.HyASTCompiler`
- `hy.compiler.get_compiler_module`
- `hy.compiler.hy_eval`
- `hy.compiler.hy_eval_user`
- `hy.compiler.hy_compile`
- `hy.completer.init_readline`
- `hy.completer.maybe_unmangle`
- `hy.completer.canonicalize`
- `hy.completer.Completer`
- `hy.completer.completion`
- `hy.core.result_macros.pvalue`
- `hy.core.result_macros.maybe_annotated`
- `hy.core.result_macros.dotted`
- `hy.core.result_macros.digest_type_params`
- `hy.core.result_macros.compile_do`
- `hy.core.result_macros.compile_eval_foo_compile`
- `hy.core.result_macros.compile_inline_python`
- `hy.core.result_macros.compile_pragma`
- `hy.core.result_macros.compile_quote`
- `hy.core.result_macros.render_quoted_form`
- `hy.core.result_macros.compile_unary_operator`
- `hy.core.result_macros.compile_logical_or_and_and_operator`
- `hy.core.result_macros.get_c_op`
- `hy.core.result_macros.compile_compare_op_expression`
- `hy.core.result_macros.compile_chained_comparison`
- `hy.core.result_macros.compile_maths_expression`
- `hy.core.result_macros.compile_augassign_expression`
- `hy.core.result_macros.compile_def_expression`
- `hy.core.result_macros.compile_let`
- `hy.core.result_macros.compile_basic_annotation`
- `hy.core.result_macros.compile_assign`
- `hy.core.result_macros.compile_deftype`
- `hy.core.result_macros.compile_global_or_nonlocal`
- `hy.core.result_macros.compile_del_expression`
- `hy.core.result_macros.compile_index_expression`
- `hy.core.result_macros.compile_attribute_access`
- `hy.core.result_macros.compile_cut_expression`
- `hy.core.result_macros.compile_unpack_iterable`
- `hy.core.result_macros.compile_if`
- `hy.core.result_macros.compile_comprehension`
- `hy.core.result_macros.compile_while_expression`
- `hy.core.result_macros.compile_break_or_continue_expression`
- `hy.core.result_macros.compile_with_expression`
- `hy.core.result_macros.compile_match_expression`
- `hy.core.result_macros.compile_pattern`
- `hy.core.result_macros.compile_raise_expression`
- `hy.core.result_macros.compile_try_expression`
- `hy.core.result_macros.compile_function_lambda`
- `hy.core.result_macros.compile_function_def`
- `hy.core.result_macros.compile_function_node`
- `hy.core.result_macros.compile_macro_def`
- `hy.core.result_macros.compile_lambda_list`
- `hy.core.result_macros.compile_arguments_set`
- `hy.core.result_macros.compile_return`
- `hy.core.result_macros.compile_yield_expression`
- `hy.core.result_macros.compile_yield_from_or_await_expression`
- `hy.core.result_macros.compile_class_expression`
- `hy.core.result_macros.module_name_str`
- `hy.core.result_macros.assignment_shape`
- `hy.core.result_macros.compile_require`
- `hy.core.result_macros.compile_import`

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

A typical implementation should allow a caller to import `hy`, construct or configure the main public object, process an input document/value/string through the documented API, inspect the returned Python object or rendered text, and receive the same observable result when the equivalent command/file workflow is supported.

## Non-Goals

The library contract does not include private helper modules, private test utilities, release automation, packaging metadata, repository-only files, unexposed network integrations, or internal caching and data-structure choices.

## Evaluation Notes

Evaluation runs a filtered subset of upstream pytest nodeids against the candidate package in an isolated oracle worktree. The retained tests are mapped to this specification and are intended to measure public import surface, atomic behavior, cross-component integration, and end-to-end workflows. Candidates receive this specification only; source code, tests, retained nodeids, taxonomy, private scoring artifacts, and prior attempts are not part of the candidate packet.
