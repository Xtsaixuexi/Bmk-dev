# Spec Validation: doit-fullrepro-001

## Files Validated

- `spec/spec_v1.md`
- `spec/spec_v1_candidate.md`
- `spec.md`

## Candidate Packet Check

- `spec/spec_v1_candidate.md` and root `spec.md` are byte-identical.
- Candidate-visible files do not include the internal header.
- Candidate-visible files do not include source checkout paths, task audit paths, test file paths, or benchmark task metadata.

## Public API Surface Considered

Top-level exports from `doit.__all__`:

- `doit.get_var`
- `doit.run`
- `doit.create_after`
- `doit.task_params`
- `doit.Globals`

Additional documented user-facing imports and extension points considered:

- `doit.get_initial_workdir`
- `doit.api.run_tasks`
- `doit.action.CmdAction`, `PythonAction`, `create_action`
- `doit.task.Task`, `dict_to_task`, `clean_targets`, `result_dep`
- `doit.tools.create_folder`, `title_with_actions`, `run_once`, `config_changed`, `timeout`, `check_timestamp_unchanged`, `LongRunning`, `Interactive`, `PythonInteractiveAction`, `set_trace`, `load_ipython_extension`
- `doit.dependency.Dependency`, `DependencyStatus`, `FileChangedChecker`, `MD5Checker`, `TimestampChecker`, `JSONCodec`, `JsonDB`, `DbmDB`, `SqliteDB`, `DatabaseException`
- `doit.cmd_base.Command`, `DoitCmdBase`, `TaskLoader2`, `ModuleTaskLoader`, `DodoTaskLoader`, `get_loader`
- `doit.doit_cmd.DoitMain`, `DoitConfig`
- `doit.cmdparse.CmdOption`, `CmdParse`, `DefaultUpdate`, `CmdParseError`
- `doit.plugin.PluginEntry`, `PluginDict`
- `doit.reporter` reporter classes
- `doit.exceptions` public exception and failure classes

## Eleven-Point Validation

1. Traceability to public docs and day-one knowledge: pass. Included behaviors come from README, docs, top-level exports, documented imports, public docstrings, and tests that exercise those public paths.
2. Internal names or undocumented module paths: pass with note. The spec names public modules that are imported in documentation or used as extension APIs. It does not require private helpers or test support modules.
3. Invariants in behavioral language: pass. Cross-view invariants are stated as observable `must` relationships across loader, CLI, task, dependency, and reporter views.
4. Non-goals listed: pass.
5. Hidden fixture shape assumptions: pass. Evaluation Notes describe dimensions only and do not expose fixture layouts or expected values.
6. Behavioral statements use `must` / `returns` / `raises`: pass. A text scan found no standalone `can`, `may`, `should`, or `could` in candidate-visible behavioral sections.
7. Conditional behavior states conditions explicitly: pass. Conditions are written as `when`, `if`, or explicit command/API contexts.
8. Failure paths included: pass. Public validation and execution failures are mapped to `InvalidCommand`, `InvalidDodoFile`, `InvalidTask`, `CmdParseError`, `DatabaseException`, `TaskFailed`, and `TaskError`.
9. Product State Model before per-subsystem sections: pass. The spec defines task-definition, execution, and persistence projections before API details and includes cross-view consistency statements there.
10. Escape hatches avoided: pass. The spec uses concrete field lists, accepted values, return-code meanings, and exception mappings for public contract areas.
11. Priority/override rules: pass with conservative handling. The spec states that multiple configuration sources are accepted and that per-task, command, and global values reach their targets, but it avoids an unverified total precedence order beyond behaviors directly reflected in public APIs and tests.

## Residual Risk

- The CLI has many option-specific formatting details. The spec intentionally covers command behavior and option categories rather than exact help text layout or completion script text.
- Some low-level classes are public through documented extension usage and tests but are not all highlighted equally in narrative docs. They are included only at behavioral-contract granularity.
