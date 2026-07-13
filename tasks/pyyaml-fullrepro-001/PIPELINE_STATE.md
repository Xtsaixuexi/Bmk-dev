# Pipeline State: pyyaml-fullrepro-001

state: QUALIFIED
created_at: 2026-07-09
updated_at: 2026-07-09
spec_iter: 0
filter_iter: 0
eval_iter: 0
functions_in_scope: 2616
functions_kept: 889
functions_excluded: 1727
oracle_count: 889

## Current Todo

Stage 3 local gate, isolated reference/dummy gates, DeepSeek v4 Pro review, and GLM 5.2 review passed. Cleanroom evaluation setup is ready.

## History

| date | from | to | note |
|---|---|---|---|
| 2026-07-09 | INIT | S1_SELECTED_PENDING_REVIEW | Selected `yaml/pyyaml` from new-e2e after de-duplication, mechanical audit, existing-task exclusion, and clean pytest collect pre-screen. |
| 2026-07-09 | S1_SELECTED_PENDING_REVIEW | S2_READY | Stage 1 reviews passed; downstream cautions recorded for public loader/dumper/resolver scope. |
| 2026-07-09 | S2_READY | S2_SPEC_IN_PROGRESS | Stage 2 spec writing started. |
| 2026-07-09 | S2_SPEC_IN_PROGRESS | S2_SPEC_DONE_PENDING_REVIEW | Wrote spec v1 candidate packet, validation notes, and GitHub spec-writer alignment. |
| 2026-07-09 | S2_SPEC_DONE_PENDING_REVIEW | S3_FILTER_IN_PROGRESS | Stage 2 DeepSeek v4 Pro and GLM 5.2 reviews passed; entering test filtering. |
| 2026-07-09 | S3_FILTER_IN_PROGRESS | S3_FILTER_DONE_PENDING_REVIEW | Processed all 2616 collected nodeids; kept 889; excluded/source-only 1727; reference gate 889/889 passed; dummy gate 0/889 passed under scorer isolation. |
| 2026-07-09 | S3_FILTER_DONE_PENDING_REVIEW | S4_SETUP | Stage 3 local gate, isolated reference/dummy gates, DeepSeek v4 Pro review, and GLM 5.2 review passed. |
| 2026-07-09 | S4_SETUP | S5_JUDGE | Cleanroom OpenCode gpt-5.5 candidate scored 3/889; ready for task-judge. |
| 2026-07-09 | S5_JUDGE | QUALIFIED | Stage 5 judge hard gates passed; DeepSeek v4 Pro and GLM 5.2 reviews returned PASS_QUALIFY. |
