# Filter Notes: jsonpickle-fullrepro-001

Stage 1 pre-screen indicates this repository can proceed to Stage 2 after model review. Stage 3 must still filter each retained test for public spec traceability and observable behavior.

## Mechanical Signals

- source LOC: 4128
- rough test functions: 336
- docs files rough: 17
- private import file rate: 0.0
- network marker file rate: 0.15
- snapshot marker file rate: 0.0

## Pytest Collect Pre-Screen

- command: `python -m pytest --collect-only -q -o addopts= <test roots>`
- status: `COLLECT_OK`
- returncode: `0`
- collected nodeids: 784
- error markers: 0

## Stage 3 Attention

- Exclude private helper, exact transcript, fixture-carrier, optional service, and internal structure assertions.
- Keep behavior only when mapped to candidate-visible spec sections.
- Preserve scorer isolation with package path removal when reference and candidate are scored.
