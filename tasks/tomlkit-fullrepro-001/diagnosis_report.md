# Diagnosis Report: tomlkit-fullrepro-001

## Verdict

QUALIFIED with runner caveat. The oracle is solvable by the reference implementation, scoring tests are spec-driven and behavioral after filter review, import provenance for both candidates points to candidate output directories, and candidate scores show meaningful failure patterns. Both OpenCode generation sessions were interrupted after writing artifacts; scores are valid artifact snapshots but may underestimate models under a fully completed run.

## Preflight output

GPT-5.5 candidate:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-tomlkit-fullrepro-001-20260701T234614Z/output/tomlkit/__init__.py
```

GLM-5.2 candidate:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-glm-5.2-tomlkit-fullrepro-001-20260701T234614Z/output/tomlkit/__init__.py
```

Both paths are under `/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/.../output/tomlkit/__init__.py`, not `/root/autodl-tmp/e2e/tomlkit` and not an installed PyPI package.

## Anti-Cheat Scan

No candidate-visible prompt included source repository paths, tests, kept nodeids, taxonomy, reference scores, review files, or prior outputs. The OpenCode prompts were created from `spec.md` plus generic implementation instructions. Scoring import provenance confirms candidate package import. The run logs should still be treated as generated trajectories, but no evidence was found in the scoring artifacts that candidates imported the reference implementation.

## Reference Solvability

Reference validation passed all scoreable tests.

```json
{
  "passed": 64,
  "total": 64,
  "pass_rate_excluding_skips": 1.0,
  "by_layer": {
    "system_e2e": {
      "passed": 20,
      "total": 20
    },
    "integration": {
      "passed": 19,
      "total": 19
    },
    "atomic": {
      "passed": 25,
      "total": 25
    }
  }
}
```

The oracle combines 12 clean upstream tests and 52 generated public tests. Step 4 and Step 5 DeepSeek/GLM reviews passed.

## Candidate Scores

| runner | model | status | score | pass_rate |
|---|---|---|---:|---:|
| opencode | gpt-5.5 | interrupted_after_artifacts_then_scored | 40/64 | 0.625000 |
| opencode | glm-5.2 | interrupted_after_artifacts_then_scored | 34/64 | 0.531250 |

GPT-5.5 by layer:

```json
{
  "atomic": {
    "passed": 12,
    "total": 25,
    "failed": 13
  },
  "integration": {
    "failed": 7,
    "total": 19,
    "passed": 12
  },
  "system_e2e": {
    "failed": 4,
    "total": 20,
    "passed": 16
  }
}
```

GLM-5.2 by layer:

```json
{
  "atomic": {
    "passed": 16,
    "total": 25,
    "failed": 9
  },
  "integration": {
    "failed": 10,
    "total": 19,
    "passed": 9
  },
  "system_e2e": {
    "failed": 11,
    "total": 20,
    "passed": 9
  }
}
```

## Fairness Audit

The kept upstream tests come only from modules without private module-level imports. Tests from modules importing `tomlkit.parser`, `tomlkit._utils`, `tomlkit._compat`, or internal container/proxy classes were excluded to avoid requiring private implementation surfaces. Generated tests import only public names and avoid private attributes, `repr()` checks, and exact exception message checks. Exact string assertions are used only for documented style-preserving serialization, line-ending preservation, or public rendering behavior.

The scoreable tests map to concrete spec sections in `filter/spec_test_map.md`; `spec_gap` count is zero after filtering. No majority failure cluster indicates a verifier dependence on private internals.

## Real Failure Clusters

### GPT-5.5

Primary root causes:

- `error-semantics`: parse failures often raise generic `ParseError` instead of public subclasses such as `InvalidNumberError`, `InvalidDateError`, `InvalidTimeError`, `InvalidDateTimeError`, `InvalidUnicodeValueError`, `EmptyTableNameError`, or `UnexpectedEofError`.
- `cross-view-consistency`: serialization of parsed or edited documents loses exact public style-preserving details such as comments, spacing, escaped keys, nested arrays, and AoT rendering.
- `state-management`: edits and TOMLFile workflows fail when item objects lack expected public rendering metadata such as comment/trivia behavior.
- `workflow-completeness`: nested list/table/AoT workflows and file read-modify-write flows are incomplete.

### GLM-5.2

Primary root causes:

- `api-surface`: parsed objects do not consistently satisfy the documented `TOMLDocument` identity and expected module exports.
- `cross-view-consistency`: comments, inline comment spacing, line endings, and table headers drift between parsed data and rendered text.
- `state-management`: table/AoT internals are not coherent enough for nested document editing and file workflows.
- `atomic-behavior`: temporal helper functions and some conversion/error paths are incorrectly wired.

## Cascade Analysis

The failures are not dominated by a single missing import or collection failure. Both candidates collect and execute all 64 scoreable tests. GPT-5.5 has stronger system workflow performance (16/20 system_e2e) but weaker atomic exception precision. GLM-5.2 has better atomic pass count than GPT-5.5 but substantially weaker integration/system behavior. This gives the task discrimination value across capability dimensions.

## Labels

- `qualified`
- `discriminating`
- `style-preservation-signal`
- `cross-view-consistency-signal`
- `runner-interrupted-caveat`

## Required Follow-Up

If this task is used for final leaderboard-quality scoring, rerun OpenCode with a bounded completion protocol or longer timeout to avoid interrupted artifact snapshots. The current task itself is valid; the runner caveat affects interpretation of these candidate scores, not oracle validity.
