---
type: experiment
node_id: exp:dd82-v3-fullgraph-weighted60-20261013
title: "Fullgraph60 dynamic pair weights: structural exit without improved best"
idea_id: "idea:dd82-fullgraph60-dynamic-pair-weights"
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "one CPU0,4GiB limit"
duration: "59.006266 CPU s /59.150185 wall s"
provenance: "proofs/dd82/construction/FULLGRAPH60_WEIGHTED_PREPARATION.md; reviews/dd82/20261013_V3_fullgraph_actual_results_review.json; .aris/traces/auto-review-loop/dd82-v3-fullgraph-weighted60-20261013/002-root-disposition.md"
added: 2026-10-13T10:46:08Z
tags: ["dd82", "construction", "bounded-pilot"]
---

# Fullgraph60 dynamic pair weights: structural exit without improved best

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-fullgraph60-dynamic-pair-weights`

## Metrics
520 complete scans +1 partial;22086250 moves evaluated;449 accepted;164 raw-uphill;best20;final26. Four complete graphs independently BFS-checked:20/22/26/20 badpairs, all diameter3.

## Reasoning
Actual final graph changes38 fiberdegreeprofiles, removes22 originalinternaledges and violates the originalC5 permutation. This establishes exit from those original representations, not absence of other symmetries. No best improvement or target. Round2 result review accepted; root paused additional unchanged heuristic computation with family open.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

