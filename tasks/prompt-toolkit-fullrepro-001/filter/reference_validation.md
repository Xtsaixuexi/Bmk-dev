# Reference Validation: prompt-toolkit-fullrepro-001

## Summary

Reference validation passed for the merged oracle.

| oracle part | runner | result |
|---|---|---:|
| upstream retained nodeids | `score_pytest_original.py` with `--remove-path src/prompt_toolkit` | 68 passed / 68 total |
| upstream retained nodeids | direct pytest with reference `PYTHONPATH` | 68 passed / 68 total |
| generated public oracle | direct pytest with reference `PYTHONPATH` | 32 passed / 32 total |
| merged oracle | scorer + pytest aggregate | 100 passed / 100 total |

## Isolation

Reference imports were isolated with:

- `PYTHONPATH=/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit/src`
- `PYTHONDONTWRITEBYTECODE=1`
- pytest working directory set to the wip task directory
- scorer upstream run used `--remove-path src/prompt_toolkit` and `--package prompt_toolkit`

The scorer provenance check resolved `prompt_toolkit` to:

`/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit/src/prompt_toolkit/__init__.py`

## Commands Run

Upstream retained scorer gate:

```bash
PYTHONDONTWRITEBYTECODE=1 python /root/autodl-tmp/Bmk-Lizhiqian/harness/score_pytest_original.py \
  --source-repo /root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit \
  --solution-dir /root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit/src \
  --nodeids /root/autodl-tmp/Bmk-Lizhiqian/wip/prompt-toolkit-fullrepro-001/filter/kept_upstream.txt \
  --taxonomy /root/autodl-tmp/Bmk-Lizhiqian/wip/prompt-toolkit-fullrepro-001/filter/taxonomy.jsonl \
  --run-dir /root/autodl-tmp/Bmk-Lizhiqian/wip/prompt-toolkit-fullrepro-001/filter/reference_upstream_run \
  --remove-path src/prompt_toolkit \
  --package prompt_toolkit \
  --json-out /root/autodl-tmp/Bmk-Lizhiqian/wip/prompt-toolkit-fullrepro-001/filter/reference_upstream_score.json
```

Result:

```text
68 passed / 68 total; pass_rate_excluding_skips = 1.0
```

Generated public oracle reference gate:

```bash
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit/src \
python -m pytest -q -o addopts= \
  /root/autodl-tmp/Bmk-Lizhiqian/wip/prompt-toolkit-fullrepro-001/filter/test_generated_public_oracle.py
```

Result:

```text
32 passed in 0.19s
```

Direct upstream pytest cross-check:

```bash
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit/src \
python -m pytest -q -o addopts= $(sed 's#^#/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit/#' \
  /root/autodl-tmp/Bmk-Lizhiqian/wip/prompt-toolkit-fullrepro-001/filter/kept_upstream.txt)
```

Result:

```text
68 passed in 0.16s
```

## Scorer Coverage Note

The available `score_pytest_original.py` runner is designed for original upstream nodeids. It was run for the upstream retained set. The 32 generated tests live under the wip `filter/` directory, so they were validated with pytest reference and dummy gates instead of the original-nodeid scorer.

If a single merged scorer report is required later, the next step is to add a runner mode that accepts both upstream nodeids and wip-local generated pytest files, then execute it against `filter/kept_nodeids.txt`.

## Aggregate Reference Score

`filter/reference_score.json` records 100 passed / 100 total: 68 upstream tests passed through isolated `score_pytest_original.py`, and 32 generated public tests passed through direct pytest with the reference implementation on `PYTHONPATH`.
