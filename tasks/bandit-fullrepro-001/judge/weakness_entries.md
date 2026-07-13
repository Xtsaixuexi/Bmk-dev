# Bandit Weakness Entries

| model | task | dimension | description | affected_tests |
|---|---|---|---|---|
| codex/gpt-5.5 | bandit-fullrepro-001 | atomic-behavior | Candidate `Issue.get_code()` does not load source context from public `fname`/`lineno`, returning an empty snippet. | 2 atomic |
| codex/gpt-5.5 | bandit-fullrepro-001 | workflow-completeness | Candidate accepts `--aggregate vuln` but retains filename ordering instead of vulnerability/test-name ordering. | 1 system_e2e |
