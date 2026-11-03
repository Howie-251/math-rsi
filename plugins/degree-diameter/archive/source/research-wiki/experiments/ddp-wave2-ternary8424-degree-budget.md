---
type: experiment
node_id: exp:ddp-wave2-ternary8424-degree-budget
title: "固定104×81三邻点degree预算提升"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/REPORT.md; research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/RESULT.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 固定104×81三邻点degree预算提升

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (12,4)；L=5832；条件性n=8424（未据此计纪录）

**距目标的证据：** 全部208控制边被迫branch3，内部余量0；0→32唯一三路仅27<81。

**其他指标（保持原计数类型）：**
```json
{
  "forced_edges": 208,
  "unique_distance4_ordered_slots": 2208,
  "capacity": 27,
  "required_states": 81,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/REPORT.md](../../research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/REPORT.md)；[research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/RESULT.json](../../research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定104、branch cap3、Δ12；允许内部预算但独占四路迫使全边branch3

**正向保证：** 2208个unique-distance4有序槽用于强迫预算；另有真实无四walk的三路见证

**仍未完成：** 不排更高branch/不同控制器/任意lift。

**启发与重启依据：** 须改变degree/路径机制，不能仅换域赋值。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

