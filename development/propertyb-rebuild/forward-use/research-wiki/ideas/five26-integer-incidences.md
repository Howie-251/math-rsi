---
type: idea
node_id: idea:five26-integer-incidences
title: "Integer degrees exclude 26 vertices under pair coverage"
stage: piloted
outcome: positive
added: 2026-11-01T11:06:40Z
based_on: []
target_gaps: []
tags: ["propertyb", "incidence", "integer"]
---

# Integer degrees exclude 26 vertices under pair coverage

**stage:** `piloted`  ·  **outcome:** `positive`

Pair-covering 5-uniform graphs with at most33 edges have v<=25 by total degree.

## Thesis
A pair-covering finite simple 5-uniform hypergraph with at most 33 edges has at most 25 vertices. For v>=26, every vertex has degree at least ceil((v-1)/4)>=7, so total degree is at least 182 but at most 165, contradiction. The coarse v(v-1)<=660 alone permits v=26 since 650<=660. This is a complete conditional incidence proof, also checked by exact integer arithmetic. Applying it to arbitrary original hypergraphs requires the minimum-vertex noncolorable quotient reduction; the short lemma alone is not the entire 33-edge Property B theorem. No Lean or cross-family audit is performed here. See PROOF_PACKAGE_26.md and SCOPE_RESULTS.json.

## Key risks
The pair-covering hypothesis must come from a valid caller; this is not the full 33-edge coloring theorem.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

