# Step 7 Final Corrected Candidate Evaluation Report: cerberus-fullrepro-001

date: 2026-07-02
state: S7_JUDGE_DONE_PENDING_MODEL_REVIEW

## Final Filter

Filter v4 is the current valid filter.

- collected: 247
- kept / scoreable: 81
- source-only: 155
- excluded: 11
- spec_gap: 0
- layers: atomic 25, integration 46, system_e2e 10

Corrections removed tests that depended on API/helper details absent from candidate-visible spec v1: top-level import carriers, error constants/ErrorList internals, exact default message wording, deprecation warnings, internal/context attrs, docstring-derived metadata, `contains`, and integer-as-float behavior.

## Reference

- reference score: 81/81
- pass_rate_excluding_skips: 1.0
- collection_error: 0
- unknown layers: 0

## Candidate Scores

All scores use `harness/score_pytest_overlay.py`.

| runner | model | run_id | score | pass_rate_excluding_skips | collection_error |
|---|---|---|---:|---:|---:|
| codex-bypass | gpt-5.5 | `codex-gpt-5.5-cerberus-fullrepro-001-bypass-20260701T194148Z` | 65/81 | 0.802469 | 0 |
| codex-subagent | gpt-5.5 | `codex-subagent-gpt-5.5-cerberus-fullrepro-001-20260702T000000Z` | 72/81 | 0.888889 | 0 |

## Best Candidate

- runner/model: `codex-subagent + gpt-5.5`
- run id: `codex-subagent-gpt-5.5-cerberus-fullrepro-001-20260702T000000Z`
- score: 72/81
- pass_rate_excluding_skips: 0.888889

## Remaining Best-Candidate Failures

The best candidate has 9 failures:

- 7 integration failures in normalization: custom coerce + rename, nullable coercion, rename handler, nested purge unknown, defaults with nullable fields, tuple normalization;
- 2 system_e2e failures: complex normalization with non-deepcopyable values and rules-set schema behavior.

These are observable behavior gaps covered by spec v1.

## Supplemental Agent Runs

After qualification, additional runs were executed according to `模型与Agent调用方式.md`:

| runner | model | score/status | pass_rate | notes |
|---|---|---:|---:|---|
| opencode | gpt-5.5 | 65/81 | 0.802469 | scored with overlay v4 |
| opencode | glm-5.2 | 7/81 | 0.086420 | scored with overlay v4 |
| mini-swe-agent | gpt-5.5 | 69/81 | 0.851852 | scored with overlay v4 |
| mini-swe-agent | glm-5.2 | tool_failed | n/a | RepeatedFormatError; no output files |
| swe-agent | gpt-5.5 | tool_failed | n/a | bashlex heredoc failures; no patch/output |

The best candidate remains `codex-subagent + gpt-5.5` at 72/81.
