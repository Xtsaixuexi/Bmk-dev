<!-- INTERNAL
task_id: doit-fullrepro-001
spec_version: v1
delta: Initial Stage 2 candidate-visible specification for pydoit/doit. Includes public task model, CLI surface, embedded API, actions, dependency persistence, tools, extension APIs, error semantics, invariants, workflows, non-goals, and evaluation notes.
source_boundary: candidate_selection.md; source_audit.json; source_pointer.md; filter_notes.md; README.rst; pyproject.toml; docs under doc/index.rst, doc/tasks.rst, doc/dependencies.rst, doc/uptodate.rst, doc/cmd-run.rst, doc/cmd-other.rst, doc/task-args.rst, doc/task-creation.rst, doc/configuration.rst, doc/extending.rst, doc/tools.rst, doc/globals.rst; public package files doit/__init__.py, doit/api.py, doit/action.py, doit/task.py, doit/loader.py, doit/dependency.py, doit/cmd_base.py, doit/doit_cmd.py, doit/cmdparse.py, doit/plugin.py, doit/reporter.py, doit/tools.py, doit/exceptions.py; public behavior sampled from tests for api, loader, task, action, dependency, cmdparse, command, reporter, tools, runner, control, plugin, and CLI command modules.
-->
# doit Specification

## Product Overview

`doit` is a Python-native task runner and automation library. A project describes work in normal Python code, most commonly in a `dodo.py` file, by defining task-creator functions whose names start with `task_`. Each task is represented by a dictionary or by a `Task` object. A task declares actions, file dependencies, task dependencies, generated targets, parameters, cleanup actions, and up-to-date checks.

The command line program `doit` loads tasks, builds a dependency graph, decides which selected tasks are out of date, runs required actions in dependency order, records successful execution state in a persistent dependency database, and skips tasks whose observable inputs have not changed. The Python API exposes the same model for embedded applications, custom loaders, custom commands, custom reporters, and reusable task utilities.

## Scope

This specification covers the installed `doit` package, the `doit` command line entry point, task dictionaries and `Task` objects, action execution, task loading, dependency persistence, built-in up-to-date helpers, configuration loading, reporter behavior, plugin registration, and the extension APIs documented for users.

The covered behavior is the public contract needed to define, load, inspect, execute, clean, forget, ignore, and extend `doit` tasks. The contract includes user-visible exception classes, return codes, task status meanings, and the shared state that connects the CLI, Python API, dependency manager, reporters, and task objects.

## Installable Surface

Installing the package provides:

- Import package: `doit`.
- Console script: `doit`, equivalent to `python -m doit`.
- Top-level imports: `doit.__version__`, `doit.get_var(name, default=None)`, `doit.get_initial_workdir()`, `doit.run(task_creators)`, `doit.create_after(executed=None, target_regex=None, creates=None)`, `doit.task_params(param_def=None)`, and `doit.Globals`.
- Public modules for task authors and embedders: `doit.action`, `doit.api`, `doit.cmd_base`, `doit.cmdparse`, `doit.dependency`, `doit.doit_cmd`, `doit.exceptions`, `doit.loader`, `doit.plugin`, `doit.reporter`, `doit.runner`, `doit.task`, and `doit.tools`.

The command line form is:

```console
doit [run] [options] [task-or-target task-options]* [name=value ...]
```

When no subcommand is supplied, the command must behave as `doit run`.

## Product State Model

`doit` maintains one logical task state with three public projections:

- The task-definition projection: task creators, task dictionaries, `Task` objects, task parameters, task dependencies, file dependencies, targets, action lists, cleanup lists, and metadata.
- The execution projection: selected task names or targets, command-line variables, parsed task option values, action results, captured output, failures, ignored tasks, and reporter events.
- The persistence projection: the dependency database storing successful file-dependency states, saved action values, saved task results, ignored markers, and backend-specific storage files.

The projections must remain coherent during one command invocation:

- A task loaded from a `dodo.py` task creator must be the same task selected by CLI name, listed by `doit list`, inspected by `doit info`, passed to reporters, and saved by the dependency manager.
- A value returned by a successful Python action as a dictionary must be visible through the task object's `values` during the run and through `Globals.dep_manager.get_value()` after a successful save.
- A task result saved by an action must be the result compared by `result_dep()` and the result returned by `Dependency.get_result()`.
- A file dependency declared in a task dictionary must be normalized into the task object, used to decide up-to-date status, shown by dependency-aware commands, and saved in the dependency database after success.
- A task marked ignored through the command interface must be skipped by the runner and reported as ignored until the saved state is removed.
- A task forgotten through the command interface must lose its successful execution record so the next compatible run treats it as not up to date when no other up-to-date evidence remains.

## Public API

### Top-Level API

```python
doit.get_var(name, default=None)
doit.get_initial_workdir()
doit.run(task_creators)
doit.create_after(executed=None, target_regex=None, creates=None)
doit.task_params(param_def=None)
doit.Globals.dep_manager
```

`get_var()` returns command-line variables passed as `name=value`. It returns `default` when the variable was not passed after command-line variable storage has been initialized. It returns `None` when called before command-line variable storage is initialized.

`get_initial_workdir()` returns the directory from which the `doit` command was invoked, even when task loading changes the current working directory to the dodo file directory or to `--dir`.

`run(task_creators)` runs `DoitMain(ModuleTaskLoader(task_creators))` with `sys.argv[1:]` and must raise `SystemExit` with the command return code. `task_creators` must be a module or dictionary containing task creator functions or task creator objects.

`create_after()` returns a decorator for delayed task creation. The decorated task creator must be evaluated after the task named by `executed` has run. `target_regex` declares target names that delayed tasks are able to create. `creates` declares one or more task basenames when the delayed creator creates names that differ from the creator function name.

`task_params(param_def)` returns a decorator that attaches task-creator command-line parameters. `param_def` must be a list of parameter dictionaries. Passing `None` or a non-list value must raise `ValueError`. A task creator decorated with `task_params()` must not return a task dictionary that also contains `params`; that combination must raise `InvalidTask`.

`Globals.dep_manager` is set to the current dependency manager before tasks are loaded for task-aware commands. Task creators, actions, cleanup actions, and advanced tools must read it to access persistent task values and results during the command lifecycle.

### Embedded Execution API

```python
doit.api.run(task_creators)
doit.api.run_tasks(loader, tasks, extra_config=None)
```

`run_tasks(loader, tasks, extra_config=None)` runs selected tasks through the `run` command without CLI parsing. `loader` must be a `TaskLoader2` instance. `tasks` must be a mapping from task name to task option values; the mapping keys are the selected task names. Task option values must be applied as task configuration, including positional arguments when the task defines `pos_arg`. The return value must be the same numeric return code produced by command execution. User-facing command, dodo, and task validation failures must be re-raised as their original public exception classes.

### Task Definitions

A task creator function must have a name starting with `task_`, or an object in the loaded namespace must expose `create_doit_tasks`. A task creator returns one task dictionary, yields task dictionaries, returns a `Task` object, yields `Task` objects, yields nested generators, or returns `None` for no tasks.

Task dictionaries accept these public fields:

```python
{
    "actions": list | tuple | None,
    "basename": str,
    "name": str,
    "file_dep": list | tuple,
    "task_dep": list | tuple,
    "uptodate": list | tuple,
    "calc_dep": list | tuple,
    "targets": list | tuple,
    "setup": list | tuple,
    "clean": list | tuple | True,
    "teardown": list | tuple,
    "doc": str | None,
    "params": list | tuple,
    "pos_arg": str | None,
    "verbosity": None | 0 | 1 | 2,
    "io": dict | None,
    "getargs": dict,
    "title": callable | None,
    "watch": list | tuple,
    "meta": dict | None,
}
```

`actions` is required when a dictionary represents an executable task. `actions=None` represents a group task with no actions. A dictionary returned directly from `task_x` must not include `name`; its task name must default to `x` unless `basename` is supplied. A dictionary yielded by a generator must include either `name` for a subtask or `basename` for a normal task. A yielded `name=None` dictionary must create an empty group task for the basename.

Subtask names must be `basename:name`. The group task for a set of subtasks must depend on all generated subtasks. Duplicate task names or duplicate group definitions must raise `InvalidTask`.

Task names must not contain `=`. A task creator name must not collide with a command name. A task dictionary with an unknown field, a missing required `actions` field, or a field value of an invalid type must raise `InvalidTask`.

`file_dep`, `targets`, and list-form command action elements accept strings and `pathlib` path objects. Path objects must be converted to strings. Other item types in those fields must raise `InvalidTask`.

`task_dep` entries containing `*` are wildcard task dependencies. Other entries are exact task dependencies. `calc_dep` entries are task names whose results are evaluated after execution to add more dependencies. `setup` entries are setup task dependencies.

`doc` must be the first non-empty line of the task dictionary `doc` field. When no `doc` field is supplied, the first non-empty line of the task creator docstring must be used.

`getargs` maps an action parameter name to `(task_name, value_key)`. It must implicitly depend on the referenced task result. A malformed `getargs` value must raise `InvalidTask`. During execution, the referenced saved value must be passed to actions using that parameter.

### Task Object API

```python
doit.task.Task(
    name, actions, file_dep=(), targets=(), task_dep=(), uptodate=(),
    calc_dep=(), setup=(), clean=(), teardown=(), subtask_of=None,
    has_subtask=False, doc=None, params=(), pos_arg=None, verbosity=None,
    io=None, title=None, getargs=None, watch=(), meta=None, loader=None,
)
doit.task.dict_to_task(task_dict)
doit.task.clean_targets(task, dryrun)
doit.task.result_dep(dep_task_name, setup_dep=False)
doit.task.first_line(doc)
```

`Task.actions` returns action objects lazily created from action declarations. `Task.init_options(args=None)` initializes task option defaults once and returns unparsed positional arguments when arguments are supplied. Task config values must override parameter defaults before CLI task options are parsed. Task option values parsed from the command line or provided by `run_tasks()` must be visible to Python actions and command action formatting.

`Task.execute(stream)` must run actions sequentially. It must stop at the first action returning a `BaseFail` instance and return that failure. On successful actions, the task must update `result` from the action result and merge action `values` into task `values`.

`Task.save_extra_values()` must run every callable in `value_savers` and merge the returned dictionaries into `values`. `Task.clean(outstream, dryrun)` must remove targets when `clean=True`; otherwise it must execute clean actions. In dry run mode, a Python clean action must run only when the callable accepts a `dryrun` parameter, and the parameter value passed must be the dry run boolean.

`clean_targets(task, dryrun)` must remove target files and empty target directories in reverse lexical order. It must leave missing targets alone. It must not remove a non-empty directory.

`result_dep(dep_task_name, setup_dep=False)` returns an up-to-date checker that compares the saved result of another task. It must add an implicit `task_dep` unless `setup_dep=True`, in which case it must add an implicit setup dependency. For group tasks it must compare the result mapping of all subtasks.

### Actions

```python
doit.action.CmdAction(
    action, task=None, save_out=None, shell=True, encoding="utf-8",
    decode_error="replace", buffering=0, **pkwargs
)
doit.action.PythonAction(py_callable, args=None, kwargs=None, task=None)
doit.action.create_action(action, task_ref, param_name)
```

Action declarations in task dictionaries must be converted as follows:

- A `BaseAction` instance must be reused and attached to the task.
- A string must create a shell `CmdAction`.
- A list must create a non-shell `CmdAction`.
- A tuple of `(callable,)`, `(callable, args)`, or `(callable, args, kwargs)` must create a `PythonAction`.
- Any other callable must create a `PythonAction`.
- A tuple longer than three items or an unsupported action type must raise `InvalidTask`.

`CmdAction` must reject `stdout` and `stderr` keyword arguments with `InvalidTask`. It must pass all other keyword arguments to `subprocess.Popen`. String commands use `shell=True` by default. List commands use `shell=False` when created through `create_action()`.

For string command actions attached to a task, formatting must expose `targets`, `dependencies`, `changed`, task option names, and the task positional argument name. The formatting mode is `old`, `new`, or `both`, controlled by `action_string_formatting`. List command actions must not apply string formatting and must convert path elements to strings. Invalid list elements must raise `InvalidTask`.

`CmdAction.execute(out=None, err=None)` must capture stdout and stderr into `out`, `err`, and `result` when task I/O capture is enabled. It must write real-time output to the supplied streams according to task verbosity. A process return code of `0` returns `None`; a nonzero return code up to `125` returns `TaskFailed`; a return code greater than `125` returns `TaskError`. When `save_out` is set, successful execution must save captured stdout in `values[save_out]`.

`PythonAction` must reject non-callables, classes, built-in functions, non-list/non-tuple `args`, and non-dict `kwargs` with `InvalidTask`. It must inject task metadata arguments only when the callable declares them: `task`, `targets`, `dependencies`, and `changed`. These reserved metadata arguments must not have callable defaults; declaring a default for one of them must raise `InvalidTask`. Task option values and positional argument values must be supplied to matching callable parameters and to `**kwargs`.

`PythonAction.execute(out=None, err=None)` must capture stdout and stderr when task I/O capture is enabled, and must restore original streams afterward. Return values have these meanings: `True` or `None` means success; `False` returns `TaskFailed`; `str` means success and becomes `result`; `dict` means success and becomes both `values` and `result`; `TaskFailed` or `TaskError` is returned as-is; an exception returns `TaskError`; any other return type returns `TaskError`.

### Dependency State

```python
doit.dependency.get_md5(input_data)
doit.dependency.get_file_md5(path)
doit.dependency.JSONCodec()
doit.dependency.JsonDB(name, codec, *, module_name=None)
doit.dependency.DbmDB(name, codec, *, module_name=None)
doit.dependency.SqliteDB(name, codec, *, module_name=None)
doit.dependency.FileChangedChecker
doit.dependency.MD5Checker
doit.dependency.TimestampChecker
doit.dependency.Dependency(db_class, backend_name, checker_cls=MD5Checker, codec_cls=JSONCodec, module_name=None)
doit.dependency.DependencyStatus(get_log)
doit.dependency.UptodateCalculator
```

`get_md5()` returns the hexadecimal MD5 digest of a UTF-8 encoded string. `get_file_md5()` returns the hexadecimal MD5 digest of a file's bytes.

Database backends must expose `get(task_id, dependency)`, `set(task_id, dependency, value)`, `in_(task_id)`, `remove(task_id)`, `remove_all()`, and `dump()`. Missing keys must return `None`. Corrupt JSON, corrupt DBM, or corrupt SQLite storage must raise `DatabaseException` with a user-facing recovery message.

`JSONCodec.encode(data)` and `JSONCodec.decode(data)` must use JSON encoding and decoding for per-task stored data.

`MD5Checker` must store `(mtime, size, md5)` state. It must consider a file unchanged when the modification time is unchanged, changed when size differs, and otherwise compare content MD5. `TimestampChecker` must store and compare only modification time.

`Dependency.save_success(task, result_hash=None)` must save task values, task result, checker name, every file dependency state, and the set of file dependencies. A supplied `result_hash` must override result hashing. A string result must be saved as its MD5 digest. A dictionary result must be saved as the dictionary.

`Dependency.get_values(task_name)` returns the saved values dictionary or `{}`. `Dependency.get_value(task_id, key_name)` returns a single saved value; it must raise an exception when the task has no stored values or when the key is missing. `Dependency.get_result(task_name)` returns the saved task result. `Dependency.remove_success(task)` removes saved success data. `Dependency.ignore(task)` marks a task ignored. `Dependency.status_is_ignore(task)` returns the ignored marker when present.

`Dependency.get_status(task, tasks_dict, get_log=False)` returns a `DependencyStatus` whose `status` is `run`, `up-to-date`, or `error`, and it must set `task.dep_changed`. A task is not up to date when any up-to-date item evaluates false, when it has no file dependencies and no true up-to-date evidence, when a target is missing, when the file checker changed, when file dependencies were added or removed, or when a file dependency's checker state changed. A missing file dependency must produce status `error`.

`UptodateCalculator.setup(dep_manager, tasks_dict)` must provide calculator instances with access to the dependency manager getter and the loaded task dictionary before they are called.

### Up-To-Date Helpers and Tools

```python
doit.tools.create_folder(dir_path)
doit.tools.title_with_actions(task)
doit.tools.run_once(task, values)
doit.tools.config_changed(config, encoder=None)
doit.tools.timeout(timeout_limit)
doit.tools.check_timestamp_unchanged(file_name, time="mtime", cmp_op=operator.eq)
doit.tools.LongRunning(action, ...)
doit.tools.Interactive(action, ...)
doit.tools.PythonInteractiveAction(py_callable, ...)
doit.tools.set_trace()
doit.tools.load_ipython_extension(ip=None)
```

`create_folder()` must create the directory and parent directories when absent and must do nothing when the directory already exists.

`title_with_actions(task)` returns a title containing the task name and action descriptions. For a group task with no actions it returns a group title containing task dependencies.

`run_once(task, values)` must register a value saver for `{"run-once": True}` and return whether the prior values already contain that key.

`config_changed(config, encoder=None)` accepts a string or dictionary. A string is the comparison digest as-is. A dictionary must be JSON encoded with sorted keys and optional custom encoder, then stored as an MD5 digest. Invalid config types must raise an exception. The checker must return false when no previous config digest exists and true only when the saved digest equals the current digest.

`timeout(timeout_limit)` accepts an integer number of seconds or a `datetime.timedelta`. Other values must raise an exception. It must save the current success time after execution and return true only while elapsed time since last success is less than the configured limit.

`check_timestamp_unchanged(file_name, time="mtime", cmp_op=operator.eq)` accepts `mtime`/`modify`, `ctime`/`status`, or `atime`/`access`. Any other `time` value must raise `ValueError`. It must save the selected timestamp after success. It must return false on the first run and otherwise return `cmp_op(previous_time, current_time)`. A missing file must raise the `os.stat` exception.

`LongRunning` must run a command without captured output, ignore `KeyboardInterrupt`, and not fail based on process return code. `Interactive` must run a command without captured output and return `TaskFailed` when the process return code is nonzero. `PythonInteractiveAction` must run a Python callable without captured output; a returned string must become `result`, a returned dictionary must become both `values` and `result`, and an exception must return `TaskError`.

`load_ipython_extension()` must register a `%doit` line magic using task creators from the IPython user namespace and must store the dependency database under the IPython profile directory.

### Command, Loader, Parser, Plugin, and Reporter APIs

```python
doit.doit_cmd.DoitMain(task_loader=None, config_filenames=("pyproject.toml", "doit.cfg"), extra_config=None)
doit.doit_cmd.DoitConfig()
doit.cmd_base.Command(config=None, bin_name="doit", opt_vals=None, **kwargs)
doit.cmd_base.DoitCmdBase(task_loader, cmds=None, **kwargs)
doit.cmd_base.TaskLoader2()
doit.cmd_base.ModuleTaskLoader(mod_dict)
doit.cmd_base.DodoTaskLoader()
doit.cmd_base.get_loader(config, task_loader=None, cmds=None)
doit.cmdparse.CmdOption(opt_dict)
doit.cmdparse.CmdParse(options)
doit.cmdparse.DefaultUpdate()
doit.plugin.PluginEntry(category, name, location)
doit.plugin.PluginDict()
```

`DoitMain.run(all_args)` returns process codes: `0` for success, `1` for task failure, `2` for task execution error, and `3` for command, loading, parsing, or validation errors before task execution starts. `--version` must print the version and package path and return `0`. `--help` must print usage and return `0`. Command-line variables are non-option arguments containing `=` and must be removed from the command arguments before command selection.

`DoitConfig` must read TOML configuration from `tool.doit`, command sections from `tool.doit.commands`, task sections from `tool.doit.tasks`, plugin sections from `tool.doit.plugins`, and legacy INI sections. `pyproject.toml` and `doit.cfg` are the default configuration filenames when present. TOML plugin categories must be exposed as uppercase plugin sections. TOML task configuration must be exposed as `task:<name>`.

`Command` subclasses define `name`, documentation strings, `cmd_options`, and `execute(opt_values, pos_args)`. `parse_execute(in_args)` must parse command options, merge loader option values, set the post-mortem debugger flag when present, and return `execute()`'s result. `help()` returns a help text containing purpose, usage, options, and description when a description is supplied.

`DoitCmdBase` subclasses operate on tasks. They must merge base database options, loader options, and command options; set `Globals.dep_manager`; load tasks; select default tasks when no positional task arguments are supplied; support built-in backends `dbm`, `json`, and `sqlite3`; support checkers `md5` and `timestamp`; and reject unknown checkers with `InvalidCommand`.

`TaskLoader2` is the custom loader interface. `setup(opt_values)` runs before configuration loading. `load_doit_config()` returns configuration values. `load_tasks(cmd, pos_args)` returns loaded `Task` objects. `ModuleTaskLoader` loads task creators from a module or dictionary. `DodoTaskLoader` loads the configured dodo file and supports `--file`, `--dir`, and `--seek-file`.

`CmdOption` option dictionaries must contain `name` and `default`. They accept `section`, `type`, `short`, `long`, `inverse`, `choices`, `help`, `metavar`, and `env_var`. Unknown option dictionary fields or missing required fields must raise `CmdParseError`. Boolean string parsing must accept `1/yes/true/on` and `0/no/false/off`. List parsing from strings must split on commas and drop empty parts. Choices must be validated after type conversion.

`CmdParse` must parse short options, long options, boolean flags, inverse boolean flags, environment-backed defaults, positional arguments, and option defaults. Invalid options, invalid values, and invalid choices must raise `CmdParseError`.

`PluginEntry.get()` must import and cache an object from a `<module>:<attribute>` location. Missing modules or attributes must raise exceptions. `PluginDict.add_plugins(config, category)` must add local configured plugins and installed entry-point plugins. `get_plugin(name)` must load `PluginEntry` values before returning them. `to_dict()` must return a plain dictionary of loaded plugin objects.

Reporters are callback objects used by runners. `ConsoleReporter` must print `.  task` for executed visible tasks, `-- task` for up-to-date visible tasks, and `!! task` for ignored tasks. It must suppress execution and up-to-date lines for hidden tasks whose names start with `_`. `ExecutedOnlyReporter` must suppress skipped-task output. `ZeroReporter` must suppress normal task output and write runtime errors. `ErrorOnlyReporter` must print only task failures and errors. `JsonReporter` must capture stdout and stderr during execution and write a JSON object with `tasks`, `out`, and `err` at completion; each task result must include name, result, output, error output, error, start time, and elapsed time.

## Behavioral Sections

### Task Loading

`doit` must discover task creators from all namespace objects whose names start with `task_` and are functions or methods. It must also discover any object exposing `create_doit_tasks`. For a `create_doit_tasks` callable with a `basename` attribute, that basename must be used as the task name.

Task creators must be processed in source definition order when line-number information is available. A normal task creator must be evaluated during task loading. A delayed task creator decorated with `create_after()` must produce a placeholder task during `run`-style loading and must be evaluated only after the configured dependency has executed. Commands that do not execute tasks must load delayed creators immediately unless the command explicitly requests delayed loading.

`get_module(dodo_file, cwd=None, seek_parent=False)` must locate and import the dodo module. Relative dodo paths are resolved from the current working directory. With `seek_parent=True`, missing relative dodo files must be searched in parent directories up to the filesystem root. When the dodo file is found, its directory must be inserted into `sys.path`, and the process current directory must become the dodo directory unless `cwd` is supplied. A missing dodo file must raise `InvalidDodoFile`. A supplied `cwd` that is not a directory must raise `InvalidCommand`.

`load_doit_config()` must return `{}` when `DOIT_CONFIG` is absent and must raise `InvalidDodoFile` when `DOIT_CONFIG` exists but is not a dictionary.

### Task Selection and Execution

The selected task set must be command-line task names, target names, wildcard task patterns, or configured default tasks. If no task is selected and no default task list is configured, all tasks are selected. Selecting a group task must select its subtasks. Selecting a target must select the task that declares that target. Selecting a wildcard pattern containing `*` must match task names by glob-like matching. Selecting an unknown task, target, or unmatched pattern must raise `InvalidCommand`.

Before running a selected task, `doit` must run its task dependencies and setup dependencies unless single-task execution is requested. Task dependencies must enforce order but must not by themselves make a task up to date. A task whose dependency failed, errored, or was ignored must not run and must be reported with the appropriate dependency failure.

Actions within one task must always run sequentially. Parallel execution must apply only across independent tasks whose dependencies are satisfied. A task must save dependency state only after all actions complete successfully. Teardown actions must run during teardown handling and return failures through the same `BaseFail` mechanism.

### Up-To-Date Decisions

A task with no file dependencies and no true up-to-date checker evidence must run every time. A task with unchanged file dependencies and existing targets must be skipped only when enough dependency evidence exists from a previous successful run.

`uptodate` items must accept booleans, `None`, strings, callables, and `(callable, args, kwargs)` tuples. `False` means not up to date. `True` contributes positive up-to-date evidence but must not override changed files or missing targets. `None` must be ignored. A string must run as a shell command; exit code `0` means up to date and any other exit code means not up to date. A callable must receive `task` and `values` positional arguments only when its signature declares them in that order.

`calc_dep` and `getargs` dependencies must update the execution dependency model before dependent values are used. A value requested with `getargs` must come from the saved values of the referenced task.

### CLI Commands

`run` must execute selected tasks and update dependency state. `list` must list tasks alphabetically by default, support definition-order sorting, optionally show subtasks, private tasks, dependencies, and status. `info` must show task metadata and must include the reason when a task is not up to date. `forget` must remove saved successful execution state for selected tasks, default tasks, all tasks, or task groups according to its options. `ignore` must mark selected tasks ignored. `clean` must execute cleanup for selected tasks, default tasks, all tasks, and optionally task dependencies. `dumpdb` must print readable dependency database content. `tabcompletion` must print shell completion scripts. `strace` must inspect command-action file access for one task when the platform utility is available. `reset-dep` must recompute and save file dependency state without executing task actions and must preserve existing saved values and results.

### Configuration

Configuration values must be accepted from `pyproject.toml`, `doit.cfg`, `DOIT_CONFIG`, command-line options, and explicit API configuration. The names used in configuration are the option `name` fields, which are not always the long command-line flag names. The `--file` and `--dir` loader controls must not be taken from `DOIT_CONFIG` because they control how the dodo file itself is loaded.

Per-task configuration must be available to task parameters. Command configuration must be available to matching commands. Global configuration must be available to commands that define the configured option.

### Cleaning and Ignoring

`clean=True` must remove declared targets only. A clean action list must use the same action conversion rules as normal actions. Cleaning a group or selected task set must respect command options for dependencies and all tasks. `clean --forget` and `cleanforget` must remove dependency state for cleaned tasks.

An ignored task must be reported as ignored and must not execute actions. Forgetting the ignored task must remove the ignored marker.

## Error Semantics

Public exception classes:

```python
doit.exceptions.InvalidCommand
doit.exceptions.InvalidDodoFile
doit.exceptions.InvalidTask
doit.exceptions.CatchedException
doit.exceptions.BaseFail
doit.exceptions.TaskFailed
doit.exceptions.TaskError
doit.exceptions.UnmetDependency
doit.exceptions.SetupError
doit.exceptions.DependencyError
doit.dependency.DatabaseException
doit.cmdparse.CmdParseError
```

`InvalidCommand` must represent invalid command-line arguments, unknown commands, unknown task selections, invalid loader directories, invalid checker names, and invalid command usage. When `not_found` is supplied, its string form must distinguish between an invalid command/task/target before command selection and an invalid task/target for a selected command.

`InvalidDodoFile` must represent missing dodo files, invalid `DOIT_CONFIG`, task names that collide with command names, invalid `action_string_formatting`, and unsatisfied minimum version requirements.

`InvalidTask` must represent invalid task dictionaries, invalid task names, invalid action declarations, invalid task parameter combinations, invalid field types, invalid dependency element types, duplicate generated tasks, malformed `getargs`, unsupported Python actions, and reserved metadata parameters with defaults.

`TaskFailed` must represent an action that ran and reported failure. `TaskError` must represent an error while creating or executing an action, an exception raised by a Python action, an invalid Python action return type, command return codes greater than `125`, dependency-checking errors, and setup errors. `UnmetDependency`, `SetupError`, and `DependencyError` must be task-error subclasses for dependency, setup, and dependency-manager failures.

`BaseFail.get_msg()` returns the failure message plus traceback text when available. `BaseFail.get_name()` returns the concrete failure class name. `report=False` failures must not be reported by reporters that honor the report flag.

`CmdParseError` must represent invalid option definitions, invalid option names, missing option values, type conversion failures, invalid boolean strings, and invalid choices.

`DatabaseException` must represent backend corruption or backend load failures that require a user-facing database recovery message.

`DoitMain.run()` must catch `CmdParseError`, `InvalidDodoFile`, `InvalidCommand`, and `InvalidTask`, write an `ERROR:` line to stderr, and return code `3`. Other unexpected exceptions before task execution must write a traceback to stderr and return code `3`.

## Cross-View Invariants

1. A task name created by the loader must be the name accepted by CLI selection, returned by list-like commands, used as the dependency database task key, and passed to reporter callbacks.
2. A task target declared in `targets` must select that task from the CLI, participate in missing-target up-to-date checks, and be removed by `clean=True`.
3. A file path declared in `file_dep` must be normalized to a string on the task object, used for action keyword injection as `dependencies`, checked by the configured file checker, and saved under the task key after success.
4. A Python action dictionary return must update the action `values`, the task `values`, the dependency database `_values_:` entry after success, and later `getargs` lookups.
5. A Python action string return and a command action captured output must update the action result, task result, saved dependency result, and `result_dep()` comparisons.
6. A task option value from CLI parsing, task configuration, or `run_tasks()` must be visible to Python action parameters, command action string formatting, and the task object's `options`.
7. A task marked ignored in the dependency manager must be skipped by the runner, reported as ignored by reporters, and listed as ignored in status-oriented command output.
8. A successful `forget` operation must remove the saved success state used by `get_status()`, `result_dep()`, and `getargs` for that task.
9. A hidden task whose name starts with `_` must remain executable and dependency-addressable while normal console reporter output and default list output suppress it unless private output is requested.
10. A delayed task placeholder must preserve the creator, declared dependency, declared target regex, declared created task names, and task creator parameters until the delayed creator is evaluated.

## Representative Workflows

### Basic Incremental Build

```python
def task_compile():
    return {
        "actions": ["cc -c main.c -o main.o"],
        "file_dep": ["main.c"],
        "targets": ["main.o"],
        "clean": True,
    }

def task_link():
    return {
        "actions": ["cc main.o -o app"],
        "file_dep": ["main.o"],
        "targets": ["app"],
        "clean": True,
    }
```

Running `doit` must execute `compile` before `link` because `main.o` is a target of `compile` and a file dependency of `link`. A second run with unchanged dependencies and existing targets must skip both tasks as up to date. Removing `app` must make `link` run. Running `doit clean` must remove generated targets for the selected default tasks.

### Parameterized Task Creator and Embedded Run

```python
from doit import task_params
from doit.api import run_tasks
from doit.cmd_base import ModuleTaskLoader

@task_params([{"name": "count", "default": 2, "type": int, "long": "count"}])
def task_echo(count):
    for index in range(count):
        yield {
            "name": str(index),
            "actions": [(print, (f"item {index}",))],
            "verbosity": 2,
        }

run_tasks(
    ModuleTaskLoader(globals()),
    {"echo": {"count": 3}},
    extra_config={"GLOBAL": {"dep_file": ".doit.db"}},
)
```

The embedded run must load tasks from the supplied namespace, pass `count=3` to the task creator, generate three subtasks under the `echo` group, execute the selected group, and return the normal command return code.

### Stored Results and `getargs`

```python
def task_compute():
    def action():
        return {"answer": "42"}
    return {"actions": [action]}

def task_use():
    def action(answer):
        print(answer)
    return {
        "actions": [action],
        "getargs": {"answer": ("compute", "answer")},
    }
```

`doit use` must execute `compute` as an implicit dependency, save its returned dictionary values, pass the saved `"answer"` value to `use`, and use the same saved value for later dependency decisions.

## Non-Goals

This specification does not require compatibility with private helper functions, undocumented support utilities, exact traceback formatting, exact terminal column widths, exact generated shell completion script text, exact DBM implementation-specific file extensions, or platform-specific behavior of external tools beyond the public command behavior described here.

This specification does not require implementing the optional `auto` watch command supplied by a separate package. It does not require network access. It does not require preserving internal module organization as long as the public import paths and behavior are provided.

## Evaluation Notes

Evaluation checks the behavior visible through public imports, task dictionaries, documented command-line flows, dependency persistence, reporter callbacks, plugin and loader extension APIs, and error classes. Tests exercise both direct Python API usage and command-style workflows in isolated temporary projects.

Scoring is based on observable compatibility: task loading, task naming, action conversion and execution, up-to-date status, dependency database behavior, configuration parsing, CLI command return codes, cleanup, ignore and forget state, reporter output categories, parser errors, and documented extension points. Fixture names, private helper layouts, and implementation internals are not part of the scoring contract.
