# Bmk-dev Unit/System Gap Tasks

This repository contains benchmark task packets for evaluating whether code agents can pass isolated unit behavior while still failing harder end-to-end system behavior.

## Primary Deliverables

The two primary task packets in this branch are:

- `task/minishell-realrepo-001/prd.md`
- `task/minishell-realrepo-001/rubric.json`
- `task/minibuildgraph-realrepo-001/prd.md`
- `task/minibuildgraph-realrepo-001/rubric.json`

The current exploratory task packet is:

- `task/minidotenv-realrepo-001/prd.md`
- `task/minidotenv-realrepo-001/rubric.json`

The consolidated score table is:

- `score_summary.csv`

## Scope And Status

This repository also keeps three previously validated context tasks:

- `task/sqlite-utils-realrepo-001`
- `task/zk-realrepo-001`
- `task/miniurlutils-realrepo-001`

`SQLite`, `ZK`, `MiniURLUtils`, and `MiniDotenv` already have executable code-agent runs meeting the current core-strong gap policy.

`MiniShell` and `MiniBuildGraph` are active deliverables that still need a stronger executable code-agent gap. Plain GPT / DeepSeek / Doubao bare-model runs are intentionally excluded from the public score evidence.

## Included Context

Each task directory keeps the public product requirements in `prd.md` and the executable grading cases in `rubric.json`.

Supporting files live under `doc/`:

- `source_repo.md`
- `requirement_map.md`
- `score_reports/`

Agent coverage and route status are tracked in:

- `code_agent_execution_matrix.csv`

## Validation

Run the repository consistency check:

```bash
python tools/validate_scores.py --root .
```

Current validation status: 6 manifest tasks, 27 score rows, 0 errors, 0 warnings.
