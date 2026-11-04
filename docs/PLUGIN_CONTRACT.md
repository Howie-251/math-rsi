# Base 与领域插件怎样合作

插件把数学知识带进研究，不接管原目标或核心维护。Base 组织人和工具，不凭字段齐全判定证明。第一版用 agent 可读的 Markdown 约定合作，以下概念可以写进已有文档，不要求五份表或一个统一 JSON 文件。

## 在子工作流的具体位置接入

[主工作流](../base/skills/mathrsi-research/SKILL.md)调用五项子工作流，领域能力在当前阶段接入。传给插件的是原规格、当前义务、实际输入、已证与待证条件、要返回的产物及写入归属。插件处理相关范围后回当前调用处，不再从头运行整条研究流程。

后继阶段只由持有当前义务的调用方启动一次。插件给下一动作及证据，不能先替父流程调用prove/verify，父流程又再启动一遍。内部所需文献/程序/独核继续执行，完成后逐层返回。

| 调用方 | Property B实际入口 | 输入与返回用途 |
|---|---|---|
| prepare/survey | [propertyb-literature](../plugins/propertyb/skills/propertyb-literature/SKILL.md) | 当前k/预算/待核公式、旧查询→准确基线/原文条件/反例；合入同一文献报告 |
| route-loop | [propertyb-bound-lab](../plugins/propertyb/skills/propertyb-bound-lab/SKILL.md) 的方法诊断 | 活跃失败型、旧预算、共同对象→结构入口或有信息的探针；用于选择路线 |
| prove | 同一bound-lab的具体义务执行 | 已选路线、准确参数与进口→选锁/真实迹/共同坏对证明或实际证书；回接原caller |
| verify | [propertyb-certificate](../plugins/propertyb/skills/propertyb-certificate/SKILL.md) | 当前正文、真实输入、域与证书→覆盖/算术/输入连接证据；交verify装配原结论 |
| handoff | 已有领域正文与核验记录 | 只提供领域复现命令、条件与关键源码；展示/交接由handoff组织 |

DD使用相同合同，四个实际技能及返回点如下：

| 调用方 | Degree–diameter实际入口 | 输入与返回用途 |
|---|---|---|
| prepare/survey | [mathrsi-degree-diameter](../plugins/degree-diameter/skills/mathrsi-degree-diameter/SKILL.md)＋[dd-transfer-diagnosis](../plugins/degree-diameter/skills/dd-transfer-diagnosis/SKILL.md) | 原图目标、公开来源、已查baseline→准确对象/进口/比较，竞争任务据此更新队列；共享一次调查 |
| route-loop | transfer＋[dd-construction](../plugins/degree-diameter/skills/dd-construction/SKILL.md) | 失败输入、实际共同对象→新规则、保留条件与首项探针 |
| prove | construction或[dd-obstruction-certificate](../plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md) | 真实source/参数/允许操作→图定义、degree与全点对caller，或准确条件性排除 |
| verify | [dd-obstruction-certificate](../plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md) | 实际图、正文/model、有限域与证书→精确有限命题及原图连接；§4–5也核正构造的字面属性、覆盖、证据继承和固定Lean导出，不递归完整verify |
| handoff | 已核证明与程序状态 | 领域复现命令/源码/缺件范围回交base；历史wiki只读，新题结果写工作区 |

通用survey和领域literature共享同一次检索任务，按术语、来源或深读对象分工，不能分别重复全轮。通用verify持有完整证明验收；certificate在其中执行领域核验时，只回交该scope证据，不递归启动另一个最终verify/proof-checker循环。独立调用领域技能仍可按它自己的完整合同工作，但嵌入调用必须把当前阶段和返回点明确传入。

路线/证明中的新文献疑问交survey增量处理，survey可再调用领域literature，随后结果回原义务。文献发现一般条件只在prove证明实际输入满足后才能使用。局部certificate或Lean已核则回当前证明，不自动跳到最终handoff。共同写入由父调用者指定一个owner，其他worker交新增正文和证据位置；没有统一强制JSON或额外Python接口。

六个领域的当前入口与逐阶段动作统一维护在[DOMAIN_ROUTING](DOMAIN_ROUTING.md)。各实际SKILL在发生领域调用处读取该资源并执行对应部分；它明确新ECC与三个领域的输入、原程序/数学能力、返回及消费，不只列插件名称。旧Property B/DD接口继续有效。

## 任务与义务

任务来自用户与正式规格。插件先解释本领域对象，列出已有定理与合法操作，再帮助 Root 判断有哪些证明路线。领域惯用的正则、线性、满支撑、自同构等附加条件，必须有无损归约才可用于原题全域；否则只是搜索子族。

义务描述一项精确待证明结论及其依赖。一次归约说明它是等价关系、每个原对象都进入的必要域、足以产生目标的构造，还是便于寻找见证的局部搜索。相同的程序输出因这个方向不同，会支持完全不同的结论。

对一条路线，若多个子结论必须同时成立，保存共同对象、相容选择和需要全部完成的连接。不同路线能任选其一时，说明它们是替代关系；某条完整路线已经证明原题后，无需继续填完被放弃路线的节点。
不同子族的分情况需要合起来覆盖原域，不是可任选其一的替代路线；局部成果只关闭其实际覆盖的子族。

## 行动与结果

插件建议一个具体行动：为什么此时值得做、实际输入是什么、希望新增哪条事实、如何影响当前瓶颈。方法可以是推导、文献查询、约束求解、程序生成、验算、反例搜索或 Lean；base 不规定统一数值优化器。

规模估计需要看联合域。代表数量变少但各代表的后续扩张指数增大，可能没有提速。先做短探针，再依据真实耗时、内存、证据量和需要的覆盖决定是否扩算；不把所有任务都变成资源报表。

结果要返回精确结论、条件、范围、支撑位置和未解决部分。一个反例对候选引理可能决定性有用，即使没解决主定理；一个已核对的条件引理也可以长期复用。进度用它改变了什么解释，不以文件数或“分支百分比”替代。

## 验证能力

验证接入的单位是一个证明义务。例如 ECC 的显式矩阵验距、完整陪集集合、全配对拒绝与模型无损编码，是四种不同问题。检查器接入说明：读取什么实际数据；检查什么属性；输出怎样解释；成功后还缺哪条数学连接。

调用方式先复用任务里的现成程序和命令，无需包成统一 Python 类。需要工程适配时，接口只承担输入输出转换和明确的执行职责；不要在适配层偷偷收窄对象域，或把超时／UNKNOWN 转成不存在。

最短可读例子：

```text
能力：显式二元生成矩阵完整验距。
输入：规格中的 n、k、目标距离，以及候选矩阵和位序。
检查：形状、二元元素、GF(2) 秩、所有非零消息的码字重量。
输出：实际最小距离及低权消息／码字；保存真实执行结果。
能支持：这个矩阵是否为目标构造。
不能支持：不存在其它满足条件的矩阵。
```

这不是全领域统一“verifier passed”状态。原题结论由 Root 把不同义务的证据正确连接；模型审阅、程序检查和 Lean 都按实际作用使用。

## 范围与可组合性

领域插件可以调用现有工具、更新本题知识、提出新的引理与策略；它不在解题中直接修改 base 或验收定义。插件提出通用流程改进时，应附实际问题与建议的可观察行为，交 [mathrsi-meta-evolve](../base/skills/mathrsi-meta-evolve/SKILL.md) 消费。维护owner负责实际补丁、针对性讨论、实际使用及修订／拒绝／接纳决定；默认可由协调者自己使用，子代理协助具体工作，不强制另换无历史执行者。领域数学内容仍先保存完整条件与原证据。

多个插件可在同一任务中组合，但共同符号、对象与归约方向需要对齐。例如把编码构造转为组合对象，必须保留原参数和性质的数学连接，不能因为两个检查器各自通过就宣布转换正确。

目录分层本身不是操作系统权限机制。实际文件写入范围、命令授权、模型选择和总预算继续服从用户与宿主约束。

## 插件的实质内容和验收

一个可用插件至少让 agent 找到：本领域的任务表达方法、适用的数学策略与条件、已有知识和程序的位置、几个真正有用的失败诊断、结果怎样回到原题。领域技能是入口，长案例或来源地图按需链接，避免每次启动灌入全部历史。

Property B已有完整领域知识库和四个技能；DD新增四项技能、整理层与原wiki/支撑原件，具体本轮使用范围见[v2变化](V2_CHANGES.md)；ECC已在原插件升级证据与专门核验能力，另有极值超立方体、Hamilton超立方体与Happy Ending三个领域入口；具体可运行范围见[v3变化](V3_CHANGES.md)。原始资料必须在仓内可找到；入口下需有足以实际调用的定理/公式/证明、失败输入、适用范围与重试条件，不能只有一个source路径表。验收围绕真实任务片段检查命令、输入域和原题连接，协调者可以直接按技能执行；有具体疑问或原题合同要求时再安排相应独立核对。格式通过不是内容验收，也不要求为插件更新重跑整道旧题。

领域入口： [Degree–diameter](../plugins/degree-diameter/skills/mathrsi-degree-diameter/SKILL.md)、[Property B](../plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)、[ECC](../plugins/ecc/skills/mathrsi-ecc/SKILL.md)。没有合适插件时，可以直接通过 base 开展研究，在出现真实可复用经验后再提炼插件。
