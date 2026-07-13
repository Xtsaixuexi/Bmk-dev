# Independent Stage 1 Review: hypercorn-fullrepro-001

Review only this candidate-selector evidence. Do not browse, use tools, inspect files, or consider any other project.

Evidence:

- repository: `pgjones/hypercorn`
- product: ASGI/WSGI server with Hypercorn-specific configuration, programmatic serving, asyncio/trio backends, application wrappers, worker context, lifecycle, and logging plus standard HTTP/WebSocket protocols
- source LOC: 4775
- source Python files: 43
- docs signal: 28 rough docs files covering configuration, programmatic serving, asyncio/trio, workers, logging, and protocols
- isolated install with development test dependencies collected 196 nodeids with zero errors
- private import file rate: 0.032
- network/environment marker rate: 0.161
- snapshot marker rate: 0.032
- shared configured server/application state is projected through CLI/config objects, wrappers/scopes, lifecycle callbacks, concurrency backends, access logs, and request/response behavior

Proposed routing: retain documented Hypercorn-specific behavior and deterministic in-memory interactions; exclude standard-only HTTP/2/WebSocket checks, internal protocol-task shapes, live sockets/TLS, timing-sensitive event-loop behavior, and arbitrary exact logs.

Return only:

- `VERDICT`: PASS_CONTINUE or REJECT
- `HARD_GATES`: PASS or FAIL
- `HYPERCORN_SPECIFIC_CORE`: PASS or FAIL
- `CLOSED_STANDARD_RISK_ROUTING`: ACCEPT or FAIL
- `NEXT_STATE`: S2_READY or RETIRED
- `BLOCKERS`: mandatory issues only
