---
type: experiment
node_id: exp:dd82-hs-augmentation-first-batch
title: "HS50 construction and star-deletion redesign"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-11"
hardware: "single pinned CPU;60second caps"
duration: "solver wall:0.189s,30.292s,0.132s,0.589s"
provenance: "computations/dd82/construction/hs_augmentation"
added: 2026-10-11T14:49:40Z
tags: ["dd82", "construction", "hs"]
---

# HS50 construction and star-deletion redesign

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
star58,petersen60,delete_star6_58,delete_star7_58: checked UNSAT. Complete8regular seeds have105,160,97,66 bad pairs respectively; diameter3.

## Reasoning
Actual complete candidates fail distance2. Fixed attachment formulas independently LRAT checked. Counting rules out all induced-HS models and forces58 deletion repairs into6/7-edge shapes; change mechanism, do not repeat inputs.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

