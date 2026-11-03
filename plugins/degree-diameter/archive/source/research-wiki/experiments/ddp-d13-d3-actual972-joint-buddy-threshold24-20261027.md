---
type: experiment
node_id: exp:ddp-d13-d3-actual972-joint-buddy-threshold24-20261027
title: "Actual972 adjacent-buddy974 model: LP22.266 feasible, integer solve UNKNOWN at20CPU"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/CAPACITY_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/LP_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/run.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/REPORT.md"
added: 2026-10-27T21:21:43Z
tags: ["ddp", "method-ledger"]
---

# Actual972 adjacent-buddy974 model: LP22.266 feasible, integer solve UNKNOWN at20CPU

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (13,3)；L=972；条件性n=974（未据此计纪录）

**距目标的证据：** LP completed feasible with minimum totalattachment22.2655666823<=24. One MIP feasibility call timed out withoutincumbent(status1/primalNone); totalprocess19.519218651CPU. UNKNOWN, no completegraph/newrootBFS/new lowerbound. Not a claim of infeasibility.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 972,
  "source_m": 6264,
  "eligible_pins": 108,
  "binary_variables": 216,
  "cover_constraints": 1944,
  "disjointness_constraints": 108,
  "attachment_budgets": [
    12,
    12
  ],
  "LP_status": 0,
  "LP_fractional_minimum": 22.265566682261568,
  "MIP_calls": 1,
  "MIP_status": 1,
  "MIP_status_label": "TIME_LIMIT_NO_INCUMBENT",
  "solver_time_limit_seconds": 19.003997115,
  "process_CPU_seconds": 19.519218651,
  "source_R2_balls_recomputed": 0,
  "source_allroot_BFS": 0,
  "source_single_root_BFS": 0,
  "candidate_newroot_BFS": 0,
  "new_lower_bounds": 0,
  "prediction": "UNRESOLVED_TIME_LIMIT",
  "UNKNOWN": 1,
  "complete_candidates": 0,
  "ordinary_bad_pair_count_units": "No candidate, so no ordinary badpair count. Empty selected arrays are noincumbent placeholders.",
  "parent_C_R2": 999999,
  "parent_C_R1": 997321,
  "original_integer_weight_on_free_vertices": 13876887,
  "total_integer_target_weight": 14775252,
  "capacity_diagnostic_only": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/CAPACITY_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/CAPACITY_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/LP_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/LP_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/run.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/run.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/joint_buddy_cover/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/buddy_capacity/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual972 source,108 degree12 pins. Add adjacenta/b, disjoint oldpinsetsA/B each<=12, retain all oldedges, no additional old-old edges.216binary/1944covers/108disjoint/2budgets; one20CPU LP+MIP attempt, not exhaustive family rejection.

**仍未完成：** Integer feasibility of this same buddy model remains open, along with broader multi-helper/edge-changing constructions and generalN(13,3).

**启发与重启依据：** Adjacent helper changes old-target coverage from a singleR2 union to complementary R2/R1 unions. Source capacity and LP permit this rule, but integer existence remains unsettled at the frozen budget. Stop this run without score/seed/time continuation; any later task must give a new structural reduction or explicitly reassess the unresolved model.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

