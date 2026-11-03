---
type: experiment
node_id: exp:dd82-cyclic5-four-orbit-quotient-profile
title: "Complete quotient profile up to four orbit replacements"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "Profile .910667 CPU/.911611 wall; complete batch1.728296 CPU/1.738711 wall seconds"
provenance: "proofs/dd82/construction/CYCLIC5_FOUR_ORBIT_QUOTIENT_PROFILE.md"
added: 2026-10-12T08:23:52Z
tags: ["dd82", "construction"]
---

# Complete quotient profile up to four orbit replacements

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
49995 deletion sets,105 endpoint pairings each,5249475 total;5083155 diagonal,1195155 row types,165915 D>=0;all survivors have zero independent orbits

## Reasoning
Padding and endpoint-degree preservation include every target at distance<=4 in this fixed action. Pure all-internal-cycle obstruction closes all survivors; no surviving graph to expand or BFS.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

