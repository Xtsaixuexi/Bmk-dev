# Spec Test Map

filter/oracle_source: upstream_only

| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `tests/loader_sample.py::task_xxx1` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/loader_sample.py::task_yyy2` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/loader_sample.py::bad_seed` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/module_with_tasks.py::task_xxx1` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/module_with_tasks.py::blabla` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::get_abspath` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::remove_all_db` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::tasks_sample` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::tasks_bad_sample` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::CmdFactory` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::DepManagerMixin::setUp` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::DepManagerMixin::tearDown` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::DepfileNameMixin::setUp` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::DepfileNameMixin::tearDown` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::DependencyFileMixin::setUp` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::DependencyFileMixin::tearDown` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::RestoreCwdMixin::setUp` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/support.py::RestoreCwdMixin::tearDown` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test___init__.py::TestGetInitialWorkdir::test_get_initial_workdir` | atomic | Top-Level API | covered | upstream public behavior mapped to spec |
| `tests/test___main__.py::TestMain::test_execute` | system_e2e | Installable Surface | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_env` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_error` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_failure` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_repr` | atomic | - | source-only | repr format is source-only |
| `tests/test_action.py::TestCmdAction::test_result` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_str` | atomic | - | source-only | exact action string formatting is source-only |
| `tests/test_action.py::TestCmdAction::test_success` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_success_noshell` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdAction::test_unicode` | atomic | - | source-only | exact action string formatting is source-only |
| `tests/test_action.py::TestCmdAction::test_values` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdActionParams::test_changePath` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdActionParams::test_invalid_param_stdout` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdActionParams::test_noPathSet` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdVerbosity::test_captureStderr` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdVerbosity::test_captureStdout` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdVerbosity::test_noCaptureStderr` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdVerbosity::test_noCaptureStdout` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestTaskIOCapture::test_cmd_io_capture_no` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestTaskIOCapture::test_cmd_io_capture_yes` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestTaskIOCapture::test_py_io_capture_no` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestTaskIOCapture::test_py_io_capture_yes` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_callable_invalid` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_callable_return_command_str` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_callable_tuple_return_command_str` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_list_can_contain_path` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_list_should_contain_strings_or_paths` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_string_list_cant_be_expanded` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_task_meta_reference` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_task_options` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_task_pos_arg` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdExpandAction::test_task_pos_arg_None` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdActionStringFormatting::test_both` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdActionStringFormatting::test_new` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmdActionStringFormatting::test_old` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCmd_print_process_output_line::test_line_buffered_output` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_non_unicode_string_error_replace` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_non_unicode_string_error_strict` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_non_unicode_string_ok` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_unbuffered_env` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_unbuffered_output` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_unicode_string` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmd_print_process_output_line::test_unicode_string2` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestCmdSaveOuput::test_success` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestWriter::test_fileno` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestWriter::test_fileno_not_supported` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestWriter::test_isatty_false` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestWriter::test_isatty_true` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestWriter::test_write` | atomic | - | source-only | helper stream/private output reader behavior is not public API contract |
| `tests/test_action.py::TestPythonAction::test_callable_obj` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_error_exception` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_error_object` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_error_taskerror` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_error_taskfail` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_fail_bool` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_functionParameters` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_action.py::TestPythonAction::test_functionParametersArgs` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_action.py::TestPythonAction::test_functionParametersFail` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_action.py::TestPythonAction::test_functionParametersKwargs` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_action.py::TestPythonAction::test_init` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_action.py::TestPythonAction::test_init_callable_builtin` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_init_callable_class` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_repr` | atomic | - | source-only | repr format is source-only |
| `tests/test_action.py::TestPythonAction::test_result` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_result_dict` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_str` | atomic | - | source-only | exact action string formatting is source-only |
| `tests/test_action.py::TestPythonAction::test_success_None` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_success_bool` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_success_dict` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_success_str` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonAction::test_values` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonVerbosity::test_captureStderr` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonVerbosity::test_captureStdout` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonVerbosity::test_noCaptureStderr` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonVerbosity::test_noCaptureStdout` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonVerbosity::test_redirectStderr` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonVerbosity::test_redirectStdout` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_action_modifies_task_but_not_attrs` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_callable_obj` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_extra_arg_overwritten` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_extra_kwarg_overwritten` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_keyword_extra_args` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_kwonlyargs_full` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_kwonlyargs_minimal` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_meta_arg_default_disallowed` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_method` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_mixed_args` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_named_extra_args` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_no_extra_args` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_option_default_allowed` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_task_options` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestPythonActionPrepareKwargsMeta::test_task_pos_arg` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testBaseAction` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testInvalidActionNone` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testInvalidActionObject` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testListStringAction` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testMethodAction` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testStringAction` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testTupleAction` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::testTupleActionMoreThanThreeElements` | atomic | Actions | covered | upstream public behavior mapped to spec |
| `tests/test_action.py::TestCreateAction::test_invalid_action_task_param_name` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_api.py::TestRun::test_run` | integration | Embedded Execution API | covered | upstream public behavior mapped to spec |
| `tests/test_api.py::TestRunTasks::test_run_tasks_error` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_api.py::TestRunTasks::test_run_tasks_pos` | integration | Embedded Execution API | covered | upstream public behavior mapped to spec |
| `tests/test_api.py::TestRunTasks::test_run_tasks_success` | integration | Embedded Execution API | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestVersionTuple::test_version_tuple` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCommand::test_call_value_cmd_line_arg` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCommand::test_call_value_option_default` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCommand::test_call_value_overwritten_default` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCommand::test_configure` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCommand::test_failCall` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCommand::test_help` | atomic | - | source-only | exact help text is non-goal |
| `tests/test_cmd_base.py::TestModuleTaskLoader::test_load_tasks_from_dict` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestModuleTaskLoader::test_load_tasks_from_module` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestModuleTaskLoader::test_task_config` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestModuleTaskLoader::test_task_opt_from_api_to_action` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestModuleTaskLoader::test_task_opt_from_api_to_creator` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDodoTaskLoader::test_load_tasks` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::testCustomChecker` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::testCustomCodec` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::testInvalidChecker` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::testPluginBackend` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_cmd_base.py::TestDoitCmdBase::testPluginLoader` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_cmd_base.py::TestDoitCmdBase::test_execute` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::test_execute_provides_dep_manager` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::test_minversion` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestDoitCmdBase::test_new_cmd` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestForceVerbosity::test_force_verbosity` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCheckTasksExist::test_None` | atomic | - | excluded | dummy gate passed this nodeid; insufficient behavioral signal |
| `tests/test_cmd_base.py::TestCheckTasksExist::test_invalid` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestCheckTasksExist::test_valid` | atomic | - | excluded | dummy gate passed this nodeid; insufficient behavioral signal |
| `tests/test_cmd_base.py::TestTaskAndDepsIter::test_dep_iter` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_base.py::TestSubtaskIter::test_sub_iter` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_all` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_all_ignores_default` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_default` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_default_all` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_forget_selected` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_forget_taskdep` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_invalid_task` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_selected` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_selected_wildcard` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_subtasks` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_taskdep` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_taskdep_once` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_clean.py::TestCmdClean::test_clean_taskdep_recursive` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_completion.py::TestInvalidShell::test_invalid_shell_option` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionBash::test_cmd_takes_file_args` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionBash::test_no_dodo__hardcoded_tasks` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionBash::test_with_dodo__dynamic_tasks` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionZsh::test_cmd_arg_list` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionZsh::test_cmds_with_params` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionZsh::test_hardcoded_tasks` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_completion.py::TestCmdCompletionZsh::test_zsh_arg_line` | atomic | - | excluded | shell completion exact script text is a non-goal |
| `tests/test_cmd_dumpdb.py::TestCmdDumpDB::testDefault` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testDisableDefault` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testDontForgetTaskDependency` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testForgetAll` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testForgetDefault` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testForgetGroup` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testForgetInvalid` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testForgetOne` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_forget.py::TestCmdForget::testForgetTaskDependency` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_help.py::TestHelp::test_help_cmd` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelp::test_help_plugin_name` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelp::test_help_task_params` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelp::test_help_usage` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelp::test_help_usage_custom_name` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelpWithLoader::test_help_no_dodo_file` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelpWithLoader::test_help_task_name` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_help.py::TestHelpWithLoader::test_help_wrong_name` | atomic | - | excluded | exact help text and task-help formatting are non-goals |
| `tests/test_cmd_ignore.py::TestCmdIgnore::testDontIgnoreTaskDependency` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_ignore.py::TestCmdIgnore::testIgnoreAll` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_ignore.py::TestCmdIgnore::testIgnoreGroup` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_ignore.py::TestCmdIgnore::testIgnoreInvalid` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_ignore.py::TestCmdIgnore::testIgnoreOne` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_info.py::TestCmdInfo::test_info_basic_attrs` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_info.py::TestCmdInfo::test_invalid_command_args` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_info.py::TestCmdInfoStatus::test_execute_status_run` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_info.py::TestCmdInfoStatus::test_execute_status_uptodate` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_info.py::TestCmdInfoStatus::test_hide_execute_status` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_info.py::TestGetReasons::test_get_reasons_str` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testCustomTemplate` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testDependencies` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testDoc` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testFilter` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testFilterAll` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testFilterSubtask` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testListInvalidTask` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testNoPrivate` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testQuiet` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testSortByDefinition` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testSortByName` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testSubTask` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdList::testWithPrivate` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdListWithDeps::testErrorStatus` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdListWithDeps::testStatus` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdListWithDeps::testStatus_result_dep_bug_gh44` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_list.py::TestCmdListWithDeps::test_unicode_name` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_execute` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_file_dep` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_file_dep_change_checker` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_file_dep_up_to_date` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_filter` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_invalid_task` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_missing_dep_and_target` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_missing_file_dep` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_resetdep.py::TestCmdResetDep::test_values_and_results` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testInvalidParType` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testMP_not_available` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRun` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunEmptyFilter` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunFilter` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunMP` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunMThread` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunSingle` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunSingleSubtasks` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRun::testProcessRunSingleWithArgs` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRunReporter::testCustomReporter` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRunReporter::testPluginReporter` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRunReporter::testReporterInstance` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_run.py::TestCmdRunOptions::test_outfile` | atomic | - | excluded | direct command internals or exact command transcript/storage assertions |
| `tests/test_cmd_strace.py::TestCmdStrace::test_dep` | atomic | - | excluded | platform-specific strace details are non-goals |
| `tests/test_cmd_strace.py::TestCmdStrace::test_ignore_python_actions` | atomic | - | excluded | platform-specific strace details are non-goals |
| `tests/test_cmd_strace.py::TestCmdStrace::test_invalid_command_args` | atomic | - | excluded | platform-specific strace details are non-goals |
| `tests/test_cmd_strace.py::TestCmdStrace::test_opt_keep_trace` | atomic | - | excluded | platform-specific strace details are non-goals |
| `tests/test_cmd_strace.py::TestCmdStrace::test_opt_show_all` | atomic | - | excluded | platform-specific strace details are non-goals |
| `tests/test_cmd_strace.py::TestCmdStrace::test_target` | atomic | - | excluded | platform-specific strace details are non-goals |
| `tests/test_cmdparse.py::TestDefaultUpdate::test` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestDefaultUpdate::test_add_defaults` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestDefaultUpdate::test_pickle` | atomic | - | source-only | pickle/internal serialization shape is source-only |
| `tests/test_cmdparse.py::TestCmdOption::test_invalid_field` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption::test_missing_field` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption::test_non_required_fields` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption::test_repr` | atomic | - | source-only | repr format is source-only |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_bool` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_int` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_invalid_value` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_list` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_non_string_values_are_not_converted` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_str` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_str2val::test_str2boolean` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCmdOption_help_param::test_bool_param` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_param::test_metavar` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_param::test_no_long` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_param::test_non_bool_param` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_doc::test_choices_desc_doc` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_doc::test_choices_nodesc_doc` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_doc::test_name_config_env` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_doc::test_no_doc_param` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCmdOption_help_doc::test_param` | atomic | - | source-only | exact help formatting is non-goal |
| `tests/test_cmdparse.py::TestCommand::test_contains` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_env_val` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_env_val_bool` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_getOption` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_getitem` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_long` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_option_list` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_overwrite_defaults` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_overwrite_defaults_convert_type` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parseDefaults` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parseError` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parseLongValues` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parsePositionalArgs` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parseShortValues` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parseWrongChoice` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_parseWrongType` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_cmdparse.py::TestCommand::test_short` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_control.py::TestTaskControlInit::test_addInvalidTask` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_addTask` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_addTaskSameName` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_bug770150_task_dependency_from_target` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_sameTarget` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_targetDependency` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_userErrorSetupTask` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_userErrorTaskDependency` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlInit::test_wild` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilter` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilterEmptyList` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilterPattern` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilterSubtask` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilterTarget` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilterWrongName` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testFilterWrongSubtaskName` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testOptions` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testPosParam` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testProcessAll` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::testProcessSelection` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::test_filter_delayed_multi_select` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::test_filter_delayed_regex_auto` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::test_filter_delayed_regex_multiple_match` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::test_filter_delayed_regex_single` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskControlCmdOptions::test_filter_delayed_subtask` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestExecNode::test_parent_status_failure` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestExecNode::test_parent_status_ignore` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestExecNode::test_ready_select__not_waiting` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestExecNode::test_repr` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestExecNode::test_step` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestDecoratorNoNone::test_filtering` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_GenNone::test_already_created` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_GenNone::test_create` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_GenNone::test_cyclic` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_node_add_wait_run::test_calc_dep_already_executed` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_node_add_wait_run::test_deps_not_ok` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_node_add_wait_run::test_none` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_node_add_wait_run::test_wait` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_calc_dep` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_calc_dep_already_executed` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_delayed_creation` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_delayed_creation_sub_task` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_delayed_creation_target_regex` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_no_deps` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_regex_group_already_created` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_regex_not_found` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_setup_task__run` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_task_deps` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_task_deps_already_created` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_add_task::test_task_deps_no_wait` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_get_next_node::test_none` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_get_next_node::test_ready` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_get_next_node::test_to_run` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_get_next_node::test_to_run_none` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_update_waiting::test_wait_run` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_update_waiting::test_wait_run_deps_not_ok` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_update_waiting::test_wait_select` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_update_waiting::test_waiting_node_updated` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_dispatcher_generator::test_delayed_creation` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_control.py::TestTaskDispatcher_dispatcher_generator::test_normal` | atomic | - | excluded | internal dispatcher/control graph API not in candidate-visible spec |
| `tests/test_dependency.py::TestUtilFunctions::test_md5` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestUtilFunctions::test_sqlite_import` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestUtilFunctions::test_unicode_md5` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_corrupted_file` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_corrupted_file_unrecognized_excep` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_dump` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_getNonExistent` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_get_set` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_get_set_unicode_name` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_in` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_remove` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_remove_all` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbJson::test_remove_from_non_empty_file` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_corrupted_file` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_corrupted_file_unrecognized_excep` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_dump` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_getNonExistent` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_get_set` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_get_set_unicode_name` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_in` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_remove` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_remove_all` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbSqlite::test_remove_from_non_empty_file` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_corrupted_file` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_corrupted_file_unrecognized_excep` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_dump` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_getNonExistent` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_get_set` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_get_set_unicode_name` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_in` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_remove` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_remove_all` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmGnu::test_remove_from_non_empty_file` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_corrupted_file` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_corrupted_file_unrecognized_excep` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_dump` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_getNonExistent` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_get_set` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_get_set_unicode_name` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_in` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_remove` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_remove_all` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmNdbm::test_remove_from_non_empty_file` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_corrupted_file` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_corrupted_file_unrecognized_excep` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_dump` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_getNonExistent` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_get_set` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_get_set_unicode_name` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_in` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_remove` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_remove_all` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyDbDbmDumb::test_remove_from_non_empty_file` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_file_md5` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_files` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_resultNone` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_result_dict` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_result_hash` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_skip` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessJson::test_save_values` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_file_md5` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_files` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_resultNone` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_result_dict` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_result_hash` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_skip` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessSqlite::test_save_values` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_file_md5` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_files` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_result` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_resultNone` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_result_dict` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_result_hash` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_skip` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmGnu::test_save_values` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_file_md5` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_files` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_result` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_resultNone` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_result_dict` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_result_hash` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_skip` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmNdbm::test_save_values` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_file_md5` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_files` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_resultNone` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_result_dict` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_result_hash` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_skip` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestSaveSuccessDbmDumb::test_save_values` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueJson::test_all_values` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueJson::test_invalid_key` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueJson::test_invalid_taskid` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueJson::test_ok` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueJson::test_ok_dot_on_task_name` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueSqlite::test_all_values` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueSqlite::test_invalid_key` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueSqlite::test_invalid_taskid` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueSqlite::test_ok` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueSqlite::test_ok_dot_on_task_name` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueDbmGnu::test_all_values` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmGnu::test_invalid_key` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmGnu::test_invalid_taskid` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmGnu::test_ok` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmGnu::test_ok_dot_on_task_name` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmNdbm::test_all_values` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmNdbm::test_invalid_key` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmNdbm::test_invalid_taskid` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmNdbm::test_ok` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmNdbm::test_ok_dot_on_task_name` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetValueDbmDumb::test_all_values` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueDbmDumb::test_invalid_key` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueDbmDumb::test_invalid_taskid` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueDbmDumb::test_ok` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetValueDbmDumb::test_ok_dot_on_task_name` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestRemoveSuccessJson::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestRemoveSuccessSqlite::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestRemoveSuccessDbmGnu::test_save_result` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestRemoveSuccessDbmNdbm::test_save_result` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestRemoveSuccessDbmDumb::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestIgnoreJson::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestIgnoreSqlite::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestIgnoreDbmGnu::test_save_result` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestIgnoreDbmNdbm::test_save_result` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestIgnoreDbmDumb::test_save_result` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestMD5Checker::test_md5` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestMD5Checker::test_size` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestMD5Checker::test_timestamp` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestCustomChecker::test_not_implemented` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestTimestampChecker::test_timestamp` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyStatus::test_add_reason` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyStatus::test_add_reason_error` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyStatus::test_get_error_message` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyStatus::test_no_log` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestDependencyStatus::test_set_reason` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateCallable_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateCallable_added_attributes` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateCommand_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateCommand_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateFalse` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateFunction_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateFunction_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateFunction_extra_args_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateFunction_without_args_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateMethod_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateNone` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_UptodateTrue` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_change_checker` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_fileDependencies` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_fileDependencies_changed` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_fileDependencies_changed_get_log` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_file_dependency_not_exist` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_ignore` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_noDependency` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_targetFolder` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_targets` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_targets_notThere` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusJson::test_uptodate_call_all_even_if_some_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateCallable_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateCallable_added_attributes` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateCommand_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateCommand_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateFalse` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateFunction_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateFunction_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateFunction_extra_args_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateFunction_without_args_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateMethod_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateNone` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_UptodateTrue` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_change_checker` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_fileDependencies` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_fileDependencies_changed` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_fileDependencies_changed_get_log` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_file_dependency_not_exist` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_ignore` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_noDependency` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_targetFolder` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_targets` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_targets_notThere` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusSqlite::test_uptodate_call_all_even_if_some_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateCallable_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateCallable_added_attributes` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateCommand_False` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateCommand_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateFalse` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateFunction_False` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateFunction_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateFunction_extra_args_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateFunction_without_args_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateMethod_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateNone` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_UptodateTrue` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_change_checker` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_fileDependencies` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_fileDependencies_changed` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_fileDependencies_changed_get_log` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_file_dependency_not_exist` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_ignore` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_noDependency` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_targetFolder` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_targets` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_targets_notThere` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmGnu::test_uptodate_call_all_even_if_some_False` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateCallable_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateCallable_added_attributes` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateCommand_False` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateCommand_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateFalse` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateFunction_False` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateFunction_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateFunction_extra_args_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateFunction_without_args_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateMethod_True` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateNone` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_UptodateTrue` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_change_checker` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_fileDependencies` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_fileDependencies_changed` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_fileDependencies_changed_get_log` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_file_dependency_not_exist` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_ignore` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_noDependency` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_targetFolder` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_targets` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_targets_notThere` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmNdbm::test_uptodate_call_all_even_if_some_False` | atomic | - | excluded | reference run skipped this nodeid due optional/platform backend availability |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateCallable_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateCallable_added_attributes` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateCommand_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateCommand_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateFalse` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateFunction_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateFunction_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateFunction_extra_args_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateFunction_without_args_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateMethod_True` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateNone` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_UptodateTrue` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_change_checker` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_fileDependencies` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_fileDependencies_changed` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_fileDependencies_changed_get_log` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_file_dependency_not_exist` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_ignore` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_noDependency` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_targetFolder` | atomic | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_targets` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_targets_notThere` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_dependency.py::TestGetStatusDbmDumb::test_uptodate_call_all_even_if_some_False` | integration | Dependency State | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_cmdline_loader_option_before_cmd_name` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_cmdline_loader_option_mixed` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_cmdline_novars` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_doit_cmd.py::TestRun::test_cmdline_vars` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_cmdline_vars_not_opts` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_run_is_default` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_run_other_subcommand` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_task_loader_has_cmd_list` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRun::test_usage` | atomic | - | source-only | exact usage/help text is non-goal |
| `tests/test_doit_cmd.py::TestRun::test_version` | integration | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestRunExtraConfig::test_extra_config` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestErrors::test_internal_error` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestErrors::test_interrupt` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestErrors::test_user_error` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_doit_cmd.py::TestConfig::test_execute_command_plugin` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_doit_cmd.py::TestConfig::test_find_pyproject_toml_config` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_doit_cmd.py::TestConfig::test_load_plugins_command` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_doit_cmd.py::TestConfig::test_merge_api_ini_config` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_doit_cmd.py::TestConfig::test_merge_api_toml_config` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_doit_cmd.py::TestConfig::test_no_ini_config_file` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_exceptions.py::TestInvalidCommand::test_custom_binary_name` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestInvalidCommand::test_just_string` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestInvalidCommand::test_param_not_found` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestInvalidCommand::test_task_not_found` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestBaseFail::test_caught` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestBaseFail::test_exception` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestBaseFail::test_msg_notraceback` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestBaseFail::test_name` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_exceptions.py::TestAllCaught::test` | atomic | - | excluded | exact exception string/repr wording is non-goal |
| `tests/test_loader.py::TestFlatGenerator::test_nested` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGetModule::testAbsolutePath` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGetModule::testInParentDir` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGetModule::testInvalidCwd` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGetModule::testRelativePath` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGetModule::testWrongFileName` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGetModule::testWrongFileNameInParentDir` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestLoadTasks::testCreateAfterDecorator` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestLoadTasks::testCreateAfterDecoratorOnMethod` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestLoadTasks::testCreateAfterDecoratorOnMethodWithParams` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testDocString` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testInitialLoadDelayedTask` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testInitialLoadDelayedTask_creates` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testInitialLoadDelayedTask_no_delayed` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testMetaInfo` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testNameInBlacklist` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestLoadTasks::testNormalCase` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testUse_create_doit_tasks` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestLoadTasks::testUse_create_doit_tasks_basename_kwargs` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testUse_create_doit_tasks_class_method` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestLoadTasks::testUse_object_methods` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_args` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_args_second` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_call_api` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_config` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_default` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_delayed` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_dup_param` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_method` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestTaskGeneratorParams::test_task_params_annotations` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestDodoConfig::testConfigDict_Ok` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestDodoConfig::testConfigType_Error` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestDodoConfig::testDefaultConfig_Dict` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTaskInvalid::testInvalidValue` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTaskNone::testEmpty` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksSingle::testBaseName` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksSingle::testDict` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksSingle::testDocstringNotUsed` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksSingle::testInvalidNameField` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksSingle::testTaskObj` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksSingle::testUseDocstring` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGenerator` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorBaseOnly` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorBasename` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorBasenameCanNotRepeat` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorBasenameCanNotRepeatNonGroup` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorBasenameName` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorDictMissingAction` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorDictMissingName` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorDocString` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorDoesntReturnDict` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorNameCanNotRepeat` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorReturnTaskObj` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testGeneratorWithNoTasks` | integration | Task Loading | covered | upstream public behavior mapped to spec |
| `tests/test_loader.py::TestGenerateTasksGenerator::testMultiLevelGenerator` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_plugin.py::TestPluginEntry::test_get` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_plugin.py::TestPluginEntry::test_load_error_module_not_found` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_plugin.py::TestPluginEntry::test_load_error_obj_not_found` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_plugin.py::TestPluginEntry::test_repr` | atomic | - | source-only | repr format is source-only |
| `tests/test_plugin.py::TestPluginDict::test_add_plugins_from_dict` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_plugin.py::TestPluginDict::test_add_plugins_from_pkg_resources` | atomic | Command, Loader, Parser, Plugin, and Reporter APIs | covered | upstream public behavior mapped to spec |
| `tests/test_plugin.py::TestPluginDict::test_get_plugin_actual_plugin` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_plugin.py::TestPluginDict::test_get_plugin_not_a_plugin` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_plugin.py::TestPluginDict::test_to_dict` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_reporter.py::TestConsoleReporter::test_addFailure` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_addSuccess` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_cleanupError` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_complete_run_verbosity0` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_complete_run_verbosity0_not_executed` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_complete_run_verbosity1` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_complete_run_verbosity2` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_complete_run_verbosity2_redisplay` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_executeGroupTask` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_executeHidden` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_executeTask` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_executeTask_unicode` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_failure_no_report` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_initialize` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_runtime_error` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_skipIgnore` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_skipUptodate` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_skipUptodate_hidden` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_startTask` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestConsoleReporter::test_teardownTask` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestExecutedOnlyReporter::test_skipIgnore` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestExecutedOnlyReporter::test_skipUptodate` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestZeroReporter::test_executeTask` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestZeroReporter::test_runtime_error` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestErrorOnlyReporter::test_error_report` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestErrorOnlyReporter::test_executeTask` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestErrorOnlyReporter::test_faile_no_report` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestTaskResult::test` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestJsonReporter::test_cleanup_error` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestJsonReporter::test_ignore_stdout` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestJsonReporter::test_normal` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_reporter.py::TestJsonReporter::test_runtime_error` | atomic | - | excluded | collected helper/non-test artifact, not a scoreable public behavior test |
| `tests/test_runner.py::TestRunner::testInit` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_DependencyError` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_alwaysExecute` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_getargs_dict` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_getargs_fail` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_getargs_group` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_getargs_group_value` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_getargs_ok` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_ignore` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_noSetup_ok` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_ready` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_upToDate` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunner_SelectTask::test_withSetup` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestTask_Teardown::test_errors` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestTask_Teardown::test_ok` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestTask_Teardown::test_reverse_order` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestTask_RunAll::test_reporter_runtime_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::testActionModifiesFiledep` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::testSystemExitRaises` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_continue` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_continue_dep_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_continue_dont_execute_parent_of_failed_task` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_continue_ignored_dep` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_dependency_error_after_execution` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_failureOutput` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_getargs` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_result` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_success` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_teardown` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_Runner::test_updateDependencies` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::testActionModifiesFiledep` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::testSystemExitRaises` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_continue` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_continue_dep_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_continue_dont_execute_parent_of_failed_task` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_continue_ignored_dep` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_failureOutput` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_getargs` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_result` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_success` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_teardown` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MThread::test_updateDependencies` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::testActionModifiesFiledep` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::testSystemExitRaises` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_continue` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_continue_dep_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_continue_dont_execute_parent_of_failed_task` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_continue_ignored_dep` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_error` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_failureOutput` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_getargs` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_result` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_success` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_teardown` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestRunnerRunTasks_MRunner::test_updateDependencies` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMReporter::testNonReporterMethod` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMReporter::testReporterMethod` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestJobTask::test_closure_is_picklable` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestJobTask::test_not_picklable_raises_InvalidTask` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunnerPickable::test_MRunner_pickable` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_get_next_job::test_delayed_loaded` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_get_next_job::test_run_task` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_get_next_job::test_stop_running` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_get_next_job::test_waiting` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_get_next_job::test_waiting_controller` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_start_process::test_all_processes` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_start_process::test_less_processes` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_start_process::test_waiting_process` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_parallel_run_tasks::test_task_cloudpicklabe_multiprocess` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_parallel_run_tasks::test_task_not_picklabe_thread` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_execute_task::test_full_task` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_execute_task::test_full_task_fail` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMRunner_execute_task::test_hold` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_runner.py::TestMThreadRunner_available::test_MThreadRunner_available` | atomic | - | excluded | internal runner scheduling API and private worker methods are implementation-shaped |
| `tests/test_task.py::TestStream::test_force_global` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestStream::test_from_task` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestStream::test_task_verbosity_not_specified` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCheckInput::testFailType` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCheckInput::testFailValue` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCheckInput::testOkType` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCheckInput::testOkTypeABC` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCheckInput::testOkValue` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCompare::test_equal` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskCompare::test_lt` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_dependencyNotSequence` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_dependencySequenceIsValid` | atomic | - | excluded | dummy gate passed this nodeid; insufficient behavioral signal |
| `tests/test_task.py::TestTaskInit::test_forbid_equal_sign_on_name` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_groupTask` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_options` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_options_from_cfg` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_options_from_cfg_override` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskInit::test_setup` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskValueSavers::test_execute_value_savers` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_FalseRunalways` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_NoneIgnored` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_callable_function` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_callable_instance_method` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_invalid` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_object_with_configure` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_str` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskUpToDate::test_tuple` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskExpandFileDep::test_dependencyStringIsFile` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskExpandFileDep::test_file_dep_path` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskExpandFileDep::test_file_dep_str` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskExpandFileDep::test_file_dep_unicode` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDeps::test_calc_dep` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDeps::test_task_dep` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDeps::test_update_deps` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskTargets::test_targets_can_be_path` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskTargets::test_targets_should_be_string_or_path` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTask_Loader::test_delayed_after_execution` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTask_Getargs::test_invalid_desc` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTask_Getargs::test_invalid_desc_tuple` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTask_Getargs::test_ok` | integration | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskTitle::test_custom_title` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskTitle::test_title` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskRepr::test_repr` | atomic | - | source-only | repr format is source-only |
| `tests/test_task.py::TestTaskActions::test_fail_first` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_fail_second` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_failure` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_many` | integration | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_mixed` | integration | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_result` | integration | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_success` | integration | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskActions::test_values` | integration | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskTeardown::test_fail` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskTeardown::test_ok` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskClean::test_clean_action_error` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskClean::test_clean_action_kwargs` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskClean::test_clean_actions` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_clean_any_order` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_clean_empty_dirs` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_clean_non_existent_targets` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskClean::test_clean_nothing` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_clean_targets` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_dryrun_actions_not_executed` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_dryrun_actions_with_param_false` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_dryrun_actions_with_param_true` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_dryrun_dir` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_dryrun_file` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskClean::test_keep_non_empty_dirs` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestTaskDoc::test_just_new_line` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDoc::test_multiple_lines` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDoc::test_no_doc` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDoc::test_single_line` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskDoc::test_start_with_empty_lines` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestTaskPickle::test_geststate` | atomic | - | source-only | pickle/internal serialization shape is source-only |
| `tests/test_task.py::TestTaskPickle::test_safedict` | atomic | - | source-only | pickle/internal serialization shape is source-only |
| `tests/test_task.py::TestTaskUpdateFromPickle::test_change_value` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_task.py::TestDictToTask::testDictFieldTypo` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestDictToTask::testDictMissingFieldAction` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestDictToTask::testDictOkMinimum` | atomic | Task Object API | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestResultDep::test_group` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_task.py::TestResultDep::test_single` | integration | Cross-View Invariants | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestCreateFolder::test_create_folder` | atomic | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestCreateFolder::test_error_if_path_is_a_file` | atomic | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestTitleWithActions::test_actions` | atomic | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestTitleWithActions::test_group` | atomic | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestRunOnce::test_run` | atomic | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestConfigChanged::test_dict` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestConfigChanged::test_invalid_type` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestConfigChanged::test_nested_dict` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestConfigChanged::test_string` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestConfigChanged::test_unicode` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestConfigChanged::test_using_custom_encoder` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestTimeout::test_int` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestTimeout::test_invalid` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestTimeout::test_timedelta` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestTimeout::test_timedelta_big` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestCheckTimestampUnchanged::test_file_missing` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_tools.py::TestCheckTimestampUnchanged::test_multiple_checks` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_tools.py::TestCheckTimestampUnchanged::test_op_bad_custom` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_tools.py::TestCheckTimestampUnchanged::test_op_ge` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestCheckTimestampUnchanged::test_time_selection` | atomic | - | excluded | accesses or calls private implementation state/methods |
| `tests/test_tools.py::TestLongRunning::test_ignore_keyboard_interrupt` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestLongRunning::test_success` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestInteractive::test_fail` | integration | Error Semantics | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestInteractive::test_success` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestPythonInteractiveAction::test_ignore_keyboard_interrupt` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestPythonInteractiveAction::test_returned_dict_saved_result_values` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestPythonInteractiveAction::test_returned_string_saved_result` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |
| `tests/test_tools.py::TestPythonInteractiveAction::test_success` | integration | Up-To-Date Helpers and Tools | covered | upstream public behavior mapped to spec |

Total: 909 | kept (covered): 438 | spec_gap: 0 | source-only: 35 | excluded: 436 | final scoreable: 438
