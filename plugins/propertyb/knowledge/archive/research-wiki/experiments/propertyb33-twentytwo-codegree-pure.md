---
type: experiment
node_id: exp:propertyb33-twentytwo-codegree-pure
title: "22点候选：共度图覆盖与纯单锁扣除"
idea_id: "idea:propertyb-five-33-edge-threshold"
verdict: partial
confidence: high
date: "2026-10-08"
hardware: ""
duration: ""
provenance: "proofs/propertyb33/TWENTY_TWO.md"
added: 2026-10-07T16:45:07Z
tags: ["property-b", "codegree", "exact-arithmetic"]
---

# 22点候选：共度图覆盖与纯单锁扣除

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:propertyb-five-33-edge-threshold`

## Metrics
新稿TWENTY_TWO.md；21个所需局部型严格过且独立逐位置ABC复算；其中16个三/四锁型有精确双乘子扣除证书。最紧使用型14567/14586。

## Reasoning
无六度时至少11七度点；共度≥3用二锁，λ2图有诱导P3用三锁，否则团并选(3,1)/(2,1,1)，空图选含三点迹的unit四锁。纯link配额进入真实坏对的放松加权下界。完整数学候选正在B4跨模型审阅，新七度分支尚未Lean形式化。早期77 pair普通加强324/323仅证明旧估计不足。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

