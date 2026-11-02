---
type: claim
node_id: claim:dd82-free-factor-cyclic58-new-columns-not-both-five
name: "自由左右因子58源中两新增列不能均为5度"
description: ""
node_type: claim
status: verified
provenance: "computations/dd82/construction/free_factors_cyclic58_run/ROW_CHANGE_GEOMETRY.md; reviews/dd82/20261018_free_factors_cyclic58_geometry_review.json"
tags: ["dd82", "58", "construction"]
date: 2026-10-18
added: 2026-10-18T12:31:52Z
---

# 自由左右因子58源中两新增列不能均为5度

**status:** `verified`

## Statement
固定A={0,3,6,10,14,19}的28旧列只删，左右二因子自由且右加匹配的58目标中，两新增跨列不可能均为5度。

## Honest scope
完整纸面证明已获直接ACCEPT，非Lean、非全58排除。后续5+6也获独立直接接受；两者合并得两新列均6的冗余剪枝，代码delta待核对，正式输入未生成。

## Evidence chain
唯一共邻伙伴损失计数2m+k；5+5迫k=0，只能偏移0/10；每旧列至多一删除迫14行轨道，与至多10修改行矛盾。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

