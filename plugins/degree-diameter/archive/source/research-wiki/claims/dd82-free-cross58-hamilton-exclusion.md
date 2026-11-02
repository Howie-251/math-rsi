---
type: claim
node_id: claim:dd82-free-cross58-hamilton-exclusion
name: "58点双诱导29圈划分的计算辅助排除"
description: ""
node_type: claim
status: verified
provenance: "proofs/dd82/construction/FREE_CROSS58_HAMILTON_BRIDGE.md; computations/dd82/construction/free_cross58_run/encoding.json; computations/dd82/construction/free_cross58_run/certification/result.json; computations/dd82/construction/free_cross58_run/certification/certificate_check.log; computations/dd82/construction/free_cross58_run/CODE_REVIEW.md; reviews/dd82/20261018_free_cross58_final_review.json"
tags: ["dd82", "58", "construction", "checked-unsat", "induced-cycles"]
date: 2026-10-18
added: 2026-10-18T08:42:36Z
---

# 58点双诱导29圈划分的计算辅助排除

**status:** `verified`

## Statement
不存在58点有限简单无向图，同时满足最大度数至多8、直径至多2，且存在29+29顶点划分使两个诱导子图各自恰为C29。全部跨侧邻接自由，P不固定。

## Honest scope
完整受限族计算辅助排除：精确CNF独立LRAT认证，图族双向桥接经实际Gemini最终第2轮接受。verified表示该证据等级，不是Lean。仅含两圈二因子、其他圈型、侧内有弦及全部58阶不在本结论范围。

## Evidence chain
若点度≤7则两步球≤57，故目标8正则、每点6跨边；独立沿两圈重标，841主变量完全自由；精确行列计数与穷尽跨侧/同侧路径AND可正反扩展。保存31581变量102341子句由lrat-trim实际exit20+s VERIFIED核验；同线程第2轮接受精确结论，机制CLOSED2/4。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

