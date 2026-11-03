---
type: experiment
node_id: exp:dd82-petersen-binary-palette
title: "Complete fifteen-interface seven-route preserving palette fails"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "Palette0.005639CPU; search0.116577childCPU; parent+BFS0.021836478CPU; wall0.272546608"
provenance: "computations/dd82/construction/petersen_binary_palette_run"
added: 2026-10-12T06:02:54Z
tags: ["dd82", "construction"]
---

# Complete fifteen-interface seven-route preserving palette fails

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
All15local palettes exactly2matchings;32768/32768fullgraphs examined,minimum20bad/E50. Exactly4commonminima masks0,16383,16384,32767;independentBFS all60/240/8regular/diam3.

## Reasoning
Complete finite exclusion only when every L_ij=M+PiM+MPj equals its original double-HS seed matrix. Generalq0 and fullsixP not excluded. Root read full exact-cover preparation, Gray-code exhaustive source and independentBFS/results. No solver used.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

