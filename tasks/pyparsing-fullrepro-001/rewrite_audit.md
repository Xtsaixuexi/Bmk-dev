# Rewrite Audit: pyparsing-fullrepro-001

No upstream tests were rewritten in Step 4. Filtering is by nodeid retention/exclusion only.

Import audit summary:

- Top-level private `pyparsing._...` imports: 0 files.
- Upstream tests import public `pyparsing`, documented aliases, test helpers, examples, matplotlib, and optional diagram dependencies.
- Example application tests and third-party matplotlib regression tests were excluded instead of rewritten because they require non-package public artifacts or external project behavior.

Track B trigger: not triggered. Track A retained 298 nodeids with non-zero atomic, integration, and system_e2e coverage.
