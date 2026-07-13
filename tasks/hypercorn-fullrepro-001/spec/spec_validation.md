# Hypercorn v1 Specification Validation

Date: 2026-07-12 UTC

## Bmk-dev Principles

- Like a developer: PASS. The candidate body is formal Hypercorn author-to-user documentation.
- Spec-driven: PASS. Public imports, signatures, defaults, state transitions, precedence, failures, and cross-view agreements are explicit.
- Behavioral: PASS. Requirements concern observable caller and operator behavior without prescribing internal organization or algorithms.
- Q1 public contract: PASS for every included surface; internal protocol and worker objects are explicitly omitted.
- Q2 non-derivable balance: PASS; Hypercorn-specific details are retained without restating external protocol standards.

## Required Structure

- Product State Model: PASS; configuration, application, and service projections are unified.
- Cross-View Invariants: PASS; 10 numbered observable invariants span configuration, CLI, TLS, routing, middleware, lifecycle, logging, and metrics.
- Representative Workflows: PASS; programmatic asyncio and command-line TLS workflows are complete.
- Non-Goals: PASS.
- Failure paths: PASS for configuration loading, application loading, CLI parsing, TLS, inherited sockets, redirects, WSGI adaptation, and lifespan handling.
- Precedence: PASS; CLI-over-file and mapping-then-keyword conflicts were checked against the pinned reference.

## Candidate-Safety Audits

- Forbidden process-language matches: 0.
- Weak behavioral modal matches (`can`, `may`, `might`, `could`, `should`, `typically`, `generally`): 0.
- Private/internal implementation symbol matches: 0.
- Test names, fixture content, source paths, expected values from tests, and scoring information: none.

## Independent Reviews

- DeepSeek v4 Pro: `PASS_AUTHOR_SPEC`; all eight substantive dimensions PASS, process leakage NONE, blockers empty.
- GLM 5.2: `PASS_GITHUB_PRINCIPLES`; all eight substantive dimensions PASS, process leakage NONE, blockers empty.

Result: PASS. The v1 body is frozen for Stage 3 import and behavior mapping.
