# Stage 3 Test Filter Alignment: doit-fullrepro-001

## Inputs

- Stage 3 skill: `github_alignment/raw_main/skills/test-filter/SKILL.md`
- Synthesizer skill: `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- Source repository: `/root/autodl-tmp/new-e2e/pydoit__doit`
- Candidate-visible spec: `spec.md`

## Process

1. Collected upstream tests from the clean upstream checkout.
2. Processed all 909 collected nodeids, including helper/sample collection artifacts, into `filter/spec_test_map.md`.
3. Kept only public, spec-mapped behavior tests.
4. Excluded exact help text, traceback/message text, shell completion exact script text, DBM file-extension assumptions, private helper/private method access, optional auto-watch behavior, strace details, internal runner/control tests, optional skipped backend variants, and dummy-gate pass-through tests.
5. Ran the final retained upstream oracle against the reference implementation.
6. Ran a sandboxed dummy gate using copied tests and a dummy `doit` package placed first on `PYTHONPATH`.
7. Copied required filter artifacts to the task root.

## Results

- final oracle source: upstream_only
- final retained nodeids: 438
- reference result: 438 passed / 438 direct pytest and 438 passed / 438 isolated scorer
- dummy result: 0 passed / 438
- taxonomy layers: {'atomic': 230, 'integration': 207, 'system_e2e': 1}
- spec gaps: 0

## Notes

No generated tests were added. No spec patch was requested. The kept set exceeds the global oracle floor and maps to existing `spec.md` headings.

## Scorer Isolation

Scorer isolation used current Bmk-dev `harness/score_pytest_original.py` with `--remove-path doit`; pytest rootdir was pinned to the isolated oracle worktree so reported nodeids match `kept_nodeids.txt`. The resulting `filter/reference_score.json` passed 438 / 438 with non-zero layer counts and no unknown layer bucket.
