---
type: claim
node_id: claim:dd82-paper-upper63
name: "Original-graph upper bound63, now compiled"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/proof-checker-reductions-20261011"
tags: ["dd82", "scoped-proof"]
date: 2026-10-11
added: 2026-10-11T08:35:10Z
---

# Original-graph upper bound63, now compiled

**status:** `verified`

## Statement
Every finite simple undirected graph of maximum degree at most8 and genuine diameter at most2 has at most63 vertices.

## Honest scope
The Lean original-graph theorem is universe-polymorphic. The exact value remains open; the paper upper62 is separate.

## Evidence chain
proofs/dd82/FOUNDATIONS.md; proofs/dd82/N65_MOD29_TRACE.md; proofs/dd82/N64_MOD11_TRACE.md; reviews/dd82/proof-checker-reductions-20261011 PASS paper audit; formal/DegreeDiameter/Moore65.lean, Moore64Structure.lean, Moore64.lean; formal/logs/build-moore64-integrated.log and review-moore64-audit.log exit0, only propext/Classical.choice/Quot.sound. Gemini B6 actual-source review accepted, with zero reviewer command execution; reviews/dd82/20261011_B6_upper63_brown9_n62.json.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

