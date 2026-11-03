# MathRSI meta-evolve：DD context 驱动的 v1→v2

## 本轮入口与执行顺序

2026-11-03，Root 开始实际使用已写成并集成的
[mathrsi-meta-evolve](../../../base/skills/mathrsi-meta-evolve/SKILL.md)。
此前工作是源材料阅读、原版 ARIS meta 补包和本技能开发；此前没有 DD 插件或五个解题技能的 DD 修改。
本次从技能第0节恢复维护范围，消费已成熟阅读，不继续把全库未读数量当成实施前置。

基点 main 提交：847490841644a78d83100a06ecc84e552974444f。
当前分支 feat/evidence-driven-evolution；meta 技能、参考、七份说明及发现别名已在工作树，尚未提交。
Root 自己执行本技能，Sol 承担具体作者和核对，不新增强制无历史全流程试跑。
用户授权本地开发、跨模型讨论和 DD 吸收；不恢复 DD／Property B／ECC 旧研究，不运行历史大搜索或 Lean。

源项目：/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff，只读。
既有 [源库存](intake/SOURCE_INVENTORY.json)、[数学原件提炼](intake/DD_MATHEMATICAL_EXTRACTION.md)、
[base输入](intake/EVOLUTION_INPUT_BASE.md)、[效率输入](intake/EVOLUTION_INPUT_EFFICIENCY.md)均为本次输入。
原件全文、部分阅读、结构解析、重复与未读状态分开记录，没有全库已读声明。
输入底稿中较早的“必须独立使用者试跑”建议已被用户后续指示覆盖，本轮不采用。

## 第1–2节消费：选择有证据的改动

### B1：固定 Lean 目标有直接入口

Root 已读现行 verify 的执行图、输入表及§2–4。它已支持按需 Lean，但图和“完整候选仍进入checker”的表述会把只要求固定形式目标的任务导向 TeX 审计。
接受小幅修订：显式 Lean-only 分支，保持自然语言正式审计原合同；
直接消费原声明、实际模块/导出、定义与公理证据后返回原 caller。
历史构建静态复用与本次新构建必须分开。不是删除原题要求的 proof-checker，也不把 Lean 当所有任务默认。

源证据：F4Graph3840 实际公式图出口、DD 原始审计以及 input B1。
归属 base：verify／research 的直接入口，必要时 assemble 的范围澄清；具体 Lean 数据／route 引理进入 DD 插件。
使用核查：本轮静态消费已有 Lean 入口选择正确路径，不重新编译旧数学工程；真实命令变化按涉及范围检查。

### B2：新基线必须改变正在执行的动作

v1 已有增量回文献与精确目标，不新增第六个解题流程。
接受把返回消费写具体：确定竞争目标时，来源变化要更新比较、候选队列与下一任务；固定数学任务不能被更强公开结果擅自替换。
DD 的 O22／P33、F7 被公开构造超过的经验进入插件，合法性与纪录价值分开。
归属 base：specify／prepare／survey／route-loop 的现有相关位置；尽量小改，已有规则正确则补实际例子。

### B3：对象改变后，分别判断正证据与负记录

接受在现有 prove／route-loop 的修法消费处明确：先写新旧对象关系；
满足原定理假设的正结论继承，只重核变化影响；旧否证依赖已解除时不能继续用其拒绝新候选。
修改过的对象若没有改变旧障碍，就不能换种子当新路线。
DD 冻结源邻域克隆、任意边界 matching 与旧 cross-only 失败为完整实例。
领域公式、具体图与旧预算不进入 base。

### B4：局部充分判据不能代替原共同目标

v1 已有共同对象和 actual caller，不另造一套义务系统。
接受一个具体操作例：局部每路满秩失败时，回到实际要求的同源路线像的并；必要门通过后仍交共同赋值及原对象覆盖义务。
不把某个失败 rank 测试自动解释为构造不可能，也不把新松弛通过解释为已构造。
归属 base 的现有路线诊断／prove 消费段；实质子空间公式、反例和 checker 进入 DD。

### P1：新增 DD 插件，保留原 wiki 和支撑原件

通过现有 PLUGIN_CONTRACT 接入五个阶段。插件提供实质定义、可调用定理、
构造/排除/迁移诊断、程序入口、失败地图和 Lean 源码地图；原交接包随仓只读保留。
整理层不缩成三份摘要，也不要求每次调用重读整个 archive。
原程序写源或依赖省略文件时，调用说明必须给工作副本／可用替代入口及准确范围。

### 不采用与暂缓

不采用每个任务至少五条事件、逐文件全文读完才实施、每次更新独立无历史完整重跑、
所有候选逐图全源 BFS／Lean／双模型终审、永久禁止有根据的续算、换一套 base 主干。
不主张 MathRSI v1 已经跑出 DD，不以本轮几个命令证明通用 RSI 提速。
DD 的实际参数、旧暂停状态与历史预算仅保留为源任务资料。

## 第3节实现分工

Root：本轮唯一协调者，主技能／来源适配、采用决定、README和版本集成的最终核查。
Sol-DD：plugins/degree-diameter，全知识库与源资料、领域技能和必要的薄适配。
Sol-formal：现有 verify／research／assemble 的 B1 及相应参考。
Sol-efficiency：现有 specify／prepare／survey／route-loop／prove 的 B2–B4；不改 ARIS 原字节。
各作者以新 meta 技能为执行合同，交实际修改、原件依据和本次核查范围，Root 及时回收。

## 当前使用与验证

- 新 meta 主技能 frontmatter 由 skill-creator 的 quick_validate 实际通过；
  PyYAML 仅准备在 /tmp/mathrsi-skill-validation-pyyaml，无全局安装。
- meta 集成现有 check_links：72份维护文档、1146本地目标，0缺失；
  git diff --check 通过。它们只支持接口／格式，不是数学证明。
- 原版 ARIS 增补214文件来源与9条离线调用的既有 smoke 复用；
  不为本轮重跑未变上游。
- Gemini、Grok 的 meta 成稿审阅均已有效完成，原回应与修法见下节。
  原件长读中断的三个调用没有有效终稿，不计认可。

## 第4节：成稿讨论已消费到实际修改

Gemini 会话 `4cdd57ea-c252-4dc9-ab12-5fcb21047a76`，实际选择
`gemini-4-argon-high/high`，SUCCESS；[原回应](reviews/GEMINI_META_DRAFT.md)及
[完整返回](reviews/GEMINI_META_DRAFT_RAW.json)保留。主体认可，提出三项具体衔接：
插件整理层与原件层、阶段挂载；证据到具体技能的caller；多作者整合及不套娃。
Root 已分别修 meta §3、evidence-and-transfer 链二至五、meta §5；
集成作者另把 DD 实际四入口接到契约、工作流图和双端发现。

Grok 会话 `053d676d-52df-41e8-8024-2a3e37c191cb`，实际
`grok-4.7-build/xhigh`，end_turn；[原回应](reviews/GROK_META_DRAFT.md)及
[完整返回](reviews/GROK_META_DRAFT_RAW.json)保留。指出原 research-review
Step4–5 与维护收束不一致，且复制提示缺 literal composed 参数。
Root 修 meta §4：只组合原件阅读与 Step3，明确不执行论文 Step4–5，
提示加 `— composed: <本轮 EVOLUTION.md>`。没有改 ARIS 原件或启动另一轮共识循环。
以上均为静态设计审阅，未认证 DD 全部数学；后续针对新插件的具体讨论另记。

## 第5节：Root 实际使用与成熟产物回收

Root 已依本技能分类 B1–B4/P1、委派现有技能的原位修改、逐项读取成熟 diff，
消费源条件和作者输出，并落实上述 reviewer 修法。这次维护本身就是新 meta 的使用，
没有在结尾再要求无历史代理重走整个项目。

- [B1实现及实际输入消费](implement/BASE_FORMAL.md)：verify/research/assemble
  已有直接形式目标分支，具体 F4 声明与既有审计供给真实输入。
- [B2–B4实现及六组决策](implement/BASE_EFFICIENCY.md)：五个既有技能原位新增九段。
  Root 接受基线改变竞争队列但不改固定题目、正证据继承／负证据重判、共同覆盖与必要门分流。
  六组输入是维护中的历史案例消费，不冒称重新调度旧研究。
- [跨文件静态消费核查](implement/CALL_CHAIN_REVIEW.md)：仅形式目标不被迫制作TeX；
  双要求仍进入正式自然语言审计；局部核验返回原prove，领域技能不新建同级调度。
  这是同家族静态检查，未重新运行Lean。
- [集成产物](implement/V2_INTEGRATION.md)：README双语、快速开始、契约、工作流地图与
  [v2说明](../../../docs/V2_CHANGES.md)已更新，DD四入口双端八个相对别名已可解析。
- DD 的完整提供源包已随插件保留，具体命令回收见
  [插件实现记录](../../../plugins/degree-diameter/evidence/IMPLEMENTATION.md)。
  当前实际新增运行包括364列整数dual重放、50项rebuild目录与3840图重建／字面格式及度数检查；
  未重新运行大图全根BFS、旧搜索或Lean，原数学状态保持。

Root 还让现有 `tools/check_links.py` 覆盖插件整理层 references/examples 与入口，
继续排除不可变历史原档。新公式代码段被误当链接的实际误报已用忽略 inline code 修复。
当前90份维护文档、1340目标、0缺失；后续扩写后用同入口最终读回。

## 集成审阅后的实际修正

Gemini [集成原回应](reviews/GEMINI_V2_INTEGRATION.md)指出了一个真实遗漏：
docs 的领域表已有 DD，但部分 SKILL 的派发仍只点名 Property B。
Root 将修法分给原文件 owner：prepare/survey/prove 加入明确的 DD 输入、共享检索与消费；
research/route-loop/verify 加入实际领域派发，保持唯一父调度和局部返回；
PLUGIN_CONTRACT 的 verify 明确 `dd-obstruction-certificate` 也核正构造。
不能把第一次子技能返回静态认可外推为完整派发已接通，
[调用链记录](implement/CALL_CHAIN_REVIEW.md)已补准确更正。

第二项修法统一从任务 cwd 执行：命令显式使用当前克隆的 `DD_PLUGIN`，
`--workspace`／`--output` 指任务目录。Root 已实际运行
[任务cwd重放](implement/TASK_CWD_REPLAY.json)，364列整数dual exit0；
作者的[两项工作区调用](../../../plugins/degree-diameter/evidence/WORKSPACE_COMMAND_CHECK.json)
同时覆盖50项case列表。没有为修cwd重复生成大图。
四个 DD 技能另补真实输入、执行、读回、失败去向与产物示例。

Gemini 原会话的[定点复核](reviews/GEMINI_DISPATCH_FIX.md)已有效 SUCCESS，
确认三项问题解决；只读修订路径及回执，没有执行数学程序。
因此当前“已接入”同时依据实际SKILL、父消费者和相应命令，非仅文档表格。

Grok [DD数学提炼审阅](reviews/GROK_DD_MATH.md)有效 end_turn，静态核原件与薄工具，
未执行命令／BFS／Lean。Root 全文读回 GLOBAL_COSET4_NOTE 和 DIAGONAL_FILL_GENERAL 原件：
采纳补齐实际15552 reference选取、3648/33216对覆盖及只删除相同完整global label的
virtual stay规则；一般affine-coset代数仍保留一般参考中心，不将本实例的≤2 word选择
误写成一般代数引理必需条件。另把“邻域不交，给出非D2见证”的连写歧义改成
hub与clone不相邻、无共同邻点、结合覆盖距恰3，并写明k≥1及前缀路线条件。
这些是引用原证明补齐陈述与调用，不是新数学研究或新版重证。

## 第6节：本地采用与交接

Root 采用 B1–B4、P1 和独立外层 meta 技能，作为本地 v2 的增量实现。
保留原五子工作流、Property B、ARIS双端资源及其有效既有验证；ECC仍为原草案，
未恢复任何旧研究。原版 meta-optimize/meta-apply 两端完整保留，数学适配的具体差异可读。
此次新 Python 仅一份整数dual薄适配，既有链接工具增加插件整理层与inline-code处理。

可直接使用：[v2说明](../../../docs/V2_CHANGES.md)、
[meta技能](../../../base/skills/mathrsi-meta-evolve/SKILL.md)、
[DD插件](../../../plugins/degree-diameter/README.md)。
最终接口结果在[FINAL_INTERFACE_CHECKS](implement/FINAL_INTERFACE_CHECKS.json)，
具体图／证书运行在插件evidence。模型认可、接口核查与原研究证明分别保留范围；
没有新长题、通用效率或递归改进评测。无须把全库未读材料或新独立全流程试跑加作本轮前置。

本轮在 `feat/evidence-driven-evolution` 本地保存；不推送、PR或合并。
后续新题使用v2，或新的维护按本技能从此记录的实际采用状态开始，不重做本次取证。
