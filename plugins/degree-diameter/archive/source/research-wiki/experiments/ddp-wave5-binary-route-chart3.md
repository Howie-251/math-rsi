---
type: experiment
node_id: exp:ddp-wave5-binary-route-chart3
title: "F2³通用三步chart完整枚举与Fano障碍"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md; research/ddp/breadth_20261027_wave5/binary_route_chart3/best.independent_check.json; research/ddp/breadth_20261027_wave5/binary_route_chart3/best_candidate.json; research/ddp/breadth_20261027_wave5/binary_route_chart3/run.py; research/ddp/breadth_20261027_wave5/binary_route_chart3/search.cpp; research/ddp/breadth_20261027_wave5/binary_route_chart3/search_result.json; research/ddp/breadth_20261027_wave5/binary_route_chart3/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# F2³通用三步chart完整枚举与Fano障碍

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** word-rank

**目标与阶数：** (8,3)；L=253；条件性n=256（未据此计纪录）

**距目标的证据：** 197568规范输入全部失败，最好28/36；Fano商空间短证明统一排除该模型。

**其他指标（保持原计数类型）：**
```json
{
  "normalized_inputs": 197568,
  "words": 36,
  "best_rank3_words": 28,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md)；[research/ddp/breadth_20261027_wave5/binary_route_chart3/best.independent_check.json](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/best.independent_check.json)；[research/ddp/breadth_20261027_wave5/binary_route_chart3/best_candidate.json](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/best_candidate.json)；[research/ddp/breadth_20261027_wave5/binary_route_chart3/run.py](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/run.py)；[research/ddp/breadth_20261027_wave5/binary_route_chart3/search.cpp](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/search.cpp)；[research/ddp/breadth_20261027_wave5/binary_route_chart3/search_result.json](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/search_result.json)；[research/ddp/breadth_20261027_wave5/binary_route_chart3/terminal.json](../../research/ddp/breadth_20261027_wave5/binary_route_chart3/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 四个固定逆矩阵、一步一个binary参数、全部36约化三词单route满秩

**正向保证：** 规范空间完备；保存候选36词以全部8参数赋值独立校准

**仍未完成：** 不排多route、edge-local matrices或一般(8,3)图。

**启发与重启依据：** 要改变通用单route要求，而非换此空间seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

