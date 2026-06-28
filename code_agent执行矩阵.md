# Code Agent 执行矩阵

依据 `核心路线文档.md` 中的 code agent 分类，区分工业级 code agent 与科研型 code agent。成绩只记录已有真实 score report；没有 report 的 agent 只标记可用性和待跑状态，不写入 `score_summary.csv`。

## Agent 可用性与覆盖

| 类别 | Agent | CLI / 版本 | 结果映射 | 覆盖 | 状态 |
|---|---|---|---|---:|---|
| industrial_code_agent | Claude Code | `/usr/bin/claude` / 2.1.185 (Claude Code) | `claude-code` | 0/5 tasks | auth_required |
| industrial_code_agent | Codex | `/usr/bin/codex` / codex-cli 0.141.0 | `codex-subagent-001`, `codex-local-20260623` | 5/5 tasks + 2 local reruns | scored |
| industrial_code_agent | OpenCode | `/usr/bin/opencode` / 1.17.9 | `opencode` | 0/5 tasks | credentials_required |
| research_code_agent | SWE-Agent | `/root/autodl-tmp/env/agents/swe-agent/bin/sweagent` / 1.1.0 | `swe-agent-deepseek-chat-001` | 2/5 tasks | partially_scored |
| research_code_agent | Mini-SWE-Agent | `/root/autodl-tmp/env/agents/mini-swe-agent/bin/mini-swe-agent` / 2.4.2 | `mini-swe-agent-deepseek-chat-001` | 3/5 tasks | partially_scored |
| research_code_agent | OpenHands | `/root/autodl-tmp/env/bin/openhands` / 1.21.0 | `openhands-deepseek-v4-pro-001`, `openhands-deepseek-chat-001` | 5/5 tasks | scored |

## 已有真实跑分

| Agent / solution | 任务 | Unit | System | Gap pp | Status |
|---|---|---:|---:|---:|---|
| codex-subagent-001 | SQLite | 87.50 | 41.67 | 45.83 | core_strong |
| codex-subagent-001 | ZK | 83.33 | 58.33 | 25.00 | core_strong |
| codex-subagent-001 | MiniURLUtils | 100.00 | 70.00 | 30.00 | core_strong |
| codex-subagent-001 | MiniShell | 100.00 | 100.00 | 0.00 | candidate_reviewed |
| codex-subagent-001 | MiniBuildGraph | 100.00 | 93.75 | 6.25 | candidate_reviewed |
| codex-local-20260623 | MiniShell | 100.00 | 100.00 | 0.00 | candidate_reviewed |
| codex-local-20260623 | MiniBuildGraph | 100.00 | 93.75 | 6.25 | candidate_reviewed |
| openhands-deepseek-v4-pro-001 | SQLite | 93.75 | 41.67 | 52.08 | core_strong |
| openhands-deepseek-v4-pro-001 | ZK | 83.33 | 41.67 | 41.67 | core_strong |
| openhands-deepseek-v4-pro-001 | MiniURLUtils | 100.00 | 60.00 | 40.00 | core_strong |
| openhands-deepseek-chat-001 | MiniShell | 100.00 | 100.00 | 0.00 | candidate_reviewed |
| openhands-deepseek-chat-001 | MiniBuildGraph | 87.50 | 75.00 | 12.50 | candidate_reviewed |
| mini-swe-agent-deepseek-chat-001 | MiniURLUtils | 88.89 | 60.00 | 28.89 | core_strong |
| mini-swe-agent-deepseek-chat-001 | MiniShell | 100.00 | 91.67 | 8.33 | candidate_reviewed |
| mini-swe-agent-deepseek-chat-001 | MiniBuildGraph | 93.75 | 81.25 | 12.50 | candidate_reviewed |
| swe-agent-deepseek-chat-001 | MiniShell | 68.75 | 58.33 | 10.42 | candidate_reviewed |
| swe-agent-deepseek-chat-001 | MiniBuildGraph | 93.75 | 81.25 | 12.50 | candidate_reviewed |

## 待补跑项

| Agent | 待补跑范围 | 原因 |
|---|---|---|
| Claude Code | 5 个任务 | CLI 可用但未登录；需用户完成 `claude` 登录 |
| OpenCode | 5 个任务 | CLI 可用但无 provider credentials；需用户完成 `opencode providers login` |
| SWE-Agent | SQLite、ZK、MiniURLUtils | MiniShell/MiniBuildGraph 已有 report，但还未覆盖前三个任务 |
| Mini-SWE-Agent | SQLite、ZK | MiniURLUtils/MiniShell/MiniBuildGraph 已有 report，但还未覆盖 SQLite、ZK |

## 写表原则

- `score_summary.csv` 只写已有 score report 的真实结果。
- 新 agent 生成 candidate 并跑完 rubric 后，再新增对应 `score_report_<agent>_unit_system_v1.json`，随后同步 `score_summary.csv` 与 `MANIFEST.json`。
- gap 统一使用 score report 中 raw `unit_system_gap` 乘以 100 后四舍五入到两位。
- bare GPT/DeepSeek/Doubao 只作为 auxiliary/non-core 观察，不计入核心 gap 证据；OpenHands + DeepSeek、Mini-SWE-Agent + DeepSeek、SWE-Agent + DeepSeek 这类 executable code-agent run 可以计入。
