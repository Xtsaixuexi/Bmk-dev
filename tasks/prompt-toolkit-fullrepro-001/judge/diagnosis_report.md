# Judge Diagnosis: prompt-toolkit-fullrepro-001

verdict: QUALIFIED
spec_version: v1
filter_version: upstream_plus_generated_v1
candidate_run: opencode-gpt-5.5-prompt-toolkit-fullrepro-001-20260709T-stage4-cleanroom

## Preflight output

Command:

```bash
PYTHONPATH=/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-prompt-toolkit-fullrepro-001-20260709T-stage4-cleanroom/output python -c "import prompt_toolkit; print(prompt_toolkit.__file__)"
```

Output:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-prompt-toolkit-fullrepro-001-20260709T-stage4-cleanroom/output/prompt_toolkit/__init__.py
```

The path points into the candidate output directory, not the reference source tree or an installed package.

## Anti-Cheat Scan

No cheating evidence was found in the candidate implementation. A scan of candidate output files found no references to the source repository, hidden oracle artifacts, kept nodeids, taxonomy, spec-test map, reference score, prior score result, API key file, or installed target package. The run workspace contained only the public prompt/spec and files created under its own output directory.

## Solvability

Reference oracle passes: 100/100.
Dummy gate passed 0/100.
Scorer isolation: `harness/score_pytest_original.py` with remove paths `['src/prompt_toolkit']`.

## Candidate Score

- score: 59/100
- pass_rate_excluding_skips: 0.59

```json
{
  "summary": {
    "collection_error": 15,
    "error": 5,
    "failed": 21,
    "passed": 59,
    "total": 100
  },
  "by_layer": {
    "atomic": {
      "collection_error": 12,
      "error": 1,
      "failed": 10,
      "passed": 36,
      "total": 59
    },
    "integration": {
      "collection_error": 3,
      "error": 4,
      "failed": 6,
      "passed": 20,
      "total": 33
    },
    "system_e2e": {
      "passed": 3,
      "total": 8,
      "failed": 5
    }
  }
}
```

## Gate A - Spec Mapping Spot-Check

Stage 3 review and local mechanical checks confirmed every covered row maps to a real public spec heading. The judge spot-check uses the Stage 3 coverage map and failure examples; sampled failures remain traceable to documented public API, state, error, or workflow sections.

## Gate B - Failure Pattern Audit

- `api-surface`: Candidate misses enough public module/import behavior to produce 15 upstream collection errors.
- `workflow-completeness`: PromptSession pipe input/default-accept workflows and full-screen layout buffer projection fail in generated public workflows.
- `atomic-behavior`: Formatted text Template formatting and selected style/layout utilities diverge from documented behavior.

Representative non-passing examples:

- `filter/test_generated_public_oracle.py::test_prompt_session_accept_default_workflow_reuses_session` (failed): EOFError
- `filter/test_generated_public_oracle.py::test_top_level_prompt_with_pipe_input_returns_text` (failed): EOFError
- `filter/test_generated_public_oracle.py::test_template_formatted_text_style_workflow_preserves_plain_text` (failed): ValueError: empty field names are not supported
- `filter/test_generated_public_oracle.py::test_full_screen_layout_workflow_objects_share_buffer` (failed): AttributeError: 'Layout' object has no attribute 'current_buffer'
- `filter/test_generated_public_oracle.py::test_full_screen_layout_workflow_can_focus_second_buffer` (failed): AttributeError: 'Layout' object has no attribute 'current_buffer'
- `filter/test_generated_public_oracle.py::test_full_screen_layout_workflow_includes_status_control` (failed): AttributeError: 'Application' object has no attribute 'full_screen'

These failures check observable public behavior and public importability. They are candidate implementation failures rather than verifier failures.

## Gate C - Generated-Only Oracle Spot-Check

Not generated-only. The oracle mixes upstream retained tests with generated public tests. Generated tests were validated during Stage 3 with reference 100% and dummy 0 passed; sampled generated failures check public workflows and state, not private implementation shape.

## Gate D - Coverage Gap Audit

Coverage verdict: FULL.

The merged oracle covers upstream public behavior plus 32 generated public tests, with nonzero atomic, integration, and system_e2e coverage and all reference/dummy gates satisfied.

Stage 3 coverage summary:

```text
## Verdict
## Artifact Checks
| check | result |
|---|---|
| `filter/rewrite_audit.md` exists | PASS |
| `filter/spec_test_map.md` exists and has one row per processed upstream/generated test | PASS |
| upstream rows accounted | 156 / 156 |
| generated rows accounted | 32 / 32 |
| covered rows | 100 |
| source-only rows | 28 |
| excluded rows | 60 |
| `filter/kept_nodeids.txt` line count | 100 |
| `filter/taxonomy.jsonl` line count | 100 |
| taxonomy layers non-zero | PASS: atomic 59, integration 33, system_e2e 8 |
| `filter/test_taxonomy_score.csv` exists | PASS |
| root copies exist for required public filter artifacts | PASS |
## Coverage Gate
| spec section | covered tests |
|---|---:|
| Application, Prompt, and I/O | 3 |
| Completion | 18 |
| Cross-View Invariants | 5 |
| Document and Buffer | 13 |
| Error Semantics | 8 |
| Formatted Text | 16 |
| Formatted Text and Styles | 3 |
| Full-Screen Layout With a Buffer and Exit Binding | 3 |
| Installable Surface | 3 |
| Key Bindings | 6 |
| Layout Controls | 3 |
| Product State Model | 5 |
| Prompt With Completion and Validation | 3 |
| Styles | 7 |
| Validation | 4 |
## Behavioral Filter Gate
- terminal byte stream exactness
- snapshot exact rendering
- private renderer/parser internals
- contrib servers, dialogs, progress, widget visual polish
- platform-specific terminal behavior
- test helper fixtures
## Reference Gate
- Upstream retained scorer gate: 68 passed / 68 total
- Generated public pytest gate: 32 passed / 32 total
- Merged aggregate: 100 passed / 100 total
```

## Real Failure Clusters

1. `api-surface`: Candidate misses enough public module/import behavior to produce 15 upstream collection errors.
2. `workflow-completeness`: PromptSession pipe input/default-accept workflows and full-screen layout buffer projection fail in generated public workflows.
3. `atomic-behavior`: Formatted text Template formatting and selected style/layout utilities diverge from documented behavior.

## Cascade Analysis

The score is valid as a model capability signal. Collection errors, where present, are rooted in missing documented public surface and cascade into downstream behavior; executed failures are concentrated in public state, parser/formatter, workflow, or error semantics rather than hidden internals.

## Labels

- qualified
- upstream-plus-generated-oracle
- mixed-coverage
- prompt-session-workflow-signal
- layout-cross-view-signal

## Verdict

QUALIFIED. Hard gates pass: candidate import provenance is clean, anti-cheat scan is clean, reference gate is 100%, dummy gate is 0 passed, scorer isolation is recorded, Stage 3 model reviews passed, and candidate failures are spec-driven behavioral signals.
