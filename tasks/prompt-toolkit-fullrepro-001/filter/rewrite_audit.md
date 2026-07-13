# Rewrite Audit: prompt-toolkit-fullrepro-001

Track A audited every upstream test file. Files with clean public imports and public behavioral assertions were retained directly. Files with module-level private/out-of-scope imports were excluded rather than rewritten when original collection would impose non-spec modules on candidates. Track B generated a public-only supplemental file for validation, error semantics, PromptSession, layout/application workflows, and cross-view coverage.

| file | collected_functions | covered | source-only | excluded | decision |
|---|---:|---:|---:|---:|---|
| `tests/test_async_generator.py` | 1 | 0 | 1 | 0 | eventloop async-generator helpers are outside the candidate spec scope |
| `tests/test_buffer.py` | 9 | 9 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_cli.py` | 34 | 0 | 0 | 34 | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_completion.py` | 18 | 18 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_document.py` | 12 | 12 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_filter.py` | 11 | 0 | 0 | 11 | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_formatted_text.py` | 15 | 15 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_history.py` | 4 | 0 | 4 | 0 | history classes and threaded history behavior are outside the narrowed spec scope |
| `tests/test_inputstream.py` | 11 | 0 | 0 | 11 | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_key_binding.py` | 6 | 6 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_layout.py` | 2 | 2 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_memory_leaks.py` | 1 | 0 | 1 | 0 | GC/memory lifetime behavior is outside the public behavioral contract |
| `tests/test_print_formatted_text.py` | 5 | 0 | 5 | 0 | asserts terminal escape output and platform skip helper behavior excluded by non-goals |
| `tests/test_regular_languages.py` | 4 | 0 | 4 | 0 | contrib regular language APIs are outside the narrowed spec scope |
| `tests/test_shortcuts.py` | 2 | 0 | 0 | 2 | private _split_multiline_prompt and widget visual/print-container behavior are outside scope |
| `tests/test_style.py` | 5 | 5 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_style_transformation.py` | 1 | 1 | 0 | 0 | retain direct upstream public behavioral tests |
| `tests/test_utils.py` | 1 | 0 | 1 | 0 | utility weighting helper is outside the covered public surface |
| `tests/test_vt100_output.py` | 2 | 0 | 0 | 2 | private VT100 output helpers and color table internals are non-goals |
| `tests/test_widgets.py` | 2 | 0 | 2 | 0 | widget visual polish is explicitly outside scope |
| `tests/test_yank_nth_arg.py` | 10 | 0 | 10 | 0 | history-specific yank argument behavior is not specified in the narrowed public contract |

Summary: upstream functions in scope = 156; upstream kept = 68; upstream excluded/source-only = 88; generated public tests = 32; merged oracle = 100.

No shared upstream helper files were imported by retained direct tests. No in-place rewrite of upstream source files was performed. Supplemental generated tests live in `filter/test_generated_public_oracle.py` and use only public APIs from the spec.
