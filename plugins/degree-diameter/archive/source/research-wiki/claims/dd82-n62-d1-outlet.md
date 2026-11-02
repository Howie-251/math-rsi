---
type: claim
node_id: claim:dd82-n62-d1-outlet
name: "Closed D0 components force a D1 root at order62"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/proof-checker-n62-d0-outlet-20261011"
tags: []
date: 2026-10-11
added: 2026-10-11T11:35:41Z
---

# Closed D0 components force a D1 root at order62

**status:** `verified`

## Statement
D0_MATCH and D0_EDGE_BOUT force closed alternating 2,1 four-vertex actual repeat components. The paper triple-repeat exclusion plus odd double-edge count, actual double-root classification and fixed-point-free D0 pairing imply every actual order62 graph has a D1_MATCH root. Lean n62_exists_d1_match_parent proves this from the original graph and explicit actual B≤2.

## Honest scope
D1 remains open. The triple-repeat elimination is a retained paper/exact-check dependency and is not formalized; the Lean caller retains B≤2. Global upper bound is unchanged.

## Evidence chain
Paper fresh PASS32/Gemini B16. Actual N62D0Components and N62DoubleParity sources accepted B19. N62DoubleRoot/N62D1Outlet dedicated builds and original-caller/type/axiom audits exit0 with standard axioms only; their source review is pending B20.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

