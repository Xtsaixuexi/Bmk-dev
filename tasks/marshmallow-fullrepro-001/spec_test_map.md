# spec_test_map.md
> marshmallow-fullrepro-001 Step 4 测试到当前 candidate-visible spec 的映射表。
> 每个 pytest nodeid 一行；covered 行进入 kept_nodeids/taxonomy。

| test_nodeid | layer | spec_section | status | notes |
|-------------|-------|--------------|--------|-------|
| `tests/test_context.py::TestContext::test_context_load_dump` | integration | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_context_method` | integration | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_context_function` | integration | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_function_field_handles_bound_serializer` | integration | Field Types | covered |  |
| `tests/test_context.py::TestContext::test_nested_fields_inherit_context` | system_e2e | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_nested_list_fields_inherit_context` | system_e2e | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_nested_dict_fields_inherit_context` | system_e2e | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_nested_field_with_unpicklable_object_in_context` | system_e2e | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_function_field_passed_serialize_with_context` | integration | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_function_field_deserialization_with_context` | integration | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_decorated_processors_with_context` | integration | Experimental Context | covered |  |
| `tests/test_context.py::TestContext::test_validates_schema_with_context` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorated_processors[True]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_decorated_processors[False]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_decorated_processor_returning_none[exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorated_processor_returning_none[include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorated_processor_returning_none[raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestPassOriginal::test_pass_original_single` | system_e2e | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::TestPassOriginal::test_pass_original_many` | system_e2e | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_decorated_processor_inheritance` | system_e2e | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::TestValidatesDecorator::test_validates` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesDecorator::test_validates_with_attribute` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesDecorator::test_validates_decorator` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesDecorator::test_field_not_present` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesDecorator::test_precedence` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesDecorator::test_validates_with_data_key` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesDecorator::test_validates_accepts_multiple_fields` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_validator_nested_many_invalid_data` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_validator_nested_many_schema_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_validator_nested_many_field_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_validator_nested_many_pass_original_and_pass_collection[True-expected_data0-expected_original_data0-data0]` | system_e2e | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_validator_nested_many_pass_original_and_pass_collection[False-expected_data1-expected_original_data1-data0]` | system_e2e | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_decorated_validators` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_multiple_validators` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_multiple_validators_merge_dict_errors` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_passing_original_data` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_allow_reporting_field_errors_in_schema_validator` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_allow_arbitrary_field_names_in_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_skip_on_field_errors` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::TestValidatesSchemaDecorator::test_data_key_is_used_in_errors_dict` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling_with_load[pre_load]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling_with_load[post_load]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling_with_load_dict_error[pre_load]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling_with_load_dict_error[post_load]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling_with_dump[pre_dump]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_error_handling_with_dump[post_dump]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_decorators.py::test_decorator_post_dump_with_nested_original_and_pass_collection[data0-expected_data0-expected_original_data0]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_decorator_post_load_with_nested_original_and_pass_collection[data0-expected_data0-expected_original_data0]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_load_processors_receive_unknown[exclude-meta]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_load_processors_receive_unknown[exclude-init]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_load_processors_receive_unknown[exclude-load]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_load_processors_receive_unknown[include-meta]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_load_processors_receive_unknown[include-init]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_load_processors_receive_unknown[include-load]` | integration | Decorators and Hooks | covered |  |
| `tests/test_decorators.py::test_post_load_method_that_appends_to_data` | integration | Decorators and Hooks | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[String]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Integer]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Boolean]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Float]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[DateTime]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Time]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Date]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[TimeDelta]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Dict]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Url]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Email]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[UUID]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[Decimal]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[IP]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[IPv4]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[IPv6]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[IPInterface]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[IPv4Interface]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[IPv6Interface]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[FieldClass19]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[FieldClass20]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_allow_none_deserialize_to_none[FieldClass21]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[String]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Integer]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Boolean]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Float]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[DateTime]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Time]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Date]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[TimeDelta]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Dict]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Url]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Email]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[UUID]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[Decimal]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[IP]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[IPv4]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[IPv6]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[IPInterface]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[IPv4Interface]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[IPv6Interface]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[FieldClass19]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[FieldClass20]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_fields_dont_allow_none_by_default[FieldClass21]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestDeserializingNone::test_allow_none_is_true_if_missing_is_true` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_list_field_deserialize_none_to_none` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_tuple_field_deserialize_none_to_none` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_list_of_nested_allow_none_deserialize_none_to_none` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestDeserializingNone::test_list_of_nested_non_allow_none_deserialize_none_to_validation_error` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_float_field_deserialization[bad]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_float_field_deserialization[]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_float_field_deserialization[in_val2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_float_field_deserialization[True]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_float_field_deserialization[False]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_overflow` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_integer_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_strict_integer_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_decimal_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_decimal_field_with_places` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_decimal_field_with_places_and_rounding` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_decimal_field_deserialization_string` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_decimal_field_special_values` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_decimal_field_special_values_not_permitted` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[nan-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[nan-False]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[nan-True]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[-nan-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[-nan-False]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[-nan-True]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[inf-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[inf-False]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[inf-True]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[-inf-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[-inf-False]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_float_field_allow_nan[-inf-True]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_string_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_field_deserialization_with_custom_truthy_values` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_field_deserialization_with_custom_truthy_values_invalid[notvalid]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_field_deserialization_with_custom_truthy_values_invalid[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_field_deserialization_with_empty_truthy` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_field_deserialization_with_custom_falsy_values` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_field_toggle_show_invalid_value_in_error_message` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[not-a-datetime]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[42]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[True]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[False]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[0]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[in_value6]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[2018]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[2018-01]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[17:26:51 2026-07-01]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_datetime_deserialization[07-01-2026 17:26:51]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_custom_date_format_datetime_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_rfc_datetime_field_deserialization[Sun, 10 Nov 2013 01:23:45 -0000-expected0-False-rfc]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_rfc_datetime_field_deserialization[Sun, 10 Nov 2013 01:23:45 -0000-expected0-False-rfc822]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_rfc_datetime_field_deserialization[Sun, 10 Nov 2013 01:23:45 +0000-expected1-True-rfc]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_rfc_datetime_field_deserialization[Sun, 10 Nov 2013 01:23:45 +0000-expected1-True-rfc822]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_rfc_datetime_field_deserialization[Sun, 10 Nov 2013 01:23:45 -0600-expected2-True-rfc]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_rfc_datetime_field_deserialization[Sun, 10 Nov 2013 01:23:45 -0600-expected2-True-rfc822]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45-expected0-False-iso]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45-expected0-False-iso8601]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45+00:00-expected1-True-iso]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45+00:00-expected1-True-iso8601]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45.123+00:00-expected2-True-iso]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45.123+00:00-expected2-True-iso8601]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45.123456+00:00-expected3-True-iso]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45.123456+00:00-expected3-True-iso8601]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45-06:00-expected4-True-iso]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_datetime_field_deserialization[2013-11-10T01:23:45-06:00-expected4-True-iso8601]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp-1384043025-expected0]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp-1384043025-expected1]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp-1384043025.12-expected2]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp-1384043025.123456-expected3]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp-1-expected4]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp_ms-1384043025000-expected5]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timestamp_field_deserialization[timestamp_ms-1000-expected6]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_timestamp_field_deserialization[True-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_timestamp_field_deserialization[True-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_timestamp_field_deserialization[False-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_boolean_timestamp_field_deserialization[False-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timestamp_field_deserialization[-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timestamp_field_deserialization[-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timestamp_field_deserialization[!@#-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timestamp_field_deserialization[!@#-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timestamp_field_deserialization[-1-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timestamp_field_deserialization[-1-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_oversized_timestamp_field_deserialization[MockDateTimeOSError-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_oversized_timestamp_field_deserialization[MockDateTimeOSError-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_oversized_timestamp_field_deserialization[MockDateTimeOverflowError-timestamp]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_oversized_timestamp_field_deserialization[MockDateTimeOverflowError-timestamp_ms]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_naive_datetime_with_timezone[iso-None-2013-11-10T01:23:45-expected0]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_naive_datetime_with_timezone[iso-timezone1-2013-11-10T01:23:45+00:00-expected1]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_naive_datetime_with_timezone[iso-timezone2-2013-11-10T01:23:45-03:00-expected2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_naive_datetime_with_timezone[rfc-None-Sun, 10 Nov 2013 01:23:45 -0000-expected3]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_naive_datetime_with_timezone[rfc-timezone4-Sun, 10 Nov 2013 01:23:45 +0000-expected4]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_naive_datetime_with_timezone[rfc-timezone5-Sun, 10 Nov 2013 01:23:45 -0300-expected5]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_aware_datetime_default_timezone[iso-2013-11-10T01:23:45-timezone0]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_aware_datetime_default_timezone[iso-2013-11-10T01:23:45-timezone1]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_aware_datetime_default_timezone[rfc-Sun, 10 Nov 2013 01:23:45-timezone0]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_aware_datetime_default_timezone[rfc-Sun, 10 Nov 2013 01:23:45-timezone1]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_time_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_time_field_deserialization[badvalue]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_time_field_deserialization[]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_time_field_deserialization[in_data2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_time_field_deserialization[42]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_custom_time_format_time_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45-expected0-iso]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45-expected0-iso8601]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45-expected0-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45.123-expected1-iso]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45.123-expected1-iso8601]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45.123-expected1-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45.123456-expected2-iso]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45.123456-expected2-iso8601]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45.123456-expected2-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45+01:00-expected3-iso]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45+01:00-expected3-iso8601]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_iso_time_field_deserialization[01:23:45+01:00-expected3-None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timedelta_precision` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_timedelta_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timedelta_field_deserialization[]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timedelta_field_deserialization[badvalue]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timedelta_field_deserialization[in_value2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_timedelta_field_deserialization[9999999999]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_date_field_deserialization[None]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_date_field_deserialization[%Y-%m-%d]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_date_field_deserialization[]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_date_field_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_date_field_deserialization[in_value2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_date_field_deserialization[21-08-2014]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_dict_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_structured_dict_value_deserialization` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_structured_dict_key_deserialization` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_structured_dict_key_value_deserialization` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_url_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_url_field_non_list_validators` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_relative_url_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_url_field_schemes_argument` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_email_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_email_field_non_list_validators` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_function_field_deserialization_is_noop_by_default` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_function_field_deserialization_with_callable` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_function_field_deserialization_missing_with_length_validator` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_function_field_passed_deserialize_only_is_load_only` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_function_field_passed_deserialize_and_serialize_is_not_load_only` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_uuid_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_uuid_deserialization[malformed]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_uuid_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_uuid_deserialization[in_value2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_uuid_deserialization[tooshort]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_ip_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ip_deserialization[malformed]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ip_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ip_deserialization[\x01\x02\x03]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ip_deserialization[192.168]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ip_deserialization[192.168.0.1/24]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ip_deserialization[ff::aa:1::2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_ipv4_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4_deserialization[malformed]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4_deserialization[\x01\x02\x03]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4_deserialization[192.168]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4_deserialization[192.168.0.1/24]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4_deserialization[2a00:1450:4001:81d::200e]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_ipv6_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_ipinterface_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[malformed]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[\x01\x02\x03]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[192.168]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[192.168.0.1/33]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[ff::aa:1::2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipinterface_deserialization[2a00:1450:4001:824::200e/129]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_ipv4interface_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[malformed]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[\x01\x02\x03]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[192.168]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[192.168.0.1/33]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[2a00:1450:4001:81d::200e]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv4interface_deserialization[2a00:1450:4001:824::200e/129]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_ipv6interface_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[malformed]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[123]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[\x01\x02\x03]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[ff::aa:1::2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[192.168.0.1]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[192.168.0.1/24]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_invalid_ipv6interface_deserialization[2a00:1450:4001:824::200e/129]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_symbol_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_symbol_invalid_value` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_symbol_rejects_non_member_attributes[mro]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_symbol_rejects_non_member_attributes[__class__]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_symbol_rejects_non_member_attributes[__members__]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_symbol_not_string` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_value_true_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_value_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_value_true_invalid_value` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_value_field_invalid_value` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_value_true_wrong_type` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_enum_field_by_value_field_wrong_type` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_deserialization_function_must_be_callable` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_method_field_deserialization_is_noop_by_default` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_deserialization_method` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_deserialization_method_must_be_a_method` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_method_field_deserialize_only` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_datetime_list_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_list_field_deserialize_invalid_item` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_list_field_deserialize_multiple_invalid_items` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_list_field_deserialize_value_that_is_not_a_list[notalist]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_list_field_deserialize_value_that_is_not_a_list[42]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_list_field_deserialize_value_that_is_not_a_list[value2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_datetime_int_tuple_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_tuple_field_deserialize_invalid_item` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestFieldDeserialization::test_tuple_field_deserialize_multiple_invalid_items` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_tuple_field_deserialize_value_that_is_not_a_collection[notalist]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_tuple_field_deserialize_value_that_is_not_a_collection[42]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_tuple_field_deserialize_value_that_is_not_a_collection[value2]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_tuple_field_deserialize_invalid_length` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_constant_field_deserialization` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_constant_is_always_included_in_deserialized_data` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_constant_none_allows_none_value` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_constant_with_required` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_field_deserialization_with_user_validator_function` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_field_deserialization_with_user_validator_that_raises_error_with_list` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_field_deserialization_with_validator_with_nonascii_input` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_field_deserialization_with_user_validators` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[List]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Tuple]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[String]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[UUID]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Integer]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Float]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Decimal]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Boolean]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[DateTime]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Time]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Date]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[TimeDelta]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Dict]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Url]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Email]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[IP]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[IPv4]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[IPv6]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestFieldDeserialization::test_fields_accept_internal_types[Enum]` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_to_dict` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_missing_values` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_many` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_exclude` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_single_deserialization_to_dict` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_list_deserialization_to_dict` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_single_none_not_allowed` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_many_non_not_allowed` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_single_required_missing` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_many_required_missing` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_only_basestring` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_only_basestring_with_list_data` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_nested_none_deserialization` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_attribute_param` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_attribute_param_symmetry` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_attribute_param_error_returns_field_name_not_attribute_name` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_attribute_param_error_returns_data_key_not_attribute_name` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_data_key_param` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_data_key_as_empty_string` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_dump_only_param` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_missing_param_value` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_missing_param_callable` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialize_with_missing_param_none` | integration | Field Types | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialization_raises_with_errors` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialization_raises_with_errors_with_multiple_validators` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_deserialization_many_raises_errors` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_validation_errors_are_stored` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_multiple_errors_can_be_stored_for_a_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_multiple_errors_can_be_stored_for_an_email_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_multiple_errors_can_be_stored_for_a_url_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_required_value_only_passed_to_validators_if_provided` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_partial_deserialization[True]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_partial_deserialization[False]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_partial_fields_deserialization` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_partial_fields_validation` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_unknown_fields_deserialization` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_unknown_fields_deserialization_precedence` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_unknown_fields_deserialization_with_data_key` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_unknown_fields_deserialization_with_index_errors_false` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_dump_only_fields_considered_unknown` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestSchemaDeserialization::test_unknown_fields_do_not_unpack_dotted_names` | integration | Schema Methods + Top-Level Names | covered |  |
| `tests/test_deserialization.py::TestValidation::test_integer_with_validator` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_integer_with_validators[field0]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_integer_with_validators[field1]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_integer_with_validators[field2]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_float_with_validators[field0]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_float_with_validators[field1]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_float_with_validators[field2]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_string_validator` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_function_validator` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_function_validators[field0]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_function_validators[field1]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_function_validators[field2]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::TestValidation::test_method_validator` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestValidation::test_nested_data_is_stored_when_validation_fails` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestValidation::test_nested_partial_load` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestValidation::test_deeply_nested_partial_load` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::TestValidation::test_nested_partial_tuple` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestValidation::test_nested_partial_default` | integration | Collection and Nested Fields | covered |  |
| `tests/test_deserialization.py::TestValidation::test_nested_partial_tuple_with_data_key` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[String]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Integer]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Boolean]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Float]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[DateTime]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Time]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Date]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[TimeDelta]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Dict]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Url]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Email]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[UUID]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[Decimal]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[IP]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[IPv4]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[IPv6]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[IPInterface]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[IPv4Interface]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[IPv6Interface]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[FieldClass19]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[FieldClass20]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_field_failure[FieldClass21]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_required_message_can_be_changed[My custom required message]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::test_required_message_can_be_changed[message1]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::test_required_message_can_be_changed[message2]` | integration | Schema Methods | covered |  |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[True-exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[True-include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[True-raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[False-exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[False-include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[False-raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[42-exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[42-include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[42-raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[None-exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[None-include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[None-raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[data4-exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[data4-include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_deserialization.py::test_deserialize_raises_exception_if_input_type_is_incorrect[data4-raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_error_store.py::test_missing_is_falsy` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_none_and_string` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_none_and_custom_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_none_and_list` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_none_and_dict` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_string_and_none` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_custom_error_and_none` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_list_and_none` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_dict_and_none` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_string_and_string` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_custom_error_and_string` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_string_and_custom_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_custom_error_and_custom_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_string_and_list` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_string_and_dict` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_string_and_dict_with_schema_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_custom_error_and_list` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_custom_error_and_dict` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_custom_error_and_dict_with_schema_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_list_and_string` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_list_and_custom_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_list_and_list` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_list_and_dict` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_list_and_dict_with_schema_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_dict_and_string` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_dict_and_custom_error` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_dict_and_list` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_merging_dict_and_dict` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_deep_merging_dicts` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_list_not_changed` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_error_store.py::TestMergeErrors::test_dict_not_changed` | atomic | - | excluded | tests internal error_store/merge_errors behavior outside candidate-visible spec |
| `tests/test_exceptions.py::TestValidationError::test_stores_message_in_list` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_exceptions.py::TestValidationError::test_can_pass_list_of_messages` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_exceptions.py::TestValidationError::test_stores_dictionaries` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_exceptions.py::TestValidationError::test_can_store_field_name` | atomic | Exceptions and Errors | covered |  |
| `tests/test_exceptions.py::TestValidationError::test_str` | atomic | Exceptions and Errors | covered |  |
| `tests/test_exceptions.py::TestValidationError::test_stores_dictionaries_in_messages_dict` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_exceptions.py::TestValidationError::test_messages_dict_type_error_on_badval` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::test_field_aliases[Integer-Integer]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::test_field_aliases[String-String]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::test_field_aliases[Boolean-Boolean]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::test_field_aliases[Url-Url]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestAbstractBaseFields::test_number_cannot_be_instantiated` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestAbstractBaseFields::test_mapping_cannot_be_instantiated` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestAbstractBaseFields::test_custom_number_subclass` | atomic | Field Types | covered |  |
| `tests/test_fields.py::TestAbstractBaseFields::test_custom_mapping_subclass` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestField::test_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_fields.py::TestField::test_error_raised_if_uncallable_validator_passed` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestField::test_error_raised_if_missing_is_set_on_required_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestField::test_custom_field_receives_attr_and_obj` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestField::test_custom_field_receives_data_key_if_set` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestField::test_custom_field_follows_data_key_if_set` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestParentAndName::test_simple_field_parent_and_name` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestParentAndName::test_unbound_field_root_returns_none` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestParentAndName::test_list_field_inner_parent_and_name` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_tuple_field_inner_parent_and_name` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_mapping_field_inner_parent_and_name` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_simple_field_root` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestParentAndName::test_list_field_inner_root` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_tuple_field_inner_root` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_list_root_inheritance` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_dict_root_inheritance` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_datetime_list_inner_format` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestParentAndName::test_field_named_parent_has_root` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[String]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Integer]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Boolean]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Float]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[DateTime]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Time]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Date]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[TimeDelta]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Dict]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Url]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Email]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[UUID]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[Decimal]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[IP]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[IPv4]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[IPv6]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[IPInterface]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[IPv4Interface]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[IPv6Interface]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[FieldClass19]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[FieldClass20]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestMetadata::test_extra_metadata_may_be_added_to_field[FieldClass21]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_default_error_messages_get_merged_with_parent_error_messages_cstm_msg` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_default_error_messages_get_merged_with_parent_error_messages` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_make_error[required-Missing data for required field.]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_make_error[null-Field may not be null.]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_make_error[custom-Custom error message.]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_make_error[validator_failed-Invalid value.]` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestErrorMessages::test_make_error_key_doesnt_exist` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_only_and_exclude_as_string[only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_only_and_exclude_as_string[exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_instantiation_from_dict[nested_value0]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_instantiation_from_dict[<lambda>]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[None-exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[None-include]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[None-raise]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[exclude-exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[exclude-include]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[exclude-raise]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[include-exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[include-include]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[include-raise]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[raise-exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[raise-include]` | atomic | Collection and Nested Fields + Unknown Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_unknown_override[raise-raise]` | atomic | Collection and Nested Fields + Unknown Fields | covered |  |
| `tests/test_fields.py::TestNestedField::test_nested_schema_only_and_exclude[only-fields_list0]` | atomic | OrderedSet | covered | uses `Schema.set_class = OrderedSet` to preserve ordered field-name selection |
| `tests/test_fields.py::TestNestedField::test_nested_schema_only_and_exclude[exclude-fields_list1]` | atomic | OrderedSet | covered | uses `Schema.set_class = OrderedSet` to preserve ordered field-name selection |
| `tests/test_fields.py::TestListNested::test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested[only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested[exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested[dump_only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested[load_only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_class_only_and_exclude_merged_with_nested[only-expected_attribute0-expected_dump0]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_class_only_and_exclude_merged_with_nested[exclude-expected_attribute1-expected_dump1]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_class_multiple_dumps` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_instance_only_and_exclude_merged_with_nested[only-expected_attribute0-expected_dump0]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_instance_only_and_exclude_merged_with_nested[exclude-expected_attribute1-expected_dump1]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_instance_multiple_dumps` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_lambda_only_and_exclude_merged_with_nested[only-expected_attribute0-expected_dump0]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_lambda_only_and_exclude_merged_with_nested[exclude-expected_attribute1-expected_dump1]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestListNested::test_list_nested_partial_propagated_to_nested` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestTupleNested::test_tuple_nested_only_exclude_dump_only_load_only_propagated_to_nested[dump_only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestTupleNested::test_tuple_nested_only_exclude_dump_only_load_only_propagated_to_nested[load_only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestTupleNested::test_tuple_nested_partial_propagated_to_nested` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestDictNested::test_dict_nested_only_exclude_dump_only_load_only_propagated_to_nested[only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestDictNested::test_dict_nested_only_exclude_dump_only_load_only_propagated_to_nested[exclude]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestDictNested::test_dict_nested_only_exclude_dump_only_load_only_propagated_to_nested[dump_only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestDictNested::test_dict_nested_only_exclude_dump_only_load_only_propagated_to_nested[load_only]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestDictNested::test_dict_nested_only_and_exclude_merged_with_nested[only-expected0]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestDictNested::test_dict_nested_only_and_exclude_merged_with_nested[exclude-expected1]` | atomic | Collection and Nested Fields | covered |  |
| `tests/test_fields.py::TestDictNested::test_dict_nested_partial_propagated_to_nested` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_pre_load` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_pre_load_multiple` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_post_load` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_post_load_multiple` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_pre_and_post_load` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_pre_load_validation_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_post_load_validation_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_pre_load_none` | atomic | Base Field Options | covered |  |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_field_post_load_not_called_with_none_input_when_not_allowed` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_invalid_type_passed_to_pre_load` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_fields.py::TestFieldPreAndPostLoad::test_invalid_type_passed_to_post_load` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_options.py::TestFieldOrdering::test_declared_field_order_is_maintained_on_dump` | integration | Schema Meta Options | covered |  |
| `tests/test_options.py::TestFieldOrdering::test_declared_field_order_is_maintained_on_load` | integration | Schema Meta Options | covered |  |
| `tests/test_options.py::TestFieldOrdering::test_nested_field_order_with_only_arg_is_maintained_on_dump` | integration | Schema Meta Options | covered |  |
| `tests/test_options.py::TestFieldOrdering::test_nested_field_order_with_only_arg_is_maintained_on_load` | integration | Schema Meta Options + Representative Workflows | covered |  |
| `tests/test_options.py::TestFieldOrdering::test_nested_field_order_with_exclude_arg_is_maintained` | integration | Schema Meta Options + Representative Workflows | covered |  |
| `tests/test_options.py::TestIncludeOption::test_fields_are_added` | integration | Schema Meta Options | covered |  |
| `tests/test_options.py::TestIncludeOption::test_included_fields_ordered_after_declared_fields` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_options.py::TestIncludeOption::test_added_fields_are_inherited` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_options.py::TestManyOption::test_many_by_default` | integration | Schema Meta Options | covered |  |
| `tests/test_options.py::TestManyOption::test_explicit_single` | integration | Schema Meta Options | covered |  |
| `tests/test_registry.py::test_serializer_has_class_registry` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_registry.py::test_register_class_meta_option` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_registry.py::test_serializer_class_registry_register_same_classname_different_module` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_registry.py::test_serializer_class_registry_override_if_same_classname_same_module` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_registry.py::test_two_way_nesting` | atomic | Class Registry | covered |  |
| `tests/test_registry.py::test_nesting_with_class_name_many` | atomic | Class Registry | covered |  |
| `tests/test_registry.py::test_invalid_class_name_in_nested_field_raises_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_registry.py::test_multiple_classes_with_same_name_raises_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_registry.py::test_multiple_classes_with_all` | atomic | Class Registry | covered |  |
| `tests/test_registry.py::test_can_use_full_module_path_to_class` | atomic | Class Registry | covered |  |
| `tests/test_schema.py::test_serializing_basic_object` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_serializer_dump` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_resets_errors` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_validation_error_stores_input_data_and_valid_data` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_resets_error_fields` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_errored_fields_do_not_appear_in_output` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_stores_error_indices` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_dump_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_multiple_errors_can_be_stored_for_a_given_index` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_dump_returns_a_dict` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_dumps_returns_a_string` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_dumping_single_object_with_collection_schema` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_loading_single_object_with_collection_schema` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_dumps_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_returns_an_object` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_invalid_input_type[None]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[False]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[1]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[1.2]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[val4]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[val5]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[val6]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_invalid_input_type[lol]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[None]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[False]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[1]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[1.2]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[val4]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[val5]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[val6]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_invalid_input_type[lol]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_empty_collection[val0]` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_many_empty_collection[val1]` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[False]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[1]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[1.2]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[val3]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[val4]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[val5]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_invalid_input_type[lol]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_load_many_in_nested_empty_collection[val0]` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_load_many_in_nested_empty_collection[val1]` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_loads_returns_a_user` | integration | Schema Methods + Deserialization With Load and Loads | covered |  |
| `tests/test_schema.py::test_loads_many` | integration | Schema Methods + Deserialization With Load and Loads | covered |  |
| `tests/test_schema.py::test_loads_deserializes_from_json` | integration | Schema Methods + Deserialization With Load and Loads | covered |  |
| `tests/test_schema.py::test_serializing_none` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_default_many_symmetry` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_on_bind_field_hook` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_nested_on_bind_field_hook` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestValidate::test_validate_raises_with_errors_dict` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestValidate::test_validate_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::TestValidate::test_validate_many_doesnt_store_index_if_index_errors_option_is_false` | integration | Schema Methods + Exceptions and Errors | covered |  |
| `tests/test_schema.py::TestValidate::test_validate` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestValidate::test_validate_required` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_fields_are_not_copies` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_dumps_returns_json` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_naive_datetime_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_datetime_formatted_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_datetime_iso_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_tz_datetime_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_class_variable` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_serialize_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_inheriting_schema` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_custom_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_url_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_relative_url_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_stores_invalid_url_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_email_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_stored_invalid_email` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_integer_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_as_string` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_method_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_function_field` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_fields_must_be_declared_as_instances` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_bind_field_does_not_swallow_typeerror` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_serializing_generator` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_serializing_empty_list_returns_empty_list` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_serializing_dict` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_exclude_in_init` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_only_in_init` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_invalid_only_param` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_can_serialize_uuid` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_can_serialize_time` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_render_module` | integration | Schema Declaration + Representative Workflows | covered |  |
| `tests/test_schema.py::test_custom_error_message` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_custom_unknown_error_message` | integration | Schema Methods + Unknown Fields | covered |  |
| `tests/test_schema.py::test_custom_type_error_message` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_custom_type_error_message_with_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_custom_error_messages_with_inheritance` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_load_errors_with_many` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_error_raised_if_fields_option_is_not_list` | integration | Schema Meta Options + Error Handling + Error Semantics | covered |  |
| `tests/test_schema.py::test_nested_custom_set_in_exclude_reusing_schema` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_only` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_only_inheritance` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_only_empty_inheritance` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_exclude` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_exclude_inheritance` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_only_and_exclude` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_only_then_exclude_inheritance` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_exclude_then_only_inheritance` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_exclude_and_only_inheritance` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_instance_many` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_many_should_override_schema_many_case1` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_many_should_override_schema_many_case2` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_instance_only` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_instance_exclude` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_meta_nested_exclude` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_custom_set_not_implementing_getitem` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_deeply_nested_only_and_exclude` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_nested_lambda` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_data_key_collision[f1]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_data_key_collision[f5]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_data_key_collision[None]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_attribute_collision[f1]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_attribute_collision[f5]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_attribute_collision[None]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestDeeplyNestedLoadOnly::test_load_only` | system_e2e | Schema Methods | covered |  |
| `tests/test_schema.py::TestDeeplyNestedLoadOnly::test_dump_only` | system_e2e | Schema Methods | covered |  |
| `tests/test_schema.py::TestDeeplyNestedListLoadOnly::test_load_only` | system_e2e | Schema Methods | covered |  |
| `tests/test_schema.py::TestDeeplyNestedListLoadOnly::test_dump_only` | system_e2e | Schema Methods | covered |  |
| `tests/test_schema.py::test_nested_constructor_only_and_exclude` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_only_and_exclude` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_invalid_only_and_exclude_with_fields` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_exclude_invalid_attribute` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_only_bounded_by_fields` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_only_bounded_by_additional` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_only_empty` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_only_and_exclude_as_string[only]` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_only_and_exclude_as_string[exclude]` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_nested_with_sets` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_meta_field_not_on_obj_raises_attribute_error` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_exclude_fields` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_fields_option_must_be_list_or_tuple` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_exclude_option_must_be_list_or_tuple` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_datetimeformat_option` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_dateformat_option` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_timeformat_option` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_default_dateformat` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::TestFieldValidation::test_errors_are_cleared_after_loading_collection` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestFieldValidation::test_raises_error_with_list` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestFieldValidation::test_raises_error_with_dict` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestFieldValidation::test_ignored_if_not_in_only` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_schema_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_many_with_missing_attribute` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_with_attribute_none` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_field_does_not_validate_required` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_none` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_many_fields` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_only` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_exclude` | system_e2e | Schema Meta Options | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_list_field` | system_e2e | Schema Declaration | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_load_many` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_errors` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_method_field` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_function_field` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_nested_fields_must_be_passed_a_serializer` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestNestedSchema::test_invalid_type_passed_to_nested_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_all_errors_on_many_nested_field_with_validates_decorator` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_unknown_validation[None]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_unknown_validation[raise]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_unknown_validation[include]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestNestedSchema::test_nested_unknown_validation[exclude]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestPluckSchema::test_pluck[UserSchema]` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestPluckSchema::test_pluck[user_schema1]` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestPluckSchema::test_pluck_none` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestPluckSchema::test_pluck_with_data_key` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_nesting_schema_by_passing_lambda` | integration | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_nesting_schema_by_passing_class_name` | integration | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_nesting_within_itself_exclude` | integration | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_nested_self_with_only_param` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_multiple_pluck_self_lambda` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_nested_self_many_lambda` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestSelfReference::test_nested_self_list` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::test_serialization_with_required_field` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::test_deserialization_with_required_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_deserialization_with_required_field_and_custom_validator` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::test_serializer_can_specify_nested_object_as_attribute` | system_e2e | Collection and Nested Fields | covered |  |
| `tests/test_schema.py::TestFieldInheritance::test_inherit_fields_from_schema_subclass` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_schema.py::TestFieldInheritance::test_inherit_fields_from_non_schema_subclass` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_schema.py::TestFieldInheritance::test_inheritance_follows_mro` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_schema.py::TestGetAttribute::test_get_attribute_is_used` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::TestGetAttribute::test_get_attribute_with_many` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::TestRequiredFields::test_required_string_field_missing` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestRequiredFields::test_required_string_field_failure` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestRequiredFields::test_allow_none_param` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestRequiredFields::test_allow_none_custom_message` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::TestDefaults::test_missing_inputs_are_excluded_from_dump_output` | integration | Schema Meta Options + Required, Missing, Defaults, and Nulls | covered |  |
| `tests/test_schema.py::TestDefaults::test_none_is_serialized_to_none` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_schema.py::TestDefaults::test_default_and_value_missing` | integration | Schema Declaration + Required, Missing, Defaults, and Nulls | covered |  |
| `tests/test_schema.py::TestDefaults::test_loading_none` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::TestDefaults::test_missing_inputs_are_excluded_from_load_output` | integration | Schema Meta Options + Required, Missing, Defaults, and Nulls | covered |  |
| `tests/test_schema.py::TestLoadOnly::test_load_only` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::TestLoadOnly::test_dump_only` | integration | Schema Methods | covered |  |
| `tests/test_schema.py::TestLoadOnly::test_url_field_requre_tld_false` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::TestFromDict::test_generates_schema` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::TestFromDict::test_name` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_schema.py::TestFromDict::test_generated_schemas_are_not_registered` | atomic | - | excluded | asserts private implementation attribute/registry shape |
| `tests/test_schema.py::TestFromDict::test_meta_options_are_applied` | integration | Schema Meta Options | covered |  |
| `tests/test_schema.py::test_class_registry_returns_schema_type` | system_e2e | Schema Declaration | covered |  |
| `tests/test_schema.py::test_set_dict_class[dict]` | integration | Schema Declaration | covered |  |
| `tests/test_schema.py::test_set_dict_class[OrderedDict]` | integration | Schema Declaration | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_passed_func` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_passed_serialize_only_is_dump_only` | integration | Field Types + Serialization With Dump and Dumps | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_passed_deserialize_and_serialize_is_not_dump_only` | integration | Field Types + Serialization With Dump and Dumps | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_passed_serialize` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_does_not_swallow_attribute_error` | integration | Field Types + Error Handling + Error Semantics | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_serialize_with_load_only_param` | integration | Schema Methods | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_load_only` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_function_field_passed_uncallable_object` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_integer_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_integer_as_string_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_integer_field_default` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_integer_field_default_set_to_none` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_uuid_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_ip_address_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_ipv4_address_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_ipv6_address_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_ip_interface_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_ipv4_interface_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_ipv6_interface_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_enum_field_by_symbol_serialization` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_enum_field_by_value_true_serialization` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_enum_field_by_value_field_serialization` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_decimal_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_decimal_field_string` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_decimal_field_special_values` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_decimal_field_special_values_not_permitted` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_decimal_field_fixed_point_representation` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_email_field_serialize_none` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_dict_field_serialize_none` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_dict_field_serialize` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_dict_field_serialize_ordereddict` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_structured_dict_value_serialize` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_structured_dict_key_serialize` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_structured_dict_key_value_serialize` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_url_field_serialize_none` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_method_field_with_method_missing` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_method_field_passed_serialize_only_is_dump_only` | integration | Field Types + Serialization With Dump and Dumps | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_method_field_passed_deserialize_only_is_load_only` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_method_field_with_uncallable_attribute` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_method_field_does_not_swallow_attribute_error` | integration | Field Types + Error Handling + Error Semantics | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_method_with_no_serialize_is_missing` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_serialize_with_data_key_param` | integration | Schema Methods | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_serialize_with_data_key_as_empty_string` | integration | Schema Methods | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_serialize_with_attribute_and_data_key_uses_data_key` | integration | Schema Methods | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_rfc822[value0-Sun, 10 Nov 2013 01:23:45 -0000-rfc]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_rfc822[value0-Sun, 10 Nov 2013 01:23:45 -0000-rfc822]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_rfc822[value1-Sun, 10 Nov 2013 01:23:45 +0000-rfc]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_rfc822[value1-Sun, 10 Nov 2013 01:23:45 +0000-rfc822]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_rfc822[value2-Sun, 10 Nov 2013 01:23:45 -0600-rfc]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_rfc822[value2-Sun, 10 Nov 2013 01:23:45 -0600-rfc822]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp-value0-0]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp-value1-1384043025]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp-value2-1384043025]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp-value3-1384064625]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp_ms-value4-1384043025000]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp_ms-value5-1384043025000]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_timestamp[timestamp_ms-value6-1384064625000]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value0-2013-11-10T01:23:45-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value0-2013-11-10T01:23:45-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value0-2013-11-10T01:23:45-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value1-2013-11-10T01:23:45.123456+00:00-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value1-2013-11-10T01:23:45.123456+00:00-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value1-2013-11-10T01:23:45.123456+00:00-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value2-2013-11-10T01:23:45+00:00-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value2-2013-11-10T01:23:45+00:00-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value2-2013-11-10T01:23:45+00:00-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value3-2013-11-10T01:23:45-06:00-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value3-2013-11-10T01:23:45-06:00-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_iso8601[value3-2013-11-10T01:23:45-06:00-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_field_format` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_string_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_string_field_default_to_empty_string` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value0-01:23:45-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value0-01:23:45-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value0-01:23:45-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value1-01:23:45.123000-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value1-01:23:45.123000-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value1-01:23:45.123000-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value2-01:23:45.123456-iso]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value2-01:23:45.123456-iso8601]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_iso8601[value2-01:23:45.123456-None]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_time_field_format` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_date_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_timedelta_field` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_list_field` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_list_field_serialize_none_returns_none` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_list_field_work_with_generator_single_value` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_list_field_work_with_generators_multiple_values` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_list_field_work_with_generators_empty_generator_returns_none_for_every_non_returning_yield_statement` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_list_field_work_with_set` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_list_field_work_with_custom_class_with_iterator_protocol` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_bad_list_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_serialization.py::TestFieldSerialization::test_datetime_integer_tuple_field` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_tuple_field_serialize_none_returns_none` | integration | Collection and Nested Fields | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_bad_tuple_field` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_serialization.py::TestFieldSerialization::test_serialize_does_not_apply_validators` | integration | Schema Methods | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_constant_field_serialization` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_constant_is_always_included_in_serialized_data` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_constant_field_serialize_when_omitted` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[String]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Integer]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Boolean]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Float]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[DateTime]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Time]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Date]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[TimeDelta]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Dict]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Url]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Email]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[UUID]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[Decimal]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[IP]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[IPv4]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[IPv6]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[IPInterface]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[IPv4Interface]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[IPv6Interface]` | integration | Field Types | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[FieldClass19]` | integration | Field Types + Cross-View Invariants | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[FieldClass20]` | integration | Field Types + Cross-View Invariants | covered |  |
| `tests/test_serialization.py::TestFieldSerialization::test_all_fields_serialize_none_to_none[FieldClass21]` | integration | Field Types + Cross-View Invariants | covered |  |
| `tests/test_serialization.py::TestSchemaSerialization::test_serialize_with_missing_param_value` | integration | Schema Methods + Schema Construction + Hooks and Object Construction + Cross-View Invariants | covered |  |
| `tests/test_serialization.py::TestSchemaSerialization::test_serialize_with_missing_param_callable` | integration | Schema Methods + Schema Construction + Hooks and Object Construction + Cross-View Invariants | covered |  |
| `tests/test_serialization.py::test_serializing_named_tuple` | integration | Collection and Nested Fields + Nested Relationships and Projections | covered |  |
| `tests/test_serialization.py::test_serializing_named_tuple_with_meta` | integration | Collection and Nested Fields + Nested Relationships and Projections | covered |  |
| `tests/test_serialization.py::test_serializing_slice` | integration | Schema Methods + Schema Construction + Hooks and Object Construction | covered |  |
| `tests/test_serialization.py::test_nested_field_many_serializing_generator` | integration | Collection and Nested Fields + Nested Relationships and Projections | covered |  |
| `tests/test_utils.py::test_missing_singleton_copy` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_from_object[obj0]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_from_object[obj1]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_from_object[obj2]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_from_object[obj3]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_from_namedtuple_with_default` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_for_nested_object` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value_from_dict` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_get_value` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_set_value` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_is_collection` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp[1676386740-expected0]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp[1676386740.58-expected1]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp_with_negative_value` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp_with_overflow_value` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp_ms[1676386740000-expected0]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp_ms[1000-expected1]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp_ms_rejects_booleans[True]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_from_timestamp_ms_rejects_booleans[False]` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_utils.py::test_function_field_using_type_annotation` | atomic | - | source-only | utility helper behavior not specified in candidate-visible spec |
| `tests/test_validate.py::test_url_absolute_valid[http://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[https://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[ftp://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[ftps://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://example.co.jp]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://www.example.com/a%C2%B1b]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://www.example.com/~username/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://info.example.com/?fred]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://xn--mgbh0fb.xn--kgbechtv/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://example.com/blue/red%3Fand+green]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://www.example.com/?array%5Bkey%5D=value]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://xn--rsum-bpad.example.org/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://123.45.67.8/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://123.45.67.8:8329/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://[2001:db8::ff00:42]:8329]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://[2001::1]:8329]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://www.example.com:8000/foo]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://user@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://user:pass@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://:pass@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_valid[http://AZaz09-._~%2A!$&'()*+,;=:@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http:///example.com/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[https:///example.com/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[https://example.org\\]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[https://example.org\n]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[ftp:///example.com/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[ftps:///example.com/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http//example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http:///]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http:/example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[foo://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[../icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://2001:db8::ff00:42:8329]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://[192.168.1.1]:8329]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[abc]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[..]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[ ]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[None]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://user@pass@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://@pass@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://@@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://^@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://%0G@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_absolute_invalid[http://%@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[http://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[http://123.45.67.8/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[http://example.com/foo/bar/../baz]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[https://example.com/../icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[http://example.com/./icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[ftp://example.com/../../../../g]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[http://example.com/g?y/./x]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[/foo/bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[/foo?bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_valid[/foo?bar#baz]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[http//example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[http://example.org\n]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[suppliers.html]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[../icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[../.../g]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[...]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[\\]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[ ]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_invalid[None]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_valid[/foo/bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_valid[/foo?bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_valid[?bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_valid[/foo?bar#baz]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http//example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http://example.org\n]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[suppliers.html]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[../icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[../.../g]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[...]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[\\]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[ ]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http://123.45.67.8/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http://example.com/foo/bar/../baz]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[https://example.com/../icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http://example.com/./icons/logo.gif]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[ftp://example.com/../../../../g]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_relative_only_invalid[http://example.com/g?y/./x]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://123.45.67.8/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://example]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://example.]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://example:80]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://user.name:pass.word@example]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_valid[http://example/foo/bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[http//example]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[http://example\n]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[http://.example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[http:///foo/bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[http:// /foo/bar]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_dont_require_tld_invalid[None]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_custom_scheme` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_custom_scheme_case_insensitive` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file:///tmp/tmp1234]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file://localhost/tmp/tmp1234]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file:///C:/Users/test/file.txt]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file://localhost/C:/Program%20Files/file.exe]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file:///home/user/documents/test.pdf]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file:///tmp/test%20file.txt]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file:///]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[file://localhost/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE:///tmp/tmp1234]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE://localhost/tmp/tmp1234]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE:///C:/Users/test/file.txt]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE://localhost/C:/Program%20Files/file.exe]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE:///home/user/documents/test.pdf]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE:///tmp/test%20file.txt]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE:///]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_accepts_valid_file_urls[FILE://localhost/]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_rejects_invalid_file_urls[file://]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_url_rejects_invalid_file_urls[file:/tmp/file.txt]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_url_rejects_invalid_file_urls[file:tmp/file.txt]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_url_rejects_invalid_file_urls[file://hostname/path]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_url_rejects_invalid_file_urls[file:///tmp/test file.txt]` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_url_relative_and_custom_schemes` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_url_rejects_invalid_relative_usage` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_url_idn_valid[https://\u09a4\u09cc\u09b9\u09bf\u09a6\u09c1\u09b0.\u09ac\u09be\u0982\u09b2\u09be]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_valid[https://m\xfcnchen.de]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_valid[https://\u4f8b\u3048.jp/path]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_valid[http://\u0645\u062b\u0627\u0644.\u0625\u062e\u062a\u0628\u0627\u0631]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_valid[https://\xfc\xf1\xee\xe7\xf6d\xe9.com/path?q=1#frag]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_valid[http://www.\u0627\u062e\u062a\u0628\u0627\u0631.com:8080/path]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_invalid[m\xfcnchen.de]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_url_idn_invalid[\u09a4\u09cc\u09b9\u09bf\u09a6\u09c1\u09b0.\u09ac\u09be\u0982\u09b2\u09be]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[niceandsimple@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[NiCeAnDsImPlE@eXaMpLe.CoM]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[very.common@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[a.little.lengthy.but.fine@a.iana-servers.net]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[disposable.style.email.with+symbol@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid["very.unusual.@.unusual.com"@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[!#$%&'*+-/=?^_`{}&#124;~@example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[niceandsimple@[64.233.160.0]]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[niceandsimple@localhost]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[jos\xe9@blah.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_valid[\u03b4\u03bf\u03ba.\u03b9\u03bc\u03ae@\u03c0\u03b1\u03c1\u03ac\u03b4\u03b5\u03b9\u03b3\u03bc\u03b1.\u03b4\u03bf\u03ba\u03b9\u03bc\u03ae]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[niceandsimple\n@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[NiCeAnDsImPlE@eXaMpLe.CoM\n]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[a"b(c)d,e:f;g<h>i[j\\k]l@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[just"not"right@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[this is"not\x07llowed@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[this\\ still\\"not\\\\allowed@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid["much.more unusual"@example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid["very.(),:;<>[]".VERY."very@\\ "very".unusual"@strange.example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[" "@example.org]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[user@example]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[@nouser.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[example.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[user]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_invalid[None]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[user@m\xfcnchen.de]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[user@\u4f8b\u3048.jp]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[user@\u0645\u062b\u0627\u0644.\u0625\u062e\u062a\u0628\u0627\u0631]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[user@\u043f\u0440\u0438\u043c\u0435\u0440.\u0438\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u0435]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[user@\xfc\xf1\xee\xe7\xf6d\xe9.com]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[\u03b4\u03bf\u03ba.\u03b9\u03bc\u03ae@\u03c0\u03b1\u03c1\u03ac\u03b4\u03b5\u03b9\u03b3\u03bc\u03b1.\u03b4\u03bf\u03ba\u03b9\u03bc\u03ae]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_valid[user@sub.m\xfcnchen.de]` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_idn_invalid[user@-m\xfcnchen.de]` | atomic | Validators + Serializing and Loading a User | covered |  |
| `tests/test_validate.py::test_email_idn_invalid[user@m\xfcnchen-.de]` | atomic | Validators + Serializing and Loading a User | covered |  |
| `tests/test_validate.py::test_email_idn_invalid[user@m\xfcnchen]` | atomic | Validators + Serializing and Loading a User | covered |  |
| `tests/test_validate.py::test_email_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_email_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_range_min` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_range_max` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_range_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_range_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_length_min` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_length_max` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_length_equal` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_length_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_length_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_equal` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_equal_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_equal_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_regexp_str` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_regexp_compile` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_regexp_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_regexp_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_predicate` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_predicate_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_predicate_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_noneof` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_noneof_custom_message` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_noneof_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_oneof` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_oneof_options` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_oneof_text` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_oneof_custom_message` | atomic | Validators + Custom Fields + Custom Field Extension | covered |  |
| `tests/test_validate.py::test_oneof_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_containsonly_in_list` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_contains_only_unhashable_types` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_containsonly_in_tuple` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_contains_only_in_string` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_containsonly_custom_message` | atomic | Validators + Custom Fields + Custom Field Extension | covered |  |
| `tests/test_validate.py::test_containsonly_repr` | atomic | - | source-only | asserts exact repr text, which is outside spec |
| `tests/test_validate.py::test_containsnoneof_error_message` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |
| `tests/test_validate.py::test_containsnoneof_in_list` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_containsnoneof_unhashable_types` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_containsnoneof_in_tuple` | atomic | Validators | covered |  |
| `tests/test_validate.py::test_containsnoneof_in_string` | atomic | Validators + Public API + Validate | covered |  |
| `tests/test_validate.py::test_containsnoneof_custom_message` | atomic | Validators + Public API + Custom Fields + Validate + Custom Field Extension | covered |  |
| `tests/test_validate.py::test_containsnoneof_mixing_types` | atomic | Validators + Public API + Validate | covered |  |
| `tests/test_validate.py::test_and` | atomic | - | source-only | asserts exact default error message or error aggregation shape outside spec |

Total: 1178 | kept (covered): 832 | spec_gap: 0 | source-only: 305 | excluded: 41 | final scoreable: 832
