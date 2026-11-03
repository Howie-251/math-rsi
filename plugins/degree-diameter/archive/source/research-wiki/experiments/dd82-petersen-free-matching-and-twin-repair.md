---
type: experiment
node_id: exp:dd82-petersen-free-matching-and-twin-repair
title: "Free all15 Petersen matchings and repair the double-HS failure"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-11"
hardware: "one pinned CPU;4GiB process cap"
duration: "90.003 CPU seconds free search;0.034 CPU five-match SAT;29.885 CPU nine-match SAT;90.001 CPU energy search"
provenance: "proofs/dd82/construction/PETERSEN_DOUBLE_HS_REPAIR.md; computations/dd82/construction/petersen_all_matchings_run/; petersen_cycle_energy_run/"
added: 2026-10-11T15:39:17Z
tags: ["dd82", "construction", "n60"]
---

# Free all15 Petersen matchings and repair the double-HS failure

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
Exact bad pairs50 to20; best remains60/240/degree8/diam3. Five-match twin repair checked UNSAT; nine-match UNKNOWN. Cycle energy remains50.

## Reasoning
Both old fixed-root and C5 restrictions removed. Candidate exposes twin-core obstruction, applied immediately to exact repairs and a newly proved cycle-energy objective. No valid graph found and no unchanged run repeated.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

