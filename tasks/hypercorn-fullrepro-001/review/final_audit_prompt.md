# Final Audit Prompt: Hypercorn Benchmark Package

You are auditing a completed SWE-E2E benchmark package for Hypercorn. Review only the artifacts included in this prompt. Do not assume access to repository source, prior model reviews, hidden tests, or previous audit conclusions.

Return a concise structured report with this exact shape:

VERDICT: PASS_FINAL_AUDIT | FAIL_FINAL_AUDIT
LIKE_A_DEVELOPER: PASS | FAIL - reason
SPEC_DRIVEN: PASS | FAIL - reason
BEHAVIORAL: PASS | FAIL - reason
Q1_PUBLIC_CONTRACT: PASS | FAIL - reason
Q2_NON_DERIVABLE_BALANCE: PASS | FAIL - reason
AUTHOR_SPEC_VOICE: PASS | FAIL - reason
STATE_MODEL_AND_INVARIANTS: PASS | FAIL - reason
ERROR_AND_PRECEDENCE_SEMANTICS: PASS | FAIL - reason
ORACLE_FAIRNESS: PASS | FAIL - reason
REFERENCE_DUMMY_CANDIDATE_GATES: PASS | FAIL - reason
PROCESS_LEAKAGE: NONE | FOUND - details
SATURATION_CAVEAT_HANDLED: PASS | FAIL - reason
BLOCKERS:
- list blockers, or NONE
CAVEATS:
- list caveats, or NONE
QUALIFICATION_RECOMMENDATION: QUALIFIED | QUALIFIED_WITH_CAVEATS | REPAIR_REQUIRED | RETIRE

Audit criteria:
- Like a developer: the spec must read like formal author-to-user documentation, not benchmark instructions or test answers.
- Spec-driven: every final oracle row must map to a real spec section and be derivable from it.
- Behavioral: oracle checks public observable behavior, not private modules, private state, exact reprs, internal helpers, exact diagnostic wording, or implementation shape.
- Q1 public contract: retained behavior must be public API/CLI/service/middleware contract.
- Q2 non-derivable balance: the spec must capture non-obvious behavior without becoming a test blueprint.
- Required structure: product state model, at least six cross-view invariants, failure semantics, precedence semantics, non-goals.
- No process leakage: candidate-visible spec must not mention benchmark process, hidden tests, task ids, source paths, scores, model reviews, or implementation blueprint.
- Final package gate: reference 100%, dummy 0%, candidate scored with provenance. If candidate score is saturated, verify the caveat is explicitly recorded rather than hidden.



## Candidate-visible spec.md

```text
# Hypercorn

## Product Overview

Hypercorn is an ASGI and WSGI application server. It serves HTTP/1.1, HTTP/2, and WebSocket applications with asyncio, uvloop, or Trio workers, and it supports optional HTTP/3 service when the HTTP/3 extra is installed. Applications are launched from the `hypercorn` command or served inside an existing asyncio or Trio event loop.

Hypercorn uses one configuration model across command-line and programmatic operation. The same model controls application loading, network binds, TLS, worker behavior, protocol limits, logging, and graceful shutdown. The included middleware adapts WSGI applications, dispatches requests among ASGI applications, redirects insecure traffic, and restores client information supplied by trusted proxies.

## Scope

This document covers:

- the `hypercorn` command and application-path syntax;
- the `Config` object, documented configuration sources, defaults, normalization, and precedence;
- programmatic service with asyncio and Trio;
- the middleware exported by `hypercorn.middleware`;
- application dispatch, proxy correction, HTTPS redirects, and WSGI adaptation;
- observable startup, shutdown, request-routing, response-header, and logging behavior.

The ASGI and WSGI specifications remain the authority for application call signatures and message schemas. Hypercorn-specific behavior at those boundaries is defined below.

## Product State Model

A running service has three public projections of one state:

1. **Configuration projection.** A `Config` instance contains the effective application path, bind groups, TLS settings, worker policy, protocol limits, log destinations, and lifecycle timeouts. A configuration file supplies the initial values and explicitly supplied command-line options replace the corresponding values.
2. **Application projection.** Hypercorn loads or receives an ASGI or WSGI application, optionally wraps it in middleware, and exposes request, WebSocket, and lifespan events according to the selected mode and worker backend.
3. **Service projection.** Bound endpoints, response headers, status codes, access records, metrics, and graceful-shutdown completion are observable consequences of the effective configuration and application behavior.

Changing a `Config` attribute before service startup changes both the application and service projections that depend on it. Configuration is consumed when service starts; command-line parsing and programmatic `serve()` do not create separate configuration dialects.

## Installable Surface

Hypercorn installs the `hypercorn` command and the following Python interfaces:

```python
from hypercorn import Config
from hypercorn.config import Config
from hypercorn.asyncio import serve as asyncio_serve
from hypercorn.trio import serve as trio_serve
from hypercorn.logging import Logger
from hypercorn.middleware import (
    AsyncioWSGIMiddleware,
    DispatcherMiddleware,
    HTTPToHTTPSRedirectMiddleware,
    ProxyFixMiddleware,
    TrioWSGIMiddleware,
)
```

`Config` imported from `hypercorn` and `hypercorn.config` is the same public configuration class.

## Configuration

### Creating and Loading Configuration

```python
class Config:
    @classmethod
    def from_mapping(cls, mapping=None, **kwargs) -> "Config": ...

    @classmethod
    def from_toml(cls, filename) -> "Config": ...

    @classmethod
    def from_pyfile(cls, filename) -> "Config": ...

    @classmethod
    def from_object(cls, instance) -> "Config": ...

    def set_statsd_logger_class(self, statsd_logger: type[Logger]) -> None: ...
```

- `Config()` returns a mutable configuration with the defaults listed below.
- `from_mapping()` applies entries from `mapping`, then applies keyword arguments. A keyword argument must therefore win when both sources contain the same name.
- `from_toml()` reads top-level TOML keys and applies them as configuration attributes. An unreadable or malformed file must propagate the corresponding file or TOML parsing exception.
- `from_pyfile()` executes the named Python file and applies its configuration attributes. Import and execution failures must propagate to the caller.
- `from_object()` accepts an object or a dotted import string. A dotted string names either a module or an object inside a module. Import and attribute lookup failures must propagate when the requested object cannot be resolved.
- `bind`, `insecure_bind`, and `quic_bind` accept either one string or a list of strings. Assigning one string must expose a one-element list when the attribute is read.
- Assigning `root_path` must remove trailing `/` characters; assigning `"/api/"` must therefore return `"/api"` when read.

### Documented Defaults

The following values are part of the default configuration:

| Attribute | Default |
|---|---|
| `access_log_format` | `%(h)s %(l)s %(l)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"` |
| `accesslog` | `None` |
| `alpn_protocols` | `["h2", "http/1.1"]` |
| `backlog` | `100` |
| `bind` | `["127.0.0.1:8000"]` |
| `ciphers` | `"ECDHE+AESGCM"` |
| `debug` | `False` |
| `errorlog` | `"-"` |
| `graceful_timeout` | `3` seconds |
| `h11_max_incomplete_size` | `16384` bytes |
| `h11_pass_raw_headers` | `False` |
| `h2_max_concurrent_streams` | `100` |
| `h2_max_header_list_size` | `65536` bytes |
| `h2_max_inbound_frame_size` | `16384` bytes |
| `include_date_header` | `True` |
| `include_server_header` | `True` |
| `insecure_bind` | `[]` |
| `keep_alive_max_requests` | `1000` |
| `keep_alive_timeout` | `5` seconds |
| `loglevel` | `"INFO"` |
| `max_app_queue_size` | `10` |
| `max_requests` | `None` |
| `max_requests_jitter` | `0` |
| `quic_bind` | `[]` |
| `read_timeout` | `None` |
| `root_path` | `""` |
| `server_names` | `[]` |
| `shutdown_timeout` | `60` seconds |
| `ssl_handshake_timeout` | `60` seconds |
| `startup_timeout` | `60` seconds |
| `statsd_prefix` | `""` |
| `use_reloader` | `False` |
| `websocket_max_message_size` | `16777216` bytes |
| `websocket_ping_interval` | `None` |
| `worker_class` | `"asyncio"` |
| `workers` | `1` |
| `wsgi_max_body_size` | `16777216` bytes |

Certificate paths, key passwords, logging configuration, PID path, StatsD host, user, group, umask, verification settings, and optional Alt-Svc values default to no configured value unless listed otherwise.

### Binds and TLS

- TCP binds accept `host:port`, `host`, and bracketed IPv6 forms. Omitting the port selects port `8000`.
- Unix-domain binds use `unix:/path/to/socket`. `umask`, `user`, and `group` control a created Unix socket when configured.
- Existing file descriptors use `fd://<number>` and must refer to the required socket type; a mismatched socket type must fail rather than being silently repurposed.
- Repeated bind values represent simultaneous listeners. `bind` is the normal listener group, `insecure_bind` remains plaintext when TLS is enabled, and `quic_bind` is the UDP listener group used for HTTP/3.
- TLS is enabled only when both `certfile` and `keyfile` are non-`None`. `ssl_enabled` returns that condition.
- `create_ssl_context()` returns `None` when TLS is not enabled. When enabled, it returns a server context using the configured certificate, key, key password, CA certificates, cipher string, ALPN protocols, verification mode, and verification flags; the minimum TLS version is TLS 1.2 and compression is disabled.
- `server_names` restricts accepted Host values. When the list is non-empty, an HTTP request whose Host value is absent from the list must receive a 404 response. An empty list accepts any Host value.

### Response Metadata and Metrics

- `response_headers(protocol)` returns byte-pair headers for service-generated metadata. It must include `date` when `include_date_header` is true and `server: hypercorn-<protocol>` when `include_server_header` is true.
- Every value in `alt_svc_headers` must appear as a separate `alt-svc` response header. Configured values take precedence over automatically derived HTTP/3 Alt-Svc values.
- Setting `statsd_host` enables StatsD output. `statsd_prefix` prefixes metric names and `dogstatsd_tags` supplies DogStatsD tags.
- `set_statsd_logger_class()` selects the supplied class only when `statsd_host` is configured and `logger_class` is still Hypercorn's default `Logger`. An explicitly customized `logger_class` must not be replaced.
- StatsD output covers request count, request duration, response-status count, and critical, error, warning, and exception log counts.

## Command-Line Service

```console
hypercorn [OPTIONS] MODULE_APP
```

`MODULE_APP` normally has the form `package.module:application`. A module without `:application` uses the name `app`. Prefixing the value with `asgi:` or `wsgi:` forces the corresponding application mode. A missing module or named application must terminate startup with a non-success result.

`-c` or `--config` chooses the initial configuration source:

- an unprefixed path is a TOML file;
- `file:<path>` is a Python file;
- `python:<dotted.name>` is a Python module or object.

Explicit command-line values must override values loaded from that source. Values not supplied on the command line must remain unchanged. The positional application always becomes `application_path`. Repeated `--bind`, `--insecure-bind`, `--quic-bind`, and `--server-name` options preserve their command-line order and, when present, replace the corresponding configured list.

The command exposes the documented configuration controls, including access and error log destinations, backlog, certificate and key files, ciphers, debug mode, graceful and read timeouts, worker class and count, keep-alive timeout, logging configuration and level, maximum requests and jitter, PID path, reload mode, root path, StatsD destination and prefix, Unix-socket ownership and mask, TLS verification mode, and WebSocket ping interval. `--verify-mode` accepts names from Python's `ssl.VerifyMode`; an unknown name is an invocation error.

`--access-logfile -` writes access records to stdout. `--error-logfile -` writes error records to stderr. Other non-`None` values are paths. The older `--access-log` and `--error-log` forms remain accepted but emit deprecation warnings.

## Programmatic Service

### asyncio

```python
async def hypercorn.asyncio.serve(
    app,
    config: Config,
    *,
    shutdown_trigger=None,
    mode: Literal["asgi", "wsgi"] | None = None,
) -> None: ...
```

### Trio

```python
async def hypercorn.trio.serve(
    app,
    config: Config,
    *,
    shutdown_trigger=None,
    task_status=trio.TASK_STATUS_IGNORED,
    mode: Literal["asgi", "wsgi"] | None = None,
) -> None: ...
```

- `serve()` runs inside the caller's existing event-loop environment. It must not configure a new loop or create a separate worker process.
- `mode="asgi"` and `mode="wsgi"` force application adaptation. With `mode=None`, Hypercorn selects the mode from whether the application callable is asynchronous.
- When `shutdown_trigger` is provided, Hypercorn awaits the awaitable returned by that callable. Its completion initiates graceful shutdown and waits for normal lifespan shutdown up to the configured timeout.
- `worker_class` and `workers` are process-launch settings and do not alter programmatic service. A `workers` value other than `1` must emit a warning. Enabling `debug` through `Config` must likewise emit a warning because loop-level debug setup is controlled by the caller.
- Trio service must report its bound endpoint descriptions through a supplied `task_status` when startup completes.
- Startup or shutdown lifespan timeouts and explicit lifespan failure messages must fail service rather than report successful lifecycle completion.

## Middleware

### Dispatching Applications

```python
DispatcherMiddleware(mounts: dict[str, ASGI_application])
```

Mount keys are root paths without trailing slashes. For each HTTP or WebSocket scope, `DispatcherMiddleware` selects the first insertion-ordered key for which `scope["path"].startswith(key)` is true. More-specific paths must therefore be inserted before less-specific paths.

The selected application receives a copied scope whose `root_path` is extended by the matched mount. The request `path` remains unchanged. If no mount matches, the middleware returns an empty 404 HTTP response. A lifespan request is broadcast to every mounted application; one startup or shutdown completion is sent upstream only after all mounted applications report that completion.

### Redirecting HTTP to HTTPS

```python
HTTPToHTTPSRedirectMiddleware(app, host: str | None)
```

- An HTTP scope with scheme `http` must receive status 307 and a `location` built from `https`, the redirect host, `root_path + raw_path`, and the original query string.
- A WebSocket scope with scheme `ws` and the `websocket.http.response` extension must receive a 307 denial response. The redirect scheme is `wss` for HTTP/1.x WebSockets and `https` for HTTP/2 WebSockets.
- A `ws` scope without that extension must receive `websocket.close` because a redirect response cannot be represented.
- Scopes already using secure schemes and non-HTTP/WebSocket scopes must be passed to the wrapped application unchanged.
- A non-`None` constructor `host` is authoritative. When it is `None`, the middleware uses the request Host header. If neither source provides a host, redirect construction raises `ValueError`.
- The middleware preserves the encoded `raw_path` and query string in the redirect target rather than decoding and re-encoding them.

### Restoring Proxy Information

```python
ProxyFixMiddleware(
    app,
    mode: Literal["legacy", "modern"] = "legacy",
    trusted_hops: int = 1,
)
```

For HTTP and WebSocket scopes, the middleware passes a copied scope to the application and leaves the caller's original scope unchanged.

- In `legacy` mode it reads `X-Forwarded-For`, `X-Forwarded-Proto`, and `X-Forwarded-Host`.
- In `modern` mode it reads the `for`, `proto`, and `host` parameters from `Forwarded`. If no trusted `Forwarded` value is available, legacy headers are used.
- Comma-separated proxy values are ordered from the original client toward the proxy nearest Hypercorn. The trusted value is the item `trusted_hops` positions from the right. If fewer values exist, that field must remain unchanged.
- A trusted client value replaces `scope["client"]` with `(value, 0)`. A trusted protocol replaces `scope["scheme"]`. A trusted host removes existing Host headers and appends one Host header with the trusted value.
- `trusted_hops=0` trusts no forwarded value. Lifespan and other non-HTTP scopes pass through without proxy-derived changes.

### Adapting WSGI Applications

```python
AsyncioWSGIMiddleware(wsgi_app, max_body_size: int = 65536)
TrioWSGIMiddleware(wsgi_app, max_body_size: int = 65536)
```

Each class exposes a WSGI application as an ASGI callable using the named concurrency backend. The standalone middleware default of 65536 bytes is independent from `Config.wsgi_max_body_size`, whose default applies when Hypercorn performs WSGI adaptation itself.

- HTTP request body chunks are collected into `wsgi.input` before invoking the WSGI application. If their combined size exceeds `max_body_size`, the middleware returns an empty 400 response and must not call the application.
- The WSGI environment reflects the ASGI method, root path, path, query string, server, client, protocol, scheme, headers, and body. `SCRIPT_NAME` is `root_path`; `PATH_INFO` is the remaining path. A path outside the root path returns an empty 404 response.
- `Content-Type` and `Content-Length` map to `CONTENT_TYPE` and `CONTENT_LENGTH`; other headers map to `HTTP_<UPPERCASE_NAME>`. Repeated values for one environment key are comma-joined.
- The first WSGI body item requires a prior `start_response` call. If the application yields body data without calling `start_response`, the middleware raises `RuntimeError`.
- Response header names are lowercased and encoded with Latin-1. Every yielded body item is emitted in order, and a response iterable with `close()` must be closed even when response iteration fails.
- WebSocket scopes receive `websocket.close`. Lifespan scopes complete without invoking the WSGI application.

## Logging

```python
class Logger:
    def __init__(self, config: Config) -> None: ...
    async def access(self, request, response, request_time: float) -> None: ...
    async def critical(self, message, *args, **kwargs) -> None: ...
    async def error(self, message, *args, **kwargs) -> None: ...
    async def warning(self, message, *args, **kwargs) -> None: ...
    async def info(self, message, *args, **kwargs) -> None: ...
    async def debug(self, message, *args, **kwargs) -> None: ...
    async def exception(self, message, *args, **kwargs) -> None: ...
```

`Config.logger_class` selects the logger implementation; `Logger` is the default. Access records use `Config.access_log_format`. Supported atoms include remote address (`h`), request line with or without query (`r`, `R`), method (`m`), path (`U`, `Uq`), query (`q`), protocol (`H`), status and phrase (`s`, `st`), scheme (`S`), response size (`B`, `b`), referer (`f`), user agent (`a`), durations (`T`, `D`, `L`), process ID (`p`), request and response headers (`{Header}i`, `{Header}o`), and environment variables (`{Variable}e`). A missing atom must render as `-` rather than fail access logging.

`logconfig_dict` is applied as a Python logging dictionary configuration. `logconfig` uses logging's file configuration by default; `json:` and `toml:` prefixes load dictionary configurations from the named file.

## Error Semantics

- An application path with an unsupported explicit mode, a missing module, or a missing application object must fail startup before binding service endpoints.
- A malformed command line or invalid typed option must terminate command processing with a non-success result.
- Configuration file read, parse, import, and execution errors must propagate; Hypercorn must not continue with silent defaults after an explicitly selected configuration fails.
- A TLS context request with TLS disabled returns `None`. Invalid certificate, key, CA, cipher, or verification inputs must propagate the relevant SSL or file error.
- A mismatched inherited socket type must fail socket creation.
- Missing redirect host information raises `ValueError` only when an insecure redirect is required; requests that are passed through do not require a redirect host.
- WSGI request bodies over the configured limit return 400, WSGI paths outside `root_path` return 404, and a WSGI application that yields before `start_response` raises `RuntimeError`.
- Lifespan startup or shutdown timeout and application-reported lifespan failure must be observable as service failure, not successful shutdown.

## Cross-View Invariants

1. A configuration loaded from a file and then overridden explicitly on the command line **must** produce the same effective value as assigning that final value to a `Config` instance before programmatic service.
2. A command-line bind repeated in a particular order **must** remain in that order in `Config.bind`, and service startup **must** attempt all effective binds rather than only the last value.
3. TLS-enabled `bind` endpoints **must** use the certificate and key represented by the effective configuration, while `insecure_bind` endpoints **must** remain plaintext under the same configuration.
4. The `root_path` visible to an ASGI application or mapped to WSGI `SCRIPT_NAME` **must** reflect the normalized effective `Config.root_path` plus any selected dispatcher mount.
5. A `server_names` rejection **must** produce a 404 before the application handles the request, while an accepted Host value **must** reach the configured application.
6. `include_date_header`, `include_server_header`, and Alt-Svc configuration **must** control the corresponding service-generated response headers in every supported HTTP protocol projection.
7. A middleware-generated redirect, rejection, or body-limit response **must** bypass the wrapped application; a pass-through scope **must** reach it exactly once.
8. Proxy-derived client, scheme, and Host values **must** be visible to the wrapped application together in one copied scope, while the original caller-owned scope **must** retain its original values.
9. Completion of `shutdown_trigger` **must** initiate the same graceful application shutdown sequence as normal server termination and **must** honor the effective graceful and lifespan timeout settings.
10. Access logging and StatsD metrics **must** describe the same completed request status and duration observed at the service boundary.

## Representative Workflows

### Programmatic asyncio Service

```python
import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config

from myproject import app

config = Config.from_mapping(
    bind=["127.0.0.1:8080"],
    server_names=["localhost"],
    accesslog="-",
)
shutdown = asyncio.Event()

asyncio.run(serve(app, config, shutdown_trigger=shutdown.wait))
```

The caller owns the event loop. Returning from `shutdown.wait()` starts graceful shutdown; `serve()` returns after active service and application lifespan shutdown complete or raises if shutdown fails.

### Command-Line TLS Service

```console
hypercorn \
  --config service.toml \
  --bind 0.0.0.0:443 \
  --insecure-bind 0.0.0.0:80 \
  --certfile cert.pem \
  --keyfile key.pem \
  myproject.web:app
```

The explicit binds and certificate paths replace conflicting values from `service.toml`; non-conflicting file values remain active. Redirect middleware must be the outermost application wrapper when plaintext listeners are used only to redirect clients to HTTPS.

## Non-Goals

- This document does not redefine ASGI, WSGI, HTTP, TLS, WebSocket, or StatsD standards.
- Internal protocol engines, worker-context classes, queue implementations, task groups, socket syscall order, and reload-process organization are not public interfaces.
- Exact diagnostic wording, traceback formatting, logging timestamps, operating-system error text, and absolute paths are not compatibility guarantees.
- Optional HTTP/3 protocol internals and third-party event-loop installation are outside this surface; the documented HTTP/3 extra, QUIC bind, and Alt-Svc integration remain supported.
- Deprecated or undocumented internal import paths are not stable merely because an object is reachable from them.

## Compatibility Guarantees

Alternative implementations are free to choose different internal modules, concurrency helpers, protocol engines, and data structures. Compatibility requires the documented imports, signatures, defaults, precedence rules, state transitions, side effects, return values, warnings, and failure categories to remain observable at the public boundaries above.

Variable values such as generated dates, operating-system-assigned ports, process identifiers, and platform error messages are compared by their documented meaning rather than by one captured representation. ASGI event streams and middleware effects remain ordered behavioral contracts even when their internal scheduling differs.

```


## Rewrite audit

```text
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

```


## Candidate filter map

```text
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
| `tests/protocol/test_ws_stream.py::test_send_app_error_c

[TRUNCATED FOR PROMPT SIZE]

```


## Final spec-test map

```text
# Hypercorn Oracle Spec-Test Map

oracle_source: merged_public_rewrite_and_generated

| test_nodeid | source | layer | spec_section | status | notes |
|---|---|---|---|---|---|
| `filter/rewritten_upstream_tests.py::test_config_from_pyfile_loads_public_attributes` | upstream_rewrite | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_config_from_toml_loads_public_attributes` | upstream_rewrite | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_config_from_object_loads_public_attributes` | upstream_rewrite | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_config_response_headers_follow_metadata_flags` | upstream_rewrite | atomic | Response Metadata and Metrics | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_http_raw_path_and_query[/abc]` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_http_raw_path_and_query[/abc%3C]` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_websocket_raw_path_and_query[/abc]` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_preserves_websocket_raw_path_and_query[/abc%3C]` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_uses_https_scheme_for_http2_websocket` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_closes_websocket_without_denial_extension` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_http_to_https_redirect_uses_request_host_when_constructor_host_is_none` | upstream_rewrite | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_proxy_fix_legacy_restores_trusted_client_scheme_and_host` | upstream_rewrite | integration | Restoring Proxy Information | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_proxy_fix_modern_restores_trusted_client_scheme_and_host` | upstream_rewrite | integration | Restoring Proxy Information | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_dispatcher_routes_by_insertion_order_and_updates_root_path` | upstream_rewrite | integration | Dispatching Applications | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_dispatcher_returns_404_when_no_mount_matches` | upstream_rewrite | integration | Dispatching Applications | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_dispatcher_broadcasts_lifespan_to_mounted_applications` | upstream_rewrite | integration | Dispatching Applications | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_asyncio_wsgi_middleware_emits_wsgi_response_body` | upstream_rewrite | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_asyncio_wsgi_middleware_returns_400_when_body_exceeds_limit` | upstream_rewrite | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_asyncio_wsgi_middleware_requires_start_response_before_body` | upstream_rewrite | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_trio_wsgi_middleware_emits_wsgi_response_body` | upstream_rewrite | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_documented_defaults_are_visible` | generated | atomic | Documented Defaults | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_bind_groups_accept_single_string_assignments` | generated | atomic | Binds and TLS | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_root_path_assignment_removes_trailing_slashes` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_from_mapping_applies_keyword_arguments_last` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_from_mapping_accepts_keyword_only_configuration` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_from_object_resolves_dotted_object` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_from_pyfile_propagates_missing_file` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_from_pyfile_propagates_execution_failure` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_from_toml_propagates_parse_failure` | generated | atomic | Creating and Loading Configuration | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_ssl_enabled_reflects_certificate_and_key_presence` | generated | atomic | Binds and TLS | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_response_headers_include_each_alt_svc_value` | generated | atomic | Response Metadata and Metrics | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_statsd_logger_class_requires_statsd_host` | generated | atomic | Response Metadata and Metrics | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_config_statsd_logger_class_replaces_default_when_statsd_is_enabled` | generated | atomic | Response Metadata and Metrics | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_redirect_without_constructor_or_request_host_raises_value_error` | generated | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_redirect_location_includes_root_path_before_raw_path` | generated | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_redirect_passes_secure_websocket_to_wrapped_application` | generated | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_redirect_passes_non_http_scope_without_requiring_host` | generated | integration | Redirecting HTTP to HTTPS | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_proxy_fix_without_forwarded_headers_preserves_scope_values` | generated | integration | Restoring Proxy Information | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_proxy_fix_trusted_hops_selects_value_from_the_right` | generated | integration | Restoring Proxy Information | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_proxy_fix_modern_mode_falls_back_to_legacy_headers` | generated | integration | Restoring Proxy Information | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_proxy_fix_non_http_scope_is_passed_without_copying` | generated | integration | Restoring Proxy Information | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_dispatcher_uses_first_matching_mount_even_when_later_mount_is_longer` | generated | integration | Dispatching Applications | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_dispatcher_extends_existing_root_path_for_selected_mount` | generated | integration | Dispatching Applications | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_wsgi_environment_contains_root_path_path_info_query_and_headers` | generated | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_wsgi_path_outside_root_path_returns_404_without_calling_app` | generated | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_wsgi_websocket_scope_closes_without_calling_wsgi_app` | generated | integration | Adapting WSGI Applications | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_logger_access_logfile_dash_writes_configured_access_record_to_stdout` | generated | atomic | Logging | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_logger_missing_access_atom_renders_dash` | generated | atomic | Logging | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_logger_errorlog_dash_writes_error_and_warning_to_stderr` | generated | atomic | Logging | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_asyncio_serve_warns_when_process_or_loop_settings_do_not_apply` | generated | integration | Programmatic Service | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_hypercorn_module_help_exposes_command_line_interface` | generated | system_e2e | Command-Line Service | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_hypercorn_module_rejects_unknown_verify_mode` | generated | system_e2e | Command-Line Service | covered | public observable assertion; reference and dummy gated |

Total: 52 | upstream_rewrite: 20 | generated: 32 | final scoreable: 52

```


## Coverage quota

```text
# Hypercorn Coverage Quota

Final oracle count: 52

Layer distribution from official scorer:

| layer | count |
|---|---:|
| atomic | 20 |
| integration | 30 |
| system_e2e | 2 |

The oracle exceeds the global floor of 50 nodeids and has nonzero coverage in all required layers. Track B was required because Stage 3A discarded 16 of 21 upstream test files after public rewrite attempts.

Primary public surfaces covered:

- `Config` defaults, loaders, normalization, precedence, TLS flags, response metadata, and StatsD logger selection.
- `HTTPToHTTPSRedirectMiddleware`, `ProxyFixMiddleware`, `DispatcherMiddleware`, `AsyncioWSGIMiddleware`, and `TrioWSGIMiddleware`.
- `Logger` access and error logging behavior.
- `hypercorn.asyncio.serve` warnings for process and loop settings.
- `python -m hypercorn` command help and typed invocation error behavior.

```


## Judge report

```text
# Hypercorn Judge Report

Date: 2026-07-12 UTC

## Preflight Output

Candidate import provenance from official scorer:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z/score_snapshot_final/hypercorn/__init__.py
```

Reference import provenance from official scorer:

```text
/root/autodl-tmp/new-e2e/pgjones__hypercorn/src/hypercorn/__init__.py
```

Both scorer invocations used `--remove-path src/hypercorn`.

## Anti-Cheat

Candidate-visible input was limited to:

- `spec.md`
- `prompt.md`
- empty `output/`

The cleanroom worker reported writing only under `output/`. A scan of candidate output for source paths, oracle paths, test artifact names, score files, API key paths, and filter artifact names found no matches.

Audit limitation: the multi-agent worker transcript was not materialized as a full trajectory file. Available evidence consists of the cleanroom prompt, worker final status, candidate output tree, output content scan, and scorer import provenance.

Anti-cheat verdict: PASS_WITH_TRAJECTORY_LIMITATION.

## Solvability

Reference official scorer result:

```text
52 passed / 52 total
```

Layer distribution:

| layer | passed | total |
|---|---:|---:|
| atomic | 20 | 20 |
| integration | 30 | 30 |
| system_e2e | 2 | 2 |

Dummy gate:

```text
0 passed / 52 total
```

Solvability verdict: PASS.

## Candidate Score

Cleanroom candidate:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z
```

Official candidate scorer result after fairness correction:

```text
52 passed / 52 total
```

Layer distribution:

| layer | passed | total |
|---|---:|---:|
| atomic | 20 | 20 |
| integration | 30 | 30 |
| system_e2e | 2 | 2 |

## Fairness Corrections

The first candidate score exposed verifier overconstraints:

- ASGI empty response body events were asserted as exact dictionaries rather than observable status/body behavior.
- CLI verify-mode failure was asserted with an exact phrase rather than a typed invocation error mentioning the invalid mode.
- Logger tests used a `logging.Logger` object as `Config.accesslog`/`Config.errorlog`, which was not part of the frozen public specification.
- Dispatcher lifespan rewrite sent `lifespan.shutdown` while mounted apps returned startup completion.

These were corrected in `filter/rewritten_upstream_tests.py` and `filter/generated_tests.py`, then reference, dummy, and candidate scorers were rerun.

Fairness verdict: PASS after correction.

## Coverage Audit

The final oracle covers:

- configuration loaders, defaults, normalization, precedence, TLS flags, response headers, and StatsD logger selection;
- redirect, proxy-fix, dispatcher, and WSGI middleware;
- public `Logger` output behavior;
- programmatic `asyncio.serve` warnings;
- command-line help and typed option failure.

Core sections with oracle coverage include Product State Model projections through cross-component tests, Configuration, Command-Line Service, Programmatic Service, Middleware, Logging, Error Semantics, and Cross-View Invariants.

Coverage verdict: PARTIAL_ACCEPTABLE. HTTP/2, HTTP/3, and full network service behavior remain documented but lightly covered because fair oracle generation without private protocol engines was intentionally bounded.

## Labels

- `saturated-candidate-score`
- `trivially-solved`
- `public-middleware-heavy`
- `limited-service-e2e`
- `coverage-gap-secondary-protocols`

The cleanroom candidate passed all final oracle tests with a compact implementation. This is allowed by the judge rules but should be recorded as a benchmark-value caveat: the task validates public configuration and middleware behavior more strongly than full server/protocol reconstruction.

## Verdict

Status recommendation: `QUALIFIED_WITH_CAVEATS`, pending the final one-time DeepSeek v4 Pro and GLM 5.2 audit required by the updated user policy.

```


## Reference score summary JSON

```text
{
  "source_repo": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/filter/oracle_source",
  "solution_dir": "/root/autodl-tmp/new-e2e/pgjones__hypercorn/src",
  "nodeids": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/filter/kept_nodeids.txt",
  "taxonomy": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/filter/taxonomy.jsonl",
  "run_dir": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/runs/reference_final_corrected",
  "import_provenance": {
    "returncode": 0,
    "stdout": "/root/autodl-tmp/new-e2e/pgjones__hypercorn/src/hypercorn/__init__.py\n",
    "stderr": ""
  },
  "grouped_results": {
    "filter/generated_tests.py": {
      "returncode": 0,
      "stdout": "................................                                         [100%]\n32 passed in 0.38s\n",
      "stderr": "",
      "json_report": {
        "created": 1783859029.4392083,
        "duration": 0.37210726737976074,
        "exitcode": 0,
        "root": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/runs/reference_final_corrected/oracle_worktree",
        "environment": {},
        "summary": {
          "passed": 32,
          "total": 32,
          "collected": 32
        },
        "collectors": [
          {
            "nodeid": "",
            "outcome": "passed",
            "result": [
              {
                "nodeid": "filter/generated_tests.py::test_config_documented_defaults_are_visible",
                "type": "Function",
                "lineno": 76
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_bind_groups_accept_single_string_assignments",
                "type": "Function",
                "lineno": 88
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_root_path_assignment_removes_trailing_slashes",
                "type": "Function",
                "lineno": 100
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_mapping_applies_keyword_arguments_last",
                "type": "Function",
                "lineno": 108
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_mapping_accepts_keyword_only_configuration",
                "type": "Function",
                "lineno": 121
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_object_resolves_dotted_object",
                "type": "Function",
                "lineno": 128
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_pyfile_propagates_missing_file",
                "type": "Function",
                "lineno": 144
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_pyfile_propagates_execution_failure",
                "type": "Function",
                "lineno": 149
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_toml_propagates_parse_failure",
                "type": "Function",
                "lineno": 157
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_ssl_enabled_reflects_certificate_and_key_presence",
                "type": "Function",
                "lineno": 165
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_response_headers_include_each_alt_svc_value",
                "type": "Function",
                "lineno": 177
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_statsd_logger_class_requires_statsd_host",
                "type": "Function",
                "lineno": 189
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_statsd_logger_class_replaces_default_when_statsd_is_enabled",
                "type": "Function",
                "lineno": 199
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_without_constructor_or_request_host_raises_value_error",
                "type": "Coroutine",
                "lineno": 210
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_location_includes_root_path_before_raw_path",
                "type": "Coroutine",
                "lineno": 221
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_passes_secure_websocket_to_wrapped_application",
                "type": "Coroutine",
                "lineno": 240
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_passes_non_http_scope_without_requiring_host",
                "type": "Coroutine",
                "lineno": 262
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_without_forwarded_headers_preserves_scope_values",
                "type": "Coroutine",
                "lineno": 277
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_trusted_hops_selects_value_from_the_right",
                "type": "Coroutine",
                "lineno": 293
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_modern_mode_falls_back_to_legacy_headers",
                "type": "Coroutine",
                "lineno": 322
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_non_http_scope_is_passed_without_copying",
                "type": "Coroutine",
                "lineno": 349
              },
              {
                "nodeid": "filter/generated_tests.py::test_dispatcher_uses_first_matching_mount_even_when_later_mount_is_longer",
                "type": "Coroutine",
                "lineno": 362
              },
              {
                "nodeid": "filter/generated_tests.py::test_dispatcher_extends_existing_root_path_for_selected_mount",
                "type": "Coroutine",
                "lineno": 385
              },
              {
                "nodeid": "filter/generated_tests.py::test_wsgi_environment_contains_root_path_path_info_query_and_headers",
                "type": "Coroutine",
                "lineno": 405
              },
              {
                "nodeid": "filter/generated_tests.py::test_wsgi_path_outside_root_path_returns_404_without_calling_app",
                "type": "Coroutine",
                "lineno": 443
              },
              {
                "nodeid": "filter/generated_tests.py::test_wsgi_websocket_scope_closes_without_calling_wsgi_app",
                "type": "Coroutine",
                "lineno": 466
              },
              {
                "nodeid": "filter/generated_tests.py::test_logger_access_logfile_dash_writes_configured_access_record_to_stdout",
                "type": "Coroutine",
                "lineno": 491
              },
              {
                "nodeid": "filter/generated_tests.py::test_logger_missing_access_atom_renders_dash",
                "type": "Coroutine",
                "lineno": 509
              },
              {
                "nodeid": "filter/generated_tests.py::test_logger_errorlog_dash_writes_error_and_warning_to_stderr",
                "type": "Coroutine",
                "lineno": 522
              },
              {
                "nodeid": "filter/generated_tests.py::test_asyncio_serve_warns_when_process_or_loop_settings_do_not_apply",
                "type": "Coroutine",
                "lineno": 538
              },
              {
                "nodeid": "filter/generated_tests.py::test_hypercorn_module_help_exposes_command_line_interface",
                "type": "Function",
                "lineno": 566
              }

[TRUNCATED FOR PROMPT SIZE]

```


## Dummy score JSON

```text
{
  "total": 52,
  "passed": 0,
  "failed": 52,
  "pass_rate": 0.0,
  "stdout": "logs/stage3_dummy_corrected_stdout.txt",
  "stderr": "logs/stage3_dummy_corrected_stderr.txt"
}

```


## Candidate score report

```text
# Hypercorn Candidate Score Report

Candidate run:

```text
codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z
```

Final official score:

```text
52 passed / 52 total
```

By layer:

| layer | passed | total |
|---|---:|---:|
| atomic | 20 | 20 |
| integration | 30 | 30 |
| system_e2e | 2 | 2 |

Import provenance:

```text
/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z/score_snapshot_final/hypercorn/__init__.py
```

Scorer isolation:

```text
score_pytest_original.py --remove-path src/hypercorn
```

Notes:

- Initial score was 39/52 before fairness correction.
- Final score is saturated; record `trivially-solved` and `saturated-candidate-score` caveats.

```


## Candidate final score JSON summary

```text
{
  "source_repo": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/filter/oracle_source",
  "solution_dir": "/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z/score_snapshot_final",
  "nodeids": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/filter/kept_nodeids.txt",
  "taxonomy": "/root/autodl-tmp/Bmk-Lizhiqian/wip/hypercorn-fullrepro-001/filter/taxonomy.jsonl",
  "run_dir": "/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z/score_final_corrected",
  "import_provenance": {
    "returncode": 0,
    "stdout": "/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z/score_snapshot_final/hypercorn/__init__.py\n",
    "stderr": ""
  },
  "grouped_results": {
    "filter/generated_tests.py": {
      "returncode": 0,
      "stdout": "................................                                         [100%]\n32 passed in 0.29s\n",
      "stderr": "",
      "json_report": {
        "created": 1783859043.428628,
        "duration": 0.2842671871185303,
        "exitcode": 0,
        "root": "/root/autodl-tmp/Bmk-Lizhiqian/candidate-runs/hypercorn/codex-gpt-5.6-hypercorn-fullrepro-001-20260712T000000Z/score_final_corrected/oracle_worktree",
        "environment": {},
        "summary": {
          "passed": 32,
          "total": 32,
          "collected": 32
        },
        "collectors": [
          {
            "nodeid": "",
            "outcome": "passed",
            "result": [
              {
                "nodeid": "filter/generated_tests.py::test_config_documented_defaults_are_visible",
                "type": "Function",
                "lineno": 76
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_bind_groups_accept_single_string_assignments",
                "type": "Function",
                "lineno": 88
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_root_path_assignment_removes_trailing_slashes",
                "type": "Function",
                "lineno": 100
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_mapping_applies_keyword_arguments_last",
                "type": "Function",
                "lineno": 108
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_mapping_accepts_keyword_only_configuration",
                "type": "Function",
                "lineno": 121
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_object_resolves_dotted_object",
                "type": "Function",
                "lineno": 128
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_pyfile_propagates_missing_file",
                "type": "Function",
                "lineno": 144
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_pyfile_propagates_execution_failure",
                "type": "Function",
                "lineno": 149
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_from_toml_propagates_parse_failure",
                "type": "Function",
                "lineno": 157
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_ssl_enabled_reflects_certificate_and_key_presence",
                "type": "Function",
                "lineno": 165
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_response_headers_include_each_alt_svc_value",
                "type": "Function",
                "lineno": 177
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_statsd_logger_class_requires_statsd_host",
                "type": "Function",
                "lineno": 189
              },
              {
                "nodeid": "filter/generated_tests.py::test_config_statsd_logger_class_replaces_default_when_statsd_is_enabled",
                "type": "Function",
                "lineno": 199
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_without_constructor_or_request_host_raises_value_error",
                "type": "Coroutine",
                "lineno": 210
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_location_includes_root_path_before_raw_path",
                "type": "Coroutine",
                "lineno": 221
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_passes_secure_websocket_to_wrapped_application",
                "type": "Coroutine",
                "lineno": 240
              },
              {
                "nodeid": "filter/generated_tests.py::test_redirect_passes_non_http_scope_without_requiring_host",
                "type": "Coroutine",
                "lineno": 262
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_without_forwarded_headers_preserves_scope_values",
                "type": "Coroutine",
                "lineno": 277
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_trusted_hops_selects_value_from_the_right",
                "type": "Coroutine",
                "lineno": 293
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_modern_mode_falls_back_to_legacy_headers",
                "type": "Coroutine",
                "lineno": 322
              },
              {
                "nodeid": "filter/generated_tests.py::test_proxy_fix_non_http_scope_is_passed_without_copying",
                "type": "Coroutine",
                "lineno": 349
              },
              {
                "nodeid": "filter/generated_tests.py::test_dispatcher_uses_first_matching_mount_even_when_later_mount_is_longer",
                "type": "Coroutine",
                "lineno": 362
              },
              {
                "nodeid": "filter/generated_tests.py::test_dispatcher_extends_existing_root_path_for_selected_mount",
                "type": "Coroutine",
                "lineno": 385
              },
              {
                "nodeid": "filter/generated_tests.py::test_wsgi_environment_contains_root_path_path_info_query_and_headers",
                "type": "Coroutine",
                "lineno": 405
              },
              {
                "nodeid": "filter/generated_tests.py::test_wsgi_path_outside_root_path_returns_404_without_calling_app",
                "type": "Coroutine",
                "lineno": 443
              },
              {
                "nodeid": "filter/generated_tests.py::test_wsgi_websocket_scope_closes_without_calling_wsgi_app",
                "type": "Coroutine",
                "lineno": 466
              },
              {
                "nodeid": "filter/generated_tests.py::test_logger_access_logfile_dash_writes_configured_access_record_to_stdout",
                "type": "Coroutine",
                "lineno": 491
              },
              {
                "nodeid": "filter/generated_tests.py::test_logger_missing_access_atom_renders_dash",
                "type": "Coroutine",
                "lineno": 509
              },
              {
                "nodeid": "filter/generated_tests.py::test_logger_errorlog_dash_writes_error_and_warning_to_stderr",
                "type": "Coroutine",
                "lineno": 522
              },
              {
                "nodeid": "filter/generated_tests.py::test_asyncio_serve_warns_when_process_or_loop_settings_do_not_apply",
                "type": "Coroutine",
                "lineno": 538
              },
              {
                "nodeid": "filter/generated_tests.py::test_hypercorn_module_help_exposes_command_line_interface",
                "type": "Function",
                "lineno": 566
              },
              {
                "nodeid": "filter/generated_tests.py::test_hypercorn_module_rejects_unknown_verify_mode",
                "type": "Function",
                "lineno": 579
              }
            ]
          }
        ],
        "tests": [
          {
            "nodeid": "filter/generated_tests.py::test_config_documented_defaults_are_visible",
            "lineno": 76,
            "outcome": "passed",
            "keywords": [
              "test_config_documented_defaults_are_visible",
              "generated_tests.py",
              "filter",
              "oracle_worktree",
              ""
            ],
            "setup": {
              "duration": 0.00030350126326084137,
              "outcome": "passed"
            },
            "call": {
              "duration": 0.0002134907990694046,
              "outcome": "passed"
            },
            "teardown": {
              "duration": 0.00011259131133556366,
              "outcome": "passed"
            }
          },
          {
            "nodeid": "filter/generated_tests.py::test_config_bind_groups_accept_single_string_assignments",
            "lineno": 88,
            "outcome": "passed",
            "keywords": [
              "test_config_bind_groups_accept_single_string_assignments",
              "generated_tests.py",
              "filter",
              "oracle_worktree",
              ""
            ],
            "setup": {
              "duration": 0.00012718327343463898,
              "outcome": "passed"
            },
            "call": {
              "duration": 0.0001797359436750412,
              "outcome": "passed"
            },
            "teardown": {
              "duration": 9.777955710887909e-05,
              "outcome": "passed"
            }
          },
          {
            "nodeid": "filter/generated_tests.py::test_config_root_path_assignment_removes_trailing_slashes",
            "lineno": 100,
            "outcome": "passed",
            "keywords": [
              "test_config_root_path_assignment_removes_trailing_slashes",
              "generated_tests.py",
              "filter",
              "oracle_worktree",
              ""
            ],
            "setup": {
              "duration": 0.00012204609811306,
              "outcome": "passed"
            },
            "call": {
              "duration": 0.00020904093980789185,
              "outcome": "passed"
            },
            "teardown": {
              "duration": 0.00010554306209087372,
              "outcome": "passed"
            }
          },
          {
            "nodeid": "filter/generated_tests.py::test_config_from_mapping_applies_keyword_arguments_last",
            "lineno": 108,
            "outcome": "passed",
            "keywords": [
              "test_config_from_mapping_applies_keyword_arguments_last",
              "generated_tests.py",
              "filter",
              "oracle_worktree",
              ""
            ],
            "setup": {
              "duration": 0.0001322031021118164,
              "outcome": "passed"
            },
            "call": {
              "duration": 0.0001966971904039383,
              "outcome": "passed"
            },
            "teardown": {
              "duration": 0.00011017173528671265,
              "outcome": "passed"
            }
          },
          {
            "nodeid": "filter/generated_tests.py::test_config_from_mapping_accepts_keyword_only_configuration",
            "lineno": 121,
            "outcome": "passed",
            "keywords": [
              "test_config_from_mapping_accepts_keyword_only_configuration",
              "generated_tests.py",
              "filter",
              "oracle_worktree"

[TRUNCATED FOR PROMPT SIZE]

```