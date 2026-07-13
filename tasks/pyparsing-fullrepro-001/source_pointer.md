# Source Pointer

Task ID: `pyparsing-fullrepro-001`

The reference implementation remains outside the benchmark task directory:

- Source repository: `/root/autodl-tmp/e2e/pyparsing`
- Commit: `ecb1b14dbf1ad1b699c081ed63b9746a244ee5fa`
- Package import name: `pyparsing`
- Upstream tests: `/root/autodl-tmp/e2e/pyparsing/tests`

Do not copy the source package or upstream tests into this task directory. This `wip` directory stores only benchmark construction artifacts: specification drafts, filtering notes, nodeid lists, taxonomy, reference results, judge reports, and review logs.

Candidate agents may receive only the candidate-visible `spec.md` plus a generic implementation prompt. They must not receive this file, upstream source, upstream tests, hidden oracle files, score reports, or API credentials.
