# Hypercorn Specification Sources

## Source Boundary

- `README.rst`
- `docs/tutorials/usage.rst`
- `docs/how_to_guides/api_usage.rst`
- `docs/how_to_guides/binds.rst`
- `docs/how_to_guides/configuring.rst`
- `docs/how_to_guides/dispatch_apps.rst`
- `docs/how_to_guides/http_https_redirect.rst`
- `docs/how_to_guides/logging.rst`
- `docs/how_to_guides/proxy_fix.rst`
- `docs/how_to_guides/server_names.rst`
- `docs/how_to_guides/statsd.rst`
- `docs/how_to_guides/wsgi_apps.rst`
- `src/hypercorn/__init__.py`
- `src/hypercorn/asyncio/__init__.py`
- `src/hypercorn/trio/__init__.py`
- `src/hypercorn/config.py` public signatures and docstrings
- `src/hypercorn/logging.py` documented logger surface
- `src/hypercorn/middleware/__init__.py` and exported middleware signatures
- `hypercorn --help`

Source code and tests were consulted only to confirm observable behavior and to reject internal surfaces. They are not candidate-visible sources.

## Public Surface Decisions

| Import or operation | Q1: public contract | Q2: non-derivable details | Decision |
|---|---|---|---|
| `hypercorn.Config`, `hypercorn.config.Config` | Yes; package export, README, and configuration guide | Loader forms, defaults, normalization, TLS activation, and precedence are Hypercorn-specific | Include |
| `hypercorn.asyncio.serve` | Yes; README and API guide | ignored process settings, shutdown trigger, and mode forcing are Hypercorn-specific | Include |
| `hypercorn.trio.serve` | Yes; API guide | Trio task-status argument and the same shutdown/mode rules are Hypercorn-specific | Include |
| `hypercorn.middleware.AsyncioWSGIMiddleware` | Yes; package export and WSGI guide | body limit and ASGI event behavior are Hypercorn-specific | Include |
| `hypercorn.middleware.TrioWSGIMiddleware` | Yes; package export and WSGI guide | backend selection and body limit are Hypercorn-specific | Include |
| `hypercorn.middleware.DispatcherMiddleware` | Yes; package export and dispatch guide | insertion-order prefix matching, root-path projection, fallback, and lifespan agreement are Hypercorn-specific | Include |
| `hypercorn.middleware.HTTPToHTTPSRedirectMiddleware` | Yes; package export and redirect guide | HTTP/WebSocket redirect distinctions and host resolution are Hypercorn-specific | Include |
| `hypercorn.middleware.ProxyFixMiddleware` | Yes; package export and proxy guide | mode selection and trusted-hop semantics are Hypercorn-specific and security-sensitive | Include |
| `hypercorn.logging.Logger` | Yes; logging guide names it as the customization base | asynchronous logging surface and access-format atoms are Hypercorn-specific | Include |
| CLI `hypercorn` | Yes; primary documented workflow | application syntax, config dispatch, override precedence, repeatable binds, and worker choices are Hypercorn-specific | Include |
| ASGI, WSGI, HTTP/1.1, HTTP/2, and WebSocket standards | Yes as accepted application/protocol contracts | Standard message definitions are externally specified and derivable | State support; do not restate standards |
| Protocol classes, worker contexts, lifespan internals, task groups, and private wrappers | No; not exported or documented as caller APIs | Internal organization is implementation-defined | Omit |
| Exact diagnostics, logging timestamps, socket syscall sequences, and internal queue shapes | No | These would prescribe implementation or unstable representations | Omit |

## Reference-Observed Precedence

A concrete conflict experiment loaded a TOML configuration with `workers = 2`, `bind = ["config:7000"]`, and `loglevel = "WARNING"`, then invoked the CLI with `--workers 3`, two `--bind` values, and `m:a` as the application. The resulting configuration had `workers == 3`, `bind == ["cli:8000", "cli:9000"]`, retained `loglevel == "WARNING"`, and set `application_path == "m:a"`.

A separate conflict experiment confirmed that `Config.from_mapping({"workers": 2}, workers=4)` returns a configuration whose `workers` value is `4`.

These observations support the precedence statements in the candidate-visible document.
