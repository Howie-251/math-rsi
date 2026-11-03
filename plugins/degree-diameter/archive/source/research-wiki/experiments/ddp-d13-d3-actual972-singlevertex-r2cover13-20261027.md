---
type: experiment
node_id: exp:ddp-d13-d3-actual972-singlevertex-r2cover13-20261027
title: "Actual972:108 free-pin R2 cover needs at least15 pins, threshold13 solver infeasible"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/PREFLIGHT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/LP_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/INTEGER_ROW_WEIGHTS.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/radius2_sets.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/export_row_weights.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/run.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/ANALYSIS_CHECK.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/ANALYSIS_integer_weights_check.py"
added: 2026-10-27T21:17:06Z
tags: ["ddp", "method-ledger"]
---

# Actual972:108 free-pin R2 cover needs at least15 pins, threshold13 solver infeasible

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment-and-integer-capacity-certificate

**目标与阶数：** (13,3)；L=972；条件性n=973（未据此计纪录）

**距目标的证据：** All108 oldR2 balls union972, sizes137–140, minimum target support3. One LP minimum14.7752896474 and one full108binary threshold13 MIP status2 infeasible, CPU.375166. No candidate/newrootBFS. Integer target weights W14775252, actual max-columnC999999 give W−13C1775265>0 and pin lowerbound15; exact certificate independently checked against all108 cached columns; first source ball and all108 free labels also match.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 972,
  "source_m": 6264,
  "eligible_pins": 108,
  "all_eligible_R2_union": 972,
  "ball_size_range": [
    137,
    140
  ],
  "target_minimum_support": 3,
  "unique_support_patterns": 972,
  "source_reported_D": 3,
  "source_allroot_BFS": 0,
  "source_single_root_BFS": 0,
  "candidate_newroot_BFS": 0,
  "LP_minimum": 14.775289647439969,
  "MIP_calls": 1,
  "MIP_status": 2,
  "MIP_status_label": "INFEASIBLE",
  "producer_process_CPU_seconds": 0.375165602,
  "LP_repeated_for_dual_export": 1,
  "dual_export_CPU_seconds": 0.281894559,
  "integer_weight_W": 14775252,
  "max_column_C": 999999,
  "W_minus_13C": 1775265,
  "exact_pin_lower_bound": 15,
  "strict_independent_proof_status": "PASS",
  "new_lower_bounds": 0,
  "prediction": "REFUTED_FOR_FIXED_SINGLE_APPEND_RULE",
  "method_count_note": "Related finite experiment using the recovered source; source recovery is not counted as an independent method",
  "independent_integer_check_CPU_seconds": 0.007979,
  "independent_check_BFS_scope": "Only source pin5 direct closedR2 neighbor-set binding, not full-source BFS or108-ball recomputation"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/PREFLIGHT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/PREFLIGHT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/LP_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/LP_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/INTEGER_ROW_WEIGHTS.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/INTEGER_ROW_WEIGHTS.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/radius2_sets.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/radius2_sets.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/export_row_weights.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/export_row_weights.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/run.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/run.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/ANALYSIS_CHECK.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/ANALYSIS_CHECK.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/ANALYSIS_integer_weights_check.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/monotone_R2_cover/ANALYSIS_integer_weights_check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual972 source, exactly108 degree12 eligible oldpins. Add one newvertex joined to <=13 distinct pins, retain every oldedge, no added old-old edges. All972 source targets constrained. Not arbitrary973graphs, cooperative helpers, source surgery or added old-old shortcuts.

**仍未完成：** No generalN(13,3) upper bound; changes outside the precise single-append rule remain open.

**启发与重启依据：** 108 free slots alone do not ensure D3 extension: their target support forces more attachment pins than allowed13. This exact singlevertex rule stops; a later task would need an actual new cooperative or edge-changing coverage mechanism, not more LP/MIP time, seed or near-star guards.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

