# Collection Audit: pyparsing-fullrepro-001

Command:

```bash
cd /root/autodl-tmp/e2e/pyparsing && PYTHONPATH=. pytest --collect-only -q tests
```

Result: collection succeeded after installing optional diagram dependency `railroad-diagrams`.

Collected nodeids: 2040

Stdout log: `logs/collect_stdout.txt`  
Stderr log: `logs/collect_stderr.txt`

Initial collection without `railroad-diagrams` collected 2029 nodeids then failed on `tests/test_diagram.py`; the dependency is declared in the package's `diagrams` optional extra.
