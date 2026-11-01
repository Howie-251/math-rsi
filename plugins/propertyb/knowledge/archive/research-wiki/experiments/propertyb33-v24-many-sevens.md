---
type: experiment
node_id: exp:propertyb33-v24-many-sevens
title: "24点至少18七度点：解析选点与实际坏对自适应扣除"
idea_id: "idea:propertyb-five-33-edge-threshold"
verdict: partial
confidence: high
date: "2026-10-08"
hardware: ""
duration: ""
provenance: "context/propertyb33/round01/small-math/V24_MANY_SEVENS_REPLAY.json"
added: 2026-10-07T17:40:49Z
tags: ["propertyb33", "local-classification", "adaptive-deletion"]
---

# 24点至少18七度点：解析选点与实际坏对自适应扣除

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:propertyb-five-33-edge-threshold`

## Metrics
32种有标签大迹族、320种度标记、10个彩色轨道；201个自适应输入+5基线；4944行完整独立复算，所有总界<1。

## Reasoning
完整条件候选由六度唯一坏对及禁对计数得到实际两六三七锁，满足一侧避开七锁。独立核验库存覆盖与扣除，Gemini B6只读审阅未发现缺口。尚未Lean，23及24七度点≤17未覆盖。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

