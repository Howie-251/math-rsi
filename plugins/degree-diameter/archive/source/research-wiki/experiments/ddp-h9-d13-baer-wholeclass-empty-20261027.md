---
type: experiment
node_id: exp:ddp-h9-d13-baer-wholeclass-empty-20261027
title: "(13,5)Baer whole-class迁移：8467200项card预算排空"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/RESULT.json"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# (13,5)Baer whole-class迁移：8467200项card预算排空

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (13,5)；L=51417；条件性n=51418（未据此计纪录）

**距目标的证据：** 7560个Baer13形状×1120个F3-defined平面完整一次检查，1740次whole-class closure全部pins有度数余量，但card21/22/26分别814/158/768，均超过13；合法池0，事前存在预测被反驳。CPU0.98348703，0BFS/R4/anchors。

**其他指标（保持原计数类型）：**
```json
{
  "placements": 8467200,
  "allpins_degree_legal_occurrences": 1740,
  "card_histogram": {
    "21": 814,
    "22": 158,
    "26": 768
  },
  "feasible_pinsets": 0,
  "CPU_seconds": 0.98348703,
  "prediction_verdict": "REFUTED",
  "BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All7560 Baer13 coefficient sets in1120 saved F3-defined planes, whole currentFrobenius-class closure, on actual51417 source only.

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 停止这个固定source/whole-class规则，不因有1740项degree通过而继续不可装入13的邻域。转其它参数；非F3-defined平面、其它blocking规则未排。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

