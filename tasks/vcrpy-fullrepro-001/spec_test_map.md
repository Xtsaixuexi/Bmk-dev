# vcrpy-fullrepro-001 Spec-Test Map v5
oracle_source: upstream_filtered_reference_passed
oracle_count: 55 base nodeids / 64 expanded pytest cases
oracle_count_floor: current 50-test global floor satisfied by public upstream filter and record-mode tests.

| test_nodeid | layer | spec_section | status | notes |
|-------------|-------|--------------|--------|-------|
| `tests/integration/test_basic.py::test_basic_json_use` | system_e2e | Core Workflow + Serializers + Cross-View Invariants + Error Semantics | covered | JSON serializer can record and replay a local HTTP interaction |
| `tests/integration/test_basic.py::test_nonexistent_directory` | system_e2e | Core Workflow + Persisters + Error Semantics | covered | use_cassette creates cassette paths and records local urllib traffic |
| `tests/integration/test_basic.py::test_unpatch` | system_e2e | Core Workflow + HTTP Interception | covered | HTTP patching is scoped to cassette lifecycle and cassette play_count remains consistent |
| `tests/integration/test_config.py::test_default_set_cassette_library_dir` | integration | VCR Configuration + Persisters | covered | cassette_library_dir resolves relative cassette names |
| `tests/integration/test_config.py::test_dont_record_on_exception` | integration | Exception Handling And Saving + Error Semantics | covered | record_on_exception controls save behavior for context and decorator forms |
| `tests/integration/test_config.py::test_override_match_on` | integration | VCR Configuration + Request Matching | covered | configured match_on controls replay matching |
| `tests/integration/test_config.py::test_override_set_cassette_library_dir` | integration | VCR Configuration + Persisters | covered | per-cassette overrides supersede VCR defaults |
| `tests/integration/test_config.py::test_set_drop_unused_requests` | integration | Playback Repeats And Drop Unused | covered | drop_unused_requests updates saved cassette interactions |
| `tests/integration/test_ignore.py::test_ignore_httpbin` | integration | Ignoring Requests | covered | ignore_hosts bypasses cassette recording/replay |
| `tests/integration/test_ignore.py::test_ignore_localhost` | integration | Ignoring Requests + Cassette Public API + Automatic Cassette Naming | covered | ignore_localhost bypasses cassette recording/replay |
| `tests/integration/test_ignore.py::test_ignore_localhost_and_httpbin` | integration | Ignoring Requests | covered | ignore rules compose |
| `tests/integration/test_ignore.py::test_ignore_localhost_twice` | integration | Ignoring Requests + Cross-View Invariants + Cassette Public API + Automatic Cassette Naming | covered | ignored requests remain normal across repeated cassette contexts |
| `tests/integration/test_register_matcher.py::test_registered_false_matcher` | integration | Request Matching | covered | registered custom matcher can reject replay |
| `tests/integration/test_register_matcher.py::test_registered_true_matcher` | integration | Request Matching + Custom Patches | covered | registered custom matcher can enable replay |
| `tests/integration/test_register_serializer.py::test_registered_serializer` | integration | Serializers + Custom Patches | covered | registered custom serializer is used for load/save lifecycle |
| `tests/integration/test_request.py::test_recorded_request_uri_with_redirected_request` | integration | Request Public API + Request Matching | covered | recorded Request.uri reflects normalized redirected request sequence |
| `tests/integration/test_request.py::test_records_multiple_header_values` | integration | Request Public API + Serializers | covered | recorded response headers preserve multiple values for replay/storage |
| `tests/integration/test_requests.py::test_body` | system_e2e | Core Workflow + HTTP Interception | covered | requests client replay preserves response body |
| `tests/integration/test_requests.py::test_cross_scheme` | system_e2e | Request Matching + HTTP Interception + Cross-View Invariants | covered | scheme participates in request identity across HTTP and HTTPS |
| `tests/integration/test_requests.py::test_filter_post_params` | system_e2e | Filters And Callbacks + HTTP Interception + Record Modes | covered | post-data filtering affects recorded requests made by requests |
| `tests/integration/test_requests.py::test_get_empty_content_type_json` | system_e2e | Request Matching + HTTP Interception | covered | body matcher handles empty JSON request bodies |
| `tests/integration/test_requests.py::test_gzip__decode_compressed_response_false` | system_e2e | HTTP Interception + Serializers | covered | requests compressed response replay works without forced decode |
| `tests/integration/test_requests.py::test_gzip__decode_compressed_response_true` | system_e2e | HTTP Interception + Serializers + Cross-View Invariants | covered | decode_compressed_response alters stored response and replay headers/body consistently |
| `tests/integration/test_requests.py::test_headers` | system_e2e | HTTP Interception + Request Public API | covered | requests client replay preserves response headers |
| `tests/integration/test_requests.py::test_post` | system_e2e | Core Workflow + HTTP Interception + Record Modes | covered | requests POST record/replay preserves response content |
| `tests/integration/test_requests.py::test_redirects` | system_e2e | Core Workflow + HTTP Interception + Cross-View Invariants + Record Modes | covered | requests redirect workflow records and replays multiple interactions consistently |
| `tests/integration/test_requests.py::test_status_code` | system_e2e | HTTP Interception + Unittest Integration | covered | requests client replay preserves status_code |
| `tests/unit/test_unittest.py::test_vcr_kwargs_overridden` | integration | Unittest Integration + VCR Configuration + Cassette Public API + Custom Patches + Automatic Cassette Naming | covered | VCRTestCase _get_vcr_kwargs customizes cassette defaults |
| `tests/unit/test_unittest.py::test_vcr_kwargs_passed` | integration | Unittest Integration + VCR Configuration | covered | VCRTestCase passes explicit VCR kwargs through |
| `tests/unit/test_filters.py::test_replace_headers` | atomic | Filters And Callbacks + Request Public API | covered | public header filter keeps, removes, and replaces configured values |
| `tests/unit/test_filters.py::test_replace_headers_empty` | atomic | Filters And Callbacks + Request Public API | covered | an empty filter configuration leaves headers unchanged |
| `tests/unit/test_filters.py::test_remove_headers` | atomic | Filters And Callbacks + Request Public API | covered | public remove wrapper removes selected header values |
| `tests/unit/test_filters.py::test_replace_query_parameters` | atomic | Filters And Callbacks + Request Public API | covered | query filters keep, remove, and replace configured values |
| `tests/unit/test_filters.py::test_remove_all_query_parameters` | atomic | Filters And Callbacks + Request Public API | covered | removing all query values updates the public URI consistently |
| `tests/unit/test_filters.py::test_remove_query_parameters` | atomic | Filters And Callbacks + Request Public API | covered | public remove wrapper removes selected query values |
| `tests/unit/test_filters.py::test_replace_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | form post-data filters keep, remove, and replace configured values |
| `tests/unit/test_filters.py::test_replace_post_data_parameters_empty_body` | atomic | Filters And Callbacks + Request Public API | covered | filtering an absent request body preserves the absent body |
| `tests/unit/test_filters.py::test_remove_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | public remove wrapper removes selected form values |
| `tests/unit/test_filters.py::test_preserve_multiple_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | repeated unfiltered form values remain ordered and present |
| `tests/unit/test_filters.py::test_remove_all_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | removing all form values produces an empty body |
| `tests/unit/test_filters.py::test_replace_json_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | JSON post-data filters preserve, remove, and replace fields |
| `tests/unit/test_filters.py::test_remove_json_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | public remove wrapper removes selected JSON fields |
| `tests/unit/test_filters.py::test_remove_all_json_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | removing all JSON fields produces an empty object |
| `tests/unit/test_filters.py::test_replace_dict_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | mapping post-data filters preserve, remove, and replace fields |
| `tests/unit/test_filters.py::test_remove_dict_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | public remove wrapper removes selected mapping fields |
| `tests/unit/test_filters.py::test_remove_all_dict_post_data_parameters` | atomic | Filters And Callbacks + Request Public API | covered | removing all mapping fields produces an empty mapping |
| `tests/unit/test_filters.py::test_decode_response_uncompressed` | atomic | Filters And Callbacks | covered | response decoding leaves uncompressed bodies unchanged |
| `tests/unit/test_filters.py::test_decode_response_deflate` | atomic | Filters And Callbacks | covered | deflate bodies decode before recording and update observable length |
| `tests/unit/test_filters.py::test_decode_response_deflate_already_decompressed` | atomic | Filters And Callbacks | covered | already-decoded deflate bodies remain usable |
| `tests/unit/test_filters.py::test_decode_response_gzip` | atomic | Filters And Callbacks | covered | gzip bodies decode before recording and update observable length |
| `tests/unit/test_filters.py::test_decode_response_gzip_already_decompressed` | atomic | Filters And Callbacks | covered | already-decoded gzip bodies remain usable |
| `tests/integration/test_record_mode.py::test_once_record_mode` | system_e2e | Record Modes + Error Semantics + Core Workflow | covered | once mode replays known traffic and rejects a new unmatched request |
| `tests/integration/test_record_mode.py::test_new_episodes_record_mode` | system_e2e | Record Modes + Playback Repeats And Drop Unused + Cassette Public API | covered | new-episodes mode keeps all_played and play_count projections consistent |
| `tests/integration/test_record_mode.py::test_new_episodes_record_mode_two_times` | system_e2e | Record Modes + Playback Repeats And Drop Unused + Cross-View Invariants | covered | repeated interactions remain ordered and replayable across record modes |
| `tests/integration/test_record_mode.py::test_none_record_mode` | system_e2e | Record Modes + Error Semantics | covered | none mode rejects unmatched network traffic with the public VCR error |

Total: 309 | kept (covered): 55 | spec_gap: 0 | source-only: 0 | excluded: 254 | final scoreable: 55
