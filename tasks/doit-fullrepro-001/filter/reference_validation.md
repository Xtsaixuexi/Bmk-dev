# Reference Validation

Reference command:

```bash
cd /root/autodl-tmp/new-e2e/pydoit__doit
python -m pytest -q -o addopts= --json-report --json-report-file=/root/autodl-tmp/Bmk-Lizhiqian/wip/doit-fullrepro-001/filter/reference_report.json $(cat /root/autodl-tmp/Bmk-Lizhiqian/wip/doit-fullrepro-001/filter/kept_nodeids.txt)
```

Reference result: 438 passed, 0 failed, 0 skipped, 0 error / 438 retained nodeids.

Pass rate excluding skips: 1.0.

Notes: initial reference run exposed 98 optional/platform skipped nodeids; those were removed before the final retained set.

Isolated scorer command:

```bash
python github-cache/Bmk-dev-main-ghproxy/harness/score_pytest_original.py   --source-repo /root/autodl-tmp/new-e2e/pydoit__doit   --solution-dir /root/autodl-tmp/new-e2e/pydoit__doit   --nodeids filter/kept_nodeids.txt   --taxonomy filter/taxonomy.jsonl   --run-dir filter/reference_score_run   --remove-path doit   --json-out filter/reference_score.json   --pytest-arg=-o --pytest-arg=addopts=   --pytest-arg=--rootdir=filter/reference_score_run/oracle_worktree
```

Isolated scorer result: 438 passed, 0 failed, 0 skipped, 0 unknown / 438 retained nodeids. Pass rate excluding skips: 1.0.

Isolation note: the oracle worktree is copied from the source repository with the `doit` package directory removed; imports resolve through the `solution_dir` on `PYTHONPATH`. The explicit rootdir keeps pytest json-report nodeids aligned with `kept_nodeids.txt` for this repository's tests-root configuration.
