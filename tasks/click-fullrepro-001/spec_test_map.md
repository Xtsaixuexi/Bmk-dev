| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `tests/test_arguments.py::test_nargs_star` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_tup` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_tup_composite[opts0]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_tup_composite[opts1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_tup_composite[opts2]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_mismatch_with_tuple_type` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_err` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_bytes_args` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_file_args` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_path_allow_dash` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_file_atomics` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_stdout_default` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_envvar[2--None]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_envvar[2-a-Takes 2 values but 1 was given.]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_envvar[2-a b-expect2]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_nargs_envvar_only_if_values_empty` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_empty_nargs` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_missing_arg` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_required_argument[-False-]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_required_argument[  -False-  ]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_required_argument[foo-False-foo]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_implicit_non_required` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_argument_help` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_argument_help_options_only_no_arguments_section` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_argument_help_optional_metavar` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_deprecated_usage` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_argument_metavar_marks_optional[kwargs0-FOO]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_argument_metavar_marks_optional[kwargs1-FOO]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_argument_metavar_marks_optional[kwargs2-[FOO]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_arguments.py::test_deprecated_usage_help_record[True-(DEPRECATED)]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_basic_functionality` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_repr` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_return_values` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_basic_group` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_group_commands_dict` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_group_from_list` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_string_option[args0-S:[no value]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_string_option[args1-S:[42]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_string_option[args2-Error: Option '--s' requires an argument.]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_int_option[args0-I:[84]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_int_option[args1-I:[46]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_int_option[args2-Error: Invalid value for '--i': 'x' is not a valid integer.]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_uuid_option[args0-U:[ba122011-349f-423b-873b-9d6a79c688ab]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_uuid_option[args1-U:[821592c1-c50e-4971-9cd6-e89dc6832f86]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_uuid_option[args2-Error: Invalid value for '--u': 'x' is not a valid UUID.]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_float_option[args0-F:[42.0]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_float_option[--f=23.5-F:[23.5]]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_float_option[--f=x-Error: Invalid value for '--f': 'x' is not a valid float.]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_switch[args0-True-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_switch[args1-False-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_switch[args2-None-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_flag[True-args0-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_flag[True-args1-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_flag[False-args2-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_conversion[1-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_conversion[true-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_boolean_conversion[t-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_flag_value_dual_options[True-args0-upper]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_flag_value_dual_options[True-args1-lower]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_basic.py::test_flag_value_dual_options[False-args2-upper]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_basic_chaining` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_chaining_help[args0-COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_chaining_help[args1-ROOT HELP]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_chaining_help[args2-SDIST HELP]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_chaining_with_options` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_no_command_result_callback[False-1]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_no_command_result_callback[True-[]]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_chaining_with_arguments` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_pipeline[args0-foo\nbar-expect0]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_pipeline[args1-foo \n bar-expect1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_pipeline[args2-foo \n bar-expect2]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_args_and_chain` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_group_arg_behavior` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_chain.py::test_group_chaining` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_command_no_parens` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_custom_command_no_parens` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_group_no_parens` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_params_argument` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_generate_name[init_data]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_generate_name[init_data_command]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_command_decorators.py::test_generate_name[init_data_cmd]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_other_command_invoke` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_other_command_forward` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_forwarded_params_consistency` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_auto_shorthelp` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_command_no_args_is_help` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_default_maps` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_group_with_args[args0-2-Error: Missing command.]` | system_e2e | Error Semantics + Public API Behavior + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_group_with_args[args1-0-Show this message and exit.]` | system_e2e | Cross-View Invariants + Public API Behavior + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/test_commands.py::test_group_with_args[args2-0-obj=obj1\nmove\n]` | system_e2e | Cross-View Invariants + Public API Behavior + Representative Workflow | covered | reference-passing upstream behavior |

Total: 90 | kept (covered): 90 | spec_gap: 0 | source-only: 0 | excluded: 32609 | final scoreable: 90
