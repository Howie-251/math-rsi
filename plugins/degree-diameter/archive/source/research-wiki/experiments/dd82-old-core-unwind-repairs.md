---
type: experiment
node_id: exp:dd82-old-core-unwind-repairs
title: "Complete 58 and59 graph repairs after changing obstructed old cores"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "58:0.041228 CPU sec;59:0.185895 CPU sec; core screening0.234873 CPU sec"
provenance: "proofs/dd82/construction/TWIN58_OLD_CORE_UNWIND.md; proofs/dd82/construction/HS59_OLD_CORE_REPAIR_EXPERIMENT.md"
added: 2026-10-12T02:47:09Z
tags: ["dd82", "construction", "n58", "n59"]
---

# Complete 58 and59 graph repairs after changing obstructed old cores

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
58:86400 complete choices,min47;59:139 necessary-feasible cores,141805 legal complete graphs,min41. Neither improves source21/26.

## Reasoning
Independent BFS and exact newly broken pairs saved. The specified58 repair family additionally fails a three-demands/two-free-slots argument. This is not unrestricted completion or arbitrary-order exclusion.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

