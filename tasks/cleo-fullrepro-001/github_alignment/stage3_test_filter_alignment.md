# Stage 3 Test Filter Alignment: cleo-fullrepro-001

## Inputs

- Stage 3 skill: `github_alignment/raw_main/skills/test-filter/SKILL.md`
- Synthesizer skill: `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- Source repository: `/root/autodl-tmp/new-e2e/python-poetry__cleo`
- Candidate-visible spec: `spec.md`

## Process

1. Verified `PIPELINE_STATE.md` was `S3_FILTER_IN_PROGRESS` before filtering.
2. Processed all 258 collected upstream nodeids into `filter/spec_test_map.md`.
3. Kept only public, spec-mapped behavior tests and separated source-only assertions from mechanical/protocol exclusions.
4. Excluded exact completion/help/table/progress/traceback snapshots, exact exception-message wording, private imports/assertions, terminal/environment tests, and collected helper artifacts.
5. Ran direct reference pytest on the retained set.
6. Ran isolated scorer reference validation with `--remove-path src/cleo` and `--solution-dir /root/autodl-tmp/new-e2e/python-poetry__cleo/src`.
7. Ran a dummy gate with a local unimplemented `cleo` package and removed the one dummy-passing fixture-inheritance nodeid.
8. Copied required filter artifacts to the task root and updated the manifest.

## Results

- final oracle source: upstream_only
- final retained nodeids: 87
- reference result: 87 passed / 87 direct pytest and 87 passed / 87 isolated scorer
- dummy result: 0 passed / 87
- taxonomy layers: {'integration': 22, 'atomic': 54, 'system_e2e': 11}
- spec gaps: 0

## Notes

No external review models were called. No generated tests were added. Track B was not triggered because the retained oracle exceeds the global floor and covers the primary public API, input, execution, output, error, event, tester, and question-helper surfaces. The single-command workflow example remains a review caveat because the current reference lacks the spec-mentioned `Command.default()` method.

## Scorer Isolation

Scorer isolation used current Bmk-dev `harness/score_pytest_original.py` with `--remove-path src/cleo`; pytest rootdir was pinned to the isolated oracle worktree so reported nodeids match `kept_nodeids.txt`. Import provenance from the isolated worktree resolved to `/root/autodl-tmp/new-e2e/python-poetry__cleo/src/cleo/__init__.py`. The resulting `filter/reference_score.json` passed 87 / 87 with non-zero layer counts and no unknown layer bucket.
