---
type: experiment
node_id: exp:dd82-full-false-twin58-anneal
title: "Uncoupled false-twin58 matching construction:105 to24 bad pairs"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "one CPU,pinned1"
duration: "119.003882 child CPU seconds;119.576409 wall seconds"
provenance: "computations/dd82/construction/full_matching58_anneal_run/resources.json"
added: 2026-10-13T08:40:02Z
tags: ["dd82", "false-twins", "construction"]
---

# Uncoupled false-twin58 matching construction:105 to24 bad pairs

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
One continuous chain;50232451 proposals;0 restarts;all21 free interfaces changed;independent BFS58/232/all8/diam3/24bad;all24 bad pairs betweenG1 andG6

## Reasoning
The unrestricted matching search substantially improves the seed, but the saved graph still has diameter3. This is an actual failed candidate, not a lower-bound breakthrough, family exclusion, or certified local optimum.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

