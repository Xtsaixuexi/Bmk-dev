# Filter Validation: tomlkit-fullrepro-001

Date: 2026-07-02

## Collection Summary

- Upstream collected nodeids: 1035
- Upstream clean kept nodeids: 12
- Generated public tests: 52
- Final scoreable tests: 64
- Spec gaps: 0

## Filtering Decision

The upstream suite has a high module-level private import rate. Keeping nodeids from those modules would create collection failures or require candidate implementations to expose private implementation modules not present in the public spec. Those nodeids are marked `excluded` in `spec_test_map.md`.

The scoreable set combines:

- `filter/kept_upstream.txt`: safe upstream tests from `tests/test_toml_file.py` and `tests/test_write.py`;
- `filter/generated_public_tests.py`: benchmark-owned public API tests generated from `spec.md`.

## Produced Artifacts

- `filter/all_nodeids.txt`
- `filter/kept_upstream.txt`
- `filter/generated_public_tests.py`
- `filter/generated_nodeids.txt`
- `filter/kept_nodeids.txt`
- `filter/spec_test_map.md`
- `filter/taxonomy.jsonl`
- `filter/test_taxonomy_score.csv`
- `filter/rewrite_audit.md`

## Layer Counts

- atomic: 25
- integration: 19
- system_e2e: 20

## Fairness Checks

- Candidate-visible spec covers every `covered` row through a named section in `spec.md`.
- Generated tests import only public names.
- Generated tests avoid exact `repr()` assertions, private attributes, private modules, and exact exception message wording.
- Upstream tests with private module-level imports are excluded to avoid collection-carrier unfairness.
- TOML compliance corpus cases are excluded from direct scoring because they are dominated by closed-standard coverage and private utility decoding.

## Result

Filter v1 is ready for DeepSeek/GLM Step 4 review and reference validation.
