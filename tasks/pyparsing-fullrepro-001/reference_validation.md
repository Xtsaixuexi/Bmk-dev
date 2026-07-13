# Reference Validation: pyparsing-fullrepro-001

Reference command:

```bash
cd /root/autodl-tmp/e2e/pyparsing && PYTHONPATH=. python -m pytest -q <kept_nodeids>
```

Result: pass after v4 spec correction. The 298-nodeid filter is unchanged from the v2 filter correction.

- Total scoreable nodeids: 298
- Passed nodeids: 298
- Subtests passed: 298
- Failed/errors: 0
- Pass rate excluding skips: 1.0

Layer summary:

- atomic: 167/167
- integration: 106/106
- system_e2e: 25/25

Logs:

- `logs/reference_pytest_stdout.txt`
- `logs/reference_pytest_stderr.txt`

Decision: reference oracle is valid for candidate scoring.
