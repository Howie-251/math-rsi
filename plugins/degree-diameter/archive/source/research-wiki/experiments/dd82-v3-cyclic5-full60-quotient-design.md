---
type: experiment
node_id: exp:dd82-v3-cyclic5-full60-quotient-design
title: "Free-C5 quotient design: FOUND_NOT_LIFTED"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "One CPU, pinned CPU 1; one continuous nonmonotonic quotient trajectory"
duration: "19.512925058 total CPU seconds; 19.80586227029562 wall seconds, including compilation and validation"
provenance: "computations/dd82/construction/cyclic5_full60_quotient_run/resources.json; computations/dd82/construction/cyclic5_full60_quotient_run/best_quotient.json; proofs/dd82/construction/CYCLIC5_FULL60_QUOTIENT_EXPERIMENT.md"
added: 2026-10-13T09:53:46Z
tags: ["dd82", "v3", "construction", "cyclic5"]
---

# Free-C5 quotient design: FOUND_NOT_LIFTED

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
Status QUOTIENT_FOUND_NOT_LIFTED. A complete integer 12-by-12 matrix M was saved with row sum eight, ten independent orbits, D=M^2+M-7I-5J equal to the adjacency matrix of 2 K6, and the q=2 interface graph equal to C10 plus two isolated vertices. Total CPU 19.512925058 seconds; wall 19.80586227029562 seconds. One trajectory, 17,953,317 proposals, 2,494,848 accepted moves; stopped at the first qualifying quotient. No voltage search, graph witness, or exhaustive quotient enumeration.

## Reasoning
Partial design result only: this integer quotient is not a constructed 60-vertex graph. The later complete lift-exclusion manuscript, proofs/dd82/construction/CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md, has completed fresh local proof-checker PASS (reviews/dd82/proof-checker-c5-twelve-pentagons-20261013/PROOF_AUDIT.md) and same-thread Gemini round3 acceptance. All target lifts of this saved quotient are therefore mathematically excluded; the full free-C5 family remains open. A direct generalization, including the second actual quotient, was accepted in round4. No Lean or machine certificate is asserted. Fixed-M solver preparation and launch were cancelled before any source, CNF, runner, or seed verification was produced. High confidence concerns the saved matrix and actual run only.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

