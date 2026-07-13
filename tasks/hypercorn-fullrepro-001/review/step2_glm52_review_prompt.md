# Independent Hypercorn Stage 2 v1 Review

Review only the appended Hypercorn document. Do not browse, use tools, inspect repositories, infer unseen checks, or use another reviewer's conclusion. Treat the text as documentation supplied directly to Hypercorn users.

Audit it against the active Bmk-dev principles:

- **Like a developer:** the body must read as formal documentation written by Hypercorn's authors. Benchmark, assignment, audit, answer-key, evaluator, and implementation-plan voice is prohibited.
- **Spec-driven:** every promised public import, signature, default, precedence rule, state transition, warning, failure, and cross-view agreement must be clear enough to implement without private context.
- **Behavioral:** requirements must describe observable inputs, outputs, mutations, side effects, and failures. Internal helpers, private state, algorithms, framework mandates, fixture shapes, and arbitrary exact diagnostics are blockers.
- **Q1 public contract:** every substantive requirement must be a promise to a public caller or operator.
- **Q2 non-derivable balance:** retain Hypercorn-specific details that an experienced engineer could not infer; reject generic advice and excessive implementation clues.
- The product state model must unify configuration, application, and service projections. At least six user-observable cross-view invariants, complete workflows, non-goals, conditional behavior, failure paths, and unambiguous precedence are required.
- Process leakage is prohibited, including benchmark, task, candidate, hidden test, oracle, node ID, taxonomy, score, judge, fixture, source-path, test-path, and review-process language.

Return only:

- `VERDICT`: `PASS_GITHUB_PRINCIPLES` or `PATCH_REQUIRED`
- `LIKE_A_DEVELOPER`: `PASS` or `FAIL`
- `SPEC_DRIVEN`: `PASS` or `FAIL`
- `BEHAVIORAL`: `PASS` or `FAIL`
- `Q1_PUBLIC_CONTRACT`: `PASS` or `FAIL`
- `Q2_NON_DERIVABLE_BALANCE`: `PASS` or `FAIL`
- `STATE_MODEL_AND_INVARIANTS`: `PASS` or `FAIL`
- `ERROR_AND_PRECEDENCE_SEMANTICS`: `PASS` or `FAIL`
- `PROCESS_LEAKAGE`: `NONE` or `PRESENT`
- `BLOCKERS`: exact section and minimum author-facing correction; empty on pass

The document begins after the separator.
