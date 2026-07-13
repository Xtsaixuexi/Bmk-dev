# Final Stage Product Check

Checked at: 2026-07-09T08:53:35Z

Workflow authority:

- `github_alignment/raw_main/README.md`
- `github_alignment/raw_main/skills/candidate-selector/SKILL.md`
- `github_alignment/raw_main/skills/spec-writer/SKILL.md`
- `github_alignment/raw_main/skills/test-filter/SKILL.md`
- `github_alignment/raw_main/skills/task-judge/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- `github_alignment/final_workflow_checksum_check.md`

## Stage Matrix

| stage | workflow key output | local product | checks | verdict |
|---|---|---|---|---|
| 1. Select candidate | `filter_notes.md`, `CANDIDATES.md` entry | `candidate_selection.md`, `source_audit.json`, `source_pointer.md`, `filter_notes.md`, `CANDIDATES.md` SELECTED row | Hard gates pass: 4150 package LOC, 253 regular tests, clean module-level private import audit, source commit recorded. DeepSeek v4 Pro and GLM 5.2 reviews present. | PASS |
| 2. Write spec | validated `spec_vN.md` | `spec/spec_v1.md`, `spec/spec_v1_candidate.md`, root `spec.md`, `spec/spec_validation.md`, `github_alignment/stage2_spec_writer_alignment.md` | Candidate-visible spec has required structure, no hidden artifacts, no private implementation contract; reference-observed corrections for `Averager.add`, `Lock.release`, and arbitrary `reset` names are applied. DeepSeek v4 Pro: CONTINUE; GLM 5.2: PASS/CONTINUE. | PASS |
| 3. Filter tests | `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl` | root and `filter/` copies of `spec_test_map.md`, `kept_nodeids.txt`, `taxonomy.jsonl`, `tests/test_generated_diskcache.py`, `filter/rewrite_audit.md`, `github_alignment/stage3_test_filter_alignment.md` | Generated-only public oracle has 63 scoreable tests; global floor met; dummy 0/63; reference 63/63; coverage FULL; fairness correction removed overreach before final scoring. DeepSeek v4 Pro and GLM 5.2 both continue/pass. | PASS |
| 4. Evaluate | agent trajectory and score | `/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-diskcache-fullrepro-001-20260709T-stage4-cleanroom/` | Candidate was generated cleanroom from public spec only. Preflight import path points to candidate `output/diskcache/__init__.py`. Score: 61/63, with failures limited to two integration tests. | PASS |
| 5. Judge | task status, diagnosis report, weakness table entry | `judge/diagnosis_report.md`, `judge/gate_report.md`, `review/step5_deepseekv4pro_review.md`, `review/step5_glm52_review.md`, `weakness_table.md` rows | Diagnosis includes Preflight output, anti-cheat scan, solvability, fairness, Gate C generated-only spot-check, Gate D coverage audit FULL, and real failure clusters. DeepSeek v4 Pro verdict: QUALIFIED; GLM 5.2 verdict: CONFIRMED QUALIFIED. | PASS |
| Package | migrate qualified task to `tasks/` | `/root/autodl-tmp/Bmk-Lizhiqian/tasks/diskcache-fullrepro-001` | Manifest artifact references exist; final package reference scorer re-run from task root passed 63/63; GitHub workflow checksum check passed via `gh-proxy.com`. `CANDIDATES.md` QUALIFIED row and weakness rows recorded. | PASS |

## Final Packaged Reference Check

```text
source_repo: /root/autodl-tmp/Bmk-Lizhiqian/tasks/diskcache-fullrepro-001
solution_dir: /root/autodl-tmp/new-e2e/grantjenks__python-diskcache
summary: 63 passed / 63 total
by_layer: atomic 22/22, integration 33/33, system_e2e 8/8
import_provenance: /root/autodl-tmp/new-e2e/grantjenks__python-diskcache/diskcache/__init__.py
artifact: final_reference_score_check.json
```

Verdict: PASS. All stage products required by the accelerated GitHub workflow are present and internally consistent.
