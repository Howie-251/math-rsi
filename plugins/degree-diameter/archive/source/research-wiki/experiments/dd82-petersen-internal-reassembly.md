---
type: experiment
node_id: exp:dd82-petersen-internal-reassembly
title: "Internal Petersen replacement and fixed matching route obstruction"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "single-P0 screenCPU0.111903s; independentBFS0.060616s; parent0.010747s; fixedroute witness0.013380s"
provenance: "proofs/dd82/construction/PETERSEN_INTERNAL_REASSEMBLY.md; proofs/dd82/construction/PETERSEN_ALL_INTERNAL_COMPLETION.md"
added: 2026-10-12T06:41:52Z
tags: ["dd82", "construction"]
---

# Internal Petersen replacement and fixed matching route obstruction

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
30240 P0 choices have empty fixed-P2/P3 boundary domain; changed fullgraph111bad. Old97externalcore has25 violating fixed rows and at least17bad pairs for any cubic internals; its proposed all-internal SAT canceled before encoding.

## Reasoning
Concrete four-missing/three-available boundary witness and fixedfive routes reachingonlytwo targets explain the necessary changes. No fullsixP exclusion.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

