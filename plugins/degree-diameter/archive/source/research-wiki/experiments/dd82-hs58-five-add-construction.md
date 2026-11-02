---
type: experiment
node_id: exp:dd82-hs58-five-add-construction
title: "HS58 five-addition full candidates and two checked joint failures"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "Generation2.013054268 parent CPU+0.780212 BFS CPU/2.859878wall; H14 solver1.902329CPU+check0.083424; H3 solver7.295349CPU+check0.307517"
provenance: "proofs/dd82/construction/HS58_TWO_DELETE_FIVE_ADDITIONS_CONSTRUCTION.md"
added: 2026-10-12T06:02:54Z
tags: ["dd82", "construction"]
---

# HS58 five-addition full candidates and two checked joint failures

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
25373specified switches,23582in67type domain,22Htypes/27saved full58/232/8regular/diam3,best74bad. FixedD H14 33345vars105994clauses CHECKED_UNSAT; residual H3 33344vars105990clauses CHECKED_UNSAT.

## Reasoning
Full candidates failed. Both actual CNFs leave all1050old additions and400attachments free, exact5A, fixedD/H only. H54 query canceled before launch by analytic obstruction. No rerun, no new bound; mathematical no-cross filter and any later orbit transport have separate evidence.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

