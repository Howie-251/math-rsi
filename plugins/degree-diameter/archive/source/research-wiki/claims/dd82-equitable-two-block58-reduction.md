---
type: claim
node_id: claim:dd82-equitable-two-block58-reduction
name: "58点奇偶障碍与二块equitable结构归约"
description: ""
node_type: claim
status: verified
provenance: "proofs/dd82/construction/EQUITABLE_TWO_BLOCK58_REDUCTION.md; reviews/dd82/20261018_joint_twofactor58_direction.json"
tags: ["dd82", "58", "parity", "equitable-partition"]
date: 2026-10-18
added: 2026-10-18T09:10:06Z
---

# 58点奇偶障碍与二块equitable结构归约

**status:** `verified`

## Statement
任何58点最大度≤8、直径≤2目标必有三角形或某非邻点对至少三个共同邻居；不存在内部4/跨4的29+29划分。若有非平凡两块equitable划分，则必须两侧各29、内部各2正则、跨侧6正则；自由两侧二因子允许把跨路线重复置换无损归一为P=I。

## Honest scope
完整纸面证明及实际Gemini第1轮接受，非Lean。一般必要条件不排除整个58阶；其他结论以存在二块equitable划分为前提。至少一侧非Hamilton另引用已认证旧子族排除。

## Evidence chain
无三角且非邻共邻≤2会使简单7正则缺陷图有203边，但双共邻点对=2×C4数，矛盾；4+4同侧路径饱和迫上述条件。跨边互素整除、握手奇偶和容量完成两块归约；自由右侧重标证明P=I。

## Connections
2026-10-18 旧58对齐：一般“有三角形或非邻点共邻至少3”的奇偶必要条件已由旧 after_v4_theory.md §2 覆盖，本条仅重述并用于二块归约，不另计新全域成果。二块归约及其后续完整子族排除保留原数学范围与证据。

_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._
