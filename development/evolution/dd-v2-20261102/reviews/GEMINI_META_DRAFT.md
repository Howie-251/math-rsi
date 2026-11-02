### 实际阅读范围

本轮按 `research-review` 的数学工作流维护 `composed` 适配执行静态原件审阅，实际完整读取以下文件（未扩读 DD 全库、未修改文件、未运行外部模型或重跑数学计算）：

1. [base/skills/mathrsi-meta-evolve/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md)（全文 1–217 行）
2. [base/skills/mathrsi-meta-evolve/references/aris-adaptation.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/aris-adaptation.md)（全文 1–53 行）
3. [base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md)（全文 1–283 行）
4. [docs/EVOLUTION_WORKFLOW.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/EVOLUTION_WORKFLOW.md)（全文 1–58 行）
5. 交叉核对接口契约：[AGENTS.md](file:///Users/rfy_naiveai/Desktop/MathRSI/AGENTS.md)（1–90 行）、[docs/PLUGIN_CONTRACT.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md)（1–74 行）、[docs/ARIS_REUSE.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/ARIS_REUSE.md)（1–153 行）。

---

### 已就绪且可直接执行的部分（直接认可）

1. **单入口收敛与去重干净**：[EVOLUTION_WORKFLOW.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/EVOLUTION_WORKFLOW.md#L1-L58) 已收束为 58 行人读说明与历史案例索引，将取证、分层、实现、审阅、自用与采纳的唯一执行链归口到 [mathrsi-meta-evolve/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md)，消除了文档与技能双份维护漂移，也没有按动词拆出多余的空壳子技能。
2. **无收益前置已全部清除**：
   - [SKILL.md §1](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md#L56-L65) 明确“阅读不是无限前置任务”，按因果研究链委派 Sol，某项修改证据成熟即进入实现，未读无关文件不阻塞开工；
   - [SKILL.md §5](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md#L160-L165) 与 [aris-adaptation.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/aris-adaptation.md#L18-L35) 已明确移除“无历史 agent 独立重跑完整流程”“必须有 `events.jsonl` 及 5 次调用门槛”“投稿评分收敛”“独立 `meta-apply` 人工审批门”等过度前置，改为由 Root/协调者自己按候选技能执行、多 Sol 协助具体写作与核对。
3. **五条 DD 证据链与相对路径准确**：`SKILL.md` 及两份 reference 中的全部仓库内相对链接（`../../../docs/`、`../skills-codex/`、`../../../../development/` 等）经逐一核对层级全部准确；[evidence-and-transfer.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md) 的五条链均包含真实公式、反例、原件相对路径以及 `Base / 领域插件 / 单题状态 / 不采用` 的四层切分。

---

### 真正缺口与最小具体修法（共 3 处）

对照“Root 立即读取本技能推进 base v1$\to$v2 并集成 DD 插件、多 Sol 并行协作”的实际执行需求，现有成稿仅有以下 **3 处具体衔接缺口**，均可在原位用几句话补齐：

#### 缺口 1：[SKILL.md §3](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md#L125-L134)“新领域插件”缺少随仓两层结构（整理层 + 原始资料层）及接回五个 base 子工作流的具体挂载点
- **问题所在**：§3 写了新插件要回答什么、原件可作只读 archive 保存，但没有写明 Root/Sol 在创建 DD 插件时：① 插件目录内如何组织**整理层（`skills/`）与随仓原始资料层（原 `research-wiki`、支撑证明、程序、失败实例、审阅与已省略大文件清单）**；② 如何把新插件挂载到内层五个子工作流的实际调用处（对照 [PLUGIN_CONTRACT.md:11-17](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md#L11-L17)）及宿主的仓库内发现别名（`.claude/skills/` 与 `.agents/skills/`）。若不写清，多 Sol 写完插件后容易停留在孤立目录，未能与 `survey`/`route-loop`/`prove`/`verify` 接通。
- **最小修法**：将 [SKILL.md:131-133](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md#L131-L133) 替换为以下具体挂载段落：
  ```markdown
  新插件在仓内分两层落地：**整理层**（`plugins/<domain>/skills/` 下的入口与专项技能）告诉接手代理在哪个子工作流阶段读取什么知识、调用哪个检查器或构造器、返回什么产物；**原始资料层**（随插件保存的原 `research-wiki`、证明、构造与搜索代码、失败实例、审阅记录及复现入口）保留详细依据与历史更正，标明只读来源、历史任务属性及原包已省略的大生成文件清单，不指向作者机器外部路径，也不宣称未随包大文件已读。原程序会写源目录时，把必要输入复制到当前任务的运行目录后调用；已有可移植重建入口直接复用。

  接入时同步对齐真实调用处与发现入口：明确 `prepare/survey`（领域基线与已知构造族代入）、`route-loop`（失败机制诊断与探针）、`prove`（具体构造、归约与局部定理）、`verify`（领域独立检查器、覆盖与形式化桥接）各自调用的插件技能与返回位置，更新 `docs/PLUGIN_CONTRACT.md` 的入口说明及本仓 `.claude/skills/`、`.agents/skills/` 相对发现别名。新题积累写新题自己的工作区 wiki；插件更新由外层维护处理，不在解题时静默改核心。
  ```

#### 缺口 2：[references/evidence-and-transfer.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md) 链二至链五的“可进入 base 的动作”未点名具体目标文件与上下游产物衔接（且链三漏掉了实际执行检索的 `mathrsi-survey`）
- **问题所在**：
  - 链三（[L171](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L171)）写“可进入 `prepare`／`route-loop` 的行为是：研究目标依赖当前基线时，比较已知构造族及其适用条件”，但实际在 v1 中负责查文献并生成 `LITERATURE.md` 基线的是 `mathrsi-survey`（由 `prepare`、`route-loop` 或 `prove` 调用），消费基线截停无意义候选的是 `route-loop` 与 `prove`。
  - 链二（[L144](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L144)）、链四（[L203](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L203)）、链五（[L235](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L235)）只写了阶段名，未点明多个 Sol 并行修改 `base/skills/` 时各自改哪个步骤、上游交什么返回信息、下游怎样消费。
- **最小修法**：对 `evidence-and-transfer.md` 的四处各补一句精确的 caller$\to$consumer 文件落点：
  1. **链二（[L144](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L144)）**：明确落点为 `[prove](../../mathrsi-prove/SKILL.md)`（多步构造/克隆时区分冻结源快照与演化对象，失败回交时写明所依赖的限制条件）、`[route-loop](../../mathrsi-route-loop/SKILL.md)`（修法阶段检查新方案释放了哪条旧自加限制、哪些旧负结论因前提改变而失效）及 `[verify](../../mathrsi-verify/SKILL.md)`（对象局部修改后复用未变源证明，仅直验受影响部分与新顶层绑定）。
  2. **链三（[L171](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L171)）**：将“可进入 `[prepare](../../mathrsi-prepare/SKILL.md)`／`route-loop`”修正补齐为：“可进入 `[prepare](../../mathrsi-prepare/SKILL.md)`、[`survey`](../../mathrsi-survey/SKILL.md)、`route-loop` 与 `prove` 的行为是：`survey` 在 `LITERATURE.md` 中除记录显式表值外，计算已知构造族/一般定理代入当前参数的推论基线并提取可复用公开对象；`route-loop` 与 `prove` 消费新基线后，撤掉条件规模已被超过的待跑候选、保留已生成实例的数学合法性但更新比较措辞，或将公开最优对象作为新进口改变源与中心规则。”
  3. **链四（[L203](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L203)）**：明确落点为 `[route-loop](../../mathrsi-route-loop/SKILL.md)` 的探针派发/回收与 `[prove](../../mathrsi-prove/SKILL.md)` 的停止判断（必要门通过交出剩余共同约束给 `prove`；`UNKNOWN`/样本失败保留原状态不升级为全域 `NO`；存在性完整见证或必要域严格矛盾已闭合当前义务时，立即停止同分支更昂贵的扩张计算）。
  4. **链五（[L235](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#L235)）**：同时链接 `[verify](../../mathrsi-verify/SKILL.md)` 与本仓 `lean-formalize` 调用约定，加上“大批量同构有限模块派发前先跑单个非平凡模块实测成本，需要紧缩表示时在内核证明紧凑查表等于原定义，已通过模块保持不重编”。

#### 缺口 3：[SKILL.md §5](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md#L160-L165) 多 Sol 分目录写完后的“跨文件调用链自检”与避免 meta 套娃说明
- **问题所在**：当多个 Sol 按独占写域分别修改 `base/skills/` 与 `plugins/dd/` 时，各自检查自己的单文件容易忽略“base 调用处写的入口/返回与插件实际写的入口/返回是否对齐”；同时 §5 第 2 段提到“新 meta 技能本身可以通过一次真正维护使用来检验”，需明确**本次用 `mathrsi-meta-evolve` 完成 DD 驱动的 v1$\to$v2 本身就是这次真实使用**，结束后直接收束 §6，不再套娃启动第二轮 meta。
- **最小修法**：在 [SKILL.md:164](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md#L164) 句末补充两句：
  ```markdown
  本次由 Root 实际读取本技能、吸收 DD 证据完成 v1→v2 与插件落地的全过程，即构成对本技能的真实使用检验，收束时无需在结尾再套娃运行一轮新的 meta 验收。多作者分目录修改 base 与插件后，协调者须沿实际改动走通“base 阶段调用处 → 插件或下游技能入口 → 真实有界命令/原件核对 → 返回产物被原调用处消费”的跨文件连接，不以各作者单文件写完代替衔接核查。
  ```

---

### 审阅结论

现有 [SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md)、[aris-adaptation.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/aris-adaptation.md)、[evidence-and-transfer.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md) 与 [EVOLUTION_WORKFLOW.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/EVOLUTION_WORKFLOW.md) 主体结构清晰、执行粒度具体，已准确落实“先集成 meta 再由 Root 实际使用推进 v1$\to$v2、成熟证据及时回收实施、不设无历史 agent 全流程重跑前置”的要求。补齐上述 **3 处最小修法**（新插件两层结构与五阶段挂载、五条链到 base 具体文件落点、多 Sol 跨文件连接核查与非套娃收束）后，Root 即可直接读取该技能启动 v1$\to$v2 改动与 DD 插件实现。

