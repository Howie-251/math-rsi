---
type: experiment
node_id: exp:dd82-n58-multiedge-annealing-probe
title: "Brown-plus-hub annealing with four-to-seven-edge cyclic reconnections"
idea_id: ""
verdict: no
confidence: high
date: ""
hardware: "one pinned CPU127"
duration: "60.0105 seconds"
provenance: "computations/dd82/construction/n58_annealing_probe.json"
added: 2026-10-11T12:54:55Z
tags: []
---

# Brown-plus-hub annealing with four-to-seven-edge cyclic reconnections

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
One pinned CPU127,60.0105s, six10s trajectories; 105210880 proposals,72576202 legal,4454402 accepted,1844305 uphill. New4--7-edge cyclic moves:22375570 legal,579028 accepted,267564 uphill. Best21 missing pairs, identical seed; all final scores90,82,90,91,76,101.

## Reasoning
No valid58 graph. Independently recomputed BFS on seed,best and all six final edge lists; all8regular, observed scores agree. This finite stochastic experiment does not exclude arbitrary58 graphs or even this whole search space. No unchanged rerun recommended.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

