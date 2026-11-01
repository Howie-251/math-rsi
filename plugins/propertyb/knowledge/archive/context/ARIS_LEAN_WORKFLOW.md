# 从 aris4math 提炼的 ARIS Lean 工作流

已新增 **`lean-formalize`** skill，将“数学命题→完整 Lean 主定理→可复现查验”作为它的专门职责。现有 `proof-writer`、`proof-checker`、`proof-orchestrator` 已覆盖推导、审计和持续研究；Lean 技能补上实际形式化与完成判定，不另建一套研究框架。

**已通过 [ARIS PR #461](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/pull/461) 合并**，提交 `7fa3a4f`。正式入口为 [Claude 版](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/lean-formalize/SKILL.md)和 [Codex 版](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/skills-codex/lean-formalize/SKILL.md)，各含三份按需阅读的参考。本项目 `aris-skill-drafts/lean-formalize/` 保留为前期草案快照。2026-10-07 已在本机 Codex 与 Claude Code 的全局技能目录分别安装新技能，并更新五个相关入口；私有配置和共享 reviewer 路由保留，见[安装记录](skill-evaluation/lean-formalize/local-install-20261007/INSTALLATION.md)。

## 最值得固化的经验

本项目早期已有大量通用引理和数值声明编译通过，原目标却仍只是定义。真正完成的步骤是把实际超图、类型重数、真实排列事件、严格界与原染色见证全部连起来。因此完成条件必须落在**原始命题的实际证明**上。

| 环节 | 应产出的依据 | 本项目暴露的误判 |
|---|---|---|
|固定规格|明确对象、量词、原假设、结论，并对应 Lean 定义|把内部点对覆盖、顶点数范围误加到原目标|
|局部推导|明确引理及其调用条件|看到某个分数小于1就宣称证明完成|
|实际输入连接|从任意输入构造出引理要求的对象和前提|把 profile、概率界或类型实现留成待用户提供的参数|
|整体装配|主定理消除所有内部条件，返回原结论|只完成约化或单个分支|
|机器核验|显式构建 Main、另行导入、展开声明、打印传递公理|默认 `lake build` 只编译了定义所在的根模块|
|独立查验|具体数学义务审阅、实际复现日志、范围明确|把多模型赞同或读取日志称作独立重建|
|交接维护|可读证明、完整源码、锁定环境、下一步或完成状态|把本机路径和缓存当作可移植材料，或复活旧缺口|

## 与既有 ARIS 技能的配合

```text
固定原命题与 Lean 定义
  → A：跨家族独立反译与命题对齐
  → 拆分证明义务、表示与接口
  → Lean 实现 ↔ B：关键论证、反例及实际输入连接的对抗式审阅
  → 补齐调用前提，装配原主定理
  → 执行类型、定义及传递公理审计
  → C：跨家族审阅最终导出的原定理
  → 可复现交接，并更新 research wiki 与继续工作入口
```

Lean 按需启用：用户要求、续接已有 Lean 项目，或核心结论的具体证明义务值得形式检查。普通推导和短证明保留原流程，难度本身不触发。已在 proof-writer、proof-checker、proof-orchestrator、formula-derivation 和 research-pipeline 的两个宿主版本加入入口。Lean 子任务只关闭自己实际证明的义务，再将证据交回调用者；从 Lean 委派到 proof-writer 的数学工作不递归转回 Lean。

已有数学证明可直接进入 Lean；已有 Lean 项目从剩余义务继续。A/B/C 是实质性新证明项目的流程组成部分；接续工作复用未改变且已检查的结论，小型常规形式化按任务规模执行，但用户明确要求的跨家族审阅仍须落实。

按需要用 `research-lit` / `research-wiki` 查来源和已有结论，`proof-writer` / `formula-derivation` 补数学论证，`proof-checker` 审核证据，`research-review` / `auto-review-loop` 组织讨论与修复，`render-html` 生成阅读版。不要求每道题跑遍全部技能；既有审计角色、路由及输出格式保持原样。

## 跨模型审阅怎么嵌入

本项目已授权 Grok 和 Antigravity/Gemini。用户指定两家，就分别落实两家，不以一家或同家族子代理替代另一家。可迁移技能遵循当前授权，不将特定厂商、型号、额度、代理或重试次数写成所有用户的前提。

| 检查点 | 交给审阅者的实际材料 | 要解决的问题 |
|---|---|---|
|A：命题对齐|先给必要 Lean 定义与目标独立反译，再与原题比较|对象、量词、隐含参数、表示对应是否保持原意|
|B：新论证和连接|引理与证明、真实调用者、前提来源、相关计算解释|能否找到满足前提的反例；是否遗漏分类或把结论藏进输入|
|C：最终装配|最终源码、展开声明、实际类型及公理输出、构建记录；需要交付的纸面证明|任意原始输入是否走到原结论；最终文本是否超出源码所证|

首次独立审阅不传执行者结论或另一模型意见；后续同题讨论明确标为定向复审。保留实际读取范围、原始回应及处理意见。能力不可用就保留对应待办，同时继续可进行的证明工作。

每条实质异议记录位置、理由、验证方法、处理结果和剩余动作。候选反例先核对全部前提；语义不符要给对应关系或修正；编译问题查确切声明及输出。模型也会误读，不能为获得赞同而给原题添加假设。

修复后发送受影响的声明、调用和输出。常规 tactic 调整且含义、信任基础未变，只需相应编译；命题、定义、信任基础或关键论证变化，则检查其影响。Markdown/HTML 中修改定理同样属于命题修改。

调用既有 ARIS loop 时沿用其轮次及续接规则。直接咨询依具体问题推进，问题处理完即结束；不可用就记录待办，轮数耗尽不能代替证明。未改变的材料不反复送审以积累赞同。

## 计算与证明的边界

可复用原则是“证明覆盖及语义对应，再使用经核验的计算”。本项目用户要求不以整图枚举作为最终路线；这应保留为项目约束，不能推广成所有形式化项目都禁止穷尽计算。合法有限证明、经验证的证书和一般定理可以组合；有限样例没有覆盖证明时，只提供测试证据。

同样，不把本项目实际出现的三个标准公理当成每个证明必须恰好出现的名单。要核对具体声明的传递依赖及任务允许的信任基础。编译器支持的计算涉及更大的信任范围，需按固定 Lean 版本判断并如实记录，不能为了消掉报错而悄悄扩大。相关机制见 [Lean 官方参考](https://lean-lang.org/doc/reference/latest/)及[社区维护的说明](https://leanprover-community.github.io/extras/pitfalls.html#native_decide)。

## 用多大的文件结构

保留一个技能入口、三份按需阅读的参考及 Codex UI 元数据。主文件写核心决策，参考文件展开具体 Lean 操作、审阅与最终核验。沿用项目已有规格、义务表和交接文件；只有出现重复、具体的执行需求后，再考虑加 helper。

参考已有 [auto-review-loop](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/auto-review-loop/SKILL.md) 的执行细节：明确输入、保存实际回复、判断异议、落实修改、处理续接和终止。篇幅服务可执行性，不复制与 Lean 无关的后端配置或评分门槛来增加长度。

依照 [HERO](https://github.com/wanshuiyin/HERO-Anti-OverDefense/blob/main/RULES.md)，写清真正改变下一步行动的步骤，不新增调度服务、状态数据库、重复哈希或无限审查。数学严谨及用户要求的跨模型审阅属于任务本身，照常完成。

正式贡献同时落到 `skills/lean-formalize/` 和 `skills/skills-codex/lean-formalize/`，按各宿主调整工具调用；补目录与相关技能入口，并运行仓库现有一致性检查。草案当前没有硬编码 `spawn_agent` 型号或 MCP 工具路径，便于保持两份语义一致。

2026-10-07 已完成的贡献范围为 **同一个 ARIS PR 同时提供两端**：主线给 Claude Code，`skills/skills-codex/` 给 Codex；本机 `~/.codex/skills/` 是安装位置。三份数学与 Lean 参考保持内容一致，仅适配宿主工具与 reviewer 调用。同步技能目录、`theory` 分组、数量及现有镜像检查，不另改全仓 reviewer 系统。

Claude Code 主线通常以 Codex MCP 审阅。Codex 基础包的第二 Codex agent 仍为 same-family/provisional；跨家族检查应使用用户指定或已配置的 Claude/Gemini 审阅入口，或按授权直接调用 Grok/Antigravity。现有覆盖包并不自动覆盖新 `lean-formalize`，也不覆盖 `proof-checker`：实现时要明确把 A/B/C 接到实际跨家族工具，不仅写“安装 overlay”。`gemini-review` 的 `review*` 协议与 `antigravity-exec` 的原生线程协议分别处理。Claude 文件审阅须按桥接契约每次启用只读文件工具；远程 API 审阅须实际收到源材料正文。

用户已确认 Claude reviewer 桥接此前实测可用，无需重复连通性验证。当前项目继续使用用户指定的 Grok＋Antigravity/Gemini。此次仅接入具体 Lean 工作流，不注册新 MCP 或改写其他技能的 reviewer 路由。

2026-10-07 深读 Argus 与 Archon-Horizon 后，补入固定库检索、真实 caller 试编、表示实验、诊断分流、失败层次与性能归因。Horizon 搜索代码已在本地固定 Mathlib 上运行，相关引理的实际调用与一个反例已由 Lean 编译检查；完整来源和适用范围见[数学 agent 方法综合说明](MATH_AGENT_HARNESS_SYNTHESIS.md)。

## 当前验证范围

技能结构验证和隔离行为检查的结果保存在 [skill-evaluation/lean-formalize](skill-evaluation/lean-formalize/)。两个测试源码均在 Lean 4.24.0 实际编译通过；独立测试者正确区分了仅证明 `Target → Target` 的情况与真正证明 `Target` 的情况，也没有把模拟的失败 reviewer 调用记为有效意见。测试指出的小型单文件边界已修正：直接编译并打印类型、公理可以提供相应核验，不强制另建工程。缺少额外交接核验不等于数学上缺少证明。该技能的通用效果仍需后续不同数学项目检验；本项目的一次成功不证明它可以解决任意难题。

[修订后情景检查](skill-evaluation/lean-formalize/revised-behavior-check.md)另行阅读指令，检查指定审阅缺席、较强命题桥接、合法空对象与 `def` 证明项；没有执行新的 Lean 构建。Grok 与 Antigravity/Gemini 均已首轮读取初稿并提出修订；执行者采纳及不采纳的理由见[首轮处理记录](skill-evaluation/lean-formalize/cross-model-r1/DISPOSITION.md)。两者对修订版的第二轮定向复审均返回 **Ready as a local skill draft**，未发现剩余执行性缺口，详情见[评审汇总](skill-evaluation/lean-formalize/REVIEW_SUMMARY.md)。本次审阅对象是技能指令，不是重新认证已交付的 Property B 证明。


## 上游集成的最终验证

Grok 首轮发现 Lean/proof-writer 互相转发风险和 Claude reply 会话标识未明确的问题，已在双端修复；定向复审返回 Ready。Antigravity/Gemini 只读审阅最终有效返回 Ready，且读到了修复后的返回规则。最新 PR 的 Linux/macOS 全量 CI、目录和 helper 检查均通过；本地选择安装与镜像测试 57 项通过。原始模型回复、修复 diff、执行范围及合并状态见 [上游 PR 记录](skill-evaluation/lean-formalize/upstream-pr-review/DISPOSITION.md)。这些是技能集成检查，未重新运行 Property B 证明。
