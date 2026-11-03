---
type: experiment
node_id: exp:ddp-h9-redei15-fixed-pool-20261027
title: "Rédei15固定702×1120池：N12有85项，N11为空"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_redei15/pool/REPORT.md; research/ddp/more_graphs_20261027/h9_redei15/pool/RESULT.json"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# Rédei15固定702×1120池：N12有85项，N11为空

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (12,5)；L=42342

**距目标的证据：** 786240个placement一次完成，N12得到85个不同degree合法邻域，N11得到0。未在此阶段算R4或anchors。

**其他指标（保持原计数类型）：**
```json
{
  "orbit": 702,
  "planes": 1120,
  "placements": 786240,
  "pool12": 85,
  "pool11": 0,
  "CPU_seconds": 0.209619
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_redei15/pool/REPORT.md](../../research/ddp/more_graphs_20261027/h9_redei15/pool/REPORT.md)；[research/ddp/more_graphs_20261027/h9_redei15/pool/RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/pool/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed PGL3(F3) orbit and1120 F3-defined singular planes on actual42398/37631 bases only.

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** N12存在可执行的覆盖对象，立即交生产；N11同一degree池空则停止。仅702个F3射影轨道，不外推全部F9变换。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

