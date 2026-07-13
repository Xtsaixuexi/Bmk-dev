# Stage 3 GitHub Alignment: diskcache-fullrepro-001

Generated: 2026-07-08T21:53:55Z

Authority files:

- `github_alignment/raw_main/skills/test-filter/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`

## Alignment Checks

- PASS: `rewrite_audit.md` exists before oracle merge.
- PASS: scorer isolation planned with `score_pytest_original.py --remove-path diskcache`.
- PASS: generated tests use only public imports and observable behavior.
- PASS: no private attributes, SQL schema, file layout, exact exception messages, rsync, benchmark scripts, or Django-only imports appear in scoring oracle.
- PASS: `kept_nodeids.txt`, `taxonomy.jsonl`, and `spec_test_map.md` generated with one row per scoreable oracle test.
- PASS: oracle_count is 63, satisfying the global floor of 50.
- PASS: dummy gate scored 0/63 and isolated reference gate scored 63/63.
- PASS: DeepSeek v4 Pro and GLM 5.2 Stage 3 reviews both returned CONTINUE/PASS with no blockers.
