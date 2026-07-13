# Pipeline State: doit-fullrepro-001

state: QUALIFIED
created_at: 2026-07-09
updated_at: 2026-07-09
spec_iter: 0
filter_iter: 0
eval_iter: 0
functions_in_scope: 909
functions_kept: 438
functions_excluded: 471
oracle_count: 438

## Current Todo

Stage 3 DeepSeek v4 Pro and GLM 5.2 reviews passed. Cleanroom evaluation setup is ready.

## History

| date | from | to | note |
|---|---|---|---|
| 2026-07-09 | INIT | S1_SELECTED | Selected `pydoit/doit` from new-e2e after de-duplication, mechanical audit, existing-task exclusion, and pytest collect pre-screen. |
| 2026-07-09 | S1_SELECTED | S2_SPEC_IN_PROGRESS | Stage 1 GitHub alignment, DeepSeek v4 Pro review, and GLM 5.2 review passed. |
| 2026-07-09 | S2_SPEC_IN_PROGRESS | S2_SPEC_DONE_PENDING_REVIEW | Wrote spec_v1, candidate-visible spec packet, validation notes, and Stage 2 GitHub alignment. |
| 2026-07-09 | S2_SPEC_DONE_PENDING_REVIEW | S3_FILTER_IN_PROGRESS | Stage 2 DeepSeek v4 Pro and GLM 5.2 reviews passed; entering test filtering. |
| 2026-07-09 | S3_FILTER_IN_PROGRESS | S3_FILTER_DONE_PENDING_REVIEW | Filtered 909 collected nodeids to 438 retained upstream public-behavior oracles; reference gate passed and dummy gate passed. |
| 2026-07-09 | S3_FILTER_DONE_PENDING_REVIEW | S4_SETUP | Stage 3 local gate, isolated reference score, DeepSeek v4 Pro review, and GLM 5.2 review passed. |
| 2026-07-09 | S4_SETUP | S5_JUDGE | Cleanroom OpenCode gpt-5.5 candidate scored 75/438 under `--remove-path doit`; judge artifacts prepared. |
| 2026-07-09 | S5_JUDGE | QUALIFIED | Stage 5 judge hard gates passed; DeepSeek v4 Pro and GLM 5.2 reviews returned PASS_QUALIFY. |
