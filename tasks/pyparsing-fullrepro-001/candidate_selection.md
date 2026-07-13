# Candidate Selection: pyparsing-fullrepro-001

## Decision

Selected `pyparsing` as the next full-reconstruction candidate.

Source repo: `/root/autodl-tmp/e2e/pyparsing`  
Commit: `ecb1b14dbf1ad1b699c081ed63b9746a244ee5fa`  
Task directory: `/root/autodl-tmp/Bmk-Lizhiqian/wip/pyparsing-fullrepro-001`

## Why This Candidate

`pyparsing` is a pure Python parsing toolkit with a documented public API for building grammar elements, composing parser expressions, parsing strings into `ParseResults`, attaching parse actions, and using helper namespaces such as `pyparsing.common`, `pyparsing.unicode`, and `pyparsing.testing`.

Positive signals:

- 10,004 non-comment source LOC across 17 Python source files.
- 106 test functions across 9 test files.
- README, docs, API docs, and examples are present.
- Top-level private import pre-screen is clean: no `from pyparsing._...` or `import pyparsing._...` matches in test files.
- Public behavior spans multiple projections: grammar construction API, parse result access as list/dict/attributes, helper expressions, parse actions, diagnostics/testing helpers, and documentation examples.
- Runtime dependency surface appears small at screening level. Test-only optional dependencies must be audited in Step 3.

## Gate Review

Hard gates:

- Pure Python package source LOC >= 3,000: pass.
- Not a single-file toy reconstruction: pass; public surface spans core parser elements, results, exceptions, helpers, unicode/common namespaces, testing helpers, and compatibility aliases.
- Shared fact source with multiple public projections: pass; grammar expressions produce parse results visible through list, dict, attribute, named result, parse action, and test/debug helper surfaces.
- Test suite present and not obviously network-bound: pass at screening level.
- Evaluator can be filtered toward public behavior: likely pass; Step 3 must remove tests tied to exact warnings, compatibility aliases, diagnostics formatting, diagram output, or source-specific internals.

Soft gates:

- Documentation coverage: strong, with README, docs, generated API docs, examples, and package docstrings.
- Dependency control: favorable at screening level; no mandatory network/database/service dependency found.
- Public API import audit: favorable; private import pre-screen is clean.

## Risks

- Parser-combinator libraries have a broad API and many legacy compatibility names, so the spec must carefully separate day-one public behavior from source-level compatibility trivia.
- Some tests may be implementation-shaped, especially exact diagnostic output, warning messages, railroad diagram details, or deprecated camelCase compatibility behavior.
- `pyparsing` is a mature and well-known library; benchmark value depends on retaining tests that exercise cross-component parser composition rather than only common parsing primitives.

## Decision

Keep for Step 2 after human approval.
