# Hypercorn Stage 3A Candidate Filter Map

| upstream test | status | spec section | rewritten target / exclusion reason |
|---|---|---|---|
| `tests/asyncio/test_keep_alive.py::test_http1_keep_alive_pre_request` | excluded | - | excluded: internal asyncio TCPServer/WorkerContext transport behavior |
| `tests/asyncio/test_keep_alive.py::test_http1_keep_alive_during` | excluded | - | excluded: internal asyncio TCPServer/WorkerContext transport behavior |
| `tests/asyncio/test_keep_alive.py::test_http1_keep_alive` | excluded | - | excluded: internal asyncio TCPServer/WorkerContext transport behavior |
| `tests/asyncio/test_keep_alive.py::test_http1_keep_alive_pipelining` | excluded | - | excluded: internal asyncio TCPServer/WorkerContext transport behavior |
| `tests/asyncio/test_lifespan.py::test_ensure_no_race_condition` | excluded | - | excluded: internal Lifespan/ASGIWrapper/private error surface |
| `tests/asyncio/test_lifespan.py::test_startup_timeout_error` | excluded | - | excluded: internal Lifespan/ASGIWrapper/private error surface |
| `tests/asyncio/test_lifespan.py::test_startup_failure` | excluded | - | excluded: internal Lifespan/ASGIWrapper/private error surface |
| `tests/asyncio/test_lifespan.py::test_lifespan_return` | excluded | - | excluded: internal Lifespan/ASGIWrapper/private error surface |
| `tests/asyncio/test_sanity.py::test_http1_request` | excluded | - | excluded: internal asyncio TCPServer protocol simulator |
| `tests/asyncio/test_sanity.py::test_http1_websocket` | excluded | - | excluded: internal asyncio TCPServer protocol simulator |
| `tests/asyncio/test_sanity.py::test_http2_request` | excluded | - | excluded: internal asyncio TCPServer protocol simulator |
| `tests/asyncio/test_sanity.py::test_http2_websocket` | excluded | - | excluded: internal asyncio TCPServer protocol simulator |
| `tests/asyncio/test_task_group.py::test_spawn_app` | excluded | - | excluded: internal TaskGroup/ASGIWrapper behavior |
| `tests/asyncio/test_task_group.py::test_spawn_app_error` | excluded | - | excluded: internal TaskGroup/ASGIWrapper behavior |
| `tests/asyncio/test_tcp_server.py::test_completes_on_closed` | excluded | - | excluded: internal TCPServer stream half-close behavior |
| `tests/asyncio/test_tcp_server.py::test_complets_on_half_close` | excluded | - | excluded: internal TCPServer stream half-close behavior |
| `tests/e2e/test_httpx.py::test_keep_alive_max_requests_regression` | excluded | - | excluded: fixed network bind/httpx workflow; deterministic public service coverage deferred to Track B |
| `tests/e2e/test_httpx.py::test_handle_isolate_state` | excluded | - | excluded: fixed network bind/httpx workflow; deterministic public service coverage deferred to Track B |
| `tests/middleware/test_dispatcher.py::test_dispatcher_middleware` | covered | Dispatching Applications | rewritten_upstream_tests.py::test_dispatcher_routes_by_insertion_order_and_updates_root_path + test_dispatcher_returns_404_when_no_mount_matches |
| `tests/middleware/test_dispatcher.py::test_asyncio_dispatcher_lifespan` | covered | Dispatching Applications | rewritten_upstream_tests.py::test_dispatcher_broadcasts_lifespan_to_mounted_applications |
| `tests/middleware/test_dispatcher.py::test_trio_dispatcher_lifespan` | covered | Dispatching Applications | rewritten_upstream_tests.py::test_dispatcher_broadcasts_lifespan_to_mounted_applications |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_middleware_http[/abc]` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_http_raw_path_and_query |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_middleware_http[/abc%3C]` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_http_raw_path_and_query |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_middleware_websocket[/abc]` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_websocket_raw_path_and_query |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_middleware_websocket[/abc%3C]` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_websocket_raw_path_and_query |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_middleware_websocket_http2` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_uses_https_scheme_for_http2_websocket |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_middleware_websocket_no_rejection` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_closes_websocket_without_denial_extension |
| `tests/middleware/test_http_to_https.py::test_http_to_https_redirect_new_url_header` | covered | Redirecting HTTP to HTTPS | rewritten_upstream_tests.py::test_http_to_https_redirect_uses_request_host_when_constructor_host_is_none |
| `tests/middleware/test_proxy_fix.py::test_proxy_fix_legacy` | covered | Restoring Proxy Information | rewritten_upstream_tests.py::test_proxy_fix_legacy_restores_trusted_client_scheme_and_host |
| `tests/middleware/test_proxy_fix.py::test_proxy_fix_modern` | covered | Restoring Proxy Information | rewritten_upstream_tests.py::test_proxy_fix_modern_restores_trusted_client_scheme_and_host |
| `tests/protocol/test_h11.py::test_protocol_send_response` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_preserve_headers` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_send_data` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_send_body` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_keep_alive_max_requests` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_send_stream_closed[True-expected0]` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_send_stream_closed[False-expected1]` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_instant_recycle` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_send_end_data` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_closed` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_request` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_request_with_raw_headers` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_protocol_error` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_send_client_error` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_pipelining` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_continue_request` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_max_incomplete` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_h2c_upgrade` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_h2_prior` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_data_post_response` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_data_post_end` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h11.py::test_protocol_handle_data_post_close` | excluded | - | excluded: internal h11 protocol engine, private events, and mocked protocol internals |
| `tests/protocol/test_h2.py::test_stream_buffer_push_and_pop` | excluded | - | excluded: internal h2 protocol/buffer engine and constants |
| `tests/protocol/test_h2.py::test_stream_buffer_drain` | excluded | - | excluded: internal h2 protocol/buffer engine and constants |
| `tests/protocol/test_h2.py::test_stream_buffer_closed` | excluded | - | excluded: internal h2 protocol/buffer engine and constants |
| `tests/protocol/test_h2.py::test_stream_buffer_complete` | excluded | - | excluded: internal h2 protocol/buffer engine and constants |
| `tests/protocol/test_h2.py::test_protocol_handle_protocol_error` | excluded | - | excluded: internal h2 protocol/buffer engine and constants |
| `tests/protocol/test_h2.py::test_protocol_keep_alive_max_requests` | excluded | - | excluded: internal h2 protocol/buffer engine and constants |
| `tests/protocol/test_http_stream.py::test_handle_request_http_1[1.0]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_handle_request_http_1[1.1]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_handle_request_http_2` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_handle_body` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_handle_end_body` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_handle_closed` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_response` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_invalid_server_name` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_push` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_early_hint` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_trailers` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_trailers_ignored` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_app_error` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message_given_state[ASGIHTTPState.REQUEST-not_a_real_type]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message_given_state[ASGIHTTPState.RESPONSE-http.response.start]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message_given_state[ASGIHTTPState.TRAILERS-http.response.start]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message_given_state[ASGIHTTPState.CLOSED-http.response.start]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message_given_state[ASGIHTTPState.CLOSED-http.response.body]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message_given_state[ASGIHTTPState.CLOSED-http.response.trailers]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message[201 NO CONTENT-headers0-]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message[200-headers1-]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_send_invalid_message[200-headers2-Body]` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_stream_idle` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_closure` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_http_stream.py::test_abnormal_close_logging` | excluded | - | excluded: internal HTTPStream state machine and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_buffer` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_buffer_frame_too_large` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_buffer_mixed_types[data0]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_buffer_mixed_types[data1]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_validity[headers0-1.0-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_validity[headers1-1.1-True]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_validity[headers2-1.1-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_validity[headers3-1.1-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_validity[headers4-2-True]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_validity[headers5-2-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_accept_http1` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_accept_http2` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handshake_accept_additional_headers` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handle_request` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handle_data_before_acceptance` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handle_connection` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_handle_closed` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_accept` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_accept_with_additional_headers` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_reject` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_invalid_server_name` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_app_error_handshake` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_app_error_connected` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_connection` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_pings` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.HANDSHAKE-websocket.send]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.RESPONSE-websocket.accept]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.RESPONSE-websocket.send]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.CONNECTED-websocket.http.response.start]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.CONNECTED-websocket.http.response.body]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.CLOSED-websocket.send]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.CLOSED-websocket.http.response.start]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_message_given_state[ASGIWebsocketState.CLOSED-websocket.http.response.body]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_http_message[201 NO CONTENT-headers0-]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_http_message[200-headers1-]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_send_invalid_http_message[200-headers2-Body]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_stream_idle[ASGIWebsocketState.HANDSHAKE-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_stream_idle[ASGIWebsocketState.CONNECTED-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_stream_idle[ASGIWebsocketState.RESPONSE-False]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_stream_idle[ASGIWebsocketState.CLOSED-True]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_stream_idle[ASGIWebsocketState.HTTPCLOSED-True]` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_closure` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/protocol/test_ws_stream.py::test_closed_app_send_noop` | excluded | - | excluded: internal WSStream state machine, buffer, and protocol event objects |
| `tests/test___main__.py::test_load_config_none` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_load_config_pyfile` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_load_config_pymodule` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_load_config` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--access-logformat-jeff-access_log_format]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--backlog-5-backlog]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--ca-certs-/path-ca_certs]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--certfile-/path-certfile]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--ciphers-DHE-RSA-AES128-SHA-ciphers]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--worker-class-trio-worker_class]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--keep-alive-20-keep_alive_timeout]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--keyfile-/path-keyfile]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--pid-/path-pid_path]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--root-path-/path-root_path]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_main_cli_override[--workers-2-workers]` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test___main__.py::test_verify_mode_conversion` | excluded | - | excluded: private in-process __main__ helper or monkeypatched runner; public CLI behavior deferred to Track B |
| `tests/test_app_wrappers.py::test_wsgi_trio` | covered | Adapting WSGI Applications | rewritten_upstream_tests.py::test_trio_wsgi_middleware_emits_wsgi_response_body |
| `tests/test_app_wrappers.py::test_wsgi_asyncio` | covered | Adapting WSGI Applications | rewritten_upstream_tests.py::test_asyncio_wsgi_middleware_emits_wsgi_response_body |
| `tests/test_app_wrappers.py::test_max_body_size` | covered | Adapting WSGI Applications | rewritten_upstream_tests.py::test_asyncio_wsgi_middleware_returns_400_when_body_exceeds_limit |
| `tests/test_app_wrappers.py::test_no_start_response` | covered | Adapting WSGI Applications | rewritten_upstream_tests.py::test_asyncio_wsgi_middleware_requires_start_response_before_body |
| `tests/test_app_wrappers.py::test_build_environ_encoding` | excluded | - | excluded: private app_wrappers environ builder or private exception surface |
| `tests/test_app_wrappers.py::test_build_environ_root_path` | excluded | - | excluded: private app_wrappers environ builder or private exception surface |
| `tests/test_config.py::test_config_from_pyfile` | covered | Creating and Loading Configuration | rewritten_upstream_tests.py::test_config_from_pyfile_loads_public_attributes |
| `tests/test_config.py::test_config_from_object` | covered | Creating and Loading Configuration | rewritten_upstream_tests.py::test_config_from_object_loads_public_attributes |
| `tests/test_config.py::test_ssl_config_from_pyfile` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_config_from_toml` | covered | Creating and Loading Configuration | rewritten_upstream_tests.py::test_config_from_toml_loads_public_attributes |
| `tests/test_config.py::test_create_ssl_context` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_ip[127.0.0.1:5000-AddressFamily.AF_INET-expected_binding0]` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_ip[127.0.0.1-AddressFamily.AF_INET-expected_binding1]` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_ip[[::]:5000-AddressFamily.AF_INET6-expected_binding2]` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_ip[[::]-AddressFamily.AF_INET6-expected_binding3]` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_unix` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_fd` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_create_sockets_multiple` | source-only | - | source-only: socket factory, inherited fd, exact date monkeypatch, or certificate asset assertion not retained in public rewrite |
| `tests/test_config.py::test_response_headers` | covered | Response Metadata and Metrics | rewritten_upstream_tests.py::test_config_response_headers_follow_metadata_flags |
| `tests/test_logging.py::test_access_logger_init[--hypercorn.access-StreamHandler]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_logger_init[/tmp/path-hypercorn.access-FileHandler]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_logger_init[target2-test_special-None]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_logger_init[None-None-None]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_loglevel_option[DEBUG-10]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_loglevel_option[INFO-20]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_loglevel_option[WARNING-30]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_loglevel_option[ERROR-40]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_loglevel_option[CRITICAL-50]` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_log_standard_atoms` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_log_header_atoms` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_no_log_header_atoms` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_access_log_environ_atoms` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_logging.py::test_nonstandard_status_code` | source-only | - | source-only: non-public AccessLogAtoms, logger attribute/handler shape, environment/process formatting, or exact fallback phrase |
| `tests/test_utils.py::test_suppress_body[HEAD-200-True]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_suppress_body[GET-200-False]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_suppress_body[GET-101-True]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_is_asgi[app0-False]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_is_asgi[app1-True]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_is_asgi[wsgi_callable-False]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_is_asgi[asgi_callable-True]` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_build_and_validate_headers_validate` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_build_and_validate_headers_pseudo` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_filter_pseudo_headers` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/test_utils.py::test_filter_pseudo_headers_no_authority` | excluded | - | excluded: internal hypercorn.utils/helper behavior outside public surface |
| `tests/trio/test_keep_alive.py::test_http1_keep_alive_pre_request` | excluded | - | excluded: internal Trio TCPServer/WorkerContext transport behavior |
| `tests/trio/test_keep_alive.py::test_http1_keep_alive_during` | excluded | - | excluded: internal Trio TCPServer/WorkerContext transport behavior |
| `tests/trio/test_keep_alive.py::test_http1_keep_alive` | excluded | - | excluded: internal Trio TCPServer/WorkerContext transport behavior |
| `tests/trio/test_keep_alive.py::test_http1_keep_alive_pipelining` | excluded | - | excluded: internal Trio TCPServer/WorkerContext transport behavior |
| `tests/trio/test_lifespan.py::test_startup_timeout_error` | excluded | - | excluded: internal Lifespan/ASGIWrapper/private error surface |
| `tests/trio/test_lifespan.py::test_startup_failure` | excluded | - | excluded: internal Lifespan/ASGIWrapper/private error surface |
| `tests/trio/test_sanity.py::test_http1_request` | excluded | - | excluded: internal Trio TCPServer protocol simulator |
| `tests/trio/test_sanity.py::test_http1_websocket` | excluded | - | excluded: internal Trio TCPServer protocol simulator |
| `tests/trio/test_sanity.py::test_http2_request` | excluded | - | excluded: internal Trio TCPServer protocol simulator |
| `tests/trio/test_sanity.py::test_http2_websocket` | excluded | - | excluded: internal Trio TCPServer protocol simulator |

Total: 196 | covered: 20 | spec_gap: 0 | source-only: 23 | excluded: 153 | final Track A original coverage: 20
