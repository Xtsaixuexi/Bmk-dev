<!-- INTERNAL
task_id: rich-fullrepro-001
spec_version: v1
delta: initial public-packet draft for remaining e2e project batch
source_boundary: README, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# rich Specification

## Product Overview

This document describes the public behavior of `rich`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
[![Downloads](https://pepy.tech/badge/rich/month)](https://pepy.tech/project/rich)

![Logo](https://github.com/textualize/rich/raw/main/imgs/logo.svg)

[English readme](https://github.com/textualize/rich/blob/main/README.md)
 • [简体中文 readme](https://github.com/textualize/rich/blob/main/README.cn.md)
 • [正體中文 readme](https://github.com/textualize/rich/blob/main/README.zh-tw.md)
 • [Lengua española readme](https://github.com/textualize/rich/blob/main/README.es.md)
 • [Deutsche readme](https://github.com/textualize/rich/blob/main/README.de.md)
 • [Läs på svenska](https://github.com/textualize/rich/blob/main/README.sv.md)
 • [日本語 readme](https://github.com/textualize/rich/blob/main/README.ja.md)
 • [한국어 readme](https://github.com/textualize/rich/blob/main/README.kr.md)
 • [Français readme](https://github.com/textualize/rich/blob/main/README.fr.md)
 • [Schwizerdütsch readme](https://github.com/textualize/rich/blob/main/README.de-ch.md)
 • [हिन्दी readme](https://github.com/textualize/rich/blob/main/README.hi.md)
 • [Português brasileiro readme](https://github.com/textualize/rich/blob/main/README.pt-br.md)
 • [Italian readme](https://github.com/textualize/rich/blob/main/README.it.md)
 • [Русский readme](https://github.com/textualize/rich/blob/main/README.ru.md)
 • [Indonesian readme](https://github.com/textualize/rich/blob/main/README.id.md)
 • [فارسی readme](https://github.com/textualize/rich/blob/main/README.fa.md)
 • [Türkçe readme](https://github.com/textualize/rich/blob/main/README.tr.md)
 • [Polskie readme](https://github.com/textualize/rich/blob/main/README.pl.md)


Rich is a Python library for _rich_ text and beautiful formatting in the terminal.

The [Rich API](https://rich.readthedocs.io/en/latest/) makes it easy to add color and style to terminal output. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, tracebacks, and more — out of the box.

![Features](https://github.com/textualize/rich/raw/main/imgs/features.png)

For a video introduction to Rich see [calmcode.io](https://calmcode.io/rich/introduction.html) by [@fishnets88](https://twitter.com/fishnets88).

See what [people are saying about Rich](https://www.willmcgugan.com/blog/pages/post/rich-tweets/).

## Compatibility

Rich works with Linux, macOS and Windows. True color / emoji works with new Windows Terminal, classic terminal is limited to 16 colors. R
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: span, span split, span move, span right crop, len, cell len, bool, str, repr, add, eq, contain, plain property, plain property setter, from markup, from ansi, copy, rstrip, rstrip end, stylize, dumb terminal, soft wrap, 16color terminal, truecolor terminal, kitty terminal, console options update, console options update height, init.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `rich` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names and public module members observed from the package surface include:

- `rich.IO`
- `rich.TYPE_CHECKING`
- `rich.Any`
- `rich.Callable`
- `rich.Optional`
- `rich.Union`
- `rich.load_ipython_extension`
- `rich.get_console`
- `rich.reconfigure`
- `rich.print`
- `rich.print_json`
- `rich.inspect`
- `rich._unicode_data.load`
- `rich.abc.RichRenderable`
- `rich.align.Align`
- `rich.align.VerticalCenter`
- `rich.ansi.AnsiDecoder`
- `rich.bar.Bar`
- `rich.box.Box`
- `rich.cells.CellTable`
- `rich.cells.get_character_cell_size`
- `rich.cells.cached_cell_len`
- `rich.cells.cell_len`
- `rich.cells.split_graphemes`
- `rich.cells.split_text`
- `rich.cells.set_cell_size`
- `rich.cells.chop_cells`
- `rich.color.ColorSystem`
- `rich.color.ColorType`
- `rich.color.ColorParseError`
- `rich.color.Color`
- `rich.color.parse_rgb_hex`
- `rich.color.blend_rgb`
- `rich.color_triplet.ColorTriplet`
- `rich.columns.Columns`
- `rich.console.NoChange`
- `rich.console.ConsoleDimensions`
- `rich.console.ConsoleOptions`
- `rich.console.RichCast`
- `rich.console.ConsoleRenderable`
- `rich.console.CaptureError`
- `rich.console.NewLine`
- `rich.console.ScreenUpdate`
- `rich.console.Capture`
- `rich.console.ThemeContext`
- `rich.console.PagerContext`
- `rich.console.ScreenContext`
- `rich.console.Group`
- `rich.console.group`
- `rich.console.ConsoleThreadLocals`
- `rich.console.RenderHook`
- `rich.console.get_windows_console_features`
- `rich.console.detect_legacy_windows`
- `rich.console.Console`
- `rich.constrain.Constrain`
- `rich.containers.Renderables`
- `rich.containers.Lines`
- `rich.control.Control`
- `rich.control.strip_control_codes`
- `rich.control.escape_control_codes`
- `rich.diagnose.report`
- `rich.emoji.NoEmoji`
- `rich.emoji.Emoji`
- `rich.errors.ConsoleError`
- `rich.errors.StyleError`
- `rich.errors.StyleSyntaxError`
- `rich.errors.MissingStyle`
- `rich.errors.StyleStackError`
- `rich.errors.NotRenderableError`
- `rich.errors.MarkupError`
- `rich.errors.LiveError`
- `rich.errors.NoAltScreen`
- `rich.file_proxy.FileProxy`
- `rich.filesize.pick_unit_and_suffix`
- `rich.filesize.decimal`
- `rich.highlighter.Highlighter`
- `rich.highlighter.NullHighlighter`
- `rich.highlighter.RegexHighlighter`
- `rich.highlighter.ReprHighlighter`
- `rich.highlighter.JSONHighlighter`

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

A typical implementation should allow a caller to import `rich`, construct or configure the main public object, process an input document/value/string through the documented API, inspect the returned Python object or rendered text, and receive the same observable result when the equivalent command/file workflow is supported.

## Non-Goals

The library contract does not include private helper modules, private test utilities, release automation, packaging metadata, repository-only files, unexposed network integrations, or internal caching and data-structure choices.

## Evaluation Notes

Evaluation runs a filtered subset of upstream pytest nodeids against the candidate package in an isolated oracle worktree. The retained tests are mapped to this specification and are intended to measure public import surface, atomic behavior, cross-component integration, and end-to-end workflows. Candidates receive this specification only; source code, tests, retained nodeids, taxonomy, private scoring artifacts, and prior attempts are not part of the candidate packet.
