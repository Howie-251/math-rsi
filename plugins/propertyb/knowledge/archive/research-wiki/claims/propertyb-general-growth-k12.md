---
type: claim
node_id: claim:propertyb-general-growth-k12
name: "全部k≥12的统一增长整数下界"
description: "同一RS全域最大预算与增长公式扩展至全部k≥12；Δ≥2，完整原超图结论已Lean核验。"
node_type: claim
status: verified
provenance: "context/propertyb-general/bridge-12-16-20261021/"
tags: ["property-b", "general-k", "analytic-proof", "integer-bound", "lean"]
date: 2026-10-21
added: 2026-10-21T09:06:20Z
---

# 全部k≥12的统一增长整数下界

**status:** `verified`

## Statement
对每个整数k≥12，置d=2^(k−1)、a_k(p)=1−(1−p)^k、J_k(p)=∫_0^p(1−y²)^(k−1)dy。B_RS(k)为所有满足存在p∈[0,1]使M(M−1)J_k(p)/d²<a_k(p)^(M/d)的正整数M之最大元；该最大元存在且2^k≤B_RS(k)<k2^k。令Δ(k)=floor(sqrt(B_RS(k))/(8(1+ln k)))，则Δ(k)≥2。任意有限顶点集上的简单k元超图，只要边数≤B_RS(k)+Δ(k)，就存在每条原边同时含两色的Bool染色。因此m(k)≥B_RS(k)+Δ(k)+1。

## Honest scope
全体原始有限简单k元超图，无点数、点对覆盖、度数、共度或线性附加前提。正式定义与旧rsBudget及integerGain完全相同；最大性覆盖全部正整数。主定理C的k≥12结论已端到端Lean，比较D同范围纸面、E仍k≥256纸面，二者未Lean。无最优起点、世界最强或领先渐近常数提高断言。旧35Lean／36研究暂停，无新Goal。

## Evidence chain
fresh PROOF_AUDIT.json覆盖全部7源单位／37义务，PASS_WITH_DECLARED_IMPORTS，same-family/provisional，进口及适用域已声明。formal/Aris4Math/General/Growth/Twelve.lean导出propertyB_of_general_growth_twelve、rsBudget_characterization_twelve、rsBudget_parameter_twelve、integerGain_two_twelve及非B下界；lake build Aris4Math.General.Growth.Twelve exit0（2576 jobs，15.64秒，含缓存依赖）。构建后formal/ReviewAuditGeneralGrowth12.lean以原积分、全部正整数最大预算、floor和原Bool结论独立复述，lake env lean ReviewAuditGeneralGrowth12.lean exit0（7.70秒）。六项核心导出及两个原题声明传递公理均仅propext、Classical.choice、Quot.sound；无sorryAx、新增公理或native_decide。实际证据lean/REPORT.md、VERIFICATION.json、BUILD.log、REVIEW_AUDIT.log；这是主执行者本机核验而非本导航代理重跑或第二台机器复现。首轮与最终新Grok均已有效end_turn（grok-4.7-build/xhigh）；最终全文静态读取Twelve、原题独立复述和日志，确认原始量词、全域最大预算、严格参数、Δ≥2及两区间衔接，认可且无实质问题，未执行Lean、未重审旧核心全部证明体。实际范围和GROK_FINAL_REVIEW.json见REVIEW_DISPOSITION.md。本次未调用Gemini，旧k≥17双模型终审保持历史。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

