---
type: experiment
node_id: exp:ddp-wave3-binary-branch364
title: "364核binary branching必要matching MILP"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/binary_branch364/source.edges; research/ddp/breadth_20261027_wave3/binary_branch364/source_distances.json; research/ddp/breadth_20261027_wave3/binary_branch364/source_profile.json; research/ddp/breadth_20261027_wave3/binary_branch364/terminal.json; research/ddp/breadth_20261027_wave3/binary_branch364/unique5_paths.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 364核binary branching必要matching MILP

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** solver-UNKNOWN

**目标与阶数：** (5,5)；L=650；条件性n=728（未据此计纪录）

**距目标的证据：** 25秒求解无incumbent、无不可行证明，UNKNOWN；未生成728图。

**其他指标（保持原计数类型）：**
```json
{
  "unique_path_constraints": 34860,
  "solver_status": "UNKNOWN",
  "incumbent_returned": false,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/binary_branch364/source.edges](../../research/ddp/breadth_20261027_wave3/binary_branch364/source.edges)；[research/ddp/breadth_20261027_wave3/binary_branch364/source_distances.json](../../research/ddp/breadth_20261027_wave3/binary_branch364/source_distances.json)；[research/ddp/breadth_20261027_wave3/binary_branch364/source_profile.json](../../research/ddp/breadth_20261027_wave3/binary_branch364/source_profile.json)；[research/ddp/breadth_20261027_wave3/binary_branch364/terminal.json](../../research/ddp/breadth_20261027_wave3/binary_branch364/terminal.json)；[research/ddp/breadth_20261027_wave3/binary_branch364/unique5_paths.json](../../research/ddp/breadth_20261027_wave3/binary_branch364/unique5_paths.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定364核；edge关系bijection或K2,2，必要matching必须击中全部unique5 geodesics

**正向保证：** 固定源D5及34860唯一路义务已准备

**仍未完成：** 必要matching尚未解决；即使通过仍非全图D5证书。

**启发与重启依据：** 需新结构/明确有限授权，不能把UNKNOWN当UNSAT。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

