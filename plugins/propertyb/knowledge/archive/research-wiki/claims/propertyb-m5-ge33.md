---
type: claim
node_id: claim:propertyb-m5-ge33
name: "m(5) ≥ 33"
description: "任意有限简单五元超图、至多32条边具有Property B；原目标已完整Lean形式化。"
node_type: claim
status: verified
provenance: ".aris/traces/proof-checker/2026-10-06_run09/"
tags: ["property-b", "hypergraph", "formal-proof", "lean"]
date: 2026-10-06
added: 2026-10-06T11:55:14Z
---

# m(5) ≥ 33

**status:** `verified`

## Statement
对任意有限集合V及E⊆{e⊆V:|e|=5}，若|E|≤32，则存在c:V→{0,1}，使每条边同时包含两种颜色。等价地，任何非二染色简单五元超图至少有33条边。

## Honest scope
Lean 4.24.0 与固定 Mathlib 下的完整 Target；使用 propext、Classical.choice、Quot.sound。自然语言命题与形式声明单独对照。未证明 m(5)=33，未声称人类同行评审或穷尽查新。

## Evidence chain
formal/Aris4Math/Main.lean: propertyB_of_at_most_thirty_two、two_colorable_of_at_most_thirty_two、non_propertyB_edges_ge_thirty_three；run09默认Main构建和独立导入均exit0且只有三项标准公理。context/FORMAL_VERIFICATION_PROGRESS.md给出全部分支和依赖，PROOF_AUDIT.json的final_formal_verification保存确定性证据。全称推理来自解析分类与一般计数，非整图搜索。 补充命题对照：Grok最终r8与Gemini全新会话r10均在实际只读范围未发现缺口；主代理对照源码复核，见context/reviews/research/REVIEW_NOTES.md及gemini_lean_main_fresh_r10.md。二者未亲自构建，模型意见不参与Lean逻辑依赖。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

