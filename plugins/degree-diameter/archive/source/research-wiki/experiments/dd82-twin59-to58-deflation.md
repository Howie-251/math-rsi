---
type: experiment
node_id: exp:dd82-twin59-to58-deflation
title: "Actual 58-point deflation candidate and bounded neutral search"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "Deflation and first switch 0.116162 process CPU seconds; subsequent neutral search 10 CPU seconds"
provenance: "proofs/dd82/construction/TWIN58_NONWORSENING_LEVELS.md"
added: 2026-10-12T02:47:09Z
tags: ["dd82", "construction", "n58"]
---

# Actual 58-point deflation candidate and bounded neutral search

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
148680 deflation choices,147600 legal,min24; switch gives21. Nonisomorphic to old Brown seed:5 triangles vs56. New neutral episode retained1127 states,20810752 switches,no improvement before cap,not closed.

## Reasoning
Actual58/232/all8 graphs independently BFS; still diameter3. Fixed old core forces at least6 bad pairs, so attachment-only completion cannot succeed.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

