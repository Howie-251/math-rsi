---
type: claim
node_id: claim:propertyb-general-growing-integer-gain
name: "一般k的统一增长整数下界"
description: "对全部k≥17，相对明确RS–FKG–精确积分预算B_RS，得到floor(sqrt(B_RS)/(8(1+log k)))的统一整数增益。"
node_type: claim
status: verified
provenance: "context/propertyb-general/round02/formal-audit/"
tags: ["property-b", "general-k", "analytic-proof", "integer-bound"]
date: 2026-10-21
added: 2026-10-21T04:21:09Z
---

# 一般k的统一增长整数下界

**status:** `verified`

## Statement
对每个整数 k≥17，记 d=2^(k−1)、a_k(p)=1−(1−p)^k、J_k(p)=∫_0^p(1−y²)^(k−1)dy，令 B_RS(k)=max{M∈Z_≥1 : 存在p∈[0,1]使 M(M−1)J_k(p)/d² < a_k(p)^(M/d)}。该最大值存在且2^k≤B_RS(k)<k2^k。置Δ(k)=floor(sqrt(B_RS(k))/(8(1+log k)))，log为自然对数。任意有限集合V及简单k元边族E，只要|E|≤B_RS(k)+Δ(k)，即有二染色使每条边含两色，故m(k)≥B_RS(k)+Δ(k)+1。规范完整证明：proofs/propertyb-general/CORE_THEOREM.md、UNIFORM_INTEGER_GAIN.md、CLIQUE_REFINEMENT.md。

## Honest scope
原始全超图量词，无点数、度、共度或线性附加条件。正文为全参数解析证明，不依赖整图枚举；没有新增Lean形式化。verified指本命题经正式纸面审计并有有效跨家族核心审阅，不表示无误保证或他人独立复现。严格比较对象是上述精确定义的B_RS；其他文献包络与指定零锁松弛的比较由单独成稿及终审负责，本条不自动完成整个Goal，不宣称领先渐近常数提高或世界最优。

## Evidence chain
fresh proof-checker：18/18源单位、78项义务，PROOF_AUDIT.json=PASS；Grok grok-4.7-build/xhigh end_turn与Gemini CLI gemini-4-argon-high/high SUCCESS均静态阅读全文，认可A/B/C。主代理处置context/propertyb-general/round02/reviews/CORE_DISPOSITION.md；仅改清J下界来源的一句，公式不变，审计已定向复核。原回应GROK_RAW.json/GEMINI_RAW.json保存；ARIS traces研究审阅007/008记录实际范围。数学成立来自正文而非模型投票。

完整比较终审已完成：正式BASELINE_ADDENDUM及COMBINED_AUDIT均PASS（same-family/provisional），确认k≥32的明确五项L_ref=B_RS+1、k≥256对每个M>B_RS的指定零锁必要数据松弛不通过。Grok与Gemini4的有效静态终审及最终拼接处置见context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md。Gemini为SUCCESS；Grok为同次调用原生turn_ended outcome=completed，grok-4.7-build/xhigh，原MCP envelope及stopReason缺失，保持缺失，不改填end_turn。两家未执行计算。主命题及verified状态保持原准确范围；比较不是实际H可实现性或全部潜在Grill法能力定理。最终展示及Goal交付验收已由root完成，Goal工具已实际返回status=complete（2026-10-21）。最终验收context/propertyb-general/round02/COMPLETION_AUDIT.md；最终HTML532公式离线PASS，人工交接已完成。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

