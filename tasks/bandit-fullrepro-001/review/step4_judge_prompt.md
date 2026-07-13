# Independent Final Judge: Bandit Candidate Run

Judge only the evidence below. Do not browse, use tools, inspect repositories, infer hidden tests, or introduce behavior not quoted here.

## Hard-Gate Evidence

- Candidate trajectory anti-cheat scan: no reference/WIP/oracle/taxonomy/score/API reads, no target-package install, no network, all writes under cleanroom output.
- Candidate import preflight:
  `/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/codex-gpt-5.5-bandit-fullrepro-001-20260712T102235Z-lane1-cleanroom/output/bandit/__init__.py`
- Reference official scorer: 90 passed, 0 failed, pass rate 1.0.
- Dummy gate: 0 passed, 90 failed.
- Corrected candidate official scorer: 87 passed, 3 failed, pass rate 0.9666666667.
- Candidate by layer: atomic 63/65, integration 14/14, system_e2e 10/11.
- Taxonomy totals: atomic 65, integration 14, system_e2e 11, unknown 0.
- Official scorer used `--remove-path bandit` and provenance preflight.
- Stage 3 independent review: DeepSeek v4 Pro and GLM 5.2 both passed public behavior, spec traceability, nontriviality, accounting, offline determinism, and candidate safety.
- Coverage: 90 scoreable nodeids; all core Error Semantics, Cross-View Invariants, Product State Model, report, suppression, baseline, configuration, and workflow areas have mapped coverage. Plugin Context constructor internals and non-behavioral Scope/Non-Goals/Evaluation framing are intentionally not asserted.

## Fairness Correction Already Applied

Initial candidate score was 85/90. Independent failure adjudication agreed that exact MD5 `B324` versus family-valid `B303` was a spec gap and exact stdin filename `"<stdin>"` versus `"-"` was verifier overconstraint. Those assertions were relaxed without changing candidate output. Reference remained 90/90 and dummy remained 0/90. The final score above is from the corrected oracle.

## Remaining Failures

1. Two atomic nodeids share one root: `Issue.get_code(max_lines=1)` returned `""` for an issue whose public `fname` pointed to a readable source file. The quoted spec says `get_code` "Returns a code snippet around the line where the issue occurred."
2. One system_e2e nodeid: `-a vuln` retained filename ordering (`exec_used`, then `assert_used`) instead of vulnerability/test-name ordering. The quoted spec says `-a {file,vuln}` selects filename or vulnerability/test-name ordering or grouping.

No remaining failure asserts exact diagnostic prose, private state, internal imports, hidden fixture shape, environment path prefix, or unstated test-ID mapping.

## Required Decision

Return only:

- `VERDICT`: QUALIFIED, BROKEN, or CHEAT_DETECTED
- `ANTI_CHEAT`: PASS or FAIL
- `SOLVABILITY`: PASS or FAIL
- `FAIRNESS`: PASS or FAIL
- `COVERAGE_GATE_D`: FULL, PARTIAL_ACCEPTABLE, or GAP
- `REAL_FAILURE_ROOTS`: integer and concise categories
- `CASCADE_ANALYSIS`: concise
- `TASK_LABELS`: comma-separated
- `BLOCKERS`: mandatory action before qualification; empty for QUALIFIED
