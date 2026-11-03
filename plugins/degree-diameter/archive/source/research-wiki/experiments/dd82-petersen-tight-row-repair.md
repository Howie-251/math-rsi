---
type: experiment
node_id: exp:dd82-petersen-tight-row-repair
title: "Actual matching repair of the common allowed-degree obstruction"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "repair .030486 CPU/.033222 wall; SAT .010246 CPU/.050498 wall; LRAT .003723 CPU/.005641 wall"
provenance: "proofs/dd82/construction/PETERSEN_TIGHT_ROW_DEGREE_OBSTRUCTION.md"
added: 2026-10-12T07:12:21Z
tags: ["dd82", "construction"]
---

# Actual matching repair of the common allowed-degree obstruction

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
F=0,K69→0;40 switches; full60/240/8regular graph286 bad pairs;270-variable14988-clause completion CHECKED_UNSAT

## Reasoning
All43 vertex-level allowed-degree failures were removed, but four degree-three allowed rows force internal degree4 at vertex50. Specific repaired skeleton only.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

