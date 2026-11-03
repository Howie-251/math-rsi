---
type: idea
node_id: idea:ddp-h9-partial-fold-independent-states
title: "H9部分折叠：解除群轨道常值后的联合度预算"
stage: active
outcome: pending
added: 2026-10-27T03:48:19Z
based_on: []
target_gaps: []
tags: ["ddp", "hexagon", "partial-fold", "degree12"]
---

# H9部分折叠：解除群轨道常值后的联合度预算

**stage:** `active`  ·  **outcome:** `pending`

Published point-line pairing theorem guarantees diameter<=5 for arbitrary legal fiber splits/colors. Optimize individual split/color/copy states for degree12 and order>42342; no new lower bound yet.

## Thesis
Primary source https://zenodo.org/records/23056128, sections3-5. n=33397+|S|+sum(H3 copies)+twins. Q_data and exact degree formulas are in research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/. The original orbit-constant restriction can be removed, but each phi-fiber must retain one color.

## Key risks
Fixed7959 split set and280copies admit no strict split superset, by the saved critical-merged closure. Joint trades must allow deletions or changed copies; partial-state legality is not independent full-graph verification. Later pencil-vertex construction rules are not available here.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

