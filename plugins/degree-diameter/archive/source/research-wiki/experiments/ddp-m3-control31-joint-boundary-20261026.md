---
type: experiment
node_id: exp:ddp-m3-control31-joint-boundary-20261026
title: "31点控制图共同端口瓶颈与有界联合SAT"
idea_id: "idea:ddp-m3-affine-line-cover"
verdict: no
confidence: medium
date: "2026-10-26"
hardware: "single CPU"
duration: "diagnosis about12CPU s; SAT0.02474CPU s"
provenance: "research/ddp/refresh_20261029/controller31_chain_full/EDGE_VARIABLES.json; research/ddp/refresh_20261029/controller31_chain_full/HANDLE.json; research/ddp/refresh_20261029/controller31_chain_full/LABEL_SCOPE.md; research/ddp/refresh_20261029/controller31_chain_full/MODEL.json; research/ddp/refresh_20261029/controller31_chain_full/MODEL_CODE.md; research/ddp/refresh_20261029/controller31_chain_full/PREDICTION.md; research/ddp/refresh_20261029/controller31_chain_full/RESULT.json; research/ddp/refresh_20261029/controller31_chain_full/TERMINAL.json; research/ddp/refresh_20261029/controller31_chain_full/run_once.py; research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json; research/ddp/refresh_20261029/CAPACITY_AND_CORE_SWAP_TURN.md; research/ddp/refresh_20261029/CAPACITY_CORE_SWAP_FINAL_WIKI_REPORT.md; research/ddp/m3_control31_diagnosis/REPORT.md; research/ddp/m3_control31_diagnosis/joint_boundary_sat.terminal.json"
added: 2026-10-29T22:36:54Z
tags: ["ddp", "local-diagnosis", "unproved-unsat", "method-ledger"]
---

# 31点控制图共同端口瓶颈与有界联合SAT

**verdict:** `no`  ·  **confidence:** `medium`  ·  tests `idea:ddp-m3-affine-line-cover`

## Metrics
**对象层级：** controller

**目标与阶数：** (4,3)；L=不适用／见变体；controller n=31；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': 837, 'graph_generated': False}

**距目标的证据：** 原图两无序缺孔。2885单交换严格恶化；单侧90/113400端口分配均不改善。88位置16变量边、46固定边、所有961有序对A³>0的联合模型：7326变量23052子句，一次CaDiCaL exit20，result file UNSATISFIABLE。；20261029完整380外边模型21722变量/74336子句，child90.006668CPU、准备0.122005083CPU、总90.148101772CPU，唯一-t90 UNKNOWN，0控制器/0个3875图。

**其他指标（保持原计数类型）：**
```json
{
  "full_chain_external_variables": 380,
  "full_chain_fixed_motif_edges": 33,
  "old_boundary_fixed_edges": 46,
  "full_chain_CNF_variables": 21722,
  "full_chain_CNF_clauses": 74336,
  "full_chain_solver_status": "UNKNOWN",
  "full_chain_solver_calls": 1,
  "full_chain_solver_CPU_seconds": 90.00666799999999,
  "full_chain_total_CPU_seconds": 90.148101772,
  "valid_controllers": 0,
  "complete3875_graphs": 0,
  "general31_family_excluded": false,
  "old_raw_UNSAT_certified": false,
  "intended_final_target": {
    "Delta": 12,
    "D": 3,
    "savedL": 810,
    "n_if_full_lift_valid": 837,
    "graph_generated": false
  }
}
```

**既有原文指标：** 原图两无序缺孔。2885单交换严格恶化；单侧90/113400端口分配均不改善。88位置16变量边、46固定边、所有961有序对A³>0的联合模型：7326变量23052子句，一次CaDiCaL exit20，result file UNSATISFIABLE。；20261029完整380外边模型21722变量/74336子句，child90.006668CPU、准备0.122005083CPU、总90.148101772CPU，唯一-t90 UNKNOWN，0控制器/0个3875图。

**从属变体：**
```json
[
  {
    "label": "same_overlap_chain_motif_full380_external_edge_model_F5_20261029",
    "status": "UNKNOWN_TERMINAL",
    "controller_order": 31,
    "source_literal": "research/ddp/second_mechanism/control_unrestricted_n31.edges",
    "inherited_source_A3_missing_ordered": 4,
    "interpretation": "Same overlapping-triangle controller mechanism; old88-position fixed46-edge model remains a smaller historical raw-UNSAT scope.",
    "motif": "Seven-vertex three-triangle chain plus eight disjoint K3 blocks.",
    "motif_fixed_edges": 33,
    "old_fixed_edges": 46,
    "released_old_fixed_edges": 13,
    "full_legal_external_edge_variables": 380,
    "selected_external_edges": 29,
    "expected_controller_edges": 62,
    "all_variables": 21722,
    "clauses": 74336,
    "route_condition": "adjacency or exact3walk for every distinct pair; fixed triangles give self NB3",
    "labeling": "Only eight additional K3 blocks use first-discovery parent labels; initial seven motif labels fixed.",
    "C33_triangle_factor_capacity_cuts_imported": false,
    "intended_F5_target": {
      "Delta": 20,
      "D": 3,
      "conditional_order": 3875,
      "graph_generated": false
    },
    "solver_calls": 1,
    "solver_option": "-t90",
    "solver_CPU_seconds": 90.00666799999999,
    "preparation_CPU_seconds": 0.12200508300000001,
    "aggregate_CPU_seconds": 90.148101772,
    "aggregate_CPU_budget": 110,
    "running": false,
    "valid_controllers": 0,
    "complete3875_graphs": 0,
    "old_timer_continued": false,
    "general31_family_excluded": false,
    "old88_raw_UNSAT_promoted_to_certificate": false,
    "order_or_seed_ladder_continuation": false
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/controller31_chain_full/EDGE_VARIABLES.json](../../research/ddp/refresh_20261029/controller31_chain_full/EDGE_VARIABLES.json)；[research/ddp/refresh_20261029/controller31_chain_full/HANDLE.json](../../research/ddp/refresh_20261029/controller31_chain_full/HANDLE.json)；[research/ddp/refresh_20261029/controller31_chain_full/LABEL_SCOPE.md](../../research/ddp/refresh_20261029/controller31_chain_full/LABEL_SCOPE.md)；[research/ddp/refresh_20261029/controller31_chain_full/MODEL.json](../../research/ddp/refresh_20261029/controller31_chain_full/MODEL.json)；[research/ddp/refresh_20261029/controller31_chain_full/MODEL_CODE.md](../../research/ddp/refresh_20261029/controller31_chain_full/MODEL_CODE.md)；[research/ddp/refresh_20261029/controller31_chain_full/PREDICTION.md](../../research/ddp/refresh_20261029/controller31_chain_full/PREDICTION.md)；[research/ddp/refresh_20261029/controller31_chain_full/RESULT.json](../../research/ddp/refresh_20261029/controller31_chain_full/RESULT.json)；[research/ddp/refresh_20261029/controller31_chain_full/TERMINAL.json](../../research/ddp/refresh_20261029/controller31_chain_full/TERMINAL.json)；[research/ddp/refresh_20261029/controller31_chain_full/run_once.py](../../research/ddp/refresh_20261029/controller31_chain_full/run_once.py)；[research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json](../../research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json)；[research/ddp/refresh_20261029/CAPACITY_AND_CORE_SWAP_TURN.md](../../research/ddp/refresh_20261029/CAPACITY_AND_CORE_SWAP_TURN.md)；[research/ddp/refresh_20261029/CAPACITY_CORE_SWAP_FINAL_WIKI_REPORT.md](../../research/ddp/refresh_20261029/CAPACITY_CORE_SWAP_FINAL_WIKI_REPORT.md)；[research/ddp/m3_control31_diagnosis/REPORT.md](../../research/ddp/m3_control31_diagnosis/REPORT.md)；[research/ddp/m3_control31_diagnosis/joint_boundary_sat.terminal.json](../../research/ddp/m3_control31_diagnosis/joint_boundary_sat.terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 历史88位置、46固定边联合模型的rawUNSAT仅限旧局部域且未认证。本轮保留同一7点三三角链+8K3 motif但只固定33内边，释放13旧固定外边，允许全部380合法外边；21722变量/74336子句单次90秒UNKNOWN，不排此更大域或一般31控制器。

**仍未完成：** 原88局部rawUNSAT不外推新380域；新更大完整域UNKNOWN，F5条件目标3875未生成。旧F3条件目标837仍仅历史，不与新F5混算。

**启发与重启依据：** 新模型实际改变旧固定46边的承重路由，满足历史重启条件；但单次90秒仍UNKNOWN，停止本批，不延长timer或恢复旧交换，不开31/32阶数梯子。重叠motif不是C33不交三角因子，不移植其局部容量cuts。

**单独的重启条件：** Further work requires a concrete new shared-route or variable-representation rule; no authorized restart of this timer or an order/seed ladder.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

