---
type: experiment
node_id: exp:ddp-rajiv5334-central-c3-obstruction-20261027
title: "Rajiv5334双层为何刚够：固定2667基图只有两条短路线，三层提升不可能"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/PLAN.json; research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/OBSTRUCTION.json; research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/MULTIPLICITY.json; research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/RESULT.json; research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/analyze.py"
added: 2026-10-27T15:32:28Z
tags: ["ddp", "method-ledger"]
---

# Rajiv5334双层为何刚够：固定2667基图只有两条短路线，三层提升不可能

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** necessary-route-capacity-model-no-final-graph

**目标与阶数：** (8,5)；L=5334；条件性n=8001（未据此计纪录）

**距目标的证据：** 22409约化词完整检查；8个端点仅2种模3计数向量。首端点(phase1,x48)甚至仅baC和CdB两条≤5路线；任意中央连接只能到两个sheet，不能覆盖3层。原C2奇偶[0,0,1,1]恰分别给1/0，解释源双层为何够。0个连接赋值运行、0图、0BFS，CPU0.084秒。

**其他指标（保持原计数类型）：**
```json
{
  "reduced_words": 22409,
  "witness_phase": 1,
  "witness_x": 48,
  "witness_words": [
    "baC",
    "CdB"
  ],
  "integer_signedcounts": [
    [
      -1,
      -1,
      1,
      0
    ],
    [
      0,
      1,
      1,
      -1
    ]
  ],
  "old_source_parity": [
    0,
    0,
    1,
    1
  ],
  "source_two_layer_witness_values": [
    1,
    0
  ],
  "ordinary_cover_max_sheets": 2,
  "assignments_executed": 0,
  "source_BFS": 0,
  "new_BFS": 0,
  "CPU_seconds": 0.083968252,
  "prediction_supported": true,
  "new_graphs_generated": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/PLAN.json](../../research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/PLAN.json)；[research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/OBSTRUCTION.json](../../research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/OBSTRUCTION.json)；[research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/MULTIPLICITY.json](../../research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/MULTIPLICITY.json)；[research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/analyze.py](../../research/ddp/more_graphs_20261027/d8_rajiv5334_central_transfer/analyze.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** FixedC21semidirectF127base,r25,positivephases2/3/6/8andtranslations60/122/81/42;all<=5reducedwords. DirectcentralC3 arbitraryfourvoltages excluded by witness before81assignmenttests. Furtherordinarycovercorollary requires actual two-base-walk count, notjustcountvectors.

**正向保证：** Exactorder25mod127is21;theprojectionispreciselytheexisting5334source quotient.；All22409reducedwords<=5areenumerated;theliteralwitnesshasexactlytwobasewalks.；Coveringmapsliftanybasewalkuniquely,soanyk-sheetordinarycoverwithk>2hasatmosttwoaccessibleverticesinthiswitnessfiber.

**仍未完成：** 未排除其它素域、群作用、相位或非普通提升，也未取得新的(8,5)纪录。

**启发与重启依据：** 不运行已被完整短路见证排除的81赋值，不扩中央层数或seed。固定基图只有两条短路还直接阻止任意>2-sheet普通graphcover；若继续原源机制须有效改变基图/路线，不是改centralvoltages。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

