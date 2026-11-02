---
type: idea
node_id: idea:ddp-breadth-20261027
title: "构造方法快速比较与有依据切换"
stage: active
outcome: pending
added: 2026-10-27T02:11:40Z
based_on: ["paper:ddp-record-sources-20261026"]
target_gaps: ["gap:DDP1", "gap:DDP2"]
tags: ["ddp", "construction", "breadth"]
---

# 构造方法快速比较与有依据切换

**stage:** `active`  ·  **outcome:** `pending`

## Thesis
用户已恢复Goal并要求扩大构造方法探索。本轮已完成7个有限构造试验，全部最好图均由保存边表独立全源BFS检查；已验证新下界仍为0。各失败入口已收束，没有自动追加seed或邻域。 这些试验包含一般图搜索、矩阵群Cayley、陪集轨道、Schreier置换作用、非一一匹配仿射线提升及电压图变体；类别之间有关联，不声称每一行都是完全独立的新方法。有限试验失败不排除整个图族。

## Key risks
按用户2026-10-27最新指导，策略改为优先比较更多有实质区别的构造，用subagent并行推导、实现和检验；同一构造投入过久且没有新的覆盖结构时及时跳出。

每个入口先交代点数公式、度数预算和实际覆盖步骤，运行一个有明确范围的有限试验。试验未达目标，反馈若仍只是固定源坏点对下降，就把该入口收束并换结构；不能因为预算尚有余额就补满时间、追加seed、扩大坐标邻域或把整个失败族排除完才离开。继续同一方法必须提出改变实际覆盖瓶颈的具体理由。

先用便宜的必要覆盖条件筛掉不可能入口，再快速生成完整候选。发现阻断条件立即进入下一候选；条件通过不代表构造成立。允许一次有数学依据的结构跟进，如改变邻接重数或内部边，但新条件仍失败就保存原因及时离开。

同时通常保留两条主要计算线路，并用第三个subagent做轻量侦察；全部任务合计不超过8个CPU worker。以不同构造和表示比较为主，换群、换点数、换起点如实记作方法的变体，不用来虚增独立方法数。

每个已保存候选分别只作一次独立最终全源BFS，后续复用记录。Gemini用于承重推断与方向互审；回执成功不是数学通过。真实新下界仍须最新公开基线核对、完整独立验证及规定审阅，Lean后置。


<!-- REFRESH_20261029_PRECEDENCE -->
## 2026-10-29策略适用说明

以下2026-10-26/27“当前0新图／27格／快速比较”是历史阶段记录，不是现在的结果或自动派发队列。当前继承103例／3参数、Lean0，开放表范围与[新版策略](ddp-open-parameter-construction-20261026.md)适用。反例只攻击具体承重保证；有实际问题可深入，不强迫机械短试／快速换题。旧实验和暂停D2边界保留，不重跑历史。

<!-- TWO_SUCCESSFUL_METHODS_RESUME_20261101 -->
## 2026-11-01 人工恢复后的当前适用方式

本次沿用同一Goal与唯一Wiki，已将新交接并入[扩张主线A](ddp-open-parameter-construction-20261026.md)和[仿射主线B](ddp-q3-three-step-plane-pencil31.md)。当前不是恢复上方历史的模板大筛、旧队列或机械短试；从两种已成功机制的具体覆盖条件提出预测并实际推广，默认最多两条深入数学线。旧D2/n61保持暂停。

现有合法成果104例/4参数，confirmed主表改善103例/3参数，具体公式Lean1、3750全球最新纪录未确认。上方旧0成果/Lean0为历史状态。379条方法账本记录混含实验、变体、源接口和工具，不是379种独立方法；本次只同步策略及现有证据，不新增ledger记录或成果计数。

严格排除保留原范围；UNKNOWN不改成无解，也不自动追加旧timer。允许同一机制在有具体问题和反馈时持续研究，报告按约每小时更新而不强迫换题；工程只作有限可解释pilot。

<!-- D13_CURRENT_PUBLIC_BASELINE_20261101 -->
## 2026-11-01 13度D5当前公开比较更正 保留原主表与验收历史

[原40图家族](../experiments/ddp-d13-singlefault-star-family-51457-20261027.md)的51418..51457均仍为合法D5构造，savedL与旧public_baseline=51417、原验收及超过保存主表的40例计数均保留。当前primary作者仓库已公开[(13,5)88452点图](https://github.com/rmizuno42/ddp/tree/main/results/degree13-diameter5/)，故这40例已确定不破当前公开下界，不能继续称全球纪录。

[本次只读primary选读](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/MIZUNO13_PRIMARY_READOUT.md)与实际Contents API保存显示：current README的Oct23栏目列13D5=88452；独立13度package于Oct13加入。作者现成普通全88452根queue BFS报告574938边、min=maxdegree13、exactD5，本机不重跑。它与旧14度88452虽同点数/controller，但affine charts及M/P matching不同，不是改标。本记录以current_public_lower_bound=88452单列，不覆盖历史savedL51417，也不宣称88452为全球最优。

当前110合法例/7参数、超过保存主表103例/3参数、完整具体公式Lean1不变。已知被更大公开构造超过的集合为41例：这40例与F7的20580一例；它与103个保存主表改善有40例重叠。保存主表外pending仍6例/3参数（20/21/22各两），不能用旧nonrecord1字段代表全项目非纪录；该兼容字段只含保存主表外分类。其余旧11/12家族的全球状态未由本次认证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

