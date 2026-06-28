下面按你当前课题方向，把 **MiniShell** 和 **MiniGraph / MiniBuildGraph** 两个任务整理成一套可以继续推进、补文件、写进度、提交 PR 的工作方案。

我这里默认你的 **minigraph** 指的是前面提到的基于 `quarkslab/bgraph` 的 **MiniBuildGraph** 任务；如果你们内部最终命名为 `minigraph-realrepo-001`，只需要把目录名和 task id 改掉即可。

---

## 1. 你现在的目标

你要把两个任务都推进到 Bmk-dev 当前 core task 格式：

```text
task/
  minishell-realrepo-001/
    prd.md
    rubric.json
    doc/
      source_repo.md
      requirement_map.md
      score_reports/

  minibuildgraph-realrepo-001/
    prd.md
    rubric.json
    doc/
      source_repo.md
      requirement_map.md
      score_reports/
```

当前官方仓库 README 明确要求每个 task 顶层放 `prd.md` 和 `rubric.json`，辅助审查材料放在 `doc/` 下，包括 `source_repo.md`、`requirement_map.md` 和 `score_reports/`；当前 main 中已有 `sqlite-utils-realrepo-001`、`zk-realrepo-001`、`miniurlutils-realrepo-001` 三个 confirmed tasks，可作为格式参考。([GitHub][1])

---

## 2. MiniShell 任务推进方案

### 2.1 Source repo

参考仓库：

```text
https://github.com/mcombeau/minishell
```

该仓库 README 说明它是一个 42 school 的简化 shell 项目，支持系统可执行程序、local executable、`echo/cd/env/exit/export/pwd/unset` 等 builtin、pipe、输入输出重定向、environment variable expansion，以及 `$?` 最近前台 pipeline exit status；同时明确不支持 `\`、`;`、`&&`、`||`、wildcards。([GitHub][2])

### 2.2 Mini 版本抽象

建议任务命名：

```text
task_id: minishell-realrepo-001
program: minishell.py
```

运行方式：

```bash
python3 minishell.py STATE_DIR run "COMMAND"
```

不要做交互式 shell。为了 deterministic evaluation，改成单命令 CLI：

```bash
python3 minishell.py /tmp/shdb run "echo hello"
python3 minishell.py /tmp/shdb run "export A=1"
python3 minishell.py /tmp/shdb run "echo $A"
```

`STATE_DIR` 用于保存环境变量、当前工作目录、上一条命令 exit status。这样 system tests 可以测跨命令状态。

### 2.3 功能模块

MiniShell 建议保留 8 个模块：

| 模块                 | 功能                                              |      |       |
| ------------------ | ----------------------------------------------- | ---- | ----- |
| parsing            | 空格切分、单引号、双引号、转义限制、syntax error                  |      |       |
| variable expansion | `$VAR`、`${VAR}` 可选、`$?`                         |      |       |
| builtins           | `echo`、`pwd`、`cd`、`export`、`unset`、`env`、`exit` |      |       |
| command execution  | 执行系统命令，如 `cat`、`grep`、`wc`                      |      |       |
| redirection        | `>`、`>>`、`<`                                    |      |       |
| pipeline           | `cmd1                                           | cmd2 | cmd3` |
| state persistence  | `cwd`、env、last status 跨调用持久化                    |      |       |
| error recovery     | syntax error、missing file、bad cd 不污染状态          |      |       |

### 2.4 推荐 rubric 数量

```text
unit cases: 16
system cases: 12
total: 28
```

### 2.5 MiniShell unit cases 草案

| id     | layer | category           | 测试点                           |
| ------ | ----- | ------------------ | ----------------------------- |
| USH001 | unit  | parsing            | 普通命令参数切分                      |
| USH002 | unit  | quoting            | 单引号禁止变量展开                     |
| USH003 | unit  | quoting            | 双引号允许变量展开                     |
| USH004 | unit  | builtin_echo       | `echo -n` 不输出尾随换行             |
| USH005 | unit  | builtin_pwd        | `pwd` 输出当前目录                  |
| USH006 | unit  | builtin_cd         | `cd` 成功改变 cwd                 |
| USH007 | unit  | builtin_export     | `export A=1` 设置变量             |
| USH008 | unit  | builtin_unset      | `unset A` 删除变量                |
| USH009 | unit  | env                | `env` 输出已导出变量                 |
| USH010 | unit  | last_status        | `$?` 展开为上一条命令状态               |
| USH011 | unit  | redirection_output | `>` 覆盖写文件                     |
| USH012 | unit  | redirection_append | `>>` 追加写文件                    |
| USH013 | unit  | redirection_input  | `<` 作为 stdin                  |
| USH014 | unit  | pipeline           | 两段 pipeline 输出正确              |
| USH015 | unit  | command_not_found  | 未知命令返回非零                      |
| USH016 | unit  | syntax_error       | pipe 结尾等 malformed command 失败 |

### 2.6 MiniShell system cases 草案

| id     | system_dimension            | category                          | 测试点                                |              |
| ------ | --------------------------- | --------------------------------- | ---------------------------------- | ------------ |
| SSH001 | state_accumulation          | env_persistence                   | `export A=hello` 后下一次 `echo $A` 可见 |              |
| SSH002 | state_accumulation          | cwd_persistence                   | `cd subdir` 后下一次 `pwd` 保持新目录       |              |
| SSH003 | cross_feature_dataflow      | redirection_then_cat              | `echo hi > f` 后 `cat f` 可读         |              |
| SSH004 | cross_feature_dataflow      | pipe_with_expansion               | `export X=foo` 后 `echo $X          | grep foo` 成功 |
| SSH005 | operation_order_sensitivity | overwrite_vs_append               | 先 `>` 再 `>>` 与两次 `>` 结果不同          |              |
| SSH006 | global_invariant            | failed_cd_preserves_cwd           | `cd missing` 后 cwd 不变              |              |
| SSH007 | error_atomicity             | syntax_error_preserves_env        | malformed command 不污染 env          |              |
| SSH008 | error_atomicity             | failed_redirection_preserves_file | 输入重定向文件缺失时，不创建错误输出文件               |              |
| SSH009 | boundary_crossing           | quote_expansion_pipeline          | 引号、变量展开、pipeline 同时出现              |              |
| SSH010 | boundary_crossing           | spaces_redirection                | 文件名/参数空格与重定向组合                     |              |
| SSH011 | state_accumulation          | last_status_after_pipeline        | pipeline 失败后 `$?` 正确               |              |
| SSH012 | global_invariant            | unset_then_env_then_expansion     | `unset` 后 `env` 和变量展开都一致           |              |

MiniShell 的核心 gap 预期：模型通常能单独实现 `echo/cd/export/pipeline/redirection`，但在 **pipeline + redirection + env + last status + 持久化状态** 组合时失败。

---

## 3. MiniGraph / MiniBuildGraph 任务推进方案

### 3.1 Source repo

参考仓库：

```text
https://github.com/quarkslab/bgraph
```

`bgraph` README 说明它用于从 Android.bp Soong 文件生成 dependency graph，并支持查询已有 graph。其使用场景包括查找某个 AOSP source file 的所有依赖、查找构建某个 target 涉及的 sources、查找两个 targets 的公共依赖；CLI 主命令包括 `generate`、`generate-single`、`list`、`query`。([GitHub][3])

### 3.2 Mini 版本抽象

建议任务命名：

```text
task_id: minibuildgraph-realrepo-001
program: graphmini.py
```

运行方式：

```bash
python3 graphmini.py STATE_DIR COMMAND [ARGS...]
```

建议不要直接解析完整 Android.bp。为了降低难度，可以设计一个小型 blueprint-like DSL：

```text
module {
  name: "app",
  type: "binary",
  srcs: ["main.c"],
  deps: ["liba", "libb"],
}
module {
  name: "liba",
  type: "library",
  srcs: ["a.c"],
  deps: []
}
```

### 3.3 功能模块

| 模块         | 功能                           |
| ---------- | ---------------------------- |
| load       | 从文件加载模块定义，构建依赖图              |
| list       | 列出所有模块                       |
| info       | 查询单个模块 metadata              |
| deps       | 查询直接依赖                       |
| rdeps      | 查询反向依赖                       |
| closure    | 查询传递依赖                       |
| sources    | 汇总 target 构建涉及的 source files |
| common     | 查询两个模块公共依赖                   |
| remove     | 删除模块并更新图                     |
| validation | 重名、缺失依赖、循环、malformed file    |
| atomicity  | LOAD 失败不污染旧图                 |

### 3.4 推荐 rubric 数量

```text
unit cases: 16
system cases: 16
total: 32
```

### 3.5 MiniGraph unit cases 草案

| id     | layer | category       | 测试点                |
| ------ | ----- | -------------- | ------------------ |
| UBG001 | unit  | parser         | 解析单个 module        |
| UBG002 | unit  | parser         | 解析多个 module        |
| UBG003 | unit  | list           | `list` 按名称排序       |
| UBG004 | unit  | info           | 查询 type/srcs/deps  |
| UBG005 | unit  | deps           | 查询直接依赖             |
| UBG006 | unit  | rdeps          | 查询反向依赖             |
| UBG007 | unit  | closure        | 查询传递依赖             |
| UBG008 | unit  | sources        | 汇总直接 sources       |
| UBG009 | unit  | common         | 查询公共依赖             |
| UBG010 | unit  | remove         | 删除模块               |
| UBG011 | unit  | missing_dep    | 缺失依赖报错             |
| UBG012 | unit  | duplicate_name | 重名模块报错             |
| UBG013 | unit  | cycle          | 循环依赖报错             |
| UBG014 | unit  | malformed      | malformed file 报错  |
| UBG015 | unit  | empty_graph    | 空图 list/info 行为    |
| UBG016 | unit  | persistence    | load 后 graph 状态持久化 |

### 3.6 MiniGraph system cases 草案

| id     | system_dimension            | category                        | 测试点                                |
| ------ | --------------------------- | ------------------------------- | ---------------------------------- |
| SBG001 | cross_feature_dataflow      | load_then_deps                  | LOAD 后 deps/rdeps 结果来自同一图          |
| SBG002 | cross_feature_dataflow      | deps_then_sources               | dependency closure 影响 sources 汇总   |
| SBG003 | state_accumulation          | load_remove_query               | LOAD → REMOVE → query 状态一致         |
| SBG004 | state_accumulation          | reload_replace_graph            | 第二次 LOAD 替换旧图，不混合旧模块               |
| SBG005 | global_invariant            | reverse_edges                   | deps 与 rdeps 互相一致                  |
| SBG006 | global_invariant            | no_dangling_after_remove        | REMOVE 后不存在 dangling reverse edge  |
| SBG007 | error_atomicity             | failed_load_preserves_old_graph | malformed LOAD 失败后旧图保留             |
| SBG008 | error_atomicity             | missing_dep_preserves_old_graph | 缺失依赖 LOAD 失败后旧图保留                  |
| SBG009 | error_atomicity             | cycle_preserves_old_graph       | cycle LOAD 失败后旧图保留                 |
| SBG010 | operation_order_sensitivity | remove_then_closure             | remove 前后 closure 不同且正确            |
| SBG011 | operation_order_sensitivity | reload_then_common              | reload 后 common 基于新图               |
| SBG012 | boundary_crossing           | shared_deps_and_sources         | 公共依赖 + sources 汇总组合                |
| SBG013 | boundary_crossing           | duplicate_then_valid_reload     | 失败 reload 后再 valid reload 可恢复      |
| SBG014 | boundary_crossing           | isolated_module                 | 孤立模块不影响其他模块 closure                |
| SBG015 | global_invariant            | sorted_outputs                  | 所有 list-like 输出稳定排序                |
| SBG016 | state_accumulation          | multi_step_mutation             | load → remove → load → query 全流程一致 |

MiniGraph 的核心 gap 预期：模型能分别实现 `deps/rdeps/closure/remove`，但容易在 **remove 后反向边更新、failed LOAD 原子性、reload 替换语义、循环检测后旧状态保持** 上失败。

---

## 4. 你要补的文件清单

### 4.1 MiniShell

```text
task/minishell-realrepo-001/
  prd.md
  rubric.json
  doc/
    source_repo.md
    requirement_map.md
    score_reports/
      reference.json
      doubao_seed_2_0.json
      deepseek_v4_pro.json
      gpt_5_5_thinking.json
      codex_subagent_001.json
```

### 4.2 MiniGraph

```text
task/minibuildgraph-realrepo-001/
  prd.md
  rubric.json
  doc/
    source_repo.md
    requirement_map.md
    score_reports/
      reference.json
      doubao_seed_2_0.json
      deepseek_v4_pro.json
      gpt_5_5_thinking.json
      codex_subagent_001.json
```

### 4.3 根目录还要更新

```text
MANIFEST.json
score_summary.csv
README.md
```

README 需要把你的两个任务补到 task list 里。当前官方 README 已经以 task list 形式列出 confirmed tasks。([GitHub][1])

---

## 5. PRD 写法重点

### MiniShell PRD 不要写成这样

```text
先 export A=1，再 echo $A，必须输出 1。
```

这太像 rubric 泄露。

### 应该写成这样

```text
Environment mutations performed by successful builtin commands must persist across later invocations using the same STATE_DIR. Variable expansion must always read from the current persisted environment state.
```

### MiniGraph PRD 不要写成这样

```text
LOAD graph1 后 malformed LOAD graph2，再 list，必须还是 graph1。
```

这也是直接翻译测试。

### 应该写成这样

```text
Graph-loading commands are atomic. If a new graph cannot be fully parsed and validated, the previously persisted graph must remain unchanged and available for later queries.
```

---

## 6. 你可以直接粘到进度区的文本

## 张凯杰进度区：MiniShell 与 MiniGraph / MiniBuildGraph

### 6.21 进展

根据课题组最新确定的 unit-system gap 研究方向，对个人负责的两个任务 MiniShell 和 MiniGraph / MiniBuildGraph 进行了重新对齐。重点检查两个任务是否符合 PRD-only、hidden rubric、确定性 oracle、unit/system 双层评测的要求。MiniShell 继续基于 mcombeau/minishell 抽象，MiniGraph / MiniBuildGraph 继续基于 quarkslab/bgraph 抽象，两个任务都保留真实开源项目中的状态传递、跨模块依赖和错误恢复特征。

### 6.22 进展

重新梳理 MiniShell 的任务边界。为了避免交互式 shell 难以稳定评测，将任务形式收敛为 Python CLI 程序 `minishell.py`，通过 `STATE_DIR` 保存跨调用状态。功能范围保留命令解析、引号处理、环境变量展开、builtin 命令、pipeline、redirection、last status 和错误恢复。当天重点是明确哪些行为来自原 minishell 项目，哪些行为属于 benchmark 化后的简化抽象。

### 6.23 进展

完善 MiniShell 的 PRD 和 requirement map。PRD 中强调用户可见行为和全局不变量，例如成功的 `cd/export/unset` 需要持久化，失败命令不能污染 cwd/env/last status，redirection 与 pipeline 应和变量展开后的命令结果一致。requirement_map 将 parsing、expansion、builtin、pipeline、redirection、state persistence、error atomicity 分别映射到 unit cases 和 system cases。

### 6.24 进展

设计 MiniShell 的 rubric。初步确定 16 个 unit cases 和 12 个 system cases。unit cases 主要覆盖单个功能模块，例如 echo、cd、export、unset、pwd、变量展开、输入输出重定向和两段 pipeline。system cases 重点覆盖跨命令状态、pipeline 与变量展开组合、redirection 与文件状态组合、失败 cd 后 cwd 保持、syntax error 后环境变量不污染、last status 跨调用更新等系统级行为。

### 6.25 进展

重新梳理 MiniGraph / MiniBuildGraph 的任务边界。参考 quarkslab/bgraph 从 Android.bp Soong 文件生成和查询依赖图的设计，将任务简化为 `graphmini.py`，输入为小型 blueprint-like module 文件。功能范围包括 LOAD、LIST、INFO、DEPS、RDEPS、CLOSURE、SOURCES、COMMON、REMOVE，以及重复模块、缺失依赖、循环依赖、malformed file 的错误处理。当天重点是明确 graph state 的持久化和 LOAD 失败原子性。

### 6.26 进展

完善 MiniGraph / MiniBuildGraph 的 PRD、source_repo.md 和 requirement_map.md。source_repo.md 说明任务与 bgraph 的对应关系，包括 module parsing、dependency graph construction、query、reverse dependency、common dependency 和 source aggregation。requirement_map 将模块解析、依赖图构建、图查询、传递闭包、反向边维护、删除更新、reload 替换语义和 failed LOAD 原子性映射到 unit/system 测试点。

### 6.27 进展

设计 MiniGraph / MiniBuildGraph 的 rubric。初步确定 16 个 unit cases 和 16 个 system cases。unit cases 检查单个图操作，例如解析 module、列出模块、查询直接依赖、反向依赖、传递依赖、公共依赖和删除模块。system cases 重点覆盖 LOAD 后多查询一致性、REMOVE 后无 dangling edge、reload 替换旧图、failed LOAD 保留旧图、cycle/missing dependency 不污染已有 graph state、以及 deps/rdeps/sources/common 之间的跨功能一致性。两个任务均准备进入 reference implementation 和多模型 candidate 跑分阶段。

---

## 7. 最短执行路径

你现在按这个顺序做，效率最高：

1. **先补 `source_repo.md`**

   * MiniShell：引用 minishell 支持的 builtin、pipe、redirection、env expansion、不支持项。
   * MiniGraph：引用 bgraph 的 generate/query/list、Android.bp/Soong dependency graph 用途。

2. **再写 `prd.md`**

   * 重点写自然需求和全局不变量。
   * 不要写具体测试序列。

3. **写 `requirement_map.md`**

   * 每个 REQ 对应至少 1 个 unit case。
   * 每个 system case 对应至少 2 个 REQ。

4. **写 `rubric.json`**

   * MiniShell：16 unit + 12 system。
   * MiniGraph：16 unit + 16 system。
   * system case 必须有 `system_dimension`。

5. **实现 reference**

   * reference 必须 100/100。
   * 不要让测试依赖 reference 私有存储格式。

6. **跑 3–4 个模型 candidate**

   * 目标是形成 ≥15pp gap。
   * 如果 gap 不够，优先增强 system case，不要随意加难 unit case。

---

## 8. 验收标准

| 项目                   |           MiniShell |           MiniGraph |
| -------------------- | ------------------: | ------------------: |
| `prd.md`             |                 必须有 |                 必须有 |
| `rubric.json`        | 16 unit + 12 system | 16 unit + 16 system |
| `source_repo.md`     |                 必须有 |                 必须有 |
| `requirement_map.md` |                 必须有 |                 必须有 |
| Reference score      |             100/100 |             100/100 |
| system_dimension 覆盖  |                ≥4 种 |                ≥4 种 |
| raw gap              |            目标 ≥15pp |            目标 ≥15pp |
| adjusted gap         |            尽量 ≥10pp |            尽量 ≥10pp |
| score_reports        |              ≥3 个模型 |              ≥3 个模型 |

---

## 9. 关键提醒

你这两个任务是很适合 core strong 的：

* **MiniShell** 天然有 `parser → expansion → execution → redirection/pipeline → status/env/cwd persistence` 的系统链路。
* **MiniGraph** 天然有 `parser → graph construction → deps/rdeps/closure/sources/common → mutation/reload/error atomicity` 的系统链路。

不要把主要精力放在单个命令做得多复杂。真正要卡模型的是：

```text
单个功能看起来都能过，但组合起来状态错、不变量错、失败恢复错。
```

这正好贴合你们课题的 principal claim：**部件正确 ≠ 系统正确**。

[1]: https://github.com/E2E-Bmk/Bmk-dev/tree/main "GitHub - E2E-Bmk/Bmk-dev · GitHub"
[2]: https://github.com/mcombeau/minishell "GitHub - mcombeau/minishell: Minishell is a 42 school team project to create a basic shell program in C. It implements redirections and pipes, as well as environment variables and some builtin commands. · GitHub"
[3]: https://github.com/quarkslab/bgraph "GitHub - quarkslab/bgraph: BGraph is a tool designed to generate dependencies graphs from Android.bp soong files. · GitHub"
