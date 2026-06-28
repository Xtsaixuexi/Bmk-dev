# Bmk-dev Unit/System Gap Tasks

This repository contains benchmark task packets for evaluating whether code agents can pass isolated unit behavior while still failing harder end-to-end system behavior.

## Main Deliverables

The two current task packets are:

- `task/minishell-realrepo-001/prd.md`
- `task/minishell-realrepo-001/rubric.json`
- `task/minibuildgraph-realrepo-001/prd.md`
- `task/minibuildgraph-realrepo-001/rubric.json`

The consolidated score table is:

- `score_summary.csv`

## Included Context

Each task directory keeps the public product requirements in `prd.md` and the executable grading cases in `rubric.json`.

Supporting files live under `doc/`:

- `source_repo.md`
- `requirement_map.md`
- `score_reports/`

Agent coverage and route status are tracked in:

- `code_agent_execution_matrix.csv`
- `code_agent执行矩阵.md`
- `核心路线执行核对表.md`

## Validation

Run the repository consistency check:

```bash
python tools/validate_scores.py --root .
```

Current validation status: 0 errors, 0 warnings.
