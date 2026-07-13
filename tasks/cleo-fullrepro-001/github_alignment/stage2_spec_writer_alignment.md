# Stage 2 Spec Writer Alignment: cleo-fullrepro-001

## Stage

- stage: Stage 2 spec writing
- state target: `S2_SPEC_DONE_PENDING_REVIEW`
- source repo: `python-poetry/cleo`
- checkout: `python-poetry__cleo`

## Workflow Inputs Read

- `github_alignment/raw_main/skills/spec-writer/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- `candidate_selection.md`
- `source_audit.json`
- `source_pointer.md`
- `filter_notes.md`
- `PIPELINE_STATE.md`

## Source Boundary Read

- Project overview and metadata: `README.md`, `pyproject.toml`
- User documentation: usage, single-command applications, API index, and helper documentation
- Public package code: `src/cleo/application.py`, `src/cleo/commands/command.py`, `src/cleo/helpers.py`, public input/output modules, tester modules, loader modules, formatter/style modules, events, UI helpers, and exceptions
- Public behavior sampled from tests covering applications, commands, inputs, outputs, helpers, formatters, testers, loaders, events, UI helpers, and error behavior

## Inclusion Policy Applied

The spec includes names and behavior that are part of the intended external interface through one of:

- documented imports or README examples
- public application and command authoring APIs
- documented input, output, tester, helper, UI, formatting, event, loader, and exception surfaces
- user-observable command-line behavior for help, list, completions, command selection, parsed arguments/options, output, error output, and status codes
- public behaviors consistently exercised through upstream tests

The spec excludes:

- private helpers and implementation-only names
- exact ANSI escape bytes, cursor movement, terminal width snapshots, traceback text, completion script bodies, and column layout minutiae
- benchmark metadata, source checkout paths, test paths, hidden fixture shapes, kept-nodeid lists, and taxonomy artifacts

## Output Files

- `spec/spec_v1.md`: internal header plus candidate-visible body
- `spec/spec_v1_candidate.md`: candidate-visible body only
- `spec.md`: candidate-visible body only, same as `spec/spec_v1_candidate.md`
- `spec/spec_validation.md`: Stage 2 validation record
- `github_alignment/stage2_spec_writer_alignment.md`: this alignment record
- `PIPELINE_STATE.md`: state advanced to `S2_SPEC_DONE_PENDING_REVIEW`

## Alignment Notes

- The spec is written as library behavior for Cleo command applications, not as benchmark instructions.
- `Product State Model` appears before API sections and ties definition, input, execution, and output together.
- The public contract covers application registration, command invocation, argument/option parsing, output handling, testers, built-in commands, UI helpers, loaders, events, and public exceptions.
- Exact terminal rendering is treated as a non-goal unless it affects semantic content, stream routing, or status behavior.
