# Hypercorn Stage 2 v1 Author-Documentation Audit

Review only the appended Hypercorn document. Do not browse, use tools, inspect a repository, infer hidden checks, or rely on any prior review. The document must stand on its own as formal documentation written by Hypercorn's authors for users.

Apply these Bmk-dev rules:

1. **Like a developer:** reject benchmark, assignment, evaluator, answer-key, audit, or implementation-plan voice. The document must explain the public product contract naturally.
2. **Spec-driven:** public imports, signatures, defaults, precedence, state transitions, failures, and cross-view agreements must be explicit enough to support a clean implementation.
3. **Behavioral:** retain observable inputs, outputs, side effects, mutation, warnings, precedence, and failures; reject algorithms, private fields, internal helpers, framework mandates, fixture shapes, and arbitrary exact diagnostics.
4. **Q1:** each substantive requirement must be a promise to public callers. Identify anything that is only an internal implementation detail.
5. **Q2:** each library-specific detail that a senior engineer could not derive must be stated, while generic design advice and answer-key-like detail must be removed.
6. Require a coherent product state model, at least six cross-view invariants, complete workflows, explicit non-goals, conditional behavior with stated conditions, and failure behavior for important invalid preconditions.
7. Check all precedence claims for internal clarity. Do not request source or test evidence; judge only whether the public prose is coherent and implementable.
8. Process leakage is a blocker: benchmark, task, candidate, hidden test, oracle, node ID, taxonomy, score, judge, fixture, test path, source path, and review-process language must not appear.

Return only:

- `VERDICT`: `PASS_AUTHOR_SPEC` or `PATCH_REQUIRED`
- `LIKE_A_DEVELOPER`: `PASS` or `FAIL`
- `SPEC_DRIVEN`: `PASS` or `FAIL`
- `BEHAVIORAL`: `PASS` or `FAIL`
- `Q1_PUBLIC_CONTRACT`: `PASS` or `FAIL`
- `Q2_NON_DERIVABLE_BALANCE`: `PASS` or `FAIL`
- `STATE_MODEL_AND_INVARIANTS`: `PASS` or `FAIL`
- `ERROR_AND_PRECEDENCE_SEMANTICS`: `PASS` or `FAIL`
- `PROCESS_LEAKAGE`: `NONE` or `PRESENT`
- `BLOCKERS`: exact section and the minimum necessary author-facing correction; empty on pass

The appended document begins after the separator.
