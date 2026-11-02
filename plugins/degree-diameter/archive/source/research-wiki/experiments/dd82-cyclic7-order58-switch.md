---
type: experiment
node_id: exp:dd82-cyclic7-order58-switch
title: "First full-core cyclic7 orbit descent at order58"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "Search process .040041 CPU; independent BFS .029652 CPU; complete batch1.486870 CPU/1.502499 wall seconds"
provenance: "computations/dd82/construction/cyclic7_eight_orbits58_switch_run/; reviews/dd82/20261012_automorphisms_and_cyclic5_root_notes.md"
added: 2026-10-12T08:28:23Z
tags: ["dd82", "construction"]
---

# First full-core cyclic7 orbit descent at order58

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
105 to77 to63 bad pairs; three complete neighborhoods of49221 legal moves each; final58/232/all8/diam3/63bad;zero originalHS edges deleted

## Reasoning
All220 nonfixed orbit choices were free and no quotient condition was hard-filtered. Strict descent accepted only attachment changes; final core is still induced HS and therefore cannot be completed without actual core-edge deletion. Complete local stop, no neutral/restart.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

