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
