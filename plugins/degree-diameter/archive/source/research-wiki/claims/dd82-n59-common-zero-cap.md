---
type: claim
node_id: claim:dd82-n59-common-zero-cap
name: "Any pair has at most two common zero vertices under N15"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/proof-checker-zero-core-20261011"
tags: []
date: 2026-10-11
added: 2026-10-11T09:41:50Z
---

# Any pair has at most two common zero vertices under N15

**status:** `verified`

## Statement
For an actual finite graph with matchingRow at every zero-triangle vertex, two distinct vertices have at most two common zero neighbors. A heavy ZZ pair has an actual nonzero common neighbor.

## Honest scope
Actual G and B definitions; N15 remains an explicit premise. N59ZeroCore compiles with standard axioms. Fresh paper audit and Gemini B11 actual source backtranslation accepted. No N15 universality claim.

## Evidence chain
independent_zero_common_neighbors_20261011.md; proof-checker-zero-core PROOF_AUDIT; formal/DegreeDiameter/N59ZeroCore.lean; n59-zero-core-heavy-build.log; n59-zero-core-type-axiom-audit.log; reviews/dd82/20261011_B11_global_capacity_lean.json

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

