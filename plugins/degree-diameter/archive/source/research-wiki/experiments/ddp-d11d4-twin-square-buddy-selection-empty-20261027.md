---
type: experiment
node_id: exp:ddp-d11d4-twin-square-buddy-selection-empty-20261027
title: "(11,4)删旧twin＋双新点：164个完整twin-square选点全空，未生成图"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/REPORT.md; research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/PREDICTION.json; research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/STRUCTURAL_BINDING.json; research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/RESULT.json; research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/terminal.json; research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/HOST_BINDING.json"
added: 2026-10-27T21:17:06Z
tags: ["ddp", "method-ledger"]
---

# (11,4)删旧twin＋双新点：164个完整twin-square选点全空，未生成图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** structural-premise-screen

**目标与阶数：** (11,4)；L=3645；条件性n=3646（未据此计纪录）

**距目标的证据：** PREMISE_REFUTED_NO_SELECTED_V；0graph/BFS/cutcache/alloc，原保护定理未在当前源找到适用点。不是一般cooperative3646或全部delete-v无解。

**其他指标（保持原计数类型）：**
```json
{
  "source_n_inherited": 3645,
  "source_m_inherited": 20044,
  "twins_signatures_checked": 164,
  "qualifying_ordered_twins": 0,
  "actual_graphs_generated": 0,
  "BFS": 0,
  "cutgraph_cache": 0,
  "allocations_tested": 0,
  "CPU_seconds": 0.016929184,
  "old_absorption2673_repeated": false,
  "old_switch679_repeated": false,
  "conditional_cap1_pool_size": 18,
  "conditional_A_size_min": 8,
  "conditional_A_size_max": 10,
  "baseline_date": "2026-10-27",
  "source_credit": "Nishant Bhakar current3645, inherited actual source and host recovery; no sourceBFS repeated."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/PREDICTION.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/PREDICTION.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/STRUCTURAL_BINDING.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/STRUCTURAL_BINDING.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/RESULT.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/terminal.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/redundant_vertex_buddy/terminal.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/HOST_BINDING.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/HOST_BINDING.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只筛current3645的164原twins是否保留严格完整T0/T1/L0/L1 square：两侧point-neighborhood等式与两switch均须成立，按标签选首项；实际0实例，不扩其它v。

**仍未完成：** Other vertices, weaker valid proxy structures and general3646 max11/D4 constructions remain outside this exact structural selection.

**启发与重启依据：** 原几何twin关系不能穿过201插入直接继承。保留条件同长替路定理和全cap1时精确propertyB＋8..10平衡条件；重启须实际满足保护前提的点/新的结构依据，不能自动扩v或沿旧2673/679续修。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

