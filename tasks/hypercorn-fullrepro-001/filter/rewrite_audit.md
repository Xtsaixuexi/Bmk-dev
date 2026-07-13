# Hypercorn Stage 3A Rewrite Audit

Source revision: `0e2311f1ad2ae587aaa590f3824f59aa5dc0e770`

Frozen spec: `spec/spec_v1.md`

## Shared Fixture Audit

Shared helper files were scanned before node-level work:

| file | private or non-public dependency | action |
|---|---|---|
| `tests/conftest.py` | `hypercorn.typing.ConnectionState`, `hypercorn.typing.HTTPScope`, monkeypatch of `hypercorn.config.time` | Do not import in the cleanroom rewrite. Rewritten scopes use plain ASGI dictionaries, and response-header tests avoid monkeypatching private module time. |
| `tests/helpers.py` | `hypercorn.typing.*` annotations plus socket/test helper classes | Do not import in the cleanroom rewrite. Small ASGI helper apps are recreated with plain public ASGI call signatures. |
| `tests/asyncio/helpers.py` | upstream memory stream helpers used by internal TCP server tests | Discard with internal TCP server files; no public rewrite preserves the same assertion surface. |

No shared upstream fixture is copied into the cleanroom oracle.

## File-Level Rewrite Decisions

| upstream file | collected nodeids | import classification | rewrite result | failure reason or retained behavior |
|---|---:|---|---|---|
| `tests/test_config.py` | 13 | public `Config` plus socket/syscall and module-time probes | partial rewrite | Kept public file/object/TOML loading and response metadata flags. Excluded socket factory syscall assertions, inherited fd shape, exact generated date monkeypatch, and certificate-asset SSL context details. |
| `tests/test_app_wrappers.py` | 6 | internal `hypercorn.app_wrappers` and private `_build_environ` | partial rewrite | Rewrote WSGI response, max-body, and missing `start_response` behavior through public `AsyncioWSGIMiddleware` and `TrioWSGIMiddleware`. Excluded private environ builder and private exception tests. |
| `tests/test_logging.py` | 14 | public `Config`/`Logger`, non-public `AccessLogAtoms`, `hypercorn.typing` | discard; Track B | Assertions depend on non-public atom helper, logger attributes, handler classes, environment state, process id formatting, and exact status phrase fallback. Public logging behavior should be generated from the spec. |
| `tests/test_utils.py` | 11 | internal `hypercorn.utils`, `hypercorn.typing` | discard; Track B | Utility functions are not public contract; assertions target internal header/scope helpers. |
| `tests/test___main__.py` | 16 | in-process `hypercorn.__main__`, private `_load_config`, monkeypatched runner | discard; Track B | CLI behavior is public, but these tests target private in-process helpers and monkeypatched runner internals. Public subprocess-style CLI tests should be generated instead. |
| `tests/middleware/test_dispatcher.py` | 3 | non-exported dispatcher classes and `hypercorn.typing` | rewrite pass | Rewrote route selection, 404 fallback, root path extension, and lifespan broadcast through public `DispatcherMiddleware`. |
| `tests/middleware/test_http_to_https.py` | 7 | public redirect middleware plus `hypercorn.typing`; one private `_new_url` call | rewrite pass | Rewrote all redirect behaviors through public `HTTPToHTTPSRedirectMiddleware.__call__`, including the host-header case formerly asserted through `_new_url`. |
| `tests/middleware/test_proxy_fix.py` | 2 | public `ProxyFixMiddleware` plus `hypercorn.typing` | rewrite pass | Rewrote legacy and modern forwarding behavior with plain scope dictionaries and verified copied-scope effects. |
| `tests/e2e/test_httpx.py` | 2 | public Trio serve plus real network client | discard; Track B | Uses fixed external bind address and httpx network traffic; generate deterministic public service tests separately. |
| `tests/asyncio/test_keep_alive.py` | 4 | internal `TCPServer`, `WorkerContext`, upstream memory streams | discard; Track B | Tests internal asyncio server loop and HTTP/1 connection scheduling rather than public `serve()` contract. |
| `tests/asyncio/test_lifespan.py` | 4 | internal `ASGIWrapper`, `Lifespan`, private errors | discard; Track B | Lifespan service behavior is public, but these nodeids instantiate internal lifespan objects and private exception classes. |
| `tests/asyncio/test_sanity.py` | 4 | internal `TCPServer`, `WorkerContext`, upstream memory streams | discard; Track B | Protocol transport simulation is tied to internal server classes. |
| `tests/asyncio/test_task_group.py` | 2 | internal `TaskGroup`, `ASGIWrapper` | discard; Track B | Task-group spawning is not part of the public candidate surface. |
| `tests/asyncio/test_tcp_server.py` | 2 | internal `TCPServer`, `WorkerContext`, memory streams | discard; Track B | Tests TCP server half-close internals, not public `serve()` behavior. |
| `tests/trio/test_keep_alive.py` | 4 | internal Trio `TCPServer`, `WorkerContext`, test stream fixtures | discard; Track B | Tests internal Trio transport scheduling. |
| `tests/trio/test_lifespan.py` | 2 | internal `ASGIWrapper`, `Lifespan`, private errors | discard; Track B | Internal lifespan object assertions; public lifespan failure behavior should be tested through `trio.serve()`. |
| `tests/trio/test_sanity.py` | 4 | internal Trio `TCPServer`, `WorkerContext`, protocol simulators | discard; Track B | Internal transport/protocol integration; not cleanroom-portable. |
| `tests/protocol/test_h11.py` | 22 | internal protocol events, `H11Protocol`, `HTTPStream`, worker context | discard; Track B | Tests parser engine state, private events, protocol upgrades, and mocked internals outside the public surface. |
| `tests/protocol/test_h2.py` | 6 | internal `H2Protocol`, `StreamBuffer`, constants, worker context | discard; Track B | Tests buffer and protocol internals that may differ in a correct implementation. |
| `tests/protocol/test_http_stream.py` | 25 | internal `HTTPStream`, state enum, protocol events, statsd worker context | discard; Track B | Tests ASGI message engine internals and exact event objects, not public service boundary behavior. |
| `tests/protocol/test_ws_stream.py` | 43 | internal `WSStream`, buffer, state enum, protocol events, task group | discard; Track B | Tests WebSocket protocol engine internals and private state transitions. |

## Rewrite Summary

Actual rewritten tests are in `filter/rewritten_upstream_tests.py`.

| metric | count |
|---|---:|
| upstream test files with collected nodeids | 21 |
| files retained with public API extraction | 5 |
| files discarded after rewrite attempts | 16 |
| discard rate after rewrite attempts | 76.2% |
| upstream nodeids audited | 196 |
| upstream nodeids represented by public rewrites | 20 |
| upstream nodeids excluded from Track A | 176 |
| rewritten pytest nodeids passing on reference | 20 |

Because more than 50% of upstream test files are discarded after rewrite attempts, Track B is mandatory. The Stage 3 state must move from `S3A_REWRITE` to `S3B_TRIGGER` after the candidate filter map is written.
