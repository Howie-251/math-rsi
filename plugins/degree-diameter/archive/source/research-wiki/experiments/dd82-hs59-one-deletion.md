---
type: experiment
node_id: exp:dd82-hs59-one-deletion
title: "HS59 joint auxiliary graph and attachments"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-11"
hardware: "one pinned CPU,60second cap"
duration: "0.123CPU seconds"
provenance: "computations/dd82/construction/hs59_one_delete"
added: 2026-10-11T15:04:55Z
tags: ["dd82", "construction", "hs59"]
---

# HS59 joint auxiliary graph and attachments

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
9156vars32386clauses;CHECKED_UNSAT. Complete59point236edge8regular seed has82bad pairs, all old-new.

## Reasoning
Auxiliary H left variable. Exact endpoint repair forces H universal, then endpoint can reach at most6/9new vertices. Mathematical argument closes whole one-deletion family.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

