---
type: experiment
node_id: exp:dd82-petersen-paired-core-exchange
title: "Paired core replacement preserves three local blocks but full assembly fails"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "23domain0.001102477CPU; prep0.102172317CPU+BFS0.030758CPU; solver0.025319CPU/0.133348342wall"
provenance: "proofs/dd82/construction/PETERSEN_PAIRED_CORE_EXCHANGE.md"
added: 2026-10-12T06:02:54Z
tags: ["dd82", "construction"]
---

# Paired core replacement preserves three local blocks but full assembly fails

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
Unique nonoriginal7-route preserving01/23matchings. Full60/240/8regular175bad/E208/diam3,blocks01/23/45exact. Fixednew23 plus sixfreeinterfaces:10600vars68161clauses RAW_UNSAT, no proof.

## Reasoning
Actual boundary differs from prior closed module. Three exact local blocks do not jointly give diameter2. Scope is fixednew23/eightotheroldinterfaces; fullsixP open. Raw UNSAT not upgraded; no repeated call.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

