---
type: experiment
node_id: exp:dd82-n60-a5-cayley-complete-family
title: "Complete A5 Cayley family check finds no target"
idea_id: "idea:dd82-n60-a5-cayley"
verdict: no
confidence: high
date: ""
hardware: "one pinned CPU"
duration: "0.0532s search plus compilation"
provenance: "computations/dd82/construction/a5_cayley60.json; a5_cayley60_best.verification.json"
added: 2026-10-11T09:21:35Z
tags: []
---

# Complete A5 Cayley family check finds no target

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:dd82-n60-a5-cayley`

## Metrics
600875inverseclosed8sets; maximumradius2ball53; bestgraph60vertices/240edges, degree8,210pairsdistance3 byindependentBFS.

## Reasoning
Exactconstructionsearch inone finitefamily. Enumerationcount matches sum C(22,k)C(15,8-2k); no group/type restriction used outside this experiment. No new lowerbound or arbitraryorder60exclusion.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

