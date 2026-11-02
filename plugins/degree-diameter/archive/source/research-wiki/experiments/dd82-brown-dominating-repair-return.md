---
type: experiment
node_id: exp:dd82-brown-dominating-repair-return
title: "Changed dominating-neighborhood repair returns to the same Brown trap"
idea_id: "idea:dd82-brown57-extension"
verdict: no
confidence: high
date: ""
hardware: "oneCPU for searches; independent all-pairs BFS"
duration: "0.118s domination,0.118s repair,5.000s switch profile"
provenance: "computations/dd82/construction/brown_dominating8_nonline/"
added: 2026-10-11T08:51:53Z
tags: []
---

# Changed dominating-neighborhood repair returns to the same Brown trap

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:dd82-brown57-extension`

## Metrics
A non-polar eight-point dominating set was found and independently checked in0.118s; greedy degree repair produced a regular58graph with29uncovered pairs. A5s switch profile improved29->26->21,7.77million legal moves. Independent BFS:232 distance1,1400 distance2,21 distance3 pairs.

## Reasoning
The final full graph equals the original Brown-plus-hub seed exactly after transposing vertices57 and39. This particular changed insertion neighborhood falls back into the known strict local trap; no target graph or general impossibility follows. Further unchanged switching has no new justification.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

