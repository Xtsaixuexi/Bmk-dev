# Judge Diagnosis: pyyaml-fullrepro-001

verdict: QUALIFIED
spec_version: v1
filter_version: upstream_filter_v1
candidate_run: opencode-gpt-5.5-pyyaml-fullrepro-001-20260709T-stage4-cleanroom

## Preflight output

Command:

```bash
PYTHONPATH=/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-pyyaml-fullrepro-001-20260709T-stage4-cleanroom/output python -c "import yaml; print(yaml.__file__)"
```

Output:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/opencode-gpt-5.5-pyyaml-fullrepro-001-20260709T-stage4-cleanroom/output/yaml/__init__.py
```

The path points into the candidate output directory, not the reference source tree or an installed package.

## Anti-Cheat Scan

No cheating evidence was found in the candidate implementation. A scan of candidate output files found no references to the source repository, hidden oracle artifacts, kept nodeids, taxonomy, spec-test map, reference score, prior score result, API key file, or installed target package. The run workspace contained only the public prompt/spec and files created under its own output directory.

## Solvability

Reference oracle passes: 889/889.
Dummy gate passed 0/889.
Scorer isolation: `harness/score_pytest_original.py` with remove paths `['yaml']`.

## Candidate Score

- score: 3/889
- pass_rate_excluding_skips: 0.003374578177727784

```json
{
  "summary": {
    "collection_error": 886,
    "passed": 3,
    "total": 889
  },
  "by_layer": {
    "atomic": {
      "collection_error": 321,
      "passed": 3,
      "total": 324
    },
    "integration": {
      "collection_error": 375,
      "total": 375
    },
    "system_e2e": {
      "collection_error": 190,
      "total": 190
    }
  }
}
```

## Gate A - Spec Mapping Spot-Check

Stage 3 review and local mechanical checks confirmed every covered row maps to a real public spec heading. The judge spot-check uses the Stage 3 coverage map and failure examples; sampled failures remain traceable to documented public API, state, error, or workflow sections.

## Gate B - Failure Pattern Audit

- `api-surface`: Candidate omitted public parser/composer/constructor/resolver class surface such as `yaml.composer.Composer`, causing nearly all retained legacy tests to fail collection.
- `workflow-completeness`: Only three atomic smoke cases executed; parser, token/event/node, dumping, custom resolver, and cross-view workflows are hidden behind the missing composer surface.

Representative non-passing examples:

- `tests/legacy_tests/test_yaml.py` (collection_error):  ==================================== ERRORS ==================================== _______________ ERROR collecting tests/legacy_tests/test_yaml.py _______________ tests/legacy_test

These failures check observable public behavior and public importability. They are candidate implementation failures rather than verifier failures.

## Gate C - Generated-Only Oracle Spot-Check

Not applicable. The oracle is upstream-only.

## Gate D - Coverage Gap Audit

Coverage verdict: FULL.

The oracle covers all primary behavior sections: Loading, Dumping, YAML Type Mapping, Tokens/Events/Nodes, Constructors/Representers/Resolvers/YAMLObject, Error Semantics, Cross-View Invariants, and Representative Workflows.

Stage 3 coverage summary:

```text
- processed nodeids: 2616
- final scoreable oracle: 889
- source-only: 39
- excluded: 1688
- layers: {'atomic': 324, 'integration': 375, 'system_e2e': 190}
- Track B: not triggered; Track A retained enough public behavioral coverage.
- scorer isolation: `score_pytest_original.py --remove-path yaml` with reference solution dir `/root/autodl-tmp/new-e2e/yaml__pyyaml/lib`.
## Coverage Floor
| spec section | covered rows | floor | status |
|---|---:|---:|---|
| Installable Surface | 3 | 3 | PASS |
| Product State Model | 465 | 3 | PASS |
| Loading | 230 | 3 | PASS |
| YAML Type Mapping | 47 | 3 | PASS |
| Dumping | 177 | 3 | PASS |
| Tokens, Events, And Nodes | 577 | 3 | PASS |
| Constructors, Representers, Resolvers, And YAMLObject | 99 | 3 | PASS |
| Error Semantics | 197 | 3 | PASS |
| Cross-View Invariants | 514 | 5 | PASS |
| Representative Workflows | 241 | 3 | PASS |
```

## Real Failure Clusters

1. `api-surface`: Candidate omitted public parser/composer/constructor/resolver class surface such as `yaml.composer.Composer`, causing nearly all retained legacy tests to fail collection.
2. `workflow-completeness`: Only three atomic smoke cases executed; parser, token/event/node, dumping, custom resolver, and cross-view workflows are hidden behind the missing composer surface.

## Cascade Analysis

The score is valid as a model capability signal. Collection errors, where present, are rooted in missing documented public surface and cascade into downstream behavior; executed failures are concentrated in public state, parser/formatter, workflow, or error semantics rather than hidden internals.

## Labels

- qualified
- upstream-only-oracle
- api-surface-dominated
- collection-error-cascade
- yaml-parser-surface-signal

## Verdict

QUALIFIED. Hard gates pass: candidate import provenance is clean, anti-cheat scan is clean, reference gate is 100%, dummy gate is 0 passed, scorer isolation is recorded, Stage 3 model reviews passed, and candidate failures are spec-driven behavioral signals.
