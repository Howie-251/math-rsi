---
type: claim
node_id: claim:propertyb-general-growing-integer-gain
name: "一般k的统一增长整数下界"
description: "全部k≥17，相对明确RS最大预算的统一增长整数增益；完整原命题Lean及指定终审已闭合。"
node_type: claim
status: verified
provenance: "context/propertyb-general-lean-growth/"
tags: ["property-b", "general-k", "analytic-proof", "integer-bound", "lean"]
date: 2026-10-21
added: 2026-10-21T07:05:46Z
---

# 一般k的统一增长整数下界

**status:** `verified`

## Statement
对每个整数 k≥17，记 d=2^(k−1)、a_k(p)=1−(1−p)^k、J_k(p)=∫_0^p(1−y²)^(k−1)dy，令 B_RS(k)=max{M∈Z_≥1 : 存在p∈[0,1]使 M(M−1)J_k(p)/d² < a_k(p)^(M/d)}。该最大值存在且2^k≤B_RS(k)<k2^k。置Δ(k)=floor(sqrt(B_RS(k))/(8(1+log k)))，log为自然对数。任意有限集合V及简单k元边族E，只要|E|≤B_RS(k)+Δ(k)，即有二染色使每条边含两色，故m(k)≥B_RS(k)+Δ(k)+1。规范完整证明：proofs/propertyb-general/CORE_THEOREM.md、UNIFORM_INTEGER_GAIN.md、CLIQUE_REFINEMENT.md。

## Honest scope
原始全超图量词，无点数、度、共度或线性附加条件。全部整数k≥17的主定理C现有完整解析证明与端到端Lean，最大预算的全域最大性、正参数和整数增益≥1均由内部证明。指定Main构建、独立原题复述及传递公理审计通过；不是整图枚举。比较定理D/E仍为独立纸面证明。本条不宣称领先渐近常数提高、世界最优或第二台机器复现；模型意见不替代实际证明。旧35/36状态不变。

## Evidence chain
2026-10-21新增完整Lean：formal/Aris4Math/General/Growth/Main.lean；执行lake build Aris4Math.General.Growth.Main和lake env lean ReviewAuditGeneralGrowth.lean均exit0，最大值定义及全域最大性、原Finite/Finset/Bool结论显式展开。七项传递公理均仅propext、Classical.choice、Quot.sound，无sorryAx、新增公理或native_decide。实际证据context/propertyb-general-lean-growth/{VERIFICATION.json,build-main01.log,final-audit01.log}。fresh语义审阅SEMANTIC_AUDIT.md为NO_SUBSTANTIVE_ISSUES_FOUND（same-family/provisional，未跑Lean）。结构Grok/Gemini均有效完成；完整C的Gemini4Argon/high已SUCCESS静态审阅新增14模块/原题/日志，无实质问题，未运行Lean。Grok完整C终审也已有效end_turn（grok-4.7-build/xhigh），全文核新增14模块与原题/日志，无实质问题，未执行Lean。两份完整C终审原回应与处置在context/propertyb-general-lean-growth/reviews/final/DISPOSITION.md。正文规范、原有纸面审计和比较范围均保持。

以下为此前纸面成果的原始证据链；其中532公式及Goal完成是当时交付快照，不覆盖后续展示或形式化状态。

fresh proof-checker：18/18源单位、78项义务，PROOF_AUDIT.json=PASS；Grok grok-4.7-build/xhigh end_turn与Gemini CLI gemini-4-argon-high/high SUCCESS均静态阅读全文，认可A/B/C。主代理处置context/propertyb-general/round02/reviews/CORE_DISPOSITION.md；仅改清J下界来源的一句，公式不变，审计已定向复核。原回应GROK_RAW.json/GEMINI_RAW.json保存；ARIS traces研究审阅007/008记录实际范围。数学成立来自正文而非模型投票。

完整比较终审已完成：正式BASELINE_ADDENDUM及COMBINED_AUDIT均PASS（same-family/provisional），确认k≥32的明确五项L_ref=B_RS+1、k≥256对每个M>B_RS的指定零锁必要数据松弛不通过。Grok与Gemini4的有效静态终审及最终拼接处置见context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md。Gemini为SUCCESS；Grok为同次调用原生turn_ended outcome=completed，grok-4.7-build/xhigh，原MCP envelope及stopReason缺失，保持缺失，不改填end_turn。两家未执行计算。主命题及verified状态保持原准确范围；比较不是实际H可实现性或全部潜在Grill法能力定理。最终展示及Goal交付验收已由root完成，Goal工具已实际返回status=complete（2026-10-21）。最终验收context/propertyb-general/round02/COMPLETION_AUDIT.md；最终HTML532公式离线PASS，人工交接已完成。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

