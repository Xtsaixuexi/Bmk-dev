# Independent Stage 3A Review: Bandit Import Audit

Review only the appended Stage 3A artifacts. Do not browse, use tools, inspect a repository, or infer hidden tests.

Check that:

- the file-level audit accounts for all stated upstream files and functions;
- every function has exactly one rewritten or excluded disposition;
- rewrite decisions preserve public behavior and use only candidate-visible public API;
- excluded surfaces are implementation-shaped, fixture-bound, out of scope, or exact-output brittle;
- the actual rewritten tests match the audit and would fail a materially wrong implementation;
- the stated Track B trigger follows from the audit;
- no source code, hidden fixture content, expected score, or secret is leaked to a candidate.

Return only:

- `VERDICT`: PASS_CONTINUE or PATCH_REQUIRED
- `ACCOUNTING`: PASS or FAIL
- `PUBLIC_API_ONLY`: PASS or FAIL
- `REWRITE_FAIRNESS`: PASS or FAIL
- `TRACK_B_TRIGGER`: PASS or FAIL
- `CANDIDATE_SAFETY`: PASS or FAIL
- `BLOCKERS`: exact mandatory corrections; empty for PASS_CONTINUE

---
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
# Bandit Stage 3A Candidate Filter Map

| upstream test | status | spec section | rewritten target / exclusion reason |
|---|---|---|---|
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_no_new_candidates` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_no_existing_no_new_candidates` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_no_existing_with_new_candidates` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_existing_and_new_candidates` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_no_new_candidates_include_nosec` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_new_candidates_include_nosec_only_nosecs` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_baseline.py::BaselineFunctionalTests::test_new_candidates_include_nosec_new_nosecs` | excluded | - | repository copies and internal baseline fixtures are not cleanroom-portable |
| `tests/functional/test_functional.py::FunctionalTests::test_binding` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_crypto_md5` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_ciphers` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_cipher_modes` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_eval` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_mark_safe` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_exec` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_hardcoded_passwords` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_hardcoded_tmp` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_imports_aliases` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_imports_from` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_imports_function` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_telnet_usage` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_ftp_usage` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_imports` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_imports_using_importlib` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_mktemp` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_nonsense` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_okay` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_subdirectory_okay` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_os_chmod` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_os_exec` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_os_popen` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_os_spawn` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_os_startfile` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_os_system` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_pickle` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_dill` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_shelve` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_jsonpickle` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_pandas_read_pickle` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_popen_wrappers` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_random_module` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_requests_ssl_verify_disabled` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_requests_without_timeout` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_skip` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_ignore_skip` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_sql_statements` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_multiline_sql_statements` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_ssl_insecure_version` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_subprocess_shell` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_urlopen` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_wildcard_injection` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_django_sql_injection` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_django_sql_injection_raw` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_yaml` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_host_key_verification` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_jinja2_templating` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_mako_templating` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_django_xss_secure` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_django_xss_insecure` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_xml` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_httpoxy` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_asserts` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_paramiko_injection` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_partial_path` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_try_except_continue` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_try_except_pass` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_metric_gathering` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_weak_cryptographic_key` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_multiline_code` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_code_line_numbers` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_flask_debug_true` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_nosec` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_baseline_filter` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_unverified_context` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_hashlib_new_insecure_functions` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_blacklist_pycrypto` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_no_blacklist_pycryptodome` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_blacklist_pyghmi` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_snmp_security_check` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_tarfile_unsafe_members` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_pytorch_load` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_trojansource` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_trojansource_latin1` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_markupsafe_markup_xss` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_markupsafe_markup_xss_extend_markup_names` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_markupsafe_markup_xss_allowed_calls` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_functional.py::FunctionalTests::test_huggingface_unsafe_download` | excluded | - | bidirectional internal manager/config/test-set harness constructs scanner state |
| `tests/functional/test_runtime.py::RuntimeTests::test_no_arguments` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_piped_input` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_nonexistent_config` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_help_arg` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_example_nonexistent` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_example_okay` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_example_nonsense` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_example_nonsense2` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/functional/test_runtime.py::RuntimeTests::test_example_imports` | excluded | - | depends on upstream examples and exact human-report wording |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_bandit_baseline` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_main_non_repo` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_main_git_command_failure` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_main_no_parent_commit` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_main_subprocess_error` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_init_logger` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_initialize_no_repo` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_initialize_git_command_failure` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_initialize_dirty_repo` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_initialize_existing_report_file` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_initialize_with_output_argument` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_baseline.py::BanditBaselineToolTests::test_initialize_existing_temp_file` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_config_generator.py::BanditConfigGeneratorLoggerTests::test_init_logger` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_config_generator.py::BanditConfigGeneratorTests::test_parse_args_no_defaults` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_config_generator.py::BanditConfigGeneratorTests::test_parse_args_show_defaults` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_config_generator.py::BanditConfigGeneratorTests::test_parse_args_out_file` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_config_generator.py::BanditConfigGeneratorTests::test_get_config_settings` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_config_generator.py::BanditConfigGeneratorTests::test_main_show_defaults` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainLoggerTests::test_init_logger` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainLoggerTests::test_init_logger_debug_mode` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_get_options_from_ini_no_ini_path_no_target` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_get_options_from_ini_empty_directory_no_target` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_get_options_from_ini_no_ini_path_no_bandit_files` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_get_options_from_ini_no_ini_path_multi_bandit_files` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_init_extensions` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_log_option_source_arg_val` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_log_option_source_ini_value` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_log_option_source_ini_val_with_str_default_and_no_arg_val` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_log_option_source_no_values` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_config_unopenable` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_invalid_config` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_handle_ini_options` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_profile_not_found` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_baseline_ioerror` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_invalid_output_format` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_exit_with_results` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_exit_with_no_results` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/cli/test_main.py::BanditCLIMainTests::test_main_exit_with_results_and_with_exit_zero_flag` | excluded | - | in-process internal CLI helpers or out-of-scope auxiliary command internals |
| `tests/unit/core/test_blacklisting.py::BlacklistingTests::test_report_issue` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_blacklisting.py::BlacklistingTests::test_report_issue_defaults` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestInit::test_settings` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestInit::test_file_does_not_exist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestInit::test_yaml_invalid` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestGetOption::test_levels` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestGetOption::test_levels_not_exist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestGetSetting::test_not_exist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_include` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_exclude` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_blacklist_call_data` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_blacklist_import_data` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_blacklist_call_test` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_blacklist_import_test` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_converted_exclude_blacklist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_deprecation_message` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_blacklist_error` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_config.py::TestConfigCompat::test_bad_yaml` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_context.py::ContextTests::test_context_create` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_repr` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_call_args` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_call_args_count` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_call_function_name` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_call_function_name_qual` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_call_keywords` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_node` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_string_val` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_statement` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_function_def_defaults_qual` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test__get_literal_value` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_check_call_arg_value` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_get_lineno_for_call_arg` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_get_call_arg_at_position` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_is_module_being_imported` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_is_module_imported_exact` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_is_module_imported_like` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_context.py::ContextTests::test_filename` | excluded | - | plugin Context is public, but upstream setup relies on internal raw-context shape |
| `tests/unit/core/test_docs_util.py::DocsUtilTests::test_overwrite_bib_info` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_docs_util.py::DocsUtilTests::test_plugin_call_bib` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_docs_util.py::DocsUtilTests::test_import_call_bib` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_issue.py::IssueTests::test_issue_create` | rewritten | Public API - Issue | `filter/rewritten_upstream_tests.py::test_issue_constructor_and_public_attributes` |
| `tests/unit/core/test_issue.py::IssueTests::test_issue_str` | excluded | - | exact Issue.__str__ text is outside the contract |
| `tests/unit/core/test_issue.py::IssueTests::test_issue_as_dict` | rewritten | Public API - Issue | `filter/rewritten_upstream_tests.py::test_issue_as_dict_without_code` |
| `tests/unit/core/test_issue.py::IssueTests::test_issue_filter_severity` | rewritten | Public API - Issue | `filter/rewritten_upstream_tests.py::test_issue_filter_severity_ranking` |
| `tests/unit/core/test_issue.py::IssueTests::test_issue_filter_confidence` | rewritten | Public API - Issue | `filter/rewritten_upstream_tests.py::test_issue_filter_confidence_ranking` |
| `tests/unit/core/test_issue.py::IssueTests::test_matches_issue` | rewritten | Public API - Issue | `filter/rewritten_upstream_tests.py::test_issue_equality_fields_and_location_independence` |
| `tests/unit/core/test_issue.py::IssueTests::test_get_code` | rewritten | Public API - Issue | `filter/rewritten_upstream_tests.py::test_issue_get_code_from_public_filename` |
| `tests/unit/core/test_manager.py::ManagerTests::test_create_manager` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_create_manager_with_profile` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_matches_globlist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_is_file_included` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_get_files_from_dir` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_populate_baseline_success` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_populate_baseline_invalid_json` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_results_count` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_output_results_invalid_format` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_output_results_valid_format` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_recurse_skip` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_recurse_files` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_exclude` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_exclude_dir` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_exclude_cmdline` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_exclude_glob` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_discover_files_include` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_run_tests_keyboardinterrupt` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_run_tests_ioerror` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_compare_baseline` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_manager.py::ManagerTests::test_find_candidate_matches` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_meta_ast.py::BanditMetaAstTests::test_add_node` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_meta_ast.py::BanditMetaAstTests::test_str` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::test_plugin` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_has_defaults` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_include_id` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_exclude_id` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_include_none` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_exclude_none` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_has_builtin_blacklist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_exclude_builtin_blacklist` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_exclude_builtin_blacklist_specific` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_filter_blacklist_none` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_filter_blacklist_one` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_filter_blacklist_include` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_filter_blacklist_all` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_test_set.py::BanditTestSetTests::test_profile_blacklist_compat` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_abs_typical` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_with_dot` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_abs_missingmid` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_abs_missingend` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_abs_syms` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_rel_typical` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_rel_missingmid` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_rel_missingend` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_rel_syms` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_sys` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_invalid_path` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_module_qualname_from_path_dir` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_namespace_path_join` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_namespace_path_split` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_call_name1` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_call_name2` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_get_call_name3` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_linerange` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_path_for_function` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_path_for_function_no_file` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_path_for_function_no_module` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_escaped_representation_simple` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_escaped_representation_valid_not_printable` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_escaped_representation_invalid` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_escaped_representation_mixed` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_deepgetattr` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_parse_ini_file` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_check_ast_node_good` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_check_ast_node_bad_node` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/core/test_util.py::UtilTests::test_check_ast_node_bad_type` | excluded | - | tests internal bandit.core architecture outside the candidate contract |
| `tests/unit/formatters/test_csv.py::CsvFormatterTests::test_report` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_custom.py::CustomFormatterTests::test_report` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_html.py::HtmlFormatterTests::test_report_with_skipped` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_html.py::HtmlFormatterTests::test_report_contents` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_html.py::HtmlFormatterTests::test_escaping` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_json.py::JsonFormatterTests::test_report` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_sarif.py::SarifFormatterTests::test_report` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_screen.py::ScreenFormatterTests::test_output_issue` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_screen.py::ScreenFormatterTests::test_no_issues` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_screen.py::ScreenFormatterTests::test_report_nobaseline` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_screen.py::ScreenFormatterTests::test_report_baseline` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_text.py::TextFormatterTests::test_output_issue` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_text.py::TextFormatterTests::test_no_issues` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_text.py::TextFormatterTests::test_report_nobaseline` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_text.py::TextFormatterTests::test_report_baseline` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_xml.py::XmlFormatterTests::test_report` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |
| `tests/unit/formatters/test_yaml.py::YamlFormatterTests::test_report` | excluded | - | internal manager/config/metrics fixtures and exact formatter shape |

Total: 264 | rewritten: 6 | excluded: 258
from __future__ import annotations

import bandit


def make_issue(severity=bandit.MEDIUM, confidence=bandit.MEDIUM):
    finding = bandit.Issue(severity, 605, confidence, "Test issue")
    finding.fname = "code.py"
    finding.test = "bandit_plugin"
    finding.test_id = "B999"
    finding.lineno = 1
    finding.col_offset = 8
    finding.end_col_offset = 16
    return finding


def test_issue_constructor_and_public_attributes():
    finding = make_issue()
    assert isinstance(finding, bandit.Issue)
    assert finding.fname == "code.py"
    assert finding.test == "bandit_plugin"


def test_issue_as_dict_without_code():
    data = make_issue().as_dict(with_code=False)
    assert data == {
        "filename": "code.py",
        "test_name": "bandit_plugin",
        "test_id": "B999",
        "issue_severity": "MEDIUM",
        "issue_cwe": {
            "id": 605,
            "link": "https://cwe.mitre.org/data/definitions/605.html",
        },
        "issue_confidence": "MEDIUM",
        "issue_text": "Test issue",
        "line_number": 1,
        "line_range": [],
        "col_offset": 8,
        "end_col_offset": 16,
    }


def test_issue_filter_severity_ranking():
    assert make_issue(bandit.HIGH, bandit.HIGH).filter(
        bandit.MEDIUM, bandit.UNDEFINED
    )
    assert not make_issue(bandit.LOW, bandit.HIGH).filter(
        bandit.MEDIUM, bandit.UNDEFINED
    )


def test_issue_filter_confidence_ranking():
    assert make_issue(bandit.HIGH, bandit.HIGH).filter(
        bandit.UNDEFINED, bandit.MEDIUM
    )
    assert not make_issue(bandit.HIGH, bandit.LOW).filter(
        bandit.UNDEFINED, bandit.MEDIUM
    )


def test_issue_equality_fields_and_location_independence():
    left = make_issue()
    right = make_issue()
    right.lineno = 99
    assert left == right
    right.test = "different_plugin"
    assert left != right


def test_issue_get_code_from_public_filename(tmp_path):
    source = tmp_path / "sample.py"
    source.write_text("first\nsecond\nthird\n", encoding="utf-8")
    finding = bandit.Issue(bandit.LOW, lineno=2)
    finding.fname = str(source)
    finding.linerange = [2]
    code = finding.get_code(max_lines=1)
    assert "2 second" in code
