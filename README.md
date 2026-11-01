# MathRSI

**以 ARIS 完整技能和领域知识组织数学研究。** 从文献查漏到严密证明，把发现、推导、计算、审阅、形式化与可复现交接接成实际工作流。

主流程按现有成果选择入口，并衔接五组可独立使用的子流程：**问题准备与文献 → 求解路线迭代 → 证明推进 → 装配验证 → 交付沉淀。** 每组实际执行、交付结果，由调用者读取后继续；新障碍带着具体问题回文献或路线，未变的成果直接复用。已有完整证明可直接进入验证，短证明可以直接完成，不必跑满五组。

本仓以详细 Markdown 为主，直接携带30项ARIS技能的Claude/Codex双端完整实现、共享资源、模板与helpers。MathRSI自己新增的代码只做明确的开发核查；数学研究由agent判断与执行，不另造调度平台或通用证明判分器。

## 从这里开始

- [数学研究总控](base/skills/mathrsi-research/SKILL.md)：选择起点，执行并消费子流程产物，保持原目标与已有证据的连接。
- [完整工作流与调用序列](docs/WORKFLOWS.md)：五组子流程的输入、真实动作、阶段产物、回流图及恢复例子。
- [ARIS实际调用说明](docs/ARIS_REUSE.md)：30技能双端位置、各阶段输入输出、helper命令与外部运行依赖。
- [Property B领域主技能](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)：结合完整知识库选择研究路线。
- [Property B知识库](plugins/propertyb/knowledge/README.md)：完整引理/证明/失败经验、原始wiki与源码，不依赖作者另一份工作目录。
- [工作区与恢复](docs/WORKSPACE.md)：已有项目沿用原规格和wiki，不初始化覆盖。

### 五组数学子流程

|子流程|实际动作与交接|
|---|---|
|[mathrsi-prepare](base/skills/mathrsi-prepare/SKILL.md)|先用[specify](base/skills/mathrsi-specify/SKILL.md)恢复或澄清初步问题，再由[survey](base/skills/mathrsi-survey/SKILL.md)实际广搜、深读关键进口和更新wiki，最后定稿原题；交正式规格与文献依据|
|[mathrsi-route-loop](base/skills/mathrsi-route-loop/SKILL.md)|提出具体方法，执行数学路线审阅与有区分力的推导／探针，处理结果并有界复核；交可立即执行的路线及首批任务|
|[mathrsi-prove](base/skills/mathrsi-prove/SKILL.md)|组合推导、证明写作、领域方法和独占worker，立即回收并接实际caller；交候选证明、见证或准确未闭义务|
|[mathrsi-verify](base/skills/mathrsi-verify/SKILL.md)|需要时由[assemble](base/skills/mathrsi-assemble/SKILL.md)装配，再执行适用的独核、ARIS proof-checker修复流程与按需Lean；交准确范围的验证及下一步|
|[mathrsi-handoff](base/skills/mathrsi-handoff/SKILL.md)|整理完整可读正文、实际复现材料、按需HTML／包、wiki与恢复入口；部分交接保留主目标开放状态|

这八项MathRSI技能加一个总控，使用本仓ARIS作为内部动作并做数学输入、目标和执行顺序适配。路线审阅没有定理真值评分门；局部核验返回其原证明义务，完整验证才进入最终交付。具体动作及范围以实际入口为准。

实际回流也由这些入口执行：[route-loop](base/skills/mathrsi-route-loop/SKILL.md)或[prove](base/skills/mathrsi-prove/SKILL.md)将准确新文献问题交给[survey](base/skills/mathrsi-survey/SKILL.md)，得到原文条件后回同一义务；[verify](base/skills/mathrsi-verify/SKILL.md)的局部结果返回原prove，实质缺口交prove修，核心方法失效才回route-loop。完整候选可直接verify，已核结果再交handoff。

### Property B的专用技能

|技能|承担的实际工作|
|---|---|
|[propertyb-literature](plugins/propertyb/skills/propertyb-literature/SKILL.md)|异名广搜、前后引用链、历史错误、原文定理条件与基线比较|
|[propertyb-bound-lab](plugins/propertyb/skills/propertyb-bound-lab/SKILL.md)|新预算完整域、选锁与真实迹、共同坏对、signed修复、一般k推导及失败回流|
|[propertyb-certificate](plugins/propertyb/skills/propertyb-certificate/SKILL.md)|实际输入连接、分类覆盖、精确算术、独立重放、审阅修正与原染色装配|
|[mathrsi-propertyb](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)|统筹这些能力，选择当前瓶颈对应的工具与交付路线|

ECC保留[首版草案](plugins/ecc/skills/mathrsi-ecc/SKILL.md)，等待用户安排另一位领域agent重做；它未按本次Property B标准验收，未加入项目默认技能发现。已授权的ECC原交接只读快照见[经验来源](development/context/ecc-source/README.md)；没有写入或恢复ECC原研究。

工作流的具体衔接提炼自[Property B与ECC的六条历史转折](development/workflow-redesign/REAL_PROJECT_TRANSITIONS.md)，包括局部核验返回原义务、完整覆盖与拒绝证据分工，以及较弱必要条件已足够时及时收束。本轮开发读取和整理这些经验，未重新解题或重放全部生产证据，也未据此宣称通用提速已经验证。

## 可直接使用

```text
读取 /实际路径/MathRSI/base/skills/mathrsi-research/SKILL.md，
再读 /实际路径/MathRSI/plugins/propertyb/skills/mathrsi-propertyb/SKILL.md。
在 /我的任务目录 中研究 <准确问题>，先恢复现有规格、wiki与状态。
按已有成果选择prepare、route-loop、prove、verify或handoff，
执行后读取实际产物，在同一轮内继续已授权的下一步。
所有helper显式来自 /实际路径/MathRSI/base/tools；不回退外部ARIS仓库。
```

`.agents/skills/` 和 `.claude/skills/` 提供仓库内**相对**发现别名；实际内容就在base和plugins里，复制整个MathRSI后仍有效。当前会话未刷新发现时直接读SKILL路径即可。没有全局安装、没有改写用户私有reviewer配置。Lean、TeX、模型MCP、网络服务及其凭据按实际任务环境提供；源码自包含不等于这些外部服务自动就绪。

已发现技能时，Claude可用 `/mathrsi-research` 或相应子技能；Codex可用 `$mathrsi-research` 或直接要求读真实路径。不要把slash写法当成所有宿主通用命令，也不要给子技能编造未支持的flag。[调用序列](docs/WORKFLOWS.md)给出从新题、已有证明和局部义务进入的完整例子。

## 三层边界

|层次|内容|
|---|---|
|base|通用数学研究主流程，完整ARIS能力、验证与交接契约|
|plugins|领域定理、证明方法、失败反例、计算/Lean经验及可运行案例|
|任务工作区|当前问题的规格、新证明、wiki、运行证据、预算和恢复状态|

[插件契约](docs/PLUGIN_CONTRACT.md)用自然语言说明输入、义务、行动、结果与核验，不强制统一JSON。运行插件不改base或验收条件；新领域知识在独立维护步骤纳入。历史源资料是只读快照，不恢复35 Lean、36研究或任何旧Goal。

## 验证与开发

[本轮验证记录](development/VALIDATION.md)分别报告技能资源完整性、搬迁副本执行、真实数学案例和模型审阅范围。它们不等于通用解题成功率或RSI增益评测。

```bash
python3 tools/check_links.py
python3 -B base/tests/smoke_bundle.py --help
```

链接检查覆盖维护中的主流程/插件文档和内部别名；原始历史档案里的旧HTML/日志链接另有归档说明。base的独立smoke实际验证被复制的上游资源和wiki/router/renderer。本地开发使用短期分支，尚未创建远端或推送。

## 来源

[ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 固定来源、许可证与领域提炼说明见 [PROVENANCE](docs/PROVENANCE.md)。ARIS与MathRSI工作流沿用MIT；归档学术论文与第三方原件保留各自权利，不能将仓库MIT标题理解为重新许可这些作品。
