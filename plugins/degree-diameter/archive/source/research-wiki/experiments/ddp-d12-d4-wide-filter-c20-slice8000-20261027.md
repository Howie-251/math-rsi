---
type: experiment
node_id: exp:ddp-d12-d4-wide-filter-c20-slice8000-20261027
title: "C20零三角切片8000项宽证书失败：不等于8000图不存在"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/REPORT.md; research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/RESULT.json; research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/zero_triangle_wide20/PREDICTION.json; research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/zero_triangle_wide20/RESULT.json"
added: 2026-10-27T18:32:57Z
tags: ["ddp", "method-ledger"]
---

# C20零三角切片8000项宽证书失败：不等于8000图不存在

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (12,4)；L=6156；条件性n=6480（未据此计纪录）

**距目标的证据：** 固定va=(0,x,y,0),vb=(z,0,0,1)，x,y,z∈C20，8000项全未通过有旧pencil引理依据的I∪R2∪100G4充分证书；其中7220 simple-controller、780 nonsimple全保留。全部在base0已失败，0图/BFS。

**其他指标（保持原计数类型）：**
```json
{
  "assignments": 8000,
  "simple_controllers": 7220,
  "nonsimple_controllers": 780,
  "certificate_passers": 0,
  "native_CPU": 0.006084,
  "total_CPU": 1.33422,
  "BFS": 0,
  "graphs": 0,
  "actual_lift_nonexistence_proved": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/REPORT.md](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/REPORT.md)；[research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/RESULT.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/RESULT.json)；[research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/zero_triangle_wide20/PREDICTION.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/zero_triangle_wide20/PREDICTION.json)；[research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/zero_triangle_wide20/RESULT.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/zero_triangle_wide20/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定va=(0,x,y,0),vb=(z,0,0,1)，x,y,z∈C20，8000项全未通过有旧pencil引理依据的I∪R2∪100G4充分证书；其中7220 simple-controller、780 nonsimple全保留。全部在base0已失败，0图/BFS。

**仍未完成：** This finite result does not resolve generalgraph construction or completeLean.

**启发与重启依据：** 这关闭的是充分certificate切片，不是全部actualD4 lift；不满秩路径的并仍可能补齐，所以不能把旧strict与新wide负结果当数学整族排除。原字面mod20另有actual x0缺3708的独立诊断，只有那个字面真正被refuted。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

