---
type: claim
node_id: claim:propertyb-m5-ge34
name: "至多33条五元边均可二染色：m(5)≥34"
description: "任意有限简单五元超图、边数≤33均有Property B；端到端Lean与原题独立复述已通过。"
node_type: claim
status: verified
provenance: "context/propertyb33/round02/final-audit/PROOF_AUDIT.json"
tags: ["property-b", "lean", "lower-bound", "theorem"]
date: 2026-10-13
added: 2026-10-13T07:48:37Z
---

# 至多33条五元边均可二染色：m(5)≥34

**status:** `verified`

## Statement
对任意有限集合V与不同五元子集族E，若|E|≤33，则存在c:V→{0,1}，使每条边e均有1≤Σ_{x∈e}c(x)≤4。等价地m(5)≥34。

## Honest scope
允许孤立点，不要求点数范围、点对覆盖、正则或平衡色类；不证明m(5)=34。采用Lean标准基础propext、Classical.choice、Quot.sound及锁定工具链；未宣称人类或第二台机器已独立复现。

## Evidence chain
formal/Aris4Math/ThirtyThree/Main.lean; formal/ReviewAudit33.lean; named Lake1138jobs exit0及post-build独立原题审计exit0，8项顶层只有标准三公理。context/propertyb33/round02/final-assembly/保存原始日志；final-audit/PROOF_AUDIT.json为实际proof-checker PASS。Grok/Gemini最终C读取范围内无实质问题，模型意见另列；正文两处说明性错误已修正且不影响Lean。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

