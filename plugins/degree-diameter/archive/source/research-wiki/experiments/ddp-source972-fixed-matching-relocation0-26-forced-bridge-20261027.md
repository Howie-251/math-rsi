---
type: experiment
node_id: exp:ddp-source972-fixed-matching-relocation0-26-forced-bridge-20261027
title: "(13,3)972固定0–26重定位：唯一桥825–968修首反例但仍损旧对"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/BINDING.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/ROUTE_WITNESS.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/run.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/CASES.jsonl"
added: 2026-10-27T21:29:16Z
tags: ["ddp", "method-ledger"]
---

# (13,3)972固定0–26重定位：唯一桥825–968修首反例但仍损旧对

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-matching-relocation-experiment

**目标与阶数：** (13,3)；L=972；条件性n=973（未据此计纪录）

**距目标的证据：** 1/1必要桥实测，0完整D3变体。原332-0-26-326被新332-825-968-326修复，但332到347仍>3；预测REFUTED。仅1modifiedR3/3crosspairs，继承端点0/26通过不重跑，无新R2/solver/973图。

**其他指标（保持原计数类型）：**
```json
{
  "source_n_inherited": 972,
  "source_m_inherited": 6264,
  "deleted_edge": [
    0,
    26
  ],
  "original_free_count": 108,
  "forced_bridge": [
    825,
    968
  ],
  "necessary_legal_bridges": 1,
  "bridges_tested": 1,
  "full_D3_variants": 0,
  "unattempted_bridges": 0,
  "modified_radius3_roots": 1,
  "crosspairs_checked_until_failure": 3,
  "inherited_endpoint_R3_passes_not_rerun": 2,
  "original_source_BFS": 0,
  "new_R2_balls": 0,
  "solver_runs": 0,
  "new973_graphs_generated": 0,
  "edgefiles_exported": 0,
  "route_witness": {
    "deleted_edge": [
      0,
      26
    ],
    "forced_bridge": [
      825,
      968
    ],
    "first_old_critical_route": [
      332,
      0,
      26,
      326
    ],
    "first_route_repair": [
      332,
      825,
      968,
      326
    ],
    "remaining_old_critical_route": [
      332,
      0,
      26,
      347
    ],
    "remaining_pair": [
      332,
      347
    ],
    "modified_distance_lower_bound": 4,
    "modified_exact_distance": null,
    "scope": "One complete modified radius3 traversal from332, only complete crossingcriterion needed after inheritedendpointpasses; no globalbadpaircount."
  },
  "CPU_seconds": 0.004350192000000003,
  "compile_CPU_seconds": 0,
  "baseline_date": "2026-10-27",
  "scope_not_all432": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/BINDING.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/BINDING.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/ROUTE_WITNESS.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/ROUTE_WITNESS.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/run.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_relocation/run.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/CASES.jsonl](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/CASES.jsonl)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅固定e0-26，删e加一条原108free间非边，要求旧972仍D3。full-full criticalpair332/326迫使桥825-968，因此1必要合法桥的测试完整覆盖此fixed-e任意oldfree单桥范围；不扩全部432。

**仍未完成：** Other deletedmatching edges, multiplebridges, or repair simultaneously involving a newvertex remain outside this fixed-e singlebridge scope.

**启发与重启依据：** 一个critical route会强迫连接选择，修它仍须同步保护所有中段routes。固定单桥relocation全闭后停止，不按余坏点追加桥或换e。其它改变范围须新的明确生成规则。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

