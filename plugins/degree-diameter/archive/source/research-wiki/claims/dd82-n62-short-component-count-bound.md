---
type: claim
node_id: claim:dd82-n62-short-component-count-bound
name: "At most nine repeat components using only the earlier twelve-point size bound"
description: ""
node_type: claim
status: sound-modulo-imports
provenance: "reviews/dd82/proof-checker-n62-sixth-trace-20261011/SHORT_COMPONENT_COUNT_DELTA_AUDIT.json"
tags: []
date: 2026-10-11
added: 2026-10-11T12:54:53Z
---

# At most nine repeat components using only the earlier twelve-point size bound

**status:** `sound-modulo-imports`

## Statement
Actual order62 repeat support has odd component count c<=9 using H,K>=12. The only extra packing case c11 forces h=k12, crossdegrees4, and remaining sizes eight fours and one six. The exact nonnegative budget gives4-alpha<=2-alpha^2, impossible.

## Honest scope
Retains triple-repeat exclusion, actual D1 existence, global quotient/evenness/trace, and D1 minimum-size proof through Section5. Removes the later H,K>=14 partner-exclusion chain from the connectedness proof. Paper deltaPASS6; GeminiB24 accepted within scope, no Lean countbound.

## Evidence chain
SHORT_COMPONENT_COUNT_BOUND.md, updated CONNECTED_REPEAT_REDUCTION.md Section1. Two minor source-attribution/reference corrections applied and independently rechecked. Cross-family record: reviews/dd82/20261011_B24_n62_short_bound_witnesses_sixth_quotient.md; no reviewer execution.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

