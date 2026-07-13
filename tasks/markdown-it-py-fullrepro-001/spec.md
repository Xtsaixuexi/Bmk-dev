<!-- INTERNAL
task_id: markdown-it-py-fullrepro-001
spec_version: v1
delta: initial public-packet draft for remaining e2e project batch
source_boundary: README, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# markdown-it-py Specification

## Product Overview

This document describes the public behavior of `markdown_it`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
# markdown-it-py

[![Github-CI][github-ci]][github-link]
[![PyPI][pypi-badge]][pypi-link]
[![Conda][conda-badge]][conda-link]
[![PyPI - Downloads][install-badge]][install-link]

<p align="center">
  <img alt="markdown-it-py icon" src="https://raw.githubusercontent.com/executablebooks/markdown-it-py/master/docs/_static/markdown-it-py.svg">
</p>

> Markdown parser done right.

- Follows the __[CommonMark spec](http://spec.commonmark.org/)__ for baseline parsing
- Configurable syntax: you can add new rules and even replace existing ones.
- Pluggable: Adds syntax extensions to extend the parser (see the [plugin list][md-plugins]).
- High speed (see our [benchmarking tests][md-performance])
- Easy to configure for [security][md-security]
- Member of [Google's Assured Open Source Software](https://cloud.google.com/assured-open-source-software/docs/supported-packages)

This is a Python port of [markdown-it], and some of its associated plugins.
For more details see: <https://markdown-it-py.readthedocs.io>.

For details on [markdown-it] itself, see:

- The __[Live demo](https://markdown-it.github.io)__
- [The markdown-it README][markdown-it-readme]

**See also:** [markdown-it-pyrs](https://github.com/chrisjsewell/markdown-it-pyrs) for an experimental Rust binding,
for even more speed!

## Installation

### PIP

```bash
pip install markdown-it-py[plugins]
```

or with extras

```bash
pip install markdown-it-py[linkify,plugins]
```

### Conda

```bash
conda install -c conda-forge markdown-it-py
```

or with extras

```bash
conda install -c conda-forge markdown-it-py linkify-it-py mdit-py-plugins
```

## Usage

### Python API Usage

Render markdown to HTML with markdown-it-py and a custom configuration
with and without plugins and features:

```python
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

md = (
    MarkdownIt('commonmark', {'breaks':True,'html':True})
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .enable('table')
)
text = ("""
---
a: 1
---

a | b
- | -
1 | 2

A footnote [^1]

[^1]: some details
""")
tokens = md.parse(text)
html_text = md.render(text)

## To export the html to a file, uncomment the lines below:
# from pathlib import Path
# Path("output.html").write_text(html_text)
```

### Command-line Usage

Render markdown to HTML with markdown
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: get rules, load presets, override options, gfm like2 tasklists editable, gfm like2 alert token map, enable, disable, reset, parseInline, renderInline, emptyStr, empty env, table tokens, fragments join merges adjacent text tokens, text join merges adjacent text special tokens, basic, with info, colon in info allowed, longer closing, shorter closing no match, does not interfere with backtick, unclosed block, exact match same length, exact match longer no close, exact match shorter no close, nesting pattern, unclosed exact match, override with exact match.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `markdown_it` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names and public module members observed from the package surface include:

- `markdown_it.MarkdownIt`
- `markdown_it.cli.parse.main`
- `markdown_it.cli.parse.convert`
- `markdown_it.cli.parse.convert_stdin`
- `markdown_it.cli.parse.convert_file`
- `markdown_it.cli.parse.interactive`
- `markdown_it.cli.parse.parse_args`
- `markdown_it.cli.parse.print_heading`
- `markdown_it.common.normalize_url.normalizeLink`
- `markdown_it.common.normalize_url.normalizeLinkText`
- `markdown_it.common.normalize_url.validateLink`
- `markdown_it.common.utils.charCodeAt`
- `markdown_it.common.utils.charStrAt`
- `markdown_it.common.utils.arrayReplaceAt`
- `markdown_it.common.utils.isValidEntityCode`
- `markdown_it.common.utils.fromCodePoint`
- `markdown_it.common.utils.replaceEntityPattern`
- `markdown_it.common.utils.unescapeAll`
- `markdown_it.common.utils.stripEscape`
- `markdown_it.common.utils.escapeHtml`
- `markdown_it.common.utils.escapeRE`
- `markdown_it.common.utils.isSpace`
- `markdown_it.common.utils.isStrSpace`
- `markdown_it.common.utils.isWhiteSpace`
- `markdown_it.common.utils.isPunctChar`
- `markdown_it.common.utils.isMdAsciiPunct`
- `markdown_it.common.utils.normalizeReference`
- `markdown_it.common.utils.isLinkOpen`
- `markdown_it.common.utils.isLinkClose`
- `markdown_it.helpers.parse_link_destination.parseLinkDestination`
- `markdown_it.helpers.parse_link_label.parseLinkLabel`
- `markdown_it.helpers.parse_link_title.parseLinkTitle`
- `markdown_it.main.MarkdownIt`
- `markdown_it.parser_block.ParserBlock`
- `markdown_it.parser_core.ParserCore`
- `markdown_it.parser_inline.ParserInline`
- `markdown_it.presets.gfm_like`
- `markdown_it.presets.gfm_like2`
- `markdown_it.presets.commonmark.make`
- `markdown_it.presets.default.make`
- `markdown_it.presets.zero.make`
- `markdown_it.renderer.RendererProtocol`
- `markdown_it.renderer.RendererHTML`
- `markdown_it.ruler.StateBase`
- `markdown_it.ruler.RuleOptionsType`
- `markdown_it.ruler.Rule`
- `markdown_it.ruler.Ruler`
- `markdown_it.rules_block.blockquote.blockquote`
- `markdown_it.rules_block.code.code`
- `markdown_it.rules_block.fence.make_fence_rule`
- `markdown_it.rules_block.heading.heading`
- `markdown_it.rules_block.hr.hr`
- `markdown_it.rules_block.html_block.html_block`
- `markdown_it.rules_block.lheading.lheading`
- `markdown_it.rules_block.list.skipBulletListMarker`
- `markdown_it.rules_block.list.skipOrderedListMarker`
- `markdown_it.rules_block.list.markTightParagraphs`
- `markdown_it.rules_block.list.list_block`
- `markdown_it.rules_block.paragraph.paragraph`
- `markdown_it.rules_block.reference.reference`
- `markdown_it.rules_block.reference.getNextLine`
- `markdown_it.rules_block.state_block.StateBlock`
- `markdown_it.rules_block.table.getLine`
- `markdown_it.rules_block.table.escapedSplit`
- `markdown_it.rules_block.table.table`
- `markdown_it.rules_core.block.block`
- `markdown_it.rules_core.inline.inline`
- `markdown_it.rules_core.linkify.linkify`
- `markdown_it.rules_core.normalize.normalize`
- `markdown_it.rules_core.replacements.replaceFn`
- `markdown_it.rules_core.replacements.replace_scoped`
- `markdown_it.rules_core.replacements.replace_rare`
- `markdown_it.rules_core.replacements.replace`
- `markdown_it.rules_core.smartquotes.replaceAt`
- `markdown_it.rules_core.smartquotes.process_inlines`
- `markdown_it.rules_core.smartquotes.smartquotes`
- `markdown_it.rules_core.state_core.StateCore`
- `markdown_it.rules_core.text_join.text_join`
- `markdown_it.rules_inline.autolink.autolink`
- `markdown_it.rules_inline.backticks.backtick`

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

A typical implementation should allow a caller to import `markdown_it`, construct or configure the main public object, process an input document/value/string through the documented API, inspect the returned Python object or rendered text, and receive the same observable result when the equivalent command/file workflow is supported.

## Non-Goals

The library contract does not include private helper modules, private test utilities, release automation, packaging metadata, repository-only files, unexposed network integrations, or internal caching and data-structure choices.

## Evaluation Notes

Evaluation runs a filtered subset of upstream pytest nodeids against the candidate package in an isolated oracle worktree. The retained tests are mapped to this specification and are intended to measure public import surface, atomic behavior, cross-component integration, and end-to-end workflows. Candidates receive this specification only; source code, tests, retained nodeids, taxonomy, private scoring artifacts, and prior attempts are not part of the candidate packet.
