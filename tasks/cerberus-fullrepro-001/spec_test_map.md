# spec_test_map.md
> cerberus-fullrepro-001 Step 4 测试到 candidate-visible spec 的映射表。

| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `cerberus/tests/test_assorted.py::test_pkgresources_version` | atomic | - | source-only | version metadata, docstring/MRO, or test-helper self-test outside behavioral spec |
| `cerberus/tests/test_assorted.py::test_version_not_found` | atomic | - | source-only | version metadata, docstring/MRO, or test-helper self-test outside behavioral spec |
| `cerberus/tests/test_assorted.py::test_clear_cache` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_assorted.py::test_docstring` | atomic | - | source-only | version metadata, docstring/MRO, or test-helper self-test outside behavioral spec |
| `cerberus/tests/test_assorted.py::test_that_test_fails[assert_fail-document0]` | atomic | - | source-only | version metadata, docstring/MRO, or test-helper self-test outside behavioral spec |
| `cerberus/tests/test_assorted.py::test_that_test_fails[assert_success-document1]` | atomic | - | source-only | version metadata, docstring/MRO, or test-helper self-test outside behavioral spec |
| `cerberus/tests/test_assorted.py::test_dynamic_types` | atomic | Type Checking | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_assorted.py::test_mro` | atomic | - | source-only | version metadata, docstring/MRO, or test-helper self-test outside behavioral spec |
| `cerberus/tests/test_assorted.py::test_mixin_init` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_assorted.py::test_sub_init` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_customization.py::test_contextual_data_preservation` | integration | Custom Validation | source-only | requires deprecation warning behavior not specified in spec v1 |
| `cerberus/tests/test_customization.py::test_docstring_parsing` | integration | Custom Validation | source-only | requires docstring-derived validation_rules metadata not specified in spec v1 |
| `cerberus/tests/test_customization.py::test_check_with_method[check_with]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_customization.py::test_check_with_method[validator]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_customization.py::test_validator_method[check_with]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_customization.py::test_validator_method[validator]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_customization.py::test_schema_validation_can_be_disabled_in_schema_setter` | integration | Custom Validation | source-only | requires child/internal schema context attrs not specified in spec v1 |
| `cerberus/tests/test_errors.py::test__error_1` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_errors.py::test__error_2` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_errors.py::test__error_3` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_errors.py::test_error_tree_from_subschema` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_errors.py::test_error_tree_from_anyof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_errors.py::test_nested_error_paths` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_errors.py::test_path_resolution_for_registry_references` | atomic | - | source-only | asserts exact default BasicErrorHandler message wording |
| `cerberus/tests/test_errors.py::test_queries` | integration | Errors | source-only | requires named error definition constants not listed in spec v1 |
| `cerberus/tests/test_errors.py::test_basic_error_handler` | integration | Errors | source-only | asserts BasicErrorHandler.messages and exact default message templates out of scope in spec v1 |
| `cerberus/tests/test_errors.py::test_basic_error_of_errors` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_errors.py::test_wrong_amount_of_items` | atomic | - | source-only | asserts exact default BasicErrorHandler message wording |
| `cerberus/tests/test_normalization.py::test_coerce` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_in_dictschema` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_in_listschema` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_in_listitems` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_in_dictschema_in_listschema` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_not_destructive` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_catches_ValueError` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_coerce_in_listitems_catches_ValueError` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_coerce_catches_TypeError` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_coerce_in_listitems_catches_TypeError` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_coerce_unknown` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_custom_coerce_and_rename` | integration | Normalization + Custom Validation | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_chain` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_chain_aborts` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_normalization.py::test_coerce_non_digit_in_sequence` | integration | Normalization + Cross-View Invariants | covered |  |
| `cerberus/tests/test_normalization.py::test_nullables_dont_fail_coerce` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_nullables_fail_coerce_on_non_null_values` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_normalization.py::test_normalized` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_rename` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_rename_handler` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_purge_unknown` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_purge_unknown_in_subschema` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_issue_147_complex` | system_e2e | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_issue_147_nested_dict` | system_e2e | Normalization + Nested Data Rules | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_in_valuesrules` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_coerce_in_keysrules` | integration | Normalization + Custom Validation | covered |  |
| `cerberus/tests/test_normalization.py::test_coercion_of_sequence_items` | integration | Normalization + Cross-View Invariants | covered |  |
| `cerberus/tests/test_normalization.py::test_default_missing[default0]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_missing[default1]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_existent[default0]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_existent[default1]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_none_nullable[default0]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_none_nullable[default1]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_none_nonnullable[default0]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_none_nonnullable[default1]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_none_default_value` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_missing_in_subschema[default0]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_default_missing_in_subschema[default1]` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_depending_default_setters` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_circular_depending_default_setters` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_normalization.py::test_issue_250` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_issue_250_no_type_pass_on_list` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_issue_250_no_type_fail_on_dict` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_issue_250_no_type_fail_pass_on_other` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_allow_unknown_with_of_rules` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_normalization.py::test_271_normalising_tuples` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_allow_unknown_wo_schema` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_allow_unknown_with_purge_unknown` | system_e2e | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_allow_unknown_with_purge_unknown_subdocument` | system_e2e | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_purge_readonly` | integration | Normalization | covered |  |
| `cerberus/tests/test_normalization.py::test_defaults_in_allow_unknown_schema` | system_e2e | Normalization | covered |  |
| `cerberus/tests/test_registries.py::test_schema_registry_simple` | integration | Registries + Validation Schemas | covered |  |
| `cerberus/tests/test_registries.py::test_top_level_reference` | integration | Registries | covered |  |
| `cerberus/tests/test_registries.py::test_rules_set_simple` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_registries.py::test_allow_unknown_as_reference` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_registries.py::test_recursion` | system_e2e | Registries | covered |  |
| `cerberus/tests/test_registries.py::test_references_remain_unresolved` | integration | Registries | covered |  |
| `cerberus/tests/test_registries.py::test_rules_registry_with_anyof_type` | integration | Registries | covered |  |
| `cerberus/tests/test_registries.py::test_schema_registry_with_anyof_type` | integration | Registries + Validation Schemas | covered |  |
| `cerberus/tests/test_registries.py::test_normalization_with_rules_set` | system_e2e | Registries | covered |  |
| `cerberus/tests/test_registries.py::test_rules_set_with_dict_field` | system_e2e | Registries | covered |  |
| `cerberus/tests/test_schema.py::test_empty_schema` | atomic | - | source-only | asserts exact exception message wording |
| `cerberus/tests/test_schema.py::test_bad_schema_type` | atomic | - | source-only | asserts exact exception message wording |
| `cerberus/tests/test_schema.py::test_bad_schema_type_field` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_unknown_rule` | atomic | - | source-only | asserts exact exception message wording |
| `cerberus/tests/test_schema.py::test_unknown_type` | atomic | - | source-only | asserts exact exception message wording |
| `cerberus/tests/test_schema.py::test_bad_schema_definition` | atomic | - | source-only | asserts exact exception message wording |
| `cerberus/tests/test_schema.py::test_bad_of_rules` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_normalization_rules_are_invalid_in_of_rules` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_anyof_allof_schema_validate` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_repr` | atomic | - | source-only | asserts exact repr output |
| `cerberus/tests/test_schema.py::test_validated_schema_cache` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_schema.py::test_expansion_in_nested_schema` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_unvalidated_schema_can_be_copied` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_deprecated_rule_names_in_valueschema` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_anyof_check_with` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_schema.py::test_rulename_space_is_normalized` | atomic | Validation Schemas | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_utils.py::test_compare_paths` | atomic | Installable Surface | source-only | top-level import carrier requires candidate-visible helper API not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_empty_document` | atomic | Common Validation Rules | source-only | uses upstream helper/error constants not listed in spec v1 |
| `cerberus/tests/test_validation.py::test_bad_document_type` | atomic | Type Checking | source-only | uses upstream helper/error constants not listed in spec v1 |
| `cerberus/tests/test_validation.py::test_unknown_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_empty_field_definition` | atomic | Common Validation Rules + Validator Construction | covered |  |
| `cerberus/tests/test_validation.py::test_required_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_nullable_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_nullable_skips_allowed` | atomic | Common Validation Rules | covered |  |
| `cerberus/tests/test_validation.py::test_nullable_skips_of_roles[all]` | integration | Of-Rules | covered |  |
| `cerberus/tests/test_validation.py::test_nullable_skips_of_roles[any]` | integration | Of-Rules | covered |  |
| `cerberus/tests/test_validation.py::test_nullable_skips_of_roles[none]` | integration | Of-Rules | covered |  |
| `cerberus/tests/test_validation.py::test_nullable_skips_of_roles[one]` | integration | Of-Rules | covered |  |
| `cerberus/tests/test_validation.py::test_readonly_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_readonly_field_first_rule` | atomic | Common Validation Rules | source-only | asserts exact default error message wording out of scope in spec v1 |
| `cerberus/tests/test_validation.py::test_readonly_field_with_default_value` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_nested_readonly_field_with_default_value` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_repeated_readonly` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_not_a_string` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_binary` | atomic | Validation Workflow | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_integer` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_boolean` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_datetime` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_float` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_number` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_list` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_not_a_dict` | atomic | Type Checking | source-only | uses upstream assert_bad_type helper requiring ErrorList internals not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_bad_max_length` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_max_length_binary` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_min_length` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_min_length_binary` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_max_value` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_min_value` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_schema` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_valuesrules` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_list_of_values` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_list_of_integers` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_list_of_dicts` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_array_unallowed` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_string_unallowed` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_integer_unallowed` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_integer_allowed` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_validate_update` | atomic | Validation Workflow + Cross-View Invariants | covered |  |
| `cerberus/tests/test_validation.py::test_string` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_string_allowed` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_integer` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_boolean` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_datetime` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_float` | atomic | Type Checking | source-only | expects integer to satisfy float type, which is not stated in spec v1; spec only says number accepts ints and floats |
| `cerberus/tests/test_validation.py::test_number` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_array` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_set` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_one_of_two_types` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_regex` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_regex_with_flag` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_a_list_of_dicts` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_a_list_of_values` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_an_array_from_set` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_a_list_of_integers` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_a_dict` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_a_dict_with_valuesrules` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_keysrules[keysrules]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_keysrules[keyschema]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_a_list_length` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_custom_datatype` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_custom_datatype_rule` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_custom_validator` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_empty_values[-string]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_empty_values[value1-list]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_empty_values[value2-dict]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_empty_values[value3-list]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_empty_skips_regex` | atomic | Common Validation Rules | covered |  |
| `cerberus/tests/test_validation.py::test_ignore_none_values` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_unknown_keys` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_unknown_key_dict` | atomic | Unknown Fields + Cross-Field Rules + Errors + Error Semantics + Exceptions | covered |  |
| `cerberus/tests/test_validation.py::test_unknown_key_list` | atomic | Unknown Fields + Cross-Field Rules + Errors + Error Semantics + Exceptions + Cross-View Invariants | covered |  |
| `cerberus/tests/test_validation.py::test_unknown_keys_list_of_dicts` | atomic | Unknown Fields + Cross-Field Rules + Errors + Error Semantics + Exceptions + Cross-View Invariants | covered |  |
| `cerberus/tests/test_validation.py::test_unknown_keys_retain_custom_rules` | atomic | Unknown Fields | source-only | requires deprecation warning behavior not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_nested_unknown_keys` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_novalidate_noerrors` | atomic | - | source-only | asserts exact default BasicErrorHandler message wording |
| `cerberus/tests/test_validation.py::test_callable_validator` | integration | Custom Validation + Validator Construction | covered |  |
| `cerberus/tests/test_validation.py::test_dependencies_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_list` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_list_with_required_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_list_with_subodcuments_fields` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_dict` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_dict_with_required_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_field_satisfy_nullable_field` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_field_with_mutually_dependent_nullable_fields` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_dict_with_subdocuments_fields` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_root_relative_dependencies` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_errors` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_options_passed_to_nested_validators` | system_e2e | Nested Data Rules + Validator Construction | covered |  |
| `cerberus/tests/test_validation.py::test_self_root_document` | atomic | Validation Workflow | source-only | requires root_document public/internal attr not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_validator_rule` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_validated` | atomic | Validation Workflow | covered |  |
| `cerberus/tests/test_validation.py::test_anyof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_allof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_unicode_allowed` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_unicode_allowed_py3` | atomic | Common Validation Rules | covered |  |
| `cerberus/tests/test_validation.py::test_unicode_allowed_py2` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_oneof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_noneof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_anyof_allof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_anyof_schema` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_anyof_2` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_anyof_type` | atomic | Type Checking | covered |  |
| `cerberus/tests/test_validation.py::test_oneof_schema` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_nested_oneof_type` | atomic | Type Checking + Nested Data Rules | covered |  |
| `cerberus/tests/test_validation.py::test_nested_oneofs` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_no_of_validation_if_type_fails` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_issue_107` | atomic | Validation Workflow | covered |  |
| `cerberus/tests/test_validation.py::test_dont_type_validate_nulled_values` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_error` | atomic | - | source-only | asserts exact default BasicErrorHandler message wording |
| `cerberus/tests/test_validation.py::test_dependencies_on_boolean_field_with_one_value` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_on_boolean_field_with_value_in_list` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_document_path` | atomic | Validation Workflow | source-only | requires root_document public/internal attr not specified in spec v1 |
| `cerberus/tests/test_validation.py::test_excludes` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_mutual_excludes` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_required_excludes` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_multiples_exclusions` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_bad_excludes_fields` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_boolean_is_not_a_number` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_min_max_date` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dict_length` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_forbidden` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_forbidden_number` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_mapping_with_sequence_schema` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_sequence_with_mapping_schema` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_type_error_aborts_validation` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_dependencies_in_oneof` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_allow_unknown_with_oneof_rules` | atomic | - | excluded | asserts private implementation state |
| `cerberus/tests/test_validation.py::test_contains[constraint0]` | atomic | Common Validation Rules | source-only | contains rule absent from spec v1 |
| `cerberus/tests/test_validation.py::test_contains[Terry Gilliam]` | atomic | Common Validation Rules | source-only | contains rule absent from spec v1 |
| `cerberus/tests/test_validation.py::test_require_all_simple` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_require_all_override_by_required` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_require_all_override_by_subdoc_require_all[True-True]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_require_all_override_by_subdoc_require_all[True-False]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_require_all_override_by_subdoc_require_all[False-True]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_require_all_override_by_subdoc_require_all[False-False]` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_require_all_and_exclude` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_allowed_when_passing_list_of_dicts` | atomic | - | source-only | uses upstream assert_fail helper which inspects validator._errors/ErrorList internals |
| `cerberus/tests/test_validation.py::test_schema_validation_from_rules_set` | system_e2e | Type Checking + Validation Schemas | covered |  |

Total: 247 | kept (covered): 81 | spec_gap: 0 | source-only: 155 | excluded: 11 | final scoreable: 81
