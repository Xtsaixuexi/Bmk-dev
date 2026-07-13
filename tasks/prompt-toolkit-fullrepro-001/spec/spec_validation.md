# Spec Validation: prompt-toolkit-fullrepro-001

Generated: 2026-07-09

## Inputs Reviewed

- Stage 1 handoff: `candidate_selection.md`, `source_audit.json`, `source_pointer.md`, `filter_notes.md`, `PIPELINE_STATE.md`
- Workflow authority: `github_alignment/raw_main/skills/spec-writer/SKILL.md`, `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- Public docs and package metadata: README, pyproject, prompt/input docs, full-screen app docs, key binding docs, styling docs, formatted text docs, unit-testing docs, examples
- Public package surface: top-level exports, subpackage `__all__`, public signatures/docstrings under `src/prompt_toolkit`
- Behavioral tests reviewed for public behavior only: document, buffer, completion, key binding, formatted text, style, layout, prompt/application, filter, shortcut, and print tests

## Validation Checks

1. PASS: Every included feature is traceable to public docs, examples, `__all__`, or user-facing docstrings, and is day-one knowledge for reimplementing the covered API.
2. PASS: Candidate-visible files do not include local source paths, commit IDs, Stage 1 audit metadata, test paths, or private helper names as requirements.
3. PASS: Invariants are written as observable behavior across public objects: documents, buffers, completions, validators, layout focus, formatted text, styles, and application I/O.
4. PASS: Non-goals explicitly exclude terminal byte streams, exact render snapshots, private internals, contrib servers, dialogs/progress bars/widgets, and performance internals.
5. PASS: No section assumes hidden fixture shapes. The examples use ordinary public APIs and generic input/output objects.
6. PASS: Behavioral requirements use `must`, `return`, or `raise` wording. Non-contract prose is limited to overview, scope, non-goals, and evaluation explanation.
7. PASS: Conditional behavior states concrete trigger conditions, such as read-only buffers, invalid color strings, disabled fuzzy matching, missing focus targets, and configured prompt exceptions.
8. PASS: Failure paths are listed in `Error Semantics` and attached to relevant API sections where non-obvious.
9. PASS: `Product State Model` appears before per-subsystem sections and states cross-view behavior for text, interaction, and presentation projections.
10. PASS: No escape hatch permits skipping a covered behavior; the scope is deliberately limited but explicit.
11. PASS: Priority and override rules included in the spec were verified against public docs and public behavior tests/source examples: style rule ordering, class expansion, completion delegation/order, key binding eager/longer-match behavior, dynamic/conditional wrapper fallbacks, and prompt-call override semantics. No unverified multi-source merge rule was added.

## Candidate Packet Check

- `spec/spec_v1.md` contains an internal header plus candidate-visible body.
- `spec/spec_v1_candidate.md` is the candidate-visible body only.
- Root `spec.md` is byte-identical to `spec/spec_v1_candidate.md`.
- Grep check found no candidate-visible local path, source pointer, commit, GitHub alignment, task ID, or internal header leakage.

## Scope Notes

The spec intentionally narrows the public package to stable, reconstructable behavior for Document/Buffer, completion, validation, key bindings, formatted text, styles, layout controls, and application/input-output abstractions. It avoids promising terminal driver implementation details, exact ANSI byte output, and snapshot-exact rendering.

## Review Corrections Applied

- PASS: GLM 5.2 Stage 2 feedback on style lookup was addressed by documenting `BaseStyle.get_attrs_for_style_str`, `Style.get_attrs_for_style_str`, `Attrs` fields, and `DEFAULT_ATTRS`.
- PASS: `Template.format`, `fragment_list_len`, and `fragment_list_width` now have explicit public behavior clauses.
- PASS: `PromptSession` default interrupt and EOF exception types are documented as `KeyboardInterrupt` and `EOFError`.
- PASS: `Buffer.validate(set_cursor=False)` wording is consistent across Public API and Error Semantics.

## Uncertainties

- Some exported names outside the narrowed scope, such as contrib servers, progress bars, dialogs, and widget visual details, are public in the source tree but are excluded because the Stage 2 task scope explicitly asked to avoid them.
- `Binding` is treated as public behavior where exposed by `KeyBindings.bindings` and the `key_binding.key_bindings` `__all__`, but the candidate-facing surface emphasizes using `KeyBindings` rather than constructing `Binding` directly.
