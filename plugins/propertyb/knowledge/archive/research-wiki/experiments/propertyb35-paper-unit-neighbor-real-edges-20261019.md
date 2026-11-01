---
type: experiment
node_id: exp:propertyb35-paper-unit-neighbor-real-edges-20261019
title: "23六度中心至少两条真实单位邻点五边"
idea_id: ""
verdict: yes
confidence: high
date: "2026-10-19"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/DISJOINT_BLOCK_EXTRA_SET.md; context/propertyb35-paper/round01/literature-degree/RANDOM_TRANSVERSAL_TRANSFER.md; RANDOM_TRANSVERSAL_CHECK.json"
added: 2026-10-19T18:43:13Z
tags: ["propertyb35-paper", "actual-edge", "random-repair"]
---

# 23六度中心至少两条真实单位邻点五边

**verdict:** `yes`  ·  **confidence:** `high`

## Metrics
完整q0/q1 signed caller；disjoint四块加一个五集：h3=7/160,h4=17/1280,E自身≤1/640；实际两支界7/40、1141/1280。

## Reasoning
若非B23/35/δ6，则每个六度中心单位邻点池含至少两条实际五边；22至少一条另依赖既有非单位双锁。所有zero固定迹边正负两项均保留；root读自含计数与实际共同度预算。它不保证五边经过指定低度点，未闭合22/23整支。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

