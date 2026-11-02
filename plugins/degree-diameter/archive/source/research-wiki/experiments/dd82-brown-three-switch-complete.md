---
type: experiment
node_id: exp:dd82-brown-three-switch-complete
title: "Complete Brown hub three-switch neighborhood"
idea_id: "idea:dd82-brown-three-switch"
verdict: no
confidence: high
date: ""
hardware: "One pinned CPU"
duration: "1.136 CPU seconds"
provenance: "computations/dd82/construction/brown58_three_switch.json"
added: 2026-10-11T09:41:50Z
tags: []
---

# Complete Brown hub three-switch neighborhood

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:dd82-brown-three-switch`

## Metrics
9,537,248 legal moves; minimum34 missing pairs versus seed21; hub-changing983,136 min34, fixed-hub8,554,112 min45; 146 full-score checks agree.

## Reasoning
Every declared one-step move worsens the seed. Independent BFS from saved edge lists confirms seed21 and best34 missing pairs, both diameter3. This does not exclude a multistep escape or arbitrary58 graph.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

