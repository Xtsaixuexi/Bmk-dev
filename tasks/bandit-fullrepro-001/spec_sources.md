# Bandit Spec Sources

- `README.rst`
- `doc/source/start.rst`
- `doc/source/config.rst`
- `doc/source/man/bandit.rst`
- `doc/source/plugins/index.rst`
- `doc/source/plugins/b*.rst` and public plugin docstrings
- `doc/source/blacklists/*.rst` and public blacklist generator documentation
- `doc/source/formatters/*.rst` and public formatter documentation
- `bandit/__init__.py` public re-exports
- `bandit/core/constants.py` public ranking constants
- `bandit/core/issue.py` public `Issue` and `Cwe` signatures/docstrings
- `bandit/core/test_properties.py` documented plugin decorators
- `bandit/core/context.py` documented plugin context properties/methods
- Public CLI reference probes recorded under `new-work/parallel-results/lane-1/bandit-stage2-probes/`
- Reference JSON scan of the public `examples/` tree: `new-work/parallel-results/lane-1/20260710_bandit_examples_reference.json`

No upstream test names, nodeids, hidden oracle details, candidate outputs, or score data belong in the candidate-visible specification.
