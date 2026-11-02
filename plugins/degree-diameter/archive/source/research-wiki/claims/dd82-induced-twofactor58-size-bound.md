---
type: claim
node_id: claim:dd82-induced-twofactor58-size-bound
name: "任意58点目标的诱导二正则子图至多28点"
description: ""
node_type: claim
status: verified
provenance: "proofs/dd82/construction/INDUCED_TWOFACTOR58_SIZE_BOUND.md; reviews/dd82/20261018_joint_twofactor58_induced_bound_review.json"
tags: ["dd82", "58", "induced-subgraphs", "global-necessary-condition"]
date: 2026-10-18
added: 2026-10-18T09:23:05Z
---

# 任意58点目标的诱导二正则子图至多28点

**status:** `verified`

## Statement
对任意58点最大度≤8、直径≤2图及任意非空S，若G[S]二正则，则|S|≤28；包含所有诱导圈及互无跨边的多个诱导圈并。

## Honest scope
全域必要结构，无需预设两块equitable、补集正则或对称性。纯纸面归约导入已接受二块族计算辅助排除，非Lean、非完整58阶排除。带弦圈/非诱导二因子不适用。

## Evidence chain
若s≥29，补集点的到S路线容量≤3(8-r_x)+sum_neighbor(8-r_y)先排除所有r0，再排除所有r1；故补集r≥2。跨边握手6s≤6(58-s)迫s29且补集全2正则，落入已排除二块族。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

