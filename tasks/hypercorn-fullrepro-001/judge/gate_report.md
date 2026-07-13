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
