---
type: experiment
node_id: exp:dd82-v3-cyclic5-full60-quotient-escape
title: "C5 second quotient: literal filter escaped, lift still excluded"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "One CPU, pinned CPU1; one cold trajectory"
duration: "31.449651254 total CPU seconds;32.014537714 wall seconds"
provenance: "computations/dd82/construction/cyclic5_full60_quotient_escape_run/; proofs/dd82/construction/CYCLIC5_FULL60_QUOTIENT_ESCAPE_EXPERIMENT.md"
added: 2026-10-13T10:09:19Z
tags: ["dd82", "v3", "cyclic5"]
---

# C5 second quotient: literal filter escaped, lift still excluded

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
32,073,527 proposals;2,644,040 accepted;944,706 upward. Ten independent orbits of type3,1^5; internal orbits9/11; five q3 interfaces, no q2; D nonnegative,row5,not2K6. Complete M/D saved. No voltage assignments, target graph, solver or BFS.

## Reasoning
The new trajectory implemented the prior round3 sufficient-condition exclusion and passed its literal predicate, but did not escape the actual mathematical architecture: U={0,4,6,7,10,11},V={1,2,3,5,8,9} have zero cross D and each M half is unitC5+diagonal2 singleton. The existing proof extends directly and excludes all target lifts. Root/writer checked the extension; same-thread Gemini round4 accepted it in reviews/dd82/20261013_V3_c5_generalized_obstruction_review.json. Further quotient sampling is paused; the full family remains open. The original JSON remains the historical search result, not proof of target existence.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

