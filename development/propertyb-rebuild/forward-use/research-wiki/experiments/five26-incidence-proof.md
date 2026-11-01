---
type: experiment
node_id: exp:five26-incidence-proof
title: "Complete short proof and exact arithmetic"
idea_id: "idea:five26-integer-incidences"
verdict: yes
confidence: high
date: ""
hardware: ""
duration: ""
provenance: "development/propertyb-rebuild/forward-use/PROOF_PACKAGE_26.md"
added: 2026-11-01T11:06:40Z
tags: []
---

# Complete short proof and exact arithmetic

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:five26-integer-incidences`

## Metrics
v26; coarse650<=660; min degree7; lower182>upper165.

## Reasoning
A pair-covering finite simple 5-uniform hypergraph with at most 33 edges has at most 25 vertices. For v>=26, every vertex has degree at least ceil((v-1)/4)>=7, so total degree is at least 182 but at most 165, contradiction. The coarse v(v-1)<=660 alone permits v=26 since 650<=660. This is a complete conditional incidence proof, also checked by exact integer arithmetic. Applying it to arbitrary original hypergraphs requires the minimum-vertex noncolorable quotient reduction; the short lemma alone is not the entire 33-edge Property B theorem. No Lean or cross-family audit is performed here. See PROOF_PACKAGE_26.md and SCOPE_RESULTS.json.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

