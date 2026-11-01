# 33 边 Property B：启动上下文

项目根目录：`/Users/rfy_naiveai/Desktop/aris4math`。本目录是新题的准备材料；新研究仍使用本项目原有 research wiki 和 Lean 工程。

## 目标及阶段

- 原 T32 已完成：任意有限简单五元超图至多32边均具有 Property B，即 m(5)≥33。
- 新 T33 尚未解决：判断至多33边是否仍必然可二染色；优先证明 m(5)≥34，也允许以明确33边不可染反例确定 m(5)=33。
- 本轮授权为可行性讨论和撰写详细 Goal。启动文本为项目根目录 [GOAL_PROPERTYB_33.md](../../GOAL_PROPERTYB_33.md)；正式新规格为 [FORMAL_SPEC_PROPERTYB_33.md](FORMAL_SPEC_PROPERTYB_33.md)。用户启动后按Goal持续研究，不重复启动旧题。
- 准备已完成：Grok/Gemini各一轮独立讨论和一轮定向复核均有效返回，具体纠正已落实，当前无在途调用；这是计划审阅，不是新定理证明。
- 用户提供的编码理论Goal只作写法参考，工作不涉及其他项目。

## 按义务读取

| 需要恢复的内容 | 实际入口 |
| --- | --- |
| 新题对象、量词、完整验收 | [新规格](FORMAL_SPEC_PROPERTYB_33.md) |
| 新题首批障碍、精确诊断、Lean复用边界 | [DIAGNOSTIC.md](DIAGNOSTIC.md)、[diagnose.py](diagnose.py)、[实际输出](DIAGNOSTIC.json) |
| 19点的具体增量论证与20点剩余缺口 | [SUPPLEMENT_GLOBAL_PAIRS.md](SUPPLEMENT_GLOBAL_PAIRS.md)、[交叉复算脚本](supplement_global_pairs.py)、[实际输出](SUPPLEMENT_GLOBAL_PAIRS.json) |
| 22/23点旧选点延续、24点精确分界与空型重数 | [ROUTE_CHECK.md](ROUTE_CHECK.md)（独立纸面核对，未新增Lean证明） |
| 本轮Grok/Gemini咨询及建议处置 | [REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md)、本目录原始回复 |
| 已完成旧题的正式数学对象 | [原规格](../../FORMAL_SPEC.md) |
| 旧题完整阅读稿 | [PROOF_PACKAGE_FULL.md](../../PROOF_PACKAGE_FULL.md)、[HTML](../../PROOF_PACKAGE.html) |
| 概率覆盖、类型计数、实际扣除 | [概率引理](../../proofs/PROBABILITY_LEMMAS.md) |
| 19–23点结构 | [STRUCTURE_19_23.md](../../proofs/STRUCTURE_19_23.md) |
| 24–25点结构 | [STRUCTURE_24_25.md](../../proofs/STRUCTURE_24_25.md) |
| 旧Lean主定理、环境与实际核验 | [Main.lean](../../formal/Aris4Math/Main.lean)、[formal/README.md](../../formal/README.md)、[核验记录](../FORMAL_VERIFICATION_PROGRESS.md) |
| 现有资料与失败经验 | [query_pack](../../research-wiki/query_pack.md)、[文献更新及替代路线](../LITERATURE_UPDATE_20261006.md)、[历史漏洞](../HISTORICAL_PITFALL_AUDIT.md)、[PDF索引](../../ref/README.md) |
| 候选方向与已验旧结论 | [33边方向](../../research-wiki/ideas/propertyb-five-33-edge-threshold.md)、[旧主定理claim](../../research-wiki/claims/propertyb-m5-ge33.md) |

## 已经做过什么

`diagnose.py` 使用原算术引擎、精确Fraction计算。已经核对新预算下的19–25点纸面约化、23/24/25点六度顶点数保证，并复算19点无锁、21点三个单锁、23点一个双锁剖面的旧数值界。所有这些特定旧界均超过1；这只定位方法不足，没有产生不可染超图。

关键增量：26点排除要用整数度下界26·7>165；23点新增可能无六度点的情形；24点不能直接沿用原四锁选点保证。`Numeric.validProfile` 和 `TypeCounting.RealizesProfile` 隐含总重数32，不能直接向旧应用接口输入33边类型。

本轮未改变旧Lean源码，未构建新T33，未进行整图反例搜索。咨询记录的实际读/跑范围由审阅处置文件说明，不将计划认可当作定理认可。

补充诊断中，33边19点通过全局交集双计数得到有序单交边对数≤1002，精确总界228291/230945<1；已与独立显式位置公式交叉核算一致。这为19点分支提供纸面论证及算术证据，尚未迁入新Lean定理。20点同一办法仍给4599/4420>1。

## 启动后的第一批义务

1. 定义独立Target33，对齐原对象与量词；将新19–25点约化写入Lean，采用整数度数论证。
2. 针对真实33边超图建立必要的类型实现接口，避免沿用绑定32的validProfile。
3. 将19点的全局坏对计数与真实概率接口连接为首个新Lean分支，同时按精确差额研究20–25点的结构/概率突破；并行反例尝试承担攻击候选引理的职责。
4. 每个分支分别记录已覆盖输入、严格论证和剩余情形。最后把所有分支接到任意有限超图的新主定理，而不是只证明条件化接口。

后续研究产物使用本项目内独立的33边路径，追加维护现有wiki。旧规格、完成claim与原证明包保留；更新全局导航时同时标明旧题已完成、新题实际状态。
