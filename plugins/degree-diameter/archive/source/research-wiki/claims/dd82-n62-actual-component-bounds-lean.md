---
type: claim
node_id: claim:dd82-n62-actual-component-bounds-lean
name: "Actual repeat component sizes and quotient budgets in Lean"
description: ""
node_type: claim
status: verified
provenance: "formal/logs/n62-repeat-component-bounds-type-axiom-audit.log"
tags: []
date: 2026-10-11
added: 2026-10-11T12:54:54Z
---

# Actual repeat component sizes and quotient budgets in Lean

**status:** `verified`

## Statement
Actual component sizes are positive and even; B<=2 implies each size at least4. Actual quotient budget sum_D R_CD(R_DC-1)=n_C+2-R_CC and internal square R_CC^2-2<=n_C.

## Honest scope
Only minimum-size theorem uses explicit B<=2. Seven exports and three original callers compiled, only standard three axioms. GeminiB25 source accepted. Does not give connectedness or an order62 exclusion.

## Evidence chain
N62RepeatComponentBounds.lean; n62-repeat-component-bounds-second.log and type-axiom-audit.log; B25 scoped review.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

