---
type: experiment
node_id: exp:dd82-n63-norm-table
title: "Exact nonsquare norms for all cycle conductors<=63"
idea_id: "idea:dd82-n63-cyclotomic-trace"
verdict: yes
confidence: high
date: ""
hardware: ""
duration: "less than1second,oneCPU"
provenance: "computations/dd82/construction/n63_cyclotomic_norms.json; reviews/dd82/proof-checker-n63-trace-20261011/audit_checks.json"
added: 2026-10-11T08:07:08Z
tags: ["dd82", "exact-scope"]
---

# Exact nonsquare norms for all cycle conductors<=63

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:dd82-n63-cyclotomic-trace`

## Metrics
63 conductors;62 nonsquare integer norms;sole exception3 withnorm25. Independent determinant calculation agrees.

## Reasoning
Finite arithmetic obligation passed; graph-to-field semantics are supplied and separately reviewed in the paper proof. No Lean reflection claimed.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

