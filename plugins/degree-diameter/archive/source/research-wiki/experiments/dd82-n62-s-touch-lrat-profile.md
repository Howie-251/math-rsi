---
type: experiment
node_id: exp:dd82-n62-s-touch-lrat-profile
title: "Fresh S_TOUCH base and bounded LRAT-output profile"
idea_id: "idea:dd82-n62-proof-certification"
verdict: partial
confidence: high
date: ""
hardware: "oneCPU;solver memory limit4GiB;outer wall25s"
duration: "1.614s generation plus10.10s solver"
provenance: "computations/dd82/n62/s_touch_certificate_profile/profile.json"
added: 2026-10-11T08:40:12Z
tags: []
---

# Fresh S_TOUCH base and bounded LRAT-output profile

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-n62-proof-certification`

## Metrics
Generation1.614s;399108 variables,1448815 clauses,29.15MB CNF. Solver10.10s,exit0 UNKNOWN;7204 conflicts,316.28MB peakRSS.79.04MB partial text LRAT, not a refutation.

## Reasoning
The recovered source emits a complete base and the local solver emits LRAT. This profile supplies cost evidence only; there is no UNSAT certificate, checked proof or Lean graph bridge. A rerun must have an explicit changed budget/representation and certificate plan.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

