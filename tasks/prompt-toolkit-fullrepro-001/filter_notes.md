# Filter Notes: prompt-toolkit-fullrepro-001

Stage 1 pre-screen indicates this repository can proceed to Stage 2, with Stage 3 filtering expected to remove tests that depend on private helpers, exact transcript formatting, optional environment fixtures, or non-public tooling.

## Mechanical Signals

- source LOC: 36892
- rough test functions: 156
- docs files rough: 159
- private import file rate: 0.0
- network marker file rate: 0.048
- snapshot marker file rate: 0.143

## Pytest Collect Pre-Screen

- command: `python -m pytest --collect-only -q -o addopts= <test roots>`
- status: `COLLECT_OK`
- returncode: `0`
- collected nodeids: 156
- error markers: 0

## Stage 3 Attention

- Keep tests only when behavior maps to candidate-visible spec sections.
- Exclude internal helper/import carrier tests and exact message/snapshot assertions unless the exact behavior is a public contract.
- Preserve scorer isolation with package path removal when reference and candidate are scored.
