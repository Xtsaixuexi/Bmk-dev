# Final GitHub Workflow Checksum Check

Checked at: 2026-07-09T08:53:35Z

Base URL:

```text
https://gh-proxy.com/https://raw.githubusercontent.com/E2E-Bmk/Bmk-dev/main
```

The first pass confirmed `README.md`, then the proxy returned HTTP 429 for the next request. The check was retried with delay and all remaining workflow files matched the package snapshot.

| file | sha256 | verdict |
|---|---|---|
| `README.md` | `70c35e4bc15379f7fac1b55275803faa8fbf09a6a689c4f882dd34cd36014afa` | PASS |
| `skills/candidate-selector/SKILL.md` | `bc733e48e9eaae9193729ef1f990ef6b1464d7ba09e35f6786c148d19cee9f8d` | PASS |
| `skills/spec-writer/SKILL.md` | `8be46346849b15c831d9bdc985c4dd9a7793c547c58affbdfea3e6bb98ae90c7` | PASS |
| `skills/test-filter/SKILL.md` | `aaca8196d6a0d5bc6d3767832a0725832bc9fe2daf9f9040d93138ce04ac566b` | PASS |
| `skills/task-judge/SKILL.md` | `3c7a5ac311a7fe2acde80390a51ad5c6b19b42943a59072d36831d3672f40559` | PASS |
| `skills/task-synthesizer/SKILL.md` | `e841510f432ead6a413bc30deeeb7a2f9ea4d142a38bfb3c72fca51124b45e12` | PASS |

Verdict: PASS. The task package remains aligned with the accelerated GitHub main workflow snapshot used by the stage checks.
