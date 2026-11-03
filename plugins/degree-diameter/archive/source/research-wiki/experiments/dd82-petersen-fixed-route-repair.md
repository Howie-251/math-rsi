---
type: experiment
node_id: exp:dd82-petersen-fixed-route-repair
title: "Repaired external matching skeleton with exact all-internal completion"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "repairCPU0.005582s; BFS0.030683s; prep0.037395s; solver0.009957s; LRATcheck0.003624s"
provenance: "proofs/dd82/construction/PETERSEN_FIXED_ROUTE_REPAIR_AND_INTERNAL_COMPLETION.md"
added: 2026-10-12T06:41:52Z
tags: ["dd82", "construction"]
---

# Repaired external matching skeleton with exact all-internal completion

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
21 strictswitches reduce externaldeficit26to0; actual60/240/8regular fullgraph186bad/E209. Allsixinternal-free270variable15035clause completion is CHECKED_UNSAT.

## Reasoning
All fixed five-route rows pass but six internal cubic/girth-five graphs cannot coexist for this specific new external skeleton. Exact binary remaining coverage; independent LRAT verified. General external skeletons and fullsixP remain open.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

