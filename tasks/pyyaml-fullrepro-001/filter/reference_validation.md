# Reference Validation: pyyaml-fullrepro-001

Generated: 2026-07-09T10:53:42.629221Z

## Gates

- PASS: scorer isolation used `score_pytest_original.py --remove-path yaml`.
- PASS: import provenance resolved to `/root/autodl-tmp/new-e2e/yaml__pyyaml/lib/yaml/__init__.py`.
- PASS: reference gate passed 889/889.
- PASS: dummy gate passed 0/889; outcomes were {'collection_error': 886, 'failed': 3, 'total': 889}.
- PASS: taxonomy produced no `unknown` layer cases.
- PASS: coverage floor has no below-minimum behavior sections.

## Scorer Isolation

The scorer copied the upstream repository, removed top-level `yaml`, and placed `/root/autodl-tmp/new-e2e/yaml__pyyaml/lib` first on `PYTHONPATH`.
