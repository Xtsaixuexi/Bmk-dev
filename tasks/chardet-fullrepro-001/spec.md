<!-- INTERNAL
task_id: chardet-fullrepro-001
spec_version: v1
delta: initial automated public-packet draft for e2e batch evaluation
source_boundary: README.md, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# chardet Specification

## Product Overview

This document describes the public behavior of `chardet`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
# chardet

Universal character encoding detector.

[![License: 0BSD](https://img.shields.io/badge/License-0BSD-blue.svg)](LICENSE)
[![Documentation](https://readthedocs.org/projects/chardet/badge/?version=latest)](https://chardet.readthedocs.io)
[![codecov](https://codecov.io/github/chardet/chardet/branch/main/graph/badge.svg?token=m5ZQrMd3vk)](https://codecov.io/github/chardet/chardet)

chardet 7 is a ground-up, 0BSD-licensed rewrite of [chardet](https://github.com/chardet/chardet).
Same package name, same public API — drop-in replacement for chardet 5.x/6.x, just much faster and more accurate.
Python 3.10+, zero runtime dependencies, works on PyPy.

[Read more details about the rewrite process.](https://dan-blanchard.github.io/blog/chardet-rewrite-controversy/)

## Why chardet 7?

**99.3% accuracy** on 2,517 test files. **47x faster** than chardet 6.0.0
and **1.5x faster** than charset-normalizer 3.4.6. **Language detection** for
every result. **MIME type detection** for binary files. **0BSD licensed.**

|                        | chardet 7.4.0 (mypyc) | chardet 6.0.0 | [charset-normalizer] 3.4.6 |
| ---------------------- | :--------------------: | :-----------: | :-------------------------: |
| Accuracy (2,517 files) |       **99.3%**        |     88.2%     |            85.4%            |
| Speed                  |    **551 files/s**     |  12 files/s   |         376 files/s         |
| Language detection     |       **95.7%**        |     40.0%     |            59.2%            |
| Peak memory            |     **52.9 MiB**       |   29.5 MiB    |          78.8 MiB           |
| Streaming detection    |        **yes**         |      yes      |             no              |
| Encoding era filtering |        **yes**         |      no       |             no              |
| Encoding filters       |        **yes**         |      no       |             yes             |
| MIME type detection    |        **yes**         |      no       |             no              |
| Supported encodings    |          99            |      84       |             99              |
| License                |          0BSD          |     LGPL      |            MIT              |

[charset-normalizer]: https://github.com/jawah/charset_normalizer

## Installation

~~~bash
pip install chardet
~~~

## Quick Start

~~~python
import chardet

chardet.detect(b"Python is a great programming language for beginners and experts alike.")
# {'encoding': 'ascii', 'confidence': 1.0, 'language': 'en', 'mime_type': 'text/plain'}

# UTF-8 English with accented characters
chardet.detect("The naïve approach doesn't always work in complex systems.".encode("utf-8"))
# {'encoding': 'utf-8', 'confidence': 0.84, 'language': 'en', 'mime_type': 'text/plain'}

# Japanese EUC-JP
chardet.detect("日本語の文字コード検出テストです。このテキストはEUC-JPでエンコードされています。正しく検出できるか確認します。".encode("euc-jp"))
# {'encoding': 'EUC-JP', 'confidence': 1.0, 'language': 'ja', 'mime_type': 'text/plain'}

# Get all candidate encodings ranked by confidence
text = "Le café est une boisson très populaire en France et dans le monde entier."
results = chardet.detect_all(text.encode("windows-1252"))
for r in results[:4]:
    print(r["encoding"], round(r["confidence"], 2))
# Windows-1252 0.32
# iso8859-15 0.32
# ISO-8859-1 0.32
# MacRoman 0.31
~~~

### Streaming Detection

For large files or network streams, use `UniversalDetector` to feed data incrementally:

~~~python
from chardet import UniversalDetector

detector = UniversalDetector()
w
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: detect; detect era filtered; detect streaming parity; detect returns dict; detect ascii; detect utf8 bom; detect utf8 multibyte; detect empty; detect with encoding era; encoding era excludes legacy; detect with max bytes; detect all returns list; detect all sorted by confidence; detect all each is dict.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `chardet` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names observed from the package surface include:

- `chardet.DEFAULT_MAX_BYTES`
- `chardet.MINIMUM_THRESHOLD`
- `chardet.DetectionDict`
- `chardet.DetectionResult`
- `chardet.EncodingEra`
- `chardet.LanguageFilter`
- `chardet.UniversalDetector`
- `chardet.detect`
- `chardet.detect_all`

Additional public module members observed in the package tree include:

- `chardet.cli.main`
- `chardet.detector.UniversalDetector`
- `chardet.enums.EncodingEra`
- `chardet.enums.LanguageFilter`
- `chardet.evaluation.is_language_equivalent`
- `chardet.evaluation.is_correct`
- `chardet.evaluation.is_equivalent_detection`
- `chardet.output_names.apply_preferred_superset`
- `chardet.output_names.apply_compat_names`
- `chardet.registry.EncodingInfo`
- `chardet.registry.get_candidates`
- `chardet.registry.lookup_encoding`
- `chardet.registry.normalize_encodings`

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

1. Import `chardet` from the solution package.
2. Construct or parse representative public input values using documented functions/classes.
3. Inspect public properties or return values.
4. Convert, format, serialize, tokenize, or execute the corresponding public workflow.
5. Handle invalid input using documented public exception types.

## Non-Goals

Do not reproduce upstream private helper modules, source-code layout, project release tooling, coverage tooling, or network-bound data fetching. Private implementation details and repository maintenance artifacts are outside the public contract.

## Evaluation Notes

The evaluator uses a filtered subset of public behavior checks that already pass on the reference implementation in this environment. Tests are grouped as atomic, integration, and system_e2e. Atomic tests focus on individual public functions/classes. Integration tests combine parsing, formatting, conversion, construction, or public helpers. System_e2e tests cover command or full workflow behavior when present. A correct implementation should satisfy the public behavior in this specification without matching private internals.
