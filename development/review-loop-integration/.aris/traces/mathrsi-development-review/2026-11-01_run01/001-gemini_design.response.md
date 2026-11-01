基于已完整读取的 [`mathrsi-route-loop/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md)、[`skills-codex/auto-review-loop/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/auto-review-loop/SKILL.md)、[`skills-codex/research-review/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/research-review/SKILL.md)（及对应 Claude 版 [`research-review/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/research-review/SKILL.md)、[`reviewer-backends.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/shared-references/reviewer-backends.md)、[`output-composition.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/shared-references/output-composition.md) 与上游 `mcp-servers/`），给出四项具体架构与修法意见：

---

### 1. 原 ARIS 哪些执行环节必须真实保留（不只 transport / trace）

现行 [`mathrsi-route-loop/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L49-L71) 将 ARIS 审阅压缩成了“单次问答 slot”，丢掉了 [`auto-review-loop`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/auto-review-loop/SKILL.md) 与 [`research-review`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/research-review/SKILL.md) 真正产生对抗深度的 **5 个核心执行环节**，必须完整恢复：

1. **逐 Reviewer 持久怀疑记忆（Phase B.5 `REVIEWER_MEMORY`）**：
   - 每轮调用前必须在 Prompt 顶部注入 `## Your Reviewer Memory (persistent across rounds)`，要求审阅者逐项核查“上一轮指出的漏洞是真正被新推导/探针解决，还是被文字改写绕过”，并强制返回 `Memory update` 段落追加回记忆文件。
   - 当用户同时指定多个 reviewer（如 Grok + Gemini/Antigravity）时，必须**按 reviewer 分别维护其 `threadId`/session 与对应的记忆段落**，不能混成一份无归属摘要。
2. **主报告内一字不差留存原文（Phase B & E Verbatim Raw Response）**：
   - 除写入 `.aris/traces/` 外，每轮必须把审阅模型的完整原始回复一字不差（Verbatim）放入 `ROUTE_REPORT.md` 的 `<details>` 折叠块中，严禁只写协调者提炼后的几条 bullet。
3. **基于原会话的即时反驳与追问对话（`research-review` Step 3 + `auto-review-loop` Phase B.6 Debate）**：
   - 收到初评后，对审阅者漏看已有引理、误读记号或提出无区分力的泛泛质疑，必须通过已保存的 `threadId`（`send_input` / `grok-reply` / `antigravity-reply`）发回证据反驳或追问，要求其明确裁决（accepted / partially accepted / rejected）并锁定**最小区分性动作**。
4. **先实作再复核、带 Diff 与原始新证据续接（Phase C/D → Round 2+ Continuation）**：
   - 绝不能只改计划文字就送复核。必须先完成 `formula-derivation`、`proof-writer` 或计算探针，再把 `Changed files`、`git diff` 和**新推导/探针的原始输出文件**发回**同一 `threadId` 会话**复核。
5. **抗上下文压缩的恢复记录（Initialization & Phase E State Recovery）**：
   - 每轮结束时在工作区保存当前 `run_id`、`round`、各 reviewer 的已解析 `route` + `threadId` + `cwd` 及在途探针路径。恢复或跨轮续接时直接沿原 `threadId` 进 Round $N+1$，避免每次恢复都当成 fresh start 重开新会话。

---

### 2. `mathrsi-route-loop` 外层唯一控制 + `research-review — composed: ROUTE_REPORT.md` 负责审阅对话：如何避免内外双驱动又不砍掉对话？

**该分层完全合理。** [`research-review`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/research-review/SKILL.md#L129-L135) 原生支持 `— composed: <canonical-report-path>`（不乱写独立 `RESEARCH_REVIEW.md`，保留 `.aris/traces/`，将结论交回父报告唯一 writer）。

要同时避免“内外两层都去改路线/跑探针”和“把 `research-review` 砍成哑巴单轮调用”，只需按 **“同轮对话内聚于 `research-review`，跨轮实作外控于 `mathrsi-route-loop`”** 切分职责：

```text
mathrsi-route-loop (唯一外层循环控制者，拥有 Round 1..MAX_ROUNDS 与 ROUTE_REPORT.md 写入权)
  ├── Phase 0: 恢复/初始化 (读取 FORMAL_SPEC, LITERATURE, NEXT_SESSION, 恢复已存 threadId 与 REVIEWER_MEMORY)
  ├── Phase A & B [委托 research-review — composed: ROUTE_REPORT.md]:
  │     ├── Step 1-2: 组装原件路径 + 注入 REVIEWER_MEMORY → 发起首轮调用 (或 Round 2+ 续接调用)
  │     ├── Step 3 (同轮内对话): 针对本轮回复，沿同一 threadId 执行反驳 (Debate) 与追问，
  │     │            直到锁定「最小区分性推导/探针」与「结果→路线决策矩阵」
  │     │            【硬边界：research-review 内部只读文件与对话，绝不改证明草稿、不派推导/探针 worker】
  │     └── Step 5-6: 保存 .aris/traces/，向 route-loop 返回：完整原回复、对话记录、Memory update、
  │                  threadId、以及排好序的最小实作清单
  ├── Phase C & D [route-loop 独占执行]:
  │     └── 真正调用 formula-derivation / proof-writer / mathrsi-survey / 领域探针程序，产出新数学/计算原件
  └── Phase E [route-loop 写入与停止判断]:
        └── 将本轮原回复、对话、新探针证据与 Memory update 写入 ROUTE_REPORT.md；
            若路线已可执行且关键质疑已闭 → 终轮交接首批任务给 mathrsi-prove；
            若新证据暴露新问题或需复核 → 带 git diff 与新原件进入 Round N+1 (复用同一 threadId)
```

- **修改落点**：在 [`mathrsi-route-loop/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L49-L71) §3 中，将原来的“只执行一个 slot，不启动迭代”改为：**显式传 `— composed: ROUTE_REPORT.md` 调用 `research-review` 完成本轮的初始审阅 + Step 3 反驳/追问对话，锁定最小区分性动作后返回 `mathrsi-route-loop` 执行 §4 推导与探针；§4 产出新原件后，再由 `mathrsi-route-loop` §5 调用 `research-review` 沿原 `threadId` 发起下一轮验证复核。**

---

### 3. 哪些 ML 专属条件需替换为数学路线判断（替换对照表）

| 原 ARIS (`auto-review-loop` / `research-review`) ML 环节 | `mathrsi-route-loop` 数学路线替换规则（基于 Property B / ECC 实证） |
| :--- | :--- |
| **Reviewer 角色与四问**（NeurIPS 审稿人、打 1–10 分、补 baseline/消融实验、每 GPU 周最高接收率提升） | 替换为数学路线四问：① **归约方向与自由度**（充要 vs 必要覆盖 vs 子族；多重 WLOG 是否争抢同一对称自由度）；② **共同原对象与活跃项**（局部视图松弛是否丢掉同一母超图 $H$ / 同一母码 $K$ 的全局约束；新扣除能否改变真正控制总界的活跃项）；③ **真实 Caller 连接**（任意原输入能否满足新引理前提）；④ **最小区分性动作**（最便宜的一步推导或小域探针）。 |
| **`research-review` Step 3 的 Results-to-Claims Matrix**（实验 X/Y 不同数值结果允许写什么论文 claim） | 替换为 **探针结果→路线分支矩阵（Probe-to-Route Matrix）**：明确约定“若探针证明两松弛在活跃域恒等（如 PB 21 点 DP）→ 停扩该表并换共同矩阵约束；若必要条件图为空（如 ECC 172 母码兼容 pair 图无边）→ 直接关闭高阶扩张；若仅排除部分紧配置 → 保留结构引理并收缩剩余域”。 |
| **Phase B.5.1 停止门**（`score >= 6 AND verdict ∈ {"ready", "almost"}` + `ACQUITTAL_LOG.jsonl`） | **废除分数门**，替换为 **路线可行动门（Route Actionability Gate）**：① 共同对象与归约方向无未决逻辑倒置；② 决定路线生死的最小区分性探针/推导已实际跑出并支撑该路线；③ 审阅者指出的路线级阻塞已被新证据消除，或由 Root 凭具体数学原件有据驳回（保留审阅原文与反驳证据，绝不伪造 reviewer PASS）；④ 已形成可由 `mathrsi-prove` 直接接手的独占任务包。 |
| **Phase C/D 实作与等待**（改训练脚本、SSH+screen 跑 GPU、`/training-check` 查 W&B NaN） | 替换为：调用 `formula-derivation`（固定共同对象公式）、`proof-writer`（试证关键选择引理或找反例）、`mathrsi-survey`（补查文献定理条件）或运行领域小探针（实测生成+运输+读回+独核端到端成本，如 ECC 先测 1 例完整替代扫描再扩 172 例）。 |
| **Termination 终轮收尾**（写 `## Method Description` 供画架构图 + 调 `/result-to-claim`） | 替换为：在 `ROUTE_REPORT.md` 末尾固化 **终轮交接段（Final Route Handoff）**——选定主/备路线、已证/进口/待证条件清单、已封存死胡同与重启条件、以及交由父流程调度 `mathrsi-prove` 的**第一批具体任务（含输入文件、允许假设、独占写域、真实 Caller 要求）**。 |

---

### 4. 直接携带 `grok-exec` / `antigravity-exec` MCP 的分层审查与 4 个真实必补连接

将上游 Python 标准库实现的 MCP 桥接原样带入本仓、由宿主 MCP 直接调用而不另造第二套 Python 调度器，**方向完全正确且最轻巧**。但对照上游源码与 [`reviewer-backends.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/shared-references/reviewer-backends.md)，必须补齐以下 **4 处具体连接** 才能真正跑通：

1. **`antigravity-exec` 必须随带 `aris-antigravity-review.md` 并写明安装位置**：
   - 上游 [`antigravity-exec/server.py`](file:///Users/rfy_naiveai/Desktop/aris_main/mcp-servers/antigravity-exec/server.py#L42) 第 42 行硬编码了 `--agent aris-antigravity-review`。复制 `base/mcp-servers/antigravity-exec/` 时，必须同时带入同目录的 [`aris-antigravity-review.md`](file:///Users/rfy_naiveai/Desktop/aris_main/mcp-servers/antigravity-exec/aris-antigravity-review.md)，并在说明文档中写明需将其复制到 `~/.gemini/config/agents/aris-antigravity-review.md`，否则 `agy` 调用会因找不到 subagent 报错。
2. **双宿主下 Claude Code 默认审阅器的桥接缺口（`codex-exec`）**：
   - 按 [`reviewer-backends.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/skills-codex/shared-references/reviewer-backends.md#L21) 与 Claude 版 [`research-review/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/research-review/SKILL.md#L59-L63)，当宿主是 Claude Code 且使用默认 `backend=codex` 时，它调用的是 `mcp__codex__codex`（由上游 `mcp-servers/codex-exec/server.py` 提供）。若要保持双宿主自包含，建议把同为单文件标准库的 `mcp-servers/codex-exec/`（及按需 `claude-review/`）与 `grok-exec`、`antigravity-exec` 一起放入 `base/mcp-servers/`。
3. **测试脚本相对路径与 `ARIS_SNAPSHOT.json` 清单同步**：
   - 上游 [`tests/test_grok_exec_bridge.py`](file:///Users/rfy_naiveai/Desktop/aris_main/tests/test_grok_exec_bridge.py#L13) 与 [`tests/test_antigravity_exec_bridge.py`](file:///Users/rfy_naiveai/Desktop/aris_main/tests/test_antigravity_exec_bridge.py#L13) 第 13 行均通过 `Path(__file__).resolve().parents[1] / "mcp-servers/<name>/server.py"` 定位服务。因此只要将桥接放在 `base/mcp-servers/{grok-exec,antigravity-exec}/`、测试放在 `base/tests/test_*_exec_bridge.py`，**无需改动上游一字节即可直接运行 unittest**。
   - 同时需将新增的上游文件及其 Git blob SHA 增补进 `base/ARIS_SNAPSHOT.json`，保持 [`base/tests/smoke_bundle.py`](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/ARIS_REUSE.md#L132-L138) 的快照核验一致。
4. **首轮显式传 `reviewer_route.py` 解析出的 `model`/`effort` 与续接仅传 `threadId` + `prompt`**：
   - [`antigravity-exec/server.py`](file:///Users/rfy_naiveai/Desktop/aris_main/mcp-servers/antigravity-exec/server.py#L38) 内部环境变量默认模型是 `gemini-3.8-flash-high`，而 `reviewer_route.py` 解析的默认模型是 `gemini-4-argon-high`。因此在 `mathrsi-route-loop` 和 [`docs/ARIS_REUSE.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/ARIS_REUSE.md#L88-L93) 中要写清：**首轮调用 MCP 时必须显式传入 `reviewer_route.py` 输出的 `model`、`effort` 和包含被审原件的绝对路径 `cwd`；续接调用（`grok-reply` / `antigravity-reply`）则严格只传 `threadId` 和 `prompt`**（传额外字段会被桥接拒绝）。