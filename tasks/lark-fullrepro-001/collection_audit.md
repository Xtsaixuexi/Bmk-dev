# Collection Audit: lark-fullrepro-001

- source path: `/root/autodl-tmp/e2e/lark`
- source commit: `c169b26a5bec9d47e590bf4be83691bcbdfe7b6b`
- collection command: `python -m pytest tests --collect-only`
- total collected nodeids: 1273
- kept covered nodeids: 792
- source-only: 422
- excluded: 59
- spec_gap: 0

## Taxonomy

| layer | kept |
|---|---:|
| atomic | 394 |
| integration | 248 |
| system_e2e | 150 |

## Reference Validation

- pytest exit code: 0
- reported tests: 792
- passed: 710
- failed: 0
- skipped: 82
- pass_rate_excluding_skips: 1.0
- unknown taxonomy count: 0

## Notes

Pytest collection routes upstream unittest cases through `tests/__main__.py`; scorer taxonomy keys therefore use `__main__::Class.test`.

For candidate scoring, direct nodeids were generated from `filter/node_metadata.json` by mapping each kept `tests/__main__.py::Class::test` nodeid to the class module's real test file. The direct scoring adapter was checked against the reference implementation and reproduced the same result: 710 passed, 82 skipped, 0 failed, pass_rate_excluding_skips=1.0.

The package does not contain source code. The source repository remains only at the recorded oracle path for task construction and scoring provenance.
