---
type: experiment
node_id: exp:ddp-wave3-route-chart-controller-20261027
title: "已核验通用路由表；有限控制图试验未通过"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-27"
hardware: "CPU; at most one worker per completed profile"
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/source_scout/SCOUT.json; pentagon175_controller/best.independent_check.json"
added: 2026-10-27T03:23:28Z
tags: ["ddp", "route-chart", "controller", "scoped-failure"]
---

# 已核验通用路由表；有限控制图试验未通过

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
324 route-chart words rank5 and inverse relations checked. A5xC3:3321 two-pair+8610 mixed sets failed;1365 four-involution sets disconnected. F31:C6:2926 two-pair sets failed; other compositions open. Pentagon175:4starts40000proposals,38189 scores,best exactNB5 missing ordered2696; unique saved-edge audit ordinaryD6,bad unordered315.

## Reasoning
No valid exact-NB5 controller and no new lower bound. This is reuse of a published sufficient fiber-routing construction, not an unrelated new construction class. Ordinary diameter and exact nonbacktracking length-five coverage remain distinct. Completed finite profiles stopped; no large lift generated.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

