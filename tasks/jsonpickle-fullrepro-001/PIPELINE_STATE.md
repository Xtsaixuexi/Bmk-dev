# Pipeline State: jsonpickle-fullrepro-001

state: QUALIFIED
created_at: 2026-07-09
updated_at: 2026-07-10
spec_iter: 0
filter_iter: 0
eval_iter: 0
functions_in_scope: 784
functions_kept: 12
functions_excluded: 772
oracle_count: 76

## Current Todo

Terminal `QUALIFIED`. Stage 5 Gates A-D and independent DeepSeek v4 Pro / GLM 5.2 reviews passed; task package exists under `tasks/jsonpickle-fullrepro-001`. Lane 1 audit added the missing root `spec_sources.md` and `dummy_score.json` copies.

## History

| date | from | to | note |
|---|---|---|---|
| 2026-07-09 | INIT | S1_SELECTED_PENDING_REVIEW | Selected `jsonpickle/jsonpickle` from new-e2e after de-duplication, mechanical audit, existing-task exclusion, and clean pytest collect pre-screen. |
| 2026-07-09 | S1_SELECTED_PENDING_REVIEW | S2_READY | Stage 1 reviews passed; optional backend and exact JSON formatting risks routed to Stage 3 filtering. |
| 2026-07-09 | S2_READY | S2_SPEC_IN_PROGRESS | Stage 2 spec writing started. |
| 2026-07-09 | S2_SPEC_IN_PROGRESS | S2_SPEC_DONE_PENDING_REVIEW | Wrote v1 candidate-visible spec, validation notes, and Stage 2 alignment; ready for review before Stage 3 filtering. |
| 2026-07-09 | S2_SPEC_DONE_PENDING_REVIEW | S2_SPEC_DONE_PENDING_REVIEW | Applied DeepSeek-requested Stage 2 correction for reserved wire tags and `v1_decode` behavior. |
| 2026-07-09 | S2_SPEC_DONE_PENDING_REVIEW | S3_FILTER_IN_PROGRESS | Stage 2 v2 DeepSeek v4 Pro and GLM 5.2 reviews passed; entering test filtering. |
| 2026-07-09 | S3_FILTER_IN_PROGRESS | S3_FILTER_DONE_PENDING_REVIEW | Stage 3 produced 12 retained upstream nodeids plus 64 generated nodeids; local dummy/reference/taxonomy/coverage gates passed. |
| 2026-07-09 | S3_FILTER_DONE_PENDING_REVIEW | S4_SETUP | Stage 3 local mechanical checks plus DeepSeek v4 Pro and GLM 5.2 reviews passed; ready for cleanroom candidate evaluation. |
| 2026-07-09 | S4_SETUP | S5_JUDGE | Cleanroom OpenCode gpt-5.5 candidate scored 58/76; ready for task-judge. |
| 2026-07-09 | S5_JUDGE | QUALIFIED | Stage 5 judge hard gates passed; DeepSeek v4 Pro and GLM 5.2 reviews returned PASS_QUALIFY. |
| 2026-07-10 | QUALIFIED | QUALIFIED | Lane 1 terminal audit confirmed Gate D FULL, package provenance, reference 76/76, dummy 0/76, candidate 58/76, and completed missing fixed-flow root artifact copies. |
