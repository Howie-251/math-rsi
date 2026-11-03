---
type: claim
node_id: claim:dd82-n62-three-components-excluded
name: "Order62 cannot have exactly three repeat-support components"
description: ""
node_type: claim
status: sound-modulo-imports
provenance: "reviews/dd82/proof-checker-n62-12-20-30-20261011/INTEGRATION_DELTA_AUDIT.json"
tags: []
date: 2026-10-11
added: 2026-10-11T12:17:03Z
---

# Order62 cannot have exactly three repeat-support components

**status:** `sound-modulo-imports`

## Statement
Every actual order62 degree-at-most-eight diameter-at-most-two graph has repeat-support component count different from three. Exact positive-even-size quotient classification gives only sizes6/24/32,8/24/30,12/20/30, all excluded by actual-graph proofs. This c3 theorem avoids the global triple-repeat classification and H,K>=14 chain.

## Honest scope
Paper theorem using an external exact quotient enumeration, not a Lean theorem or full order62 exclusion. The later full connectedness theorem does retain the global triple-repeat and minimum-size chain.

## Evidence chain
THREE_COMPONENT_EXCLUSION.md; widened minsize2 checker9108/18/3, deltaPASS6; original6casePASS11, fresh8casePASS22, fresh12casePASS13, integrationPASS10. GeminiB21 accepts original three proofs, B22 accepts widened domain and integration.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

