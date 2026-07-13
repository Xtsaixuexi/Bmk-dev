# Judge Diagnosis: doit-fullrepro-001

verdict: QUALIFIED
spec_version: v1
filter_version: upstream_filter_v1
candidate_run: opencode-gpt-5.5-doit-fullrepro-001-20260709T-stage4-cleanroom

## Preflight output

Command:

```bash
PYTHONPATH=/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-doit-fullrepro-001-20260709T-stage4-cleanroom/output python -c "import doit; print(doit.__file__)"
```

Output:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-doit-fullrepro-001-20260709T-stage4-cleanroom/output/doit/__init__.py
```

The path points into the candidate output directory, not the reference source tree or an installed package.

## Anti-Cheat Scan

No cheating evidence was found in the candidate implementation. A scan of the candidate output directories under `/tmp/.../output` and `candidate-runs/.../output` found no references to the source repository, oracle tests, kept nodeids, taxonomy, spec-test map, reference score, prior score result, API key file, or installed `doit` package. The run prompt explicitly prohibited those inputs, and the run workspace started with `prompt.md` plus an empty `output/` directory.

## Solvability

Reference oracle passes the scoring set under scorer isolation:

- reference: 438/438
- pass_rate_excluding_skips: 1.0
- dummy gate: 0/438 passed
- scorer isolation: `score_pytest_original.py --remove-path doit` with pytest rootdir pinned to the oracle worktree

## Candidate Score

- score: 75/438
- pass_rate_excluding_skips: 0.17123287671232876

```json
{
  "atomic": {
    "collection_error": 46,
    "error": 34,
    "failed": 86,
    "passed": 64,
    "total": 230
  },
  "integration": {
    "collection_error": 97,
    "error": 51,
    "failed": 48,
    "passed": 11,
    "total": 207
  },
  "system_e2e": {
    "failed": 1,
    "total": 1
  }
}
```

## Gate A - Spec Mapping Spot-Check

Sampled covered rows map to public spec sections and the expected outcomes are derivable from the spec:

| test | mapped section | verdict |
|---|---|---|
| `tests/test___init__.py::TestGetInitialWorkdir::test_get_initial_workdir` | Top-Level API | PASS |
| `tests/test___main__.py::TestMain::test_execute` | Installable Surface | PASS |
| `tests/test_action.py::TestCmdActionParams::test_invalid_param_stdout` | Error Semantics | PASS |
| `tests/test_action.py::TestPythonVerbosity::test_captureStdout` | Actions | PASS |
| `tests/test_cmd_base.py::TestDoitCmdBase::test_minversion` | Command, Loader, Parser, Plugin, and Reporter APIs | PASS |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_skip` | Dependency State | PASS |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateMethod_True` | Dependency State | PASS |
| `tests/test_doit_cmd.py::TestErrors::test_interrupt` | Error Semantics | PASS |
| `tests/test_task.py::TestTaskDeps::test_calc_dep` | Task Object API | PASS |
| `tests/test_tools.py::TestPythonInteractiveAction::test_success` | Up-To-Date Helpers and Tools | PASS |

## Gate B - Failure Pattern Audit

The largest failure clusters are candidate implementation gaps against documented public behavior:

- Missing public import surface causes collection errors: `doit.version`, `doit.cmd_run`, `doit.task.DelayedLoader`, and `doit.task.Stream`.
- Action execution semantics are incomplete: command output capture, callable command expansion, task option/positional argument interpolation, reserved metadata kwargs, and expected invalid-action errors.
- Command parser behavior is incomplete: option defaults, value conversion, boolean/list parsing, and short/long option lookup.
- Dependency persistence/state behavior is incomplete: sqlite availability checks, JSON DB corruption handling, status/result persistence, ignored/forgotten task state, and up-to-date decisions.
- CLI/system workflow is incomplete: `python -m doit list` exits with duplicate task error instead of a successful list command.

These failures are traceable to public spec sections and check observable outcomes, not private attributes, exact internal structures, repr strings, or hidden oracle-only behavior. They are model failures, not verifier failures.

## Gate C - Generated-Only Oracle Spot-Check

Not applicable. The oracle is upstream-only, not generated-only.

## Gate D - Coverage Gap Audit

Coverage verdict: PARTIAL acceptable.

The retained upstream oracle covers the primary public behavior sections:

```json
{
  "Actions": 65,
  "Command, Loader, Parser, Plugin, and Reporter APIs": 50,
  "Cross-View Invariants": 14,
  "Dependency State": 144,
  "Embedded Execution API": 3,
  "Error Semantics": 55,
  "Installable Surface": 1,
  "Task Loading": 37,
  "Task Object API": 48,
  "Top-Level API": 1,
  "Up-To-Date Helpers and Tools": 20
}
```

Core invariant and error sections are non-empty. The main caveat is that strict behavioral filtering leaves only one system_e2e upstream test after excluding exact CLI transcript, private runner/control scheduling, optional auto-watch, and snapshot-style command output assertions. This caveat is already recorded in `MANIFEST.json` and `filter/filter_validation.md`; it does not make the scoring set invalid because the oracle has 438 scoreable tests, reference passes 438/438, dummy passes 0/438, and the retained set covers the task/action/dependency/command state surfaces broadly.

## Real Failure Clusters

1. `api-surface`: candidate omitted documented public imports and modules including `doit.version`, `doit.cmd_run`, `DelayedLoader`, and `Stream`. This causes 143 collection_error results and hides downstream command/task coverage.
2. `atomic-behavior`: candidate approximated action and command parser APIs. Failures include command result capture (`"12"` vs `"1"`), callable command expansion, stdout/stderr capture state, task option interpolation, invalid action error semantics, default propagation, and string-to-type conversion.
3. `state-management`: candidate dependency storage and task-state lifecycle are incomplete. Failures cluster in DB corruption handling, get/set/remove behavior, saved values/results, status calculation, ignored/forgotten markers, and sqlite/json backend behavior.
4. `workflow-completeness`: candidate CLI workflow is incomplete. `python -m doit list` exits nonzero with duplicate task errors, so the single retained system_e2e test fails.

## Cascade Analysis

The score is cascade-heavy. A small set of missing public modules/exports accounts for all 143 collection_error results in `test_cmd_base.py`, `test_doit_cmd.py`, `test_loader.py`, and `test_task.py`. The remaining executed failures are concentrated in three broad roots: action execution semantics, command-line parser behavior, and dependency persistence/state lifecycle. The integration score is low primarily because these primitives are absent or partial, not because the verifier checks hidden internals.

## Labels

- qualified
- upstream-only-oracle
- partial-system-e2e-coverage
- cascade-dominated
- api-surface-signal
- dependency-state-signal
- action-parser-behavior-signal

## Verdict

QUALIFIED. Hard gates pass: clean import provenance, no cheat evidence in candidate output, reference 438/438, dummy 0/438, scorer isolation with `--remove-path doit`, nonzero taxonomy layers, and Stage 3 DeepSeek/GLM reviews passed. Candidate failures are valid model capability signals.
