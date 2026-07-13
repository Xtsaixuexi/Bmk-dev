# Bandit Stage 3A Rewrite Audit

Source revision: `c45446eaa30c4f28289c3b8ba9a955e1d78ba715`

Shared fixture scan found no candidate-portable shared helper layer: retained unit and functional files construct scanner state through `bandit.core` managers, configs, metrics, extension registries, or source-tree fixtures. More than 50% of files are discarded after rewrite analysis, so Track B is mandatory.

| upstream file | test functions | Bandit imports | decision | reason |
|---|---:|---|---|---|
| `functional/test_baseline.py` | 7 | `CLI subprocess only` | discard; Track B | repository copies and internal baseline fixtures are not cleanroom-portable |
| `functional/test_functional.py` | 79 | `bandit.core` | discard; Track B | bidirectional internal manager/config/test-set harness constructs scanner state |
| `functional/test_runtime.py` | 9 | `CLI subprocess only` | discard; Track B | depends on upstream examples and exact human-report wording |
| `unit/cli/test_baseline.py` | 12 | `bandit.cli` | discard; Track B | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `unit/cli/test_config_generator.py` | 6 | `bandit.cli, bandit.core` | discard; Track B | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `unit/cli/test_main.py` | 20 | `bandit.cli, bandit.core` | discard; Track B | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `unit/core/test_blacklisting.py` | 2 | `bandit.core` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/core/test_config.py` | 16 | `bandit.core` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/core/test_context.py` | 19 | `bandit.core` | discard; Track B | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `unit/core/test_docs_util.py` | 3 | `bandit, bandit.core.docs_utils` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/core/test_issue.py` | 7 | `bandit, bandit.core` | retain with extraction | six functions rewrite to top-level bandit.Issue/Cwe; exact str test excluded |
| `unit/core/test_manager.py` | 21 | `bandit.core` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/core/test_meta_ast.py` | 2 | `bandit.core` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/core/test_test_set.py` | 14 | `bandit.blacklists, bandit.core` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/core/test_util.py` | 30 | `bandit.core` | discard; Track B | tests internal bandit.core architecture outside the candidate contract |
| `unit/formatters/test_csv.py` | 1 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_custom.py` | 1 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_html.py` | 3 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_json.py` | 1 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_sarif.py` | 1 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_screen.py` | 4 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_text.py` | 4 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_xml.py` | 1 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |
| `unit/formatters/test_yaml.py` | 1 | `bandit, bandit.core, bandit.formatters` | discard; Track B | internal manager/config/metrics fixtures and exact formatter shape |

Total files: 24 | total test functions audited: 264 | retained file functions: 7 | rewritten: 6 | excluded in retained file: 1

Actual rewrites are in `rewritten_upstream_tests.py`; every other function is accounted for in `candidate_filter_map.md`.
