# Step 7 Judge Diagnosis: cerberus-fullrepro-001

verdict: QUALIFIED_PENDING_MODEL_REVIEW
filter_version: v4
reference: 81/81
best_candidate: codex-subagent + gpt-5.5
best_score: 72/81

## Preflight Output

Subagent corrected v4:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/cerberus/codex-subagent-gpt-5.5-cerberus-fullrepro-001-20260702T000000Z/score_overlay_v4/overlay_worktree/cerberus/__init__.py
```

Codex-bypass corrected v4:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/cerberus/codex-gpt-5.5-cerberus-fullrepro-001-bypass-20260701T194148Z/score_overlay_v4/overlay_worktree/cerberus/__init__.py
```

Both preflight paths point into candidate overlay worktrees, not the source repo or an installed reference package.

## Anti-Cheat Scan

No cheating evidence was found in available candidate prompts, metadata, and Codex CLI logs. The only matches for hidden-artifact terms were the prompt's prohibition text and post-score metadata paths. No candidate implementation-phase log showed reading `/root/autodl-tmp/e2e/cerberus`, test files, kept nodeids, taxonomy, reference scores, prior outputs, or API keys. No `pip install cerberus` evidence was found.

The original Codex workspace-sandbox run is `blocked_env` and produced no candidate score.

## Solvability

Reference oracle v4 passes the final kept set:

- total: 81
- passed: 81
- pass_rate_excluding_skips: 1.0
- collection_error: 0
- unknown layers: 0

This satisfies the solvability gate.

## Fairness Corrections

Initial candidate scoring exposed verifier/fairness issues. These were corrected before accepting scores:

- v2 removed 11 top-level import carrier nodeids requiring helper APIs absent from spec v1: `validator_factory`, `UnvalidatedSchema`, and `compare_paths_lt`.
- v3 removed 21 nodeids relying on error constants/ErrorList internals, exact `BasicErrorHandler.messages`, deprecation warnings, internal/context attrs, docstring-derived `validation_rules`, or `contains`, all absent from spec v1.
- v4 removed 2 final outliers: an exact default message wording assertion and an integer-as-float expectation absent from spec v1.

Final filter v4 has 81 scoreable nodeids, all mapped to spec v1 sections and observable behavior.

## Candidate Scores

| runner | model | score | pass_rate | atomic | integration | system_e2e |
|---|---|---:|---:|---|---|---|
| codex-subagent | gpt-5.5 | 72/81 | 0.888889 | 25/25 | 39/46 | 8/10 |
| codex-bypass | gpt-5.5 | 65/81 | 0.802469 | 22/25 | 35/46 | 8/10 |

Unavailable runner/model combinations are recorded in `code_agent_execution_matrix_cerberus.csv`.

## Failure Diagnosis

The best candidate's 9 failures are real behavioral gaps:

- Normalization composition: custom coerce and rename ordering produced the wrong key; nullable coercion still called coercers for `None`; rename handler behavior did not match the spec; nested purge_unknown did not remove nested unknown fields.
- Defaults and tuple normalization: nullable defaults/default setters and tuple-preserving normalization were incomplete.
- System workflows: complex normalization attempted to deepcopy a non-deepcopyable value; rules-set schema behavior failed to raise `SchemaError` where required.

These failures align with documented normalization, nested schema, rules-set registry, default/default_setter, coerce, rename_handler, and purge_unknown behavior.

## Labels

- `normalization-composition-signal`
- `registry-schema-validation-signal`
- `fair-filter-corrected`
- `discriminating`

## Verdict

QUALIFIED pending DeepSeek v4 Pro and GLM 5.2 review. The final v4 scoring set is solvable by reference, candidate import provenance is clean, collection errors are removed, and remaining failures are spec-driven behavioral gaps.
