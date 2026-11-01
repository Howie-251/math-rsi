---
type: experiment
node_id: exp:propertyb35-paper-small-swap-20261019
title: "≤18点唯一单色边交换计数与独立重放"
idea_id: "idea:propertyb35-paper-unique-swap"
verdict: yes
confidence: high
date: "2026-10-19"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/SMALL_VERTEX_SWAP.md；context/propertyb35-paper/round01/eighteen/REPORT.md、SWAP_CHECK.json；round01/root/UNIQUE_SWAP_REPLAY.json"
added: 2026-10-19T13:25:51Z
tags: ["property-b", "m5-ge36", "exact-counting", "small-vertices"]
---

# ≤18点唯一单色边交换计数与独立重放

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:propertyb35-paper-unique-swap`

## Metrics
完整纸面≤18点≤36边定理；五类有向边对系数50,1548,810,1320,990；两个独立位集/直接计数实现一致；m35严格余量281430，m36余量108720。

## Reasoning
yes只指这一完整小点数义务。原始输入仅添孤立点即可，不需点对覆盖、度数或补边；一般有限事件变换引理与重标号覆盖均有证明。19–25及全局目标仍未完成，未新增Lean或跨模型验收。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

