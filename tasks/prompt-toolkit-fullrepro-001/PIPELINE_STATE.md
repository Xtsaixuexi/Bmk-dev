# Pipeline State: prompt-toolkit-fullrepro-001

state: QUALIFIED
created_at: 2026-07-09
updated_at: 2026-07-09
spec_iter: 0
filter_iter: 0
eval_iter: 0
functions_in_scope: 156
functions_kept: 68
functions_excluded: 88
oracle_count: 100

## Current Todo

Stage 3 local gate, isolated reference/dummy gates, DeepSeek v4 Pro review, and GLM 5.2 review passed. Cleanroom evaluation setup is ready.

## History

| date | from | to | note |
|---|---|---|---|
| 2026-07-09 | INIT | S1_SELECTED | Selected `prompt-toolkit/python-prompt-toolkit` from new-e2e after de-duplication, mechanical audit, existing-task exclusion, and pytest collect pre-screen. |
| 2026-07-09 | S1_SELECTED | S2_SPEC_IN_PROGRESS | Stage 1 GitHub alignment, DeepSeek v4 Pro review, and GLM 5.2 review passed. |
| 2026-07-09 | S2_SPEC_IN_PROGRESS | S2_SPEC_DONE_PENDING_REVIEW | Wrote `spec/spec_v1.md`, stripped candidate specs, validation notes, and Stage 2 GitHub alignment. |
| 2026-07-09 | S2_SPEC_DONE_PENDING_REVIEW | S2_SPEC_CORRECTED_PENDING_REVIEW | Applied GLM 5.2 Stage 2 corrections for style lookup, `Attrs`, formatted text utilities, `PromptSession` defaults, and validation wording. |
| 2026-07-09 | S2_SPEC_CORRECTED_PENDING_REVIEW | S3_FILTER_IN_PROGRESS | Corrected Stage 2 DeepSeek v4 Pro and GLM 5.2 reviews passed; entering test filtering. |
| 2026-07-09 | S3_FILTER_IN_PROGRESS | S3_FILTER_DONE_PENDING_REVIEW | Filtered 156 upstream tests to 68 public behavioral tests, added 32 generated public tests, validated 100-test oracle on reference and dummy gates. |
| 2026-07-09 | S3_FILTER_DONE_PENDING_REVIEW | S4_SETUP | Stage 3 local gate, isolated reference/dummy gates, DeepSeek v4 Pro review, and GLM 5.2 review passed. |
| 2026-07-09 | S4_SETUP | S5_JUDGE | Cleanroom OpenCode gpt-5.5 candidate scored 59/100; ready for task-judge. |
| 2026-07-09 | S5_JUDGE | QUALIFIED | Stage 5 judge hard gates passed; DeepSeek v4 Pro and GLM 5.2 reviews returned PASS_QUALIFY. |
