---
type: experiment
node_id: exp:propertyb36-maximum-unit-refinement-20261015
title: "36：最大单位集的9/10锁分流与五K5刚性"
idea_id: "idea:propertyb36-40-structural-diagnosis"
verdict: partial
confidence: high
date: "2026-10-15"
hardware: ""
duration: ""
provenance: "context/propertyb36-40-diagnosis-20261015/gemini4-discussion/MAXIMUM_UNIT_SET_REFINEMENT.md"
added: 2026-10-15T13:01:28Z
tags: ["property-b", "36", "structure", "gemini4"]
---

# 36：最大单位集的9/10锁分流与五K5刚性

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:propertyb36-40-structural-diagnosis`

## Metrics
全七度25点：alpha>=9给九单位锁；alpha8/7给九锁1/2匹配异常；alpha6/5给十锁4/5匹配异常；alpha5迫使加权冲突图为五个单位权K5。

## Reasoning
Gemini4给出不同于三分区的最大独立集扩充证明及实际反例，主代理提炼更细分流并核算，6.1 Sol另核对。结构引理有纸面证明，新概率界和完整36仍开放。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

