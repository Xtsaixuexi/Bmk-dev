# Source Pointer

## Source Repository

- repo: `python-poetry/tomlkit`
- source path: `/root/autodl-tmp/e2e/tomlkit`
- commit: `43668ddebc3f082bf385d328aceed18d26976897`
- package root: `/root/autodl-tmp/e2e/tomlkit/tomlkit`
- upstream tests: `/root/autodl-tmp/e2e/tomlkit/tests`

## Boundary

The source repository is an oracle/reference input for spec writing, test filtering, and reference validation only. It must not be copied into this WIP directory or any candidate run output.

Candidate implementations may receive only:

- the candidate-visible `spec.md`;
- generic reconstruction instructions;
- dependency/environment instructions that do not reveal tests, source layout, taxonomy, kept node IDs, reference scores, reviews, or prior outputs.

Candidate implementations must not receive:

- `/root/autodl-tmp/e2e/tomlkit`;
- upstream test files;
- hidden oracle files;
- `kept_nodeids.txt`;
- `taxonomy.jsonl`;
- `spec_test_map.md`;
- `reference_score.json`;
- candidate score reports;
- `/root/autodl-tmp/api.txt`.

## Reference Use

Reference commands should run with import provenance recorded. Candidate scoring must prove that `import tomlkit` resolves from the candidate `output/` directory, not from `/root/autodl-tmp/e2e/tomlkit` or an installed PyPI package.
