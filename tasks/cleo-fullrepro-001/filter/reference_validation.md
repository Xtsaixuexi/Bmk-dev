# Reference Validation

Reference command:

```bash
cd /root/autodl-tmp/new-e2e/python-poetry__cleo
PYTHONPATH=src python -m pytest -q -o addopts= --json-report --json-report-file=/root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/reference_report.json $(cat /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/kept_nodeids.txt)
```

Reference result: 87 passed, 0 failed, 0 skipped, 0 error / 87 retained nodeids.

Pass rate excluding skips: 1.0.

Isolated scorer command:

```bash
python /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/github_alignment/raw_main/harness/score_pytest_original.py --source-repo /root/autodl-tmp/new-e2e/python-poetry__cleo --solution-dir /root/autodl-tmp/new-e2e/python-poetry__cleo/src --nodeids /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/kept_nodeids.txt --taxonomy /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/taxonomy.jsonl --run-dir /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/reference_score_run --remove-path src/cleo --json-out /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/reference_score.json --pytest-arg=-o --pytest-arg=addopts= --pytest-arg=--rootdir=/root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/reference_score_run/oracle_worktree
```

Isolated scorer result: 87 passed, 0 failed, 0 skipped, 0 unknown / 87 retained nodeids. Pass rate excluding skips: 1.0.

Dummy scorer command:

```bash
python /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/github_alignment/raw_main/harness/score_pytest_original.py --source-repo /root/autodl-tmp/new-e2e/python-poetry__cleo --solution-dir /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/runtime/dummy_solution --nodeids /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/kept_nodeids.txt --taxonomy /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/taxonomy.jsonl --run-dir /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/dummy_score_run --remove-path src/cleo --json-out /root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/dummy_score.json --pytest-arg=-o --pytest-arg=addopts= --pytest-arg=--rootdir=/root/autodl-tmp/Bmk-Lizhiqian/wip/cleo-fullrepro-001/filter/dummy_score_run/oracle_worktree
```

Dummy result: 0 passed / 87 retained nodeids. Summary: {'collection_error': 19, 'error': 12, 'failed': 56, 'total': 87}.

Isolation note: the oracle worktree is copied from the source repository with `src/cleo` removed; imports resolve through `--solution-dir /root/autodl-tmp/new-e2e/python-poetry__cleo/src` on `PYTHONPATH`. The explicit pytest rootdir keeps json-report nodeids aligned with `kept_nodeids.txt`.
