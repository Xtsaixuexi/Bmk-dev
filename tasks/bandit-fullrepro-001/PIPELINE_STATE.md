# Pipeline State: bandit-fullrepro-001

state: QUALIFIED
created_at: 2026-07-10
updated_at: 2026-07-12
spec_iter: 1
filter_iter: 1
eval_iter: 0
functions_in_scope: 7
functions_kept: 6
functions_excluded: 1
oracle_count: 90

## Current Todo

Terminal: task is qualified. Preserve candidate run, judge reports, dual-model reviews, and synthesized task packet.

## History

| date | from | to | note |
|---|---|---|---|
| 2026-07-10 | INIT | S1_SELECTED_PENDING_REVIEW | Installed Bandit editable with test and optional formatter dependencies; isolated pytest collection found 275 nodeids with zero errors. |
| 2026-07-10 | S1_SELECTED_PENDING_REVIEW | S2_READY | DeepSeek v4 Pro and GLM 5.2 independently returned PASS_CONTINUE with hard gates, offline determinism, and risk routing all accepted. |
| 2026-07-12 | S2_READY | S2_SPEC_CHECK | Drafted the scanner, plugin API, report, configuration, suppression, baseline, and invariant contract; resolved review findings against public probes and the scoped reference revision. |
| 2026-07-12 | S2_SPEC_CHECK | S2_SPEC_DONE | DeepSeek v4 Pro and GLM 5.2 independently returned PASS_CONTINUE for candidate specification v12 with all review dimensions passing. |
| 2026-07-12 | S2_SPEC_DONE | S3A_IMPORT_AUDIT | Froze candidate-visible spec v1 and advanced to oracle import/surface audit. |
| 2026-07-12 | S3A_IMPORT_AUDIT | S3A_REWRITE | Audited 24 upstream files and 264 test functions; internal manager/config/formatter saturation triggered Track B, with the public Issue file retained for per-function extraction. |
| 2026-07-12 | S3A_REWRITE | S3B_TRIGGER | Materialized six public Issue rewrites, excluded one exact-string test, passed all six on reference, and received dual-model PASS_CONTINUE for accounting, fairness, trigger, and candidate safety. |
| 2026-07-12 | S3B_TRIGGER | S3B_COVERAGE | Confirmed rewrite audit hard gate and produced branch coverage plus formatted gap artifacts. |
| 2026-07-12 | S3B_COVERAGE | S3B_GENERATE | Generated a public CLI/API oracle spanning detection families, projections, configuration, suppression, baseline, formats, metrics, and errors. |
| 2026-07-12 | S3B_GENERATE | S3B_DUMMY | Collected 84 generated nodeids and merged six public upstream rewrites. |
| 2026-07-12 | S3B_DUMMY | S3B_REFERENCE | All 90 merged tests failed the NotImplemented dummy; no trivial tests survived. |
| 2026-07-12 | S3B_REFERENCE | S3B_DONE | Reference implementation passed all 90 tests. |
| 2026-07-12 | S3B_DONE | S3_ORACLE_MERGE | Wrote final kept nodeids, complete spec-test map, taxonomy, filter notes, and coverage quota. |
| 2026-07-12 | S3_ORACLE_MERGE | S3_REFERENCE_RUN | Oracle count 90 exceeded the floor of 50; official scorer run used remove-path isolation and provenance preflight. |
| 2026-07-12 | S3_REFERENCE_RUN | S3_DONE | Official grouped scorer passed 90/90 with 65 atomic, 14 integration, 11 system_e2e, and zero unknown taxonomy. |
| 2026-07-12 | S3_DONE | S4_SETUP | DeepSeek v4 Pro and GLM 5.2 independently passed public behavior, traceability, nontriviality, accounting, determinism, and candidate-safety gates. |
| 2026-07-12 | S4_SETUP | S4_EVAL_RUN | Ran a cleanroom Codex candidate from the candidate-visible spec only; trajectory anti-cheat and candidate import provenance passed. |
| 2026-07-12 | S4_EVAL_RUN | S4_ANALYSIS | Initial official score was 85/90 with five failed nodeids. |
| 2026-07-12 | S4_ANALYSIS | S3_ORACLE_MERGE | Independent adjudication identified one exact test-ID spec gap and one stdin-sentinel overconstraint; corrected those assertions and incremented filter_iter. |
| 2026-07-12 | S3_ORACLE_MERGE | S3_REFERENCE_RUN | Corrected oracle retained 90 nodeids; reference passed 90/90 and dummy passed 0/90. |
| 2026-07-12 | S3_REFERENCE_RUN | S4_EVAL_RUN | Rescored the frozen candidate under the corrected official oracle and provenance isolation. |
| 2026-07-12 | S4_EVAL_RUN | S5_JUDGE | Final candidate score 87/90; three failures reduce to two spec-driven model roots. |
| 2026-07-12 | S5_JUDGE | QUALIFIED | Anti-cheat, solvability, fairness, Gate D, and dual-model verdict rechecks passed; task qualified with real atomic and workflow capability signals. |
