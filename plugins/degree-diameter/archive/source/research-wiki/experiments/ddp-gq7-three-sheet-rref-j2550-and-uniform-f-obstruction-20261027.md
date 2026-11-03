---
type: experiment
node_id: exp:ddp-gq7-three-sheet-rref-j2550-and-uniform-f-obstruction-20261027
title: "(10,4)2550-point geometric C3 lift with J matching: exactD5 and uniform-f obstruction"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/PREDICTION.json; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RESULT.json; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/REPORT.md; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/construct.cpp; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/run.py; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/GEOMETRY.json; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/FIRST_PAIR_ROUTE_DIAGNOSIS.json; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/ANALYSIS_RESULT.json; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RREF_J_UNIFORM_F_CLOSURE.md; research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RREF_J_THEORY_FIELDS.json"
added: 2026-10-27T22:43:55Z
tags: ["ddp", "method-ledger"]
---

# (10,4)2550-point geometric C3 lift with J matching: exactD5 and uniform-f obstruction

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (10,4)；L=2485；candidate_graph_or_family n=2550

**距目标的证据：** 实际D=5，目标D=4；Actual2550/12750/simple10regular; root6 R4 misses70, first171; universal upper5 establishes exact globalD5. Predicted9800 fully repaired unordered base point pairs supported, fullD4 refuted. At p=(0,0,1,1),r=e0 all8 norm geodesics havephase2; arbitrary uniform f yields at most2 phases.

**其他指标（保持原计数类型）：**
```json
{
  "n": 2550,
  "m": 12750,
  "Delta": 10,
  "simple": true,
  "undirected": true,
  "regular": true,
  "roots_checked": 7,
  "first_failure_root": 6,
  "first_R4_missing_target": 171,
  "R4_missing_target_count": 70,
  "layer_counts": [
    1,
    10,
    81,
    638,
    1750
  ],
  "global_diameter": 5,
  "diameter_basis": "fixed_line_fibre_and_twins_universal_upper5; actual_R4_lower_or_allroots_upper4",
  "J_repaired_opposite_point_pairs_unordered": 9800,
  "native_CPU_seconds": 0.016329,
  "status": "SOLE_CANDIDATE_EXACT_D5_NO_NEW_BOUND",
  "new_lower_bound": false,
  "compilation_CPU_seconds": 1.285614,
  "tracked_batch_CPU_seconds": 1.303726,
  "all_requested_candidate_count": 1,
  "published_source_BFS_roots": 0,
  "first_failure_coordinate_pair": [
    [
      0,
      0,
      1,
      1
    ],
    [
      1,
      0,
      0,
      0
    ]
  ],
  "first_pair_geodesic_phase_histogram": [
    0,
    0,
    8
  ],
  "ordinary_bad_pair_count_measured": false,
  "uniform_f_family_closed": true,
  "new_lower_bounds": 0,
  "new_all_source_BFS_calls": 0,
  "independent_negative_graph_BFS": 0,
  "prediction": "STRUCTURAL_REPAIR_SUPPORTED; COMPLETE_D4_REFUTED",
  "partial_theory_is_not_goal_completion": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/PREDICTION.json](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/PREDICTION.json)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RESULT.json](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RESULT.json)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/REPORT.md](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/REPORT.md)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/construct.cpp](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/construct.cpp)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/run.py](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/run.py)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/GEOMETRY.json](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/GEOMETRY.json)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/FIRST_PAIR_ROUTE_DIAGNOSIS.json](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/FIRST_PAIR_ROUTE_DIAGNOSIS.json)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/ANALYSIS_RESULT.json)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RREF_J_UNIFORM_F_CLOSURE.md](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RREF_J_UNIFORM_F_CLOSURE.md)；[research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RREF_J_THEORY_FIELDS.json](../../research/ddp/more_graphs_20261027/d10_D4_gq7_three_sheet_Jmatching2550/RREF_J_THEORY_FIELDS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** One q7/eta3/cubic-character/RREF/J candidate generated. Paper closure covers every uniform flag function under those RREF bases and the fixed J, not arbitrary line-dependent voltage assignments.

**仍未完成：** Arbitrary line-dependent voltages/bases/J remain open. No new public lower bound or Lean graph instance.

**启发与重启依据：** Do not vary eta/character/uniform coefficients inside the closed family. Any continued geometry route must change line dependence or another actual structural assumption; ordinary research stays authorized. Next q8 line-dependent circle-pole rule tests character compatibility3|(q+1), not a seed sweep.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

