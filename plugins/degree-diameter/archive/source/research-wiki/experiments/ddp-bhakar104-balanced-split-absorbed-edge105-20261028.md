---
type: experiment
node_id: exp:ddp-bhakar104-balanced-split-absorbed-edge105-20261028
title: "Bhakar104c split+absorbed edge:119808批全拒，端口诊断及继承退化闭全部合法操作"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/RESULT.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/REPORT.md; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/INPUT.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/WORKER_RESULT.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/TERMINAL.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/LIVE_HANDLE.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CASES.csv; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CHILD_GATE_CALIBRATION.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CALIBRATION105.edges; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.md; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SOURCE_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SOURCE_SCOPE.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SKIP_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SKIP_SCOPE.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/production.cpp; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/run.py; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ENDPOINT_RELEASE_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/endpoint_release_diagnostic.py; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SCOUT_GENERAL_SCOPE_CLOSURE.md; research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SCOUT_GENERAL_SCOPE_CLOSURE.json; research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md"
added: 2026-10-28T04:18:25Z
tags: ["ddp", "method-ledger"]
---

# Bhakar104c split+absorbed edge:119808批全拒，端口诊断及继承退化闭全部合法操作

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** one-family-complete-finite-surgery-experiment

**目标与阶数：** (4,4)；L=104；条件性n=105（未据此计纪录）

**距目标的证据：** 原批119808全访/0childpass；1张105/210校准仅两childR4，逐点miss集合匹配，fullD/badpairs未算。312split后诊断216双端点cover集合空、96单空、0双非空，故端点单侧覆盖已阻断而非无旧边兼容。general scope为纸面继承分类，0新退化图/BFS。

**其他指标（保持原计数类型）：**
```json
{
  "original_frozen_batch_counts_unchanged": {
    "canonical_objects": 119808,
    "skip_old40740_switch": 12,
    "skip_old230_after_first_skip": 0,
    "exact_twochild_reject": 119796,
    "child_pass": 0,
    "actual_expanded_graphs": 1,
    "actual_R4_roots": 2,
    "affected_old_roots": 0,
    "source_BFS": 0,
    "source_path_classification": 0,
    "solver_calls": 0,
    "new_lower_bound_graphs": 0
  },
  "original_batch_aggregate_CPU_seconds": 1.6428370309999996,
  "original_worker_CPU_seconds": 0.100038,
  "original_compile_CPU_seconds": 1.53756,
  "endpoint_diagnostic": {
    "canonical_splits": 312,
    "eligible_endpoints_per_split": 99,
    "mask_tests": 61776,
    "categories": {
      "BOTH_SIDES_EMPTY": 216,
      "A_ONLY_EMPTY": 64,
      "B_ONLY_EMPTY": 32,
      "BOTH_NONEMPTY_NO_SOURCE_EDGE": 0,
      "BOTH_NONEMPTY_WITH_SOURCE_EDGE": 0
    },
    "both_nonempty": 0,
    "CPU_seconds": 0.033021218,
    "candidate_graphs": 0,
    "BFS": 0,
    "original119808_replayed": 0
  },
  "general_scope_count_derivation": {
    "per_vertex_partitions": 3,
    "source_vertices": 104,
    "source_edges": 208,
    "non_v_incident_edges": 204,
    "raw_orientations_per_cut": 2,
    "raw_non_v_incident_tuples": 127296,
    "edges_outside_closed_neighborhood_per_v": 192,
    "outside_tuples": 119808,
    "non_v_edges_touching_Nv_per_v": 12,
    "proof_of_12": "Each of four neighbors has three edges away from v. No two source neighbors are adjacent because there are no triangles, so these are12 distinct edges, each with exactly one endpoint inN(v).",
    "per_partition_neighbor_touching_orientations": 24,
    "per_partition_legal_degenerate_orientations": 12,
    "per_partition_illegal_orientations": 12,
    "legal_degenerate_tuples": 3744,
    "illegal_tuples": 3744,
    "total_legal_parameter_tuples": 123552,
    "counts_role": "Parameter tuples in a canonical unordered2+2 split; not claimed distinct or nonisomorphic graphs."
  },
  "inherited_old_two_edge_absorption": {
    "id": "ddp-wave2-extension105-d4",
    "report": "research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md",
    "complete_legal_two_disjoint_edge_absorptions": 20904,
    "all_failed_D4": true
  },
  "general_scope_new_enumerations": 0,
  "general_scope_new_graphs": 0,
  "general_scope_new_BFS": 0,
  "new_lower_bound_mathematically_verified": false,
  "method_count_note": "One source-surgery family with source/diagnostic/deductive variants, not independent methods."
}
```



**从属变体：**
```json
[
  {
    "label": "finite_surgery_family",
    "n": {
      "actual": null,
      "hypothetical": 105
    },
    "actual_D": null,
    "planned": 119808,
    "visited": 119808,
    "unvisited": 0,
    "inherited_known_negative_skips": 12,
    "exact_childgate_reject": 119796,
    "childgate_pass": 0,
    "new_lower_bound_graphs": 0
  },
  {
    "label": "first_literal_exact_childgate_calibration",
    "n": {
      "actual": 105,
      "hypothetical": null
    },
    "m": 210,
    "actual_graph_Delta": 4,
    "regular_degree": 4,
    "simple": true,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "actual_R4_roots": 2,
    "u_missing_targets": [
      11,
      13,
      21,
      23,
      73,
      95
    ],
    "w_missing_targets": [
      10,
      20,
      22,
      45,
      54,
      63,
      65,
      89
    ],
    "exact_cache_match": true,
    "graph_path": "research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CALIBRATION105.edges"
  },
  {
    "label": "endpoint_coverer_diagnostic",
    "status": "COMPLETE_SOURCE_METRIC_ENDPOINT_RELEASE_DIAGNOSTIC",
    "canonical_splits": 312,
    "categories": {
      "BOTH_SIDES_EMPTY": 216,
      "A_ONLY_EMPTY": 64,
      "B_ONLY_EMPTY": 32,
      "BOTH_NONEMPTY_NO_SOURCE_EDGE": 0,
      "BOTH_NONEMPTY_WITH_SOURCE_EDGE": 0
    },
    "CPU_seconds": 0.033021218,
    "new_candidate_graphs": 0,
    "BFS": 0,
    "old_batch_replayed": 0
  },
  {
    "label": "general_legal_endpoint_scope_closure",
    "status": "FULL_FIXED_SOURCE_OPERATION_CLOSED_BY_NEW_BATCH_AND_INHERITANCE",
    "legal_parameters": 123552,
    "new_batch_parameters_inherited": 119808,
    "legal_degenerate_parameters_inherited": 3744,
    "illegal_parameters": 3744,
    "new_numeric_parameter_tests": 0,
    "new_graphs": 0,
    "BFS": 0
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/REPORT.md](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/REPORT.md)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/INPUT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/INPUT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/WORKER_RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/WORKER_RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/TERMINAL.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/TERMINAL.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/LIVE_HANDLE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/LIVE_HANDLE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CASES.csv](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CASES.csv)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CHILD_GATE_CALIBRATION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CHILD_GATE_CALIBRATION.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CALIBRATION105.edges](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/CALIBRATION105.edges)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SOURCE_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SOURCE_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SOURCE_SCOPE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SOURCE_SCOPE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SKIP_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SKIP_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SKIP_SCOPE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SKIP_SCOPE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/production.cpp](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/production.cpp)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/run.py](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/run.py)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ENDPOINT_RELEASE_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/ENDPOINT_RELEASE_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/endpoint_release_diagnostic.py](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/endpoint_release_diagnostic.py)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SCOUT_GENERAL_SCOPE_CLOSURE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SCOUT_GENERAL_SCOPE_CLOSURE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SCOUT_GENERAL_SCOPE_CLOSURE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_bhakar104_split_edge105/SCOUT_GENERAL_SCOPE_CLOSURE.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md](../../research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定triangle-free104c/208/all4regular已验D4源；平衡2+2拆成相邻children，再吸收一条有向旧边xy。119808 outsideN[v]原批保持119796 exactgate拒+12旧同标签switch继承；后续仅源缓存诊断；其余3744合法退化参数归入旧20904双边吸收排除，全部合法123552参数闭，另3744非法，不称不同图数。

**正向保证：** All legal surgery objects are simple four-regular105/210 by edge and degree conservation.；The source metric criterion is exact for simultaneous two-child R4 coverage.；First literal child missed sets match the exact cache criterion point for point.；Only affected old roots in (B2_G(v) union B1_G({x,y})) minus{v} would be needed after a child-gate pass; no object reached this stage.

**仍未完成：** 其它104源、非平衡split、多cut/其它增边与一般105/max4/D4图均未排。

**启发与重启依据：** 保留原计数与1.642837031CPU；后续diagnostic.033021218CPU只查312个source-metric coverers，不重119808。停止同固定源整条合法split+oneedge操作，不能通过换端点域重跑；新源或实质改变连接规则另行判断，不追坏对分数。

**单独的重启条件：** Only a substantively different coverage rule or source; no continuation of this exact finite family.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

