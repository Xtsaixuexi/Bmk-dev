# Filter Validation: pyparsing-fullrepro-001

Total collected nodeids: 2040
Kept covered nodeids: 298
Source-only nodeids: 307
Excluded nodeids: 1435
Spec gaps: 0

Layer counts:

- atomic: 167
- integration: 106
- system_e2e: 25

Validation checks:

1. Every kept nodeid has a real spec section mapping: pass.
2. `taxonomy.jsonl` uses scorer-compatible `test_file::Class.test` keys with parametrization suffixes stripped: pass.
3. All three layers are non-zero: pass.
4. Duplicated packrat/left-recursion mode repetitions of the same Test02 assertions are excluded to avoid multiplying identical behaviors: pass.
5. Exact warnings, debug text, diagram object internals/carrier imports, private util helpers, example applications, external matplotlib regressions, and non-retained source-shaped unit tests are excluded or source-only: pass.
6. Markdown table escaping for parameterized nodeids containing `|`: pass.

Decision: pass for reference validation.
