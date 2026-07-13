# Filter Validation: pyyaml-fullrepro-001

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

Non-behavior sections (`Product Overview`, `Scope`, `Non-Goals`, `Evaluation Notes`) are not scored as coverage targets.
