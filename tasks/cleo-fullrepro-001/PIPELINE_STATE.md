# Pipeline State: cleo-fullrepro-001

state: QUALIFIED
created_at: 2026-07-09
updated_at: 2026-07-09
spec_iter: 0
filter_iter: 0
eval_iter: 0
functions_in_scope: 258
functions_kept: 87
functions_excluded: 171
oracle_count: 87

## Current Todo

Stage 3 local gates passed: processed 258 nodeids, retained 87 upstream public-behavior tests, reference and dummy gates passed, pending Stage 3 review.

## History

| date | from | to | note |
|---|---|---|---|
| 2026-07-09 | INIT | S1_SELECTED_PENDING_REVIEW | Selected `python-poetry/cleo` from new-e2e after de-duplication, mechanical audit, existing-task exclusion, and clean pytest collect pre-screen. |
| 2026-07-09 | S1_SELECTED_PENDING_REVIEW | S2_READY | Stage 1 reviews passed; exact CLI output risk routed to Stage 3 filtering. |
| 2026-07-09 | S2_READY | S2_SPEC_DONE_PENDING_REVIEW | Wrote spec_v1, candidate-visible spec packet, validation notes, and Stage 2 GitHub alignment. |
| 2026-07-09 | S2_SPEC_DONE_PENDING_REVIEW | S3_FILTER_IN_PROGRESS | Stage 2 DeepSeek v4 Pro and GLM 5.2 reviews passed; entering test filtering. |
| 2026-07-09 | S3_FILTER_IN_PROGRESS | S3_FILTER_DONE_PENDING_REVIEW | Processed all 258 collected nodeids; retained 87 upstream public-behavior tests; reference scorer passed 87/87 with --remove-path src/cleo and dummy gate passed 0/87. |
| 2026-07-09 | S3_FILTER_DONE_PENDING_REVIEW | S4_SETUP | Stage 3 local mechanical checks plus DeepSeek v4 Pro and GLM 5.2 reviews passed; ready for cleanroom candidate evaluation. |
| 2026-07-09 | S4_SETUP | S5_JUDGE | Cleanroom OpenCode gpt-5.5 candidate scored 15/87; ready for task-judge. |
| 2026-07-09 | S5_JUDGE | QUALIFIED | Stage 5 judge hard gates passed; DeepSeek v4 Pro and GLM 5.2 reviews returned PASS_QUALIFY. |
