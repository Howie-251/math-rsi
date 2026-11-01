---
type: idea
node_id: idea:propertyb-restricted-k-general-bound
title: "限制k范围、覆盖全部超图的一般下界"
stage: active
outcome: positive
added: 2026-10-21T04:38:28Z
based_on: ["paper:cherkashin2015_note_random_greedy", "paper:grill2024_improved_lower_bounds", "paper:radhakrishnan2000_improved_bounds_algorithms"]
target_gaps: ["gap:G8"]
tags: ["property-b", "general-k", "shared-incidence", "analytic-bound"]
---

# 限制k范围、覆盖全部超图的一般下界

**stage:** `active`  ·  **outcome:** `positive`

已完成交付，Goal工具status=complete；全k≥17增长整数增益已verified，完整比较尾k≥256。

## Thesis
后续Lean试点已由用户启动（2026-10-21，Goal工具active）：一般RS真实概率核心＋任意有限简单17元、≤2^17边的完整caller。局部概率／计数／积分／残留平均和数值模块已编译、独立导入；单交对精确概率与整体装配仍在实施，完整阶段尚未验收。恢复context/propertyb-general-lean-pilot/PROGRESS.md，局部证据见exp:propertyb-general-lean-pilot-core-modules-20261021。本idea既有一般纸面成果保持完成；准备期“尚未启动”的旧导航由本条替代，不表示完整一般定理已Lean验证。

2026-10-21：数学、指定终审、离线HTML和人工交接均已完成交付；Goal工具已实际返回status=complete。最终验收入口为context/propertyb-general/round02/COMPLETION_AUDIT.md；最终HTML含532条内嵌公式，离线桌面／手机检查PASS，已用Microsoft Edge打开。旧36与35Lean暂停、v2隔离保持原状。

对全部整数k≥17及全部有限简单k元超图，已证明m(k)≥B_RS(k)+1+floor(sqrt(B_RS(k))/(8(1+log k)))；B_RS是明确RS–FKG–精确积分的最大整数可染预算。实际H接口与78项核心义务通过正式审计；核心与比较的Grok/Gemini有效终审均已完成，见context/propertyb-general/round02/formal-audit/COMBINED_AUDIT.md及round02/reviews/CORE_DISPOSITION.md、BASELINE_DISPOSITION.md。五项明确L_ref在k≥32等于B_RS+1；完整比较尾K={k≥256}另含指定零锁必要数据松弛，不能扩大为全部潜在Grill法或实际H witness。已登记claim:propertyb-general-growing-integer-gain，verified为纸面证明，无新Lean。恢复context/propertyb-general/PROGRESS.md；离线阅读PROPERTY_B_GENERAL_BOUND.html；人工交接HANDOFF_PROPERTYB_GENERAL.md。

已复用的方法链是：保留同一实际超图与共同坏对对象，经最小顶点商约化接到真实单交图；以公共点／无公共点的经典线性交族团界削减γ，再把同一个严格RS参数见证转为统一增长的整数预算。这是覆盖全部原始对象域的解析证明，不是样例归纳。

### 较早状态（历史）
原stage=active、outcome=pending，建立时间2026-10-21T03:45:08Z。原描述：一般Goal active；全k≥17增长整数增益已有完整候选，正式审计与强基线比较在途。

原始目标覆盖每个适用k的全部有限简单超图。当前完整候选：k≥17，m(k)≥B_RS(k)+1+floor(sqrt(B_RS(k))/(8(1+log k)))；B_RS为RS-FKG-exact最大整数可染预算，已证非空有限。最小顶点商、实际重染事件、公共点二分单交团、Caro–Wei/Cauchy及统一整数余量均有完整稿，见proofs/propertyb-general/CORE_THEOREM.md、UNIFORM_INTEGER_GAIN.md、CLIQUE_REFINEMENT.md。主代理/Sol已核，fresh proof-checker和跨模型终稿在途；强基线在k≥256尾范围另核。恢复context/propertyb-general/PROGRESS.md。

## Key risks
数学研究与规定审阅已闭合；最终展示／交付已完成，Goal工具已实际返回status=complete。比较仅限明确定义的五项参考包络及指定零锁松弛，不宣称世界最优、提高渐近领先常数或穷尽未来方法。旧36与35Lean继续暂停，不碰v2。

较早风险快照（历史）：尚未最终验收。必要度数松弛不是实际H；相对指定RS的改进不得直接写成所有文献都已比较完毕。旧36与35Lean暂停，不碰v2。

完成归档说明：当前idea所用stage枚举不支持completed，保留既有合法stage=active、outcome=positive；完成事实以上方正文和Goal工具complete为准，不据该字段重启研究。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

