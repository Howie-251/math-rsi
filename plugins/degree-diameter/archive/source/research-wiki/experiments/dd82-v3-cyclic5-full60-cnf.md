---
type: experiment
node_id: exp:dd82-v3-cyclic5-full60-cnf
title: "Full free-C5 order-60 CNF: bounded UNKNOWN"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "One CPU, pinned CPU 0; CaDiCaL; proof disabled"
duration: "118.335497 CPU seconds; 120.157846 wall seconds"
provenance: "computations/dd82/construction/cyclic5_full60_run/result.json; proofs/dd82/construction/CYCLIC5_FULL60_CNF_PREPARATION.md"
added: 2026-10-13T09:53:46Z
tags: ["dd82", "v3", "construction", "cyclic5"]
---

# Full free-C5 order-60 CNF: bounded UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
Status UNKNOWN. One solver call on the full 354-edge-orbit domain, with 26,826 variables and 90,544 clauses. Actual solver CPU 118.335497 seconds and wall 120.15784605965018 seconds. No model or proof was produced.

## Reasoning
Partial computational result only. The encoding permits all simple degree-eight diameter-two order-60 graphs with a free C5 action, up to legitimate orbit relabeling, without fixing a quotient. The bounded call did not decide this family. High confidence applies to the recorded execution and resource measurements, not to existence or nonexistence of a target graph.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

