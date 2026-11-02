---
type: claim
node_id: claim:dd82-n62-triangle-witness-refinement
name: "Nongenerated repeat triangle witnesses avoid all heavy endpoints"
description: ""
node_type: claim
status: sound-modulo-imports
provenance: "reviews/dd82/proof-checker-n62-triangle-witnesses-20261011/PROOF_AUDIT.json"
tags: []
date: 2026-10-11
added: 2026-10-11T12:54:53Z
---

# Nongenerated repeat triangle witnesses avoid all heavy endpoints

**status:** `sound-modulo-imports`

## Statement
All original pair witnesses of a nongenerated unit repeat triangle are nonheavy. Type1 centers have ell=m=0; type1 triangle vertices have m<=1. Hence17d+3v_extra+3c_out<=186 and tau+4t1+2|U1 minus C1|<=248-24d+2L3. The center graph has only K1,K2,P3,P4,C4 components at this stage; tips of an original-adjacent unit diamond force both triangles type0.

## Honest scope
FreshPASS14, GeminiB24 accepted within scope. Centers may lie on other triangles, witnesses and external ports may coincide. This does not exclude any remaining d or all type0/type1 triangles. A later note further excludes center C4.

## Evidence chain
CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md and direct actual D1/unittriangle/mixedtrace dependencies; repeated-port p=q case checked. Cross-family record: reviews/dd82/20261011_B24_n62_short_bound_witnesses_sixth_quotient.md; no reviewer execution.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

