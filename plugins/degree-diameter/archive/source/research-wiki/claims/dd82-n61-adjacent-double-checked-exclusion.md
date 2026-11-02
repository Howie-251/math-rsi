---
type: claim
node_id: claim:dd82-n61-adjacent-double-checked-exclusion
name: "Any order61 target has no original adjacent double-defect edge"
description: ""
node_type: claim
status: verified
provenance: "dd82-hil-epsilon1-full61-20261018; complete epsilon0/epsilon1 graph-to-CNF coverage, independent C LRAT checking and actual final scoped review"
tags: ["dd82", "n61", "actual-defect", "checked-LRAT"]
date: 2026-10-18
added: 2026-10-18T16:49:41Z
---

# Any order61 target has no original adjacent double-defect edge

**status:** `verified`

## Statement
For any simple61 graph of degree≤8 and diameter≤2, its actual defect matrix Delta=A²+A−7I−J satisfies Delta_uv≤1 on every original graph edge. Thus every edge lies in at most one triangle. Each induced neighborhood is at most two matching edges plus isolated vertices; the three common neighbors of a nonadjacent double-defect pair are independent.

## Honest scope
Computationally assisted mathematical exclusion, not Lean. Complete adjacent-double original branch; arbitrary legitimate colors and parent partitions, no reflection/C5 template, no old [3,3] RAW or I12 H/noO dependency. Nonadjacent double-defect and no-double cases remain open; no whole61 closure, no target graph, overall57≤N≤61.

## Evidence chain
proofs/dd82/n61/EPSILON1_CHECKED_EXCLUSION.md; EPSILON0_CHECKED_EXCLUSION.md; computations/dd82/n61/epsilon1_single_packing_full61_run/RESULTS.md and certification/result.json/certificate_check.log/proof.lrat; reviews/dd82/20261018_epsilon1_full61_final_review.json; .aris/traces/research-review/dd82-epsilon1-root.md

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

