---
type: experiment
node_id: exp:dd82-petersen-four-fiber-reassembly
title: "Petersen four-fiber simultaneous reconstruction"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "preparation0.102207979 parent+BFS0.030948 CPU;SAT0.027937 CPU;boundary witness0.000730616 CPU"
provenance: "computations/dd82/construction/petersen_four_fiber_reassembly_run"
added: 2026-10-12T05:26:30Z
tags: ["dd82", "construction"]
---

# Petersen four-fiber simultaneous reconstruction

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
Full60/240/8regular seed97bad,E118,E45=0,no omitted-fiber HS50. Six interfaces01,04,05,14,15,45 free with01 changed;10600vars68121clauses RAW_UNSAT, no solver proof.

## Reasoning
Actual partition reconstructed but other blocks fail. Separate analytic boundary rigidity subsequently forces old01 and excludes this changed-core module independently of RAW result.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

