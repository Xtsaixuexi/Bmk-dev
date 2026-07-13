# Independent Stage 1 Review: bandit-fullrepro-001

Review only this candidate-selector evidence. Do not browse, use tools, inspect files, or consider any other project.

Evidence:

- repository: `PyCQA/bandit`
- product: offline security-oriented static analysis of Python source
- source LOC: 17540
- source Python files: 164
- docs signal: 163 rough docs files covering CLI, configuration, plugins/checks, finding taxonomy, baselines, and report formats
- isolated collection after installing declared and optional formatter dependencies: 275 nodeids, zero errors
- private import file rate: 0.0
- network/environment marker rate: 0.156
- snapshot marker rate: 0.0
- shared finding state is projected through CLI status/output, Issue objects, severity/confidence filters, profiles/config, baselines, metrics, and CSV/JSON/SARIF/XML/YAML/text/HTML reports

Risks routed to later stages: implementation-specific AST context, plugin-manager registration shapes, exact messages, arbitrary formatter whitespace/order, and optional SARIF schema internals.

Return only:

- `VERDICT`: PASS_CONTINUE or REJECT
- `HARD_GATES`: PASS or FAIL
- `OFFLINE_DETERMINISM`: PASS or FAIL
- `RISK_ROUTING`: ACCEPT or FAIL
- `NEXT_STATE`: S2_READY or RETIRED
- `BLOCKERS`: mandatory issues only
