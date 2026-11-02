---
type: claim
node_id: claim:dd82-n59-single-triangle-exclusion
name: "Zero-row N15 excludes exactly one triangle at order59"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/proof-checker-single-triangle-20261011"
tags: ["dd82", "scoped-proof"]
date: 2026-10-11
added: 2026-10-11T08:40:12Z
---

# Zero-row N15 excludes exactly one triangle at order59

**status:** `verified`

## Statement
An original59-point graph with actual2211 matching rows at every zero-triangle vertex cannot have exactly one triangle. Together with the all-zero trace obstruction, every such graph has at least two triangles.

## Honest scope
Conditional paper theorem, not a full H5 or order59 exclusion and not yet Lean. No disjointness of repeat sets or short-cycle lemma is assumed. H5 use retains its N15 derivation.

## Evidence chain
proofs/dd82/n59/single_triangle_normal_form_exclusion_20261011.md plus full h5_nonzero_trace_constraints_20261011.md dependency; reviews/dd82/proof-checker-single-triangle-20261011 PASS32 obligations; Gemini B7 independent derivation reviews/dd82/20261011_B7_single_triangle.json.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

