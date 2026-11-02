---
type: experiment
node_id: exp:ddp-source972-single-matching-edge-release432-no-safe-20261027
title: "(13,3)972全部432单matching删边：端点R3全过，中段旧对全部损坏"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/CASES.jsonl; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/FIRST_ROUTE_WITNESS.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/probe.cpp; research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/run.py"
added: 2026-10-27T21:24:39Z
tags: ["ddp", "method-ledger"]
---

# (13,3)972全部432单matching删边：端点R3全过，中段旧对全部损坏

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-edge-release-screen

**目标与阶数：** (13,3)；L=972；条件性n=973（未据此计纪录）

**距目标的证据：** 432/432完整、0safe/未试/UNKNOWN；864endpointR3全部通过，但432条均middle-crosspair失败。事前safe-edge预测REFUTED；0新增110pin R2/solver阶段。

**其他指标（保持原计数类型）：**
```json
{
  "source_n_inherited": 972,
  "source_m_inherited": 6264,
  "matching_edges_scope": 432,
  "modified_singledelete_settings_checked": 432,
  "safe_settings": 0,
  "endpoint_u_failures": 0,
  "endpoint_v_failures": 0,
  "endpoint_R3_complete_passes": 864,
  "middle_crosspair_failures": 432,
  "modified_radius3_searches": 1918,
  "crosspairs_checked_until_firstfailure": 8768,
  "source_original_BFS": 0,
  "new973_graphs_generated": 0,
  "edgefiles_exported": 0,
  "new110pin_R2_rebuilt": false,
  "new_solver_runs": 0,
  "unattempted": 0,
  "UNKNOWN": 0,
  "first_route_witness": {
    "deleted_edge": [
      0,
      26
    ],
    "old_geodesic": [
      332,
      0,
      26,
      326
    ],
    "old_path_length": 3,
    "modified_distance_lower_bound": 4,
    "modified_exact_distance": null,
    "reason": "The recorded modified root radius3 traversal excludes the target. This is not a wholegraph badpair count or exact modified diameter."
  },
  "native_CPU_seconds": 0.019954,
  "compile_CPU_seconds": 0.7318100369999999,
  "total_batch_CPU_seconds": 0.753940094,
  "baseline_date": "2026-10-27",
  "source_credit": "Already bound current972 author literal; source D3 inherited. No old fullsourceBFS."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/CASES.jsonl](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/CASES.jsonl)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/FIRST_ROUTE_WITNESS.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/FIRST_ROUTE_WITNESS.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/probe.cpp](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/probe.cpp)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/run.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/matching_edge_release/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定actual972源每27块12matching共432条，分别只删1条并完整判H D3：u/v全部目标R3，加Nu\v×Nv\u的中段crosspairs。只隐式singledelete，不生成973图、不重源验收。

**仍未完成：** Unsafe-edge deletion plus simultaneous repair, multiplecuts and general973degree13D3 graphs remain outside this safe-first scope.

**启发与重启依据：** 端点新出口覆盖不足以保护全部旧路。每条matching至少承载一条不可替代的三步中段路线，故安全单边释放入口已闭，不按少坏对修或加第二cut；unsafe-delete再新点修复等属其它未测操作。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

