# Bandit Task Diagnosis

## Preflight output

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/codex-gpt-5.5-bandit-fullrepro-001-20260712T102235Z-lane1-cleanroom/output/bandit/__init__.py
```

## Anti-Cheat

PASS. The candidate trajectory contains no reference/WIP/oracle/taxonomy/score/API reads, no target-package install, no network operation, and no write outside the cleanroom output.

## Solvability

PASS. The pinned reference passes 90/90 under the official grouped scorer. The NotImplemented dummy passes 0/90. The scorer used `--remove-path bandit`, and reference provenance points to the pinned source checkout.

## Candidate Score

- Overall: 87/90 (96.67%)
- Atomic: 63/65
- Integration: 14/14
- System E2E: 10/11
- Collection errors: 0

## Protocol Correction

The initial score was 85/90. DeepSeek v4 Pro and GLM 5.2 independently classified exact MD5 B324 versus family-valid B303 as a spec gap and exact stdin `<stdin>` versus `-` as verifier overconstraint. The oracle was relaxed only for those two assertions. Reference remained 90/90 and dummy remained 0/90 before the frozen candidate was rescored.

## Real Failure Clusters

1. `atomic-behavior`: public `Issue.get_code()` does not read a readable `fname`, returning an empty snippet. Two nodeids share this root.
2. `workflow-completeness`: `--aggregate vuln` does not switch JSON result ordering from filename to vulnerability/test name. One system nodeid fails.

## Cascade Analysis

There are two independent roots for three failures. No failure is caused by a missing import, collection problem, environment error, or primitive cascade into unrelated integration tests.

## Gate D - Coverage Gap Audit

| spec section | uncovered behaviors | impact | recommendation |
|---|---|---|---|
| Plugin Context raw construction | Internal raw-context constructor shape is intentionally not scored; scanner detection families exercise context-mediated behavior. | Secondary; no public workflow gap. | Keep excluded to avoid implementation-shape coupling. |
| Scope / Non-Goals / Evaluation Notes | Framing sections are non-behavioral. | None. | No standalone tests. |

Coverage verdict: **FULL**. Core Error Semantics, Cross-View Invariants, Product State Model, scanning/suppression, reports, configuration, baseline, and representative workflows all have covered rows and meet global/per-domain quotas.

## Final Verdict

`QUALIFIED`. Anti-cheat, solvability, fairness, nontriviality, taxonomy, provenance, and coverage gates pass. Both independent judges confirmed QUALIFIED after applying the task-level verdict definition. Remaining failures are retained as genuine model capability evidence.
