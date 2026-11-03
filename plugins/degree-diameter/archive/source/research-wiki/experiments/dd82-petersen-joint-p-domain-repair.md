---
type: experiment
node_id: exp:dd82-petersen-joint-p-domain-repair
title: "Six nonempty full Petersen domains still fail joint cross coverage"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "repair .090874 CPU/.115431 wall; SAT .009637 CPU/.079198 wall; LRAT .003515 CPU/.004886 wall"
provenance: "proofs/dd82/construction/PETERSEN_JOINT_P_DOMAIN_REPAIR.md"
added: 2026-10-12T07:25:17Z
tags: ["dd82", "construction"]
---

# Six nonempty full Petersen domains still fail joint cross coverage

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
F0,R7→0;7 switches; domains[4,4,121,1,3,2]; actual60/240/8graph307bad;270vars14982clauses CHECKED_UNSAT

## Reasoning
Unique allowed P3 plus four actual cross-coverage clauses force four internal neighbors at vertex1. This closes only the saved external matching skeleton. Repair chain stopped.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

