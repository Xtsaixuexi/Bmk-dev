# Stage 2 Spec Writer Alignment: doit-fullrepro-001

## Stage

- stage: Stage 2 spec writing
- state target: `S2_SPEC_DONE_PENDING_REVIEW`
- source repo: `pydoit/doit`
- checkout: `pydoit__doit`

## Workflow Inputs Read

- `github_alignment/raw_main/skills/spec-writer/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- `candidate_selection.md`
- `source_audit.json`
- `source_pointer.md`
- `filter_notes.md`
- `PIPELINE_STATE.md`

## Source Boundary Read

- Project metadata and overview: `README.rst`, `pyproject.toml`
- User documentation: task basics, dependency model, up-to-date helpers, CLI run/options, other CLI commands, task arguments, task creation, configuration, extending, tools, globals
- Public package code: `doit/__init__.py`, `api.py`, `action.py`, `task.py`, `loader.py`, `dependency.py`, `cmd_base.py`, `doit_cmd.py`, `cmdparse.py`, `plugin.py`, `reporter.py`, `tools.py`, `exceptions.py`
- Public behavior sampled from tests covering API, loader, task, action, dependency, cmdparse, command base, CLI command modules, reporters, tools, runners, control, and plugin loading

## Inclusion Policy Applied

The spec includes names and behavior that are part of the intended external interface through one of:

- top-level `doit.__all__`
- explicit docs imports or Sphinx documented classes
- documented extension hooks for loaders, commands, reporters, plugins, and dependency backends
- public task dictionary and CLI contracts demonstrated in documentation
- public exceptions and failure objects users observe or catch

The spec excludes:

- private helpers and implementation-only names
- exact stdout column widths, traceback text, shell completion script bodies, and internal database file extensions
- optional external `auto` watcher package behavior
- benchmark metadata, source checkout paths, test paths, and hidden fixture shapes

## Output Files

- `spec/spec_v1.md`: internal header plus candidate-visible body
- `spec/spec_v1_candidate.md`: candidate-visible body only
- `spec.md`: candidate-visible body only, same as `spec/spec_v1_candidate.md`
- `spec/spec_validation.md`: Stage 2 validation record
- `github_alignment/stage2_spec_writer_alignment.md`: this alignment record
- `PIPELINE_STATE.md`: state advanced to `S2_SPEC_DONE_PENDING_REVIEW`

## Alignment Notes

- The spec is written as library documentation for `doit`, with benchmark protocol details confined to `Evaluation Notes`.
- `Product State Model` appears before subsystem API sections and ties task definitions, execution, and persistence together.
- `Cross-View Invariants` includes ten observable invariants spanning loader, CLI, task objects, actions, dependency persistence, reporters, ignored state, forget state, hidden tasks, and delayed tasks.
- Error semantics map public failure classes to trigger conditions.
- Public API coverage is broader than `doit.__all__` because upstream documentation exposes `doit.tools`, `doit.cmd_base`, `doit.dependency`, `doit.action`, `doit.reporter`, and `doit.plugin` as extension surfaces.
