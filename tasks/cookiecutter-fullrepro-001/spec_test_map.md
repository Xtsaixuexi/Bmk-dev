| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `test_abort_generate_on_hook_error::test_hooks_raises_errors` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_version` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_error_on_existing_output_directory` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_verbose` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_replay` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_replay_file` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_replay_generated` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_exit_on_noinput_and_replay` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_run_cookiecutter_on_overwrite_if_exists_and_replay` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_overwrite_if_exists_when_output_dir_does_not_exist` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_overwrite_if_exists_when_output_dir_exists` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_output_dir` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_help` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_user_config` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_default_user_config_overwrite` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_default_user_config` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_echo_undefined_variable_error` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_echo_unknown_extension_error` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_local_extension` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_local_extension_not_available` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_extra_context` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_extra_context_invalid_format` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_debug_file_non_verbose` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_debug_file_verbose` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_debug_list_installed_templates` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_debug_list_installed_templates_failure` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_directory_repo` | system_e2e | Public Interfaces + Template Directories and Archives + Zip Archives | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_accept_hooks` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_with_json_decoding_error` | system_e2e | Error Semantics | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cli::test_cli_with_pre_prompt_hook` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_no_input::test_cookiecutter_no_input_return_project_dir` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_no_input::test_cookiecutter_no_input_extra_context` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_no_input::test_cookiecutter_templated_context` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_no_input::test_cookiecutter_no_input_return_rendered_file` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_no_input::test_cookiecutter_dict_values_in_context` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_no_input::test_cookiecutter_template_cleanup` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_with_input::test_cookiecutter_local_with_input` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_local_with_input::test_cookiecutter_input_extra_context` | system_e2e | Public Interfaces | covered | end-to-end generation workflow through CLI or top-level API |
| `test_cookiecutter_nested_templates::test_cookiecutter_nested_templates` | integration | Public Interfaces + `cookiecutter.extensions.JsonifyExtension` + `cookiecutter.extensions.RandomStringExtension` + `cookiecutter.extensions.SlugifyExtension` + `cookiecutter.extensions.TimeExtension` + `cookiecutter.extensions.UUIDExtension` | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_custom_extensions_in_hooks::test_hook_with_extension` | integration | Public Interfaces + Custom Extensions via `_extensions` | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_default_extensions::test_jinja2_time_extension` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_default_extensions::test_jinja2_slugify_extension` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_default_extensions::test_jinja2_uuid_extension` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_environment::test_env_should_raise_for_unknown_extension` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_environment::test_env_should_come_with_default_extensions` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_exceptions::test_undefined_variable_to_str` | atomic | Error Semantics + Exceptions | covered | single public behavior or bounded helper API |
| `test_find::test_find_template` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_generate_context` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_generate_context_with_json_decoding_error` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_context::test_default_context_replacement_in_generate_context` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_generate_context_decodes_non_ascii_chars` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_does_include_unused_variables` | atomic | Public Interfaces + Dictionary Variables | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_sets_non_list_value` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_does_not_modify_choices_for_invalid_overwrite` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_invalid_overwrite` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_sets_multichoice_values` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_invalid_multichoice_values` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_error_additional_values` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_in_dictionaries` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_sets_default_for_choice_variable` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_in_nested_dict` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrite_context_as_in_nested_dict_with_additional_values` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_in_nested_dict_additional_values` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_overwrite_value_as_boolean_string` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_generate_context::test_apply_overwrites_error_overwrite_value_as_boolean_string` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_copy_without_render::test_generate_copy_without_render_extensions` | integration | Cross-View Invariants | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_copy_without_render_override::test_generate_copy_without_render_extensions` | integration | Cross-View Invariants | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_file::test_generate_file` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_jsonify_filter` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_random_ascii_string` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_with_true_condition` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_with_false_condition` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_verbose_template_syntax_error` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_does_not_translate_lf_newlines_to_crlf` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_does_not_translate_crlf_newlines_to_lf` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_file::test_generate_file_handles_mixed_line_endings` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_generate_files::test_generate_files_nontemplated_exception` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_linux_newline` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_jinja2_environment` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_trailing_newline_forced_to_linux_by_context` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_windows_newline` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_windows_newline_forced_to_linux_by_context` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_binaries` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_absolute_path` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_output_dir` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_permissions` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_overwrite_if_exists_with_skip_if_file_exists` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_skip_if_file_exists` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_generate_files_with_overwrite_if_exists` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_undefined_variable_file_name` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_undefined_variable_file_name_existing_project` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_undefined_variable_file_content` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_undefined_variable_dir_name` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_keep_project_dir_on_failure` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_undefined_variable_dir_name_existing_project` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_undefined_variable_project_dir` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_files::test_raise_empty_dir_name` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_ignore_hooks_dirs` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_run_python_hooks` | integration | Public Interfaces + Python API | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_run_python_hooks_cwd` | integration | Public Interfaces + Python API | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_empty_hooks` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_oserror_hooks` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_run_failing_hook_removes_output_directory` | integration | Error Semantics + Template Directories and Archives + Zip Archives + Password-Protected Zip Files | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_run_failing_hook_preserves_existing_output_directory` | integration | Error Semantics + Template Directories and Archives + Zip Archives + Password-Protected Zip Files | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_run_shell_hooks` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_run_shell_hooks_win` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_ignore_shell_hooks` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_generate_hooks::test_deprecate_run_hook_from_repo_dir` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_get_config::test_get_config_does_not_exist` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_get_config::test_invalid_config` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_get_config::test_get_config_empty_config_file` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_get_config::test_get_config_invalid_file_with_array_as_top_level_element` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_get_config::test_get_config_invalid_file_with_multiple_docs` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_get_user_config_valid` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_get_user_config_invalid` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_get_user_config_nonexistent` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_specify_config_path` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_default_config_path` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_force_default_config` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_expand_user_for_directories_in_config` | atomic | Public Interfaces + User Configuration | covered | single public behavior or bounded helper API |
| `test_get_user_config::test_specify_config_values` | atomic | Public Interfaces + User Configuration | covered | single public behavior or bounded helper API |
| `test_hooks::test_ignore_hook_backup_files` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestFindHooks.test_find_hook` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestFindHooks.test_no_hooks` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestFindHooks.test_unknown_hooks_dir` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestFindHooks.test_hook_not_found` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_script` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_failing_script` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_failing_script_enoexec` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_script_cwd` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_script_with_context` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_hook` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_hooks::TestExternalHooks.test_run_failing_hook` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_log::test_info_stdout_logging` | atomic | Public Interfaces + Logging | covered | single public behavior or bounded helper API |
| `test_log::test_debug_stdout_logging` | atomic | Public Interfaces + Logging | covered | single public behavior or bounded helper API |
| `test_log::test_debug_file_logging` | atomic | Public Interfaces + Logging | covered | single public behavior or bounded helper API |
| `test_main::test_original_cookiecutter_options_preserved_in__cookiecutter` | system_e2e | Public Interfaces + `--directory` Option | covered | end-to-end generation workflow through CLI or top-level API |
| `test_main::test_replay_dump_template_name` | system_e2e | Cross-View Invariants + Replay | covered | end-to-end generation workflow through CLI or top-level API |
| `test_main::test_replay_load_template_name` | system_e2e | Cross-View Invariants + Replay | covered | end-to-end generation workflow through CLI or top-level API |
| `test_main::test_custom_replay_file` | system_e2e | Public Interfaces + Replay | covered | end-to-end generation workflow through CLI or top-level API |
| `test_output_folder::test_output_folder` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_output_folder::test_exception_when_output_folder_exists` | integration | Error Semantics | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_pre_prompt_hooks::test_run_pre_prompt_python_hook` | integration | Public Interfaces + Python API | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_pre_prompt_hooks::test_run_pre_prompt_shell_hook` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_prompt::test_undefined_variable` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_cookiecutter_nested_templates` | atomic | Public Interfaces + `templates` Key (Nested Config, v2.5+) + `template` Key (Nested Config, v2.2 Old Format) | covered | single public behavior or bounded helper API |
| `test_prompt::test_cookiecutter_nested_templates_invalid_paths` | atomic | Error Semantics + `templates` Key (Nested Config, v2.5+) + `template` Key (Nested Config, v2.2 Old Format) | covered | single public behavior or bounded helper API |
| `test_prompt::test_cookiecutter_nested_templates_invalid_win_paths` | atomic | Error Semantics + Template Structure + `templates` Key (Nested Config, v2.5+) + `template` Key (Nested Config, v2.2 Old Format) | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_ask_and_rm_repo_dir` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_ask_and_exit_on_user_no_answer` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_ask_and_rm_repo_file` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_ask_and_keep_repo_on_no_reuse` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_ask_and_keep_repo_on_reuse` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_not_ask_if_no_input_and_rm_repo_dir` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::test_prompt_should_not_ask_if_no_input_and_rm_repo_file` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::TestRenderVariable.test_convert_to_str` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_prompt::TestRenderVariable.test_convert_to_str_complex_variables` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_prompt_for_config` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_prompt_for_config_with_human_prompts` | atomic | Public Interfaces + `__prompts__` Key | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_prompt_for_config_with_human_choices` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_prompt_for_config_dict` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_should_render_dict` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_should_render_deep_dict` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_should_render_deep_dict_with_human_prompts` | atomic | Public Interfaces + `__prompts__` Key | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_internal_use_no_human_prompts` | atomic | Public Interfaces + `__prompts__` Key | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_prompt_for_templated_config` | atomic | Public Interfaces + Template Structure | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_dont_prompt_for_private_context_var` | atomic | Public Interfaces + Private Variables (Single Underscore Prefix) + Private Rendered Variables (Double Underscore Prefix) | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_should_render_private_variables_with_two_underscores` | atomic | Public Interfaces + String Variables + Private Variables (Single Underscore Prefix) + Private Rendered Variables (Double Underscore Prefix) | covered | single public behavior or bounded helper API |
| `test_prompt::TestPrompt.test_should_not_render_private_variables` | atomic | Public Interfaces + String Variables + Boolean Variables + Private Variables (Single Underscore Prefix) + Private Rendered Variables (Double Underscore Prefix) | covered | single public behavior or bounded helper API |
| `test_prompt::TestReadUserChoice.test_should_invoke_read_user_choice` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_prompt::TestReadUserChoice.test_should_invoke_read_user_variable` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_prompt::TestReadUserChoice.test_should_render_choices` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_prompt::TestPromptChoiceForConfig.test_should_return_first_option_if_no_input` | atomic | Public Interfaces + `--directory` Option | covered | single public behavior or bounded helper API |
| `test_prompt::TestPromptChoiceForConfig.test_should_read_user_choice` | atomic | Public Interfaces + User Configuration | covered | single public behavior or bounded helper API |
| `test_prompt::TestPromptChoiceForConfig.test_empty_list_returns_empty_string` | atomic | Cross-View Invariants + String Variables + Choice Variables + Boolean Variables | covered | single public behavior or bounded helper API |
| `test_prompt::TestReadUserYesNo.test_should_invoke_read_user_yes_no` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_prompt::TestReadUserYesNo.test_boolean_parameter_no_input` | atomic | Cross-View Invariants + Boolean Variables | covered | single public behavior or bounded helper API |
| `test_read_repo_password::test_click_invocation` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_read_user_choice::test_click_invocation` | atomic | Public Interfaces + CLI + Choice Variables | covered | single public behavior or bounded helper API |
| `test_read_user_choice::test_raise_if_options_is_not_a_non_empty_list` | atomic | Error Semantics + Choice Variables + `--directory` Option | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_process_json_invalid_json` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_process_json_non_dict` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_process_json_valid_json` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_process_json_deep_dict` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_should_raise_type_error` | atomic | Error Semantics | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_should_call_prompt_with_process_json` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_should_not_load_json_from_sentinel` | atomic | Cross-View Invariants | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_read_user_dict_default_value` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_read_user_dict::test_json_prompt_process_response` | atomic | Public Interfaces + cookiecutter.json Variable Types | covered | single public behavior or bounded helper API |
| `test_read_user_variable::test_click_invocation` | atomic | Public Interfaces + CLI + cookiecutter.json Variable Types | covered | single public behavior or bounded helper API |
| `test_read_user_variable::test_input_loop_with_null_default_value` | atomic | Public Interfaces + cookiecutter.json Variable Types + Templated Default Values | covered | single public behavior or bounded helper API |
| `test_read_user_yes_no::test_click_invocation` | atomic | Public Interfaces + CLI | covered | single public behavior or bounded helper API |
| `test_read_user_yes_no::test_yesno_prompt_process_response` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_repo_not_found::test_should_raise_error_if_repo_does_not_exist` | atomic | Error Semantics + Exceptions | covered | single public behavior or bounded helper API |
| `test_specify_output_dir::test_api_invocation` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_specify_output_dir::test_default_output_dir` | integration | Public Interfaces + Templated Default Values + Built-in Template Extensions | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_templates::test_build_templates` | integration | Public Interfaces + Template Structure + Built-in Template Extensions | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_tz_is_required` | integration | Cross-View Invariants | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_utc_default_datetime_format` | integration | Public Interfaces + Templated Default Values + Built-in Template Extensions | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_accept_valid_timezones` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_environment_datetime_format` | integration | Public Interfaces | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_add_time` | integration | Public Interfaces + `_copy_without_render` Key + `_extensions` Key + Context Building Pipeline + Rendering and File Generation + Hooks + Local Extensions | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_substract_time` | integration | Cross-View Invariants + Dictionary Variables + `_copy_without_render` Key + `_extensions` Key + Context Building Pipeline + Rendering and File Generation + Hooks + `cookiecutter.extensions.JsonifyExtension` + `cookiecutter.extensions.RandomStringExtension` + `cookiecutter.extensions.SlugifyExtension` + `cookiecutter.extensions.TimeExtension` + `cookiecutter.extensions.UUIDExtension` + Custom Extensions via `_extensions` + Local Extensions | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_time_extension::test_offset_with_format` | integration | Public Interfaces + Dictionary Variables + `_copy_without_render` Key + `_extensions` Key + Context Building Pipeline + Rendering and File Generation + Hooks + Password-Protected Zip Files + `cookiecutter.extensions.JsonifyExtension` + `cookiecutter.extensions.RandomStringExtension` + `cookiecutter.extensions.SlugifyExtension` + `cookiecutter.extensions.TimeExtension` + `cookiecutter.extensions.UUIDExtension` + Custom Extensions via `_extensions` + Local Extensions | covered | combines context, rendering, files, hooks, extensions, or output policy |
| `test_utils::test_force_delete` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_utils::test_rmtree` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_utils::test_make_sure_path_exists` | atomic | Public Interfaces | covered | single public behavior or bounded helper API |
| `test_utils::test_make_sure_path_exists_correctly_handle_os_error` | atomic | Error Semantics + Exceptions | covered | single public behavior or bounded helper API |
| `test_utils::test_work_in` | atomic | Public Interfaces + Public Modules | covered | single public behavior or bounded helper API |
| `test_utils::test_work_in_without_path` | atomic | Public Interfaces + Public Modules | covered | single public behavior or bounded helper API |
| `test_utils::test_create_tmp_repo_dir` | atomic | Public Interfaces + Public Modules | covered | single public behavior or bounded helper API |

Total: 222 | kept (covered): 213 | spec_gap: 0 | source-only: 0 | excluded: 9 | final scoreable: 213
