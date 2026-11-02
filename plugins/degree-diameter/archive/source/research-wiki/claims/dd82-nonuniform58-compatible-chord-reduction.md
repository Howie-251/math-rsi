---
type: claim
node_id: claim:dd82-nonuniform58-compatible-chord-reduction
name: "58点固定跨矩阵的共同弦配对与右侧缺口森林约束"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/20261018_nonuniform58_structural_review.json"
tags: ["DD82", "n58", "construction", "paper-proof"]
date: 2026-10-18
added: 2026-10-18T10:09:33Z
---

# 58点固定跨矩阵的共同弦配对与右侧缺口森林约束

**status:** `verified`

## Statement
For fixed C in the C28/C30+matching6 family, cross coverage is equivalent to absence of high-column holes and a perfect matching in the mutual hole-support compatibility graph. Far-disjoint high/low column pairs must embed under the actual low-partner involution into the high-low boundary of C30, hence form a linear forest. Adding these partner conditions yields an exact matching condition for all cross and high-involving right coverage; low-low and left-far coverage remain separate.

## Honest scope
Complete paper reductions directly accepted in round3. They do not supply a realizable front C or exclude every front, and the linear-forest conclusion uses C30. No replacement of the actual partner involution by an arbitrary permutation; no solver or Lean.

## Evidence chain
computations/dd82/construction/nonuniform58_run/ROW_DEFECT_PROPAGATION.md; computations/dd82/construction/nonuniform58_run/RIGHT_SUPPORT_MATCHING_OBSTRUCTION.md; reviews/dd82/20261018_nonuniform58_structural_review.json

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

