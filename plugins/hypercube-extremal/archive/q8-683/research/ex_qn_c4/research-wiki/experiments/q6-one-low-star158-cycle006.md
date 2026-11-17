---
type: experiment
node_id: exp:q6-one-low-star158-cycle006
title: "Q6 at most one low parity vertex: star sum at most 158"
idea_id: "idea:q8-low-degree-gates"
verdict: yes
confidence: high
date: "2026-11-07"
hardware: ""
duration: ""
provenance: "proofs/low1_cycle006/analytic/PROOF.md; orbit_sat/review/REVIEW.md; Q8_BRIDGE.md; bridge_review/REVIEW.md"
added: 2026-11-06T20:57:16Z
tags: []
---

# Q6 at most one low parity vertex: star sum at most 158

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:q8-low-degree-gates`

## Metrics
Analytic L1 proof plus 11 independently reconstructed CNFs; strict RUP checks 11,687 additions to eleven empty clauses. Adding an edge at an isolated root extends to degree zero. Every 687-edge Q8 now has minimum degree at least three.

## Reasoning
The actual one-sided unique-degree-two import is retained. All new proof/certificate/bridge reviews pass at their exact scopes; no historical large traces replayed, no new canonical claim or global upper bound.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

