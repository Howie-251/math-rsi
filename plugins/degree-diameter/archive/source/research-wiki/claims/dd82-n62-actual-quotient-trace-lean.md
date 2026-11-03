---
type: claim
node_id: claim:dd82-n62-actual-quotient-trace-lean
name: "Actual repeat quotient trace identity from original graphs"
description: ""
node_type: claim
status: verified
provenance: "formal/logs/n62-repeat-quotient-trace-type-axiom-audit.log"
tags: []
date: 2026-10-11
added: 2026-10-11T13:02:47Z
---

# Actual repeat quotient trace identity from original graphs

**status:** `verified`

## Statement
Original degree-at-most8, diameter-at-most2, order62 graph hypotheses imply c+2traceR=17 for actual repeat components and their constructed quotient, hence c odd.

## Honest scope
Eight exports and two actual callers compiled with only propext/Classical.choice/Quot.sound. No B<=2, supplied trace/spectral certificate or quotient assumption. GeminiB26 source review accepted. Connectedness remains unformalized.

## Evidence chain
N62RepeatQuotientTrace.lean; successful third build and type-axiom-audit logs. Integer P=62(2R+I)-17N satisfies P^3=157604P. Exact F1063 trace divisibility plus integer bounds proves the identity. Shared entrypoints integrated. B26 disposition corrects review-only L/S, universal nonmate and exact-m shorthand; proof sources unchanged.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

