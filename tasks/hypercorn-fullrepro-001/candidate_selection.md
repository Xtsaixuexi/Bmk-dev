# Hypercorn Candidate Selection

repo: pgjones/hypercorn
source_path: /root/autodl-tmp/new-e2e/pgjones__hypercorn
commit: 0e2311f1ad2ae587aaa590f3824f59aa5dc0e770
src_loc: 4775
test_functions: 141 rough functions; 196 collected nodeids
test_files: 31
dominant_test_styles: configuration/CLI, ASGI and WSGI wrappers, asyncio/trio lifecycle, logging, HTTP/1, HTTP/2, WebSocket, worker context, and protocol integration
public_docs: README plus 28 rough docs files covering configuration, programmatic serving, asyncio/trio, workers, logging, and protocol behavior
core_fact_source: configured ASGI/WSGI application server state and per-connection lifecycle
derived_views: CLI/config objects, application wrappers/scopes, server lifecycle callbacks, asyncio/trio execution, access logs, and request/response behavior
external_deps: h11, h2, wsproto, priority, asyncio/trio; isolated install and collection succeeded
test_import_audit: authoritative private import file rate 0.032
docs_test_alignment: partly aligned at config/programmatic server/wrapper/lifecycle behavior; pure protocol-state and internal task tests require filtering
contamination_note: pgjones/hypercorn at pinned commit; release timing relative to model training cutoff unknown
decision: proposed keep
reason: Hypercorn-specific config, wrapper, lifecycle, concurrency-backend, and logging behavior remains beyond closed protocol standards
risks: standard HTTP/2/WebSocket recall, internal protocol tasks, event-loop timing, sockets/TLS, exact logging formats, and environment-dependent integration

## Collection Evidence

The isolated environment `/root/autodl-tmp/Bmk-Lizhiqian/envs/hypercorn-fullrepro-001` installed editable Hypercorn and its declared development test dependencies. Pytest collected 196 nodeids in 0.29 seconds with zero collection errors.

## Proposed Stage 1 Disposition

`S1_SELECTED_PENDING_REVIEW`, restricted later to documented Hypercorn-specific public behavior and deterministic in-memory protocol interactions.
