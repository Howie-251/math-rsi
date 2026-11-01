# lean-formalize：验证与跨模型审阅

本记录审查的是可复用的 Lean 工作流指令。没有重开已完成的 Property B 研究，也不将技能审阅当作数学证明认证。

## 当前上游状态

2026-10-07 已通过 [ARIS PR #461](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/pull/461) 合并双端技能和五处按需入口，提交 `7fa3a4f`。Grok 对集成提出两处修订，修复后的定向复审 Ready；Gemini 有效返回 Ready。最新 Linux/macOS 全量 CI 通过。正式技能在 ARIS 仓库中，本机主仓库已同步；双端全局目录也已各安装新技能并更新五个入口，保留私有配置，见[安装记录](local-install-20261007/INSTALLATION.md)。原始回复及最终事实见 [集成审阅处置](upstream-pr-review/DISPOSITION.md)和[本地核验](upstream-pr-review/VALIDATION.md)。

以下保留前期草案及其当时的验证范围，不用历史“尚未合并”覆盖上面的最终状态。

## 前期草案产物

- [中文工作流说明](../../ARIS_LEAN_WORKFLOW.md)
- [SKILL.md](../../../aris-skill-drafts/lean-formalize/SKILL.md)：核心流程、进入方式、实现循环、完成依据与持续状态。
- [Lean 工作循环](../../../aris-skill-drafts/lean-formalize/references/lean-working-loop.md)：固定库搜索、真实调用、表示实验、因果诊断、失败路线及性能处理。
- [对抗式审阅协议](../../../aris-skill-drafts/lean-formalize/references/adversarial-review.md)：A/B/C 触发、输入、提示、异议处置、复审和停止。
- [核验与交接](../../../aris-skill-drafts/lean-formalize/references/verification-and-handoff.md)：真实入口、实际类型、传递公理、固定环境及可移植源码。

前两轮审阅版本共 641 行。深读数学 agent 项目后，增加一份 184 行的 Lean 工作循环参考及主入口连接，当前主文件 318 行，三份参考共 516 行，总计 834 行。参考的 ARIS 主线 `auto-review-loop` 为 1137 行，Codex 适配版为 500 行。行数用于说明组织方式，不是质量验收指标。

## 执行层面的补充

原稿已有正确的“数学声明到 Lean 主定理”方向，但跨家族检查、异议修复和继续工作细节不足。现已将 A：命题对齐、B：关键论证及真实输入、C：最终声明审阅写入核心流程，并说明每一步实际输入与结果如何影响下一步。

遵循 [HERO](https://github.com/wanshuiyin/HERO-Anti-OverDefense/blob/main/RULES.md)：常规 tactic 调整使用受影响的编译检查；命题、关键论证或信任基础变化才重新检查相应问题。复用现有文件与 ARIS 合约，不新增状态数据库、评分体系、调度器或重复哈希。指定的 Grok/Gemini 审阅分别落实，失败调用保持待办，不替代也不伪造。

## 验证范围

- [结构检查](structure-validation.json)：官方 skill-creator 校验器退出码 0，`Skill is valid!`。
- [初始隔离案例](forward-test.md)：两份 Lean 4.24.0 源码实际编译，独立代理区分 `Target → Target` 与 `Target`，模拟失败审阅不产生 verdict。
- [修订后情景检查](revised-behavior-check.md)：阅读指令检查指定模型缺席、较强命题的蕴含桥接、合法空对象和 `def` 证明项；未执行新的 Lean 构建。
- 四份当前文档的本地相对链接已检查，无缺失目标。
- 未安装到全局技能、未改 ARIS 上游、未改已有 reviewer 路由。正式使用中的持续效果需从具体任务积累。

## 跨家族审阅

首轮均正常返回 **Needs specified revision**：[Grok](cross-model-r1/grok-response.md)、[Antigravity/Gemini](cross-model-r1/gemini-response.md)。[执行者处置](cross-model-r1/DISPOSITION.md)保留采纳、缩窄和未采纳意见的理由。两者只读文件，没有执行 Lean，也没有独立认证本项目数学结论。

修订版的两次原线程定向复审均有效返回，结论都是 **Ready as a local skill draft**，没有发现剩余的执行性缺口，也没有建议为增加篇幅补充无实际用途的规则。

| 审阅者 | 实际返回记录 | 本轮结论与范围 |
|---|---|---|
|Grok|`grok-4.7-build` / `xhigh`，`end_turn`|[原始回复](cross-model-r2/grok-response.md)：读取修订的三份技能文件、中文工作流和首轮处置；另读 UI 元数据与已安装 auto-review-loop 的执行主线。认可修订及未采纳建议的理由。|
|Antigravity/Gemini|CLI 选择 `gemini-3.8-flash-high` / `high`，`SUCCESS`|[原始回复](cross-model-r2/gemini-response.md)：读取指定的三份技能文件、中文工作流和首轮处置；认可修订及对首轮建议的数学纠正。|

两者均未运行 Lean/Lake 或修改文件。本轮是验证修订的续接，不是新的盲审；输入快照、请求和完整工具元数据保存在 `cross-model-r2/`。执行者核对了两份回复：没有剩余的具体修正要求，结束此次技能审阅。

本次结论是草案已具备所需执行细节。已完成结构校验和限定行为检查；它仍是本地草案，尚未合并或安装，不能由这次审阅推断未来任意数学任务都能成功。

## 数学 agent 调研后的增量

新增 `lean-working-loop.md` 及主文件对应路由；另将核验参考的版本表述准确写为“Lean 4.24.0 随附的 Lake”，避免把 Lean 版本当成 Lake 自身版本号。新版本结构校验通过。具体来源及真实执行见[综合说明](../../MATH_AGENT_HARNESS_SYNTHESIS.md)。

这次增加的执行指导单独送交原线程定向复审，不扩大前两轮评审的范围。两者均有效返回，没有提出剩余修正要求：

- [Grok 原始回复](harness-addition-review/grok-response.md)：`grok-4.7-build/xhigh`，`end_turn`；认为新增内容可用于本地技能草案。读取新参考、主文件改动、例子及日志，并核对固定库声明与相关上游来源。
- [Antigravity/Gemini 原始回复](harness-addition-review/gemini-response.md)：CLI 选择 `gemini-3.8-flash-high/high`，`SUCCESS`；认为该增量可以纳入本地草案。读取新参考、主文件改动、例子和执行记录，并检查来源。

两者都没有重新运行编译或审阅 Property B。执行者核对回复后保留该增量；本轮没有运行效率基准，不能由这些意见声称通用证明速度提升。实际请求、输入快照和完整工具返回保存在 [harness-addition-review/](harness-addition-review/)。
