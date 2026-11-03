---
type: experiment
node_id: exp:ddp-wave4-equitable-global
title: "H9单锚点equitable全局cell MILP"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave4/equitable_global/REPORT.md; research/ddp/breadth_20261027_wave4/equitable_global/partition.json; research/ddp/breadth_20261027_wave4/equitable_global/partition_summary.json; research/ddp/breadth_20261027_wave4/equitable_global/terminal.json; research/ddp/breadth_20261027_wave4/equitable_global/worker_result.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# H9单锚点equitable全局cell MILP

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** solver-UNKNOWN

**目标与阶数：** (12,5)；L=42342；条件性n=42343（未据此计纪录）

**距目标的证据：** 一次MILP无incumbent，UNKNOWN；未生成大图。

**其他指标（保持原计数类型）：**
```json
{
  "variables": 1312,
  "constraint_rows": 2613,
  "generic_cells": 650,
  "H3_cells": 12,
  "incumbent_returned": false,
  "solver_status": "UNKNOWN"
}
```





**原始证据：** [research/ddp/breadth_20261027_wave4/equitable_global/REPORT.md](../../research/ddp/breadth_20261027_wave4/equitable_global/REPORT.md)；[research/ddp/breadth_20261027_wave4/equitable_global/partition.json](../../research/ddp/breadth_20261027_wave4/equitable_global/partition.json)；[research/ddp/breadth_20261027_wave4/equitable_global/partition_summary.json](../../research/ddp/breadth_20261027_wave4/equitable_global/partition_summary.json)；[research/ddp/breadth_20261027_wave4/equitable_global/terminal.json](../../research/ddp/breadth_20261027_wave4/equitable_global/terminal.json)；[research/ddp/breadth_20261027_wave4/equitable_global/worker_result.json](../../research/ddp/breadth_20261027_wave4/equitable_global/worker_result.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 一个几何绝对点anchor，650genericcells/12H3cells，全部cell常值；无固定域外

**正向保证：** 33397点逐项检查equitable；非从作者S局部改进模型

**仍未完成：** cell常值是实际限制；无不可行证明。

**启发与重启依据：** 须新的结构/单独授权有限profile，不能写全逐fiber排除。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

