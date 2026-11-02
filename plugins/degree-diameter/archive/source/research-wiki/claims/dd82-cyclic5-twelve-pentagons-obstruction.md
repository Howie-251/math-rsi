---
type: claim
node_id: claim:dd82-cyclic5-twelve-pentagons-obstruction
name: "Twelve-pentagon anti-cycle architecture and two actual C5 quotients excluded"
description: "A zero cross-defect block with the specified two cycle-shaped quotient blocks forbids every target lift."
node_type: claim
status: sound-modulo-imports
provenance: "reviews/dd82/proof-checker-c5-twelve-pentagons-20261013/PROOF_AUDIT.json"
tags: ["dd82", "cyclic5", "spectral"]
date: 2026-10-13
added: 2026-10-13T10:09:19Z
---

# Twelve-pentagon anti-cycle architecture and two actual C5 quotients excluded

**status:** `sound-modulo-imports`

## Statement
No degree-eight diameter-at-most-two order60 graph consists of two halves of six pentagons with an anti-cycle perfect matching for every opposite pentagon pair. Consequently a free-C5 quotient M is impossible whenever some 6+6 partition has D[U,V]=0 for D=M^2+M-7I-5J and both M principal blocks are exactly a unit C5 plus an isolated diagonal-two label. Both actual quotient-search outputs satisfy this condition.

## Honest scope
Conditional architecture exclusion only. The complete free-C5 family and arbitrary orders58-61 stay open; no Lean or formal certificate. The original full proof and narrow corollary have fresh local PASS and Gemini round3 acceptance. The broader zero-cross-defect corollary and second instance were checked by root/writer and accepted by same-thread Gemini round4: reviews/dd82/20261013_V3_c5_generalized_obstruction_review.json. Earlier receipts do not cover the later addition.

## Evidence chain
proofs/dd82/construction/CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md; fresh proof-checker audit; reviews/dd82/20261013_V3_c5_quotient_obstruction_review.json; second instance arithmetic: computations/dd82/construction/cyclic5_full60_quotient_escape_run/best_quotient.pentagon_obstruction.json. The K6,6 voltage obstruction is the substantive mathematical import.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

