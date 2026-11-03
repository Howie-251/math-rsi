---
type: experiment
node_id: exp:ddp-h9-d13-redei702-pool-empty-20261027
title: "(13,5)稳定Rédei迁移：786240项degree合法池为空"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/redei_pool/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/redei_pool/RESULT.json"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# (13,5)稳定Rédei迁移：786240项degree合法池为空

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (13,5)；L=51417；条件性n=51418（未据此计纪录）

**距目标的证据：** 现成702轨道×1120planes完整检查，raw degree合法0、不同pinset0；至少一项合法预测被反驳。没有BFS/anchor/新图。364个F3点中仍108个free，失败不能归因为所有F3点满度。

**其他指标（保持原计数类型）：**
```json
{
  "placements": 786240,
  "distinct_feasible_pinsets": 0,
  "prediction_verdict": "REFUTED",
  "CPU_seconds": 0.210511479,
  "BFS": 0,
  "anchor_tests": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/redei_pool/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/redei_pool/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/redei_pool/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/redei_pool/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only702 F3-projectivity Rédei15 shapes ×1120 saved F3-defined singular planes on current51417 source.

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 停止同一固定池；下一规则改非稳定Baer13或whole-class closure以避开固定五个F3点的分布，先绑定映射。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

