---
type: experiment
node_id: exp:ddp-d13-d3-actual972-k6-minfdom48-fixedcenters-20261027
title: "Actual972 min-dom48 K6 model: LP/MIP infeasible with six P3 centers in distinct colors"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PARENT_DESIGN.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/LP_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/run.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/min_dom_model.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/build_model.py"
added: 2026-10-27T21:38:45Z
tags: ["ddp", "method-ledger"]
---

# Actual972 min-dom48 K6 model: LP/MIP infeasible with six P3 centers in distinct colors

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (13,3)；L=972；条件性n=978（未据此计纪录）

**距目标的证据：** LPstatus2/infeasible withobjnull; soleMIPstatus2/infeasible, total2.079969753CPU.648binary/5184cover/108disjoint/54eq, sourceR1/R2 caches reused. No incumbent/candidate/newrootBFS or newlowerbound. Numerical infeasibility only; standalone strictcapacity/Farkas certificate notyetexported.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 972,
  "source_m": 6264,
  "source_reported_D": 3,
  "hypothetical_m": 6327,
  "variables": 648,
  "coverage_rows": 5184,
  "disjoint_rows": 108,
  "equality_rows": 54,
  "total_nonzeros": 121248,
  "LP_calls": 1,
  "LP_status": 2,
  "LP_objective": null,
  "MIP_calls": 1,
  "MIP_status": 2,
  "MIP_status_label": "INFEASIBLE",
  "process_CPU_seconds": 2.079969753,
  "source_allroot_BFS": 0,
  "candidate_newroot_BFS": 0,
  "cached_R2_balls_recomputed": 0,
  "new_lower_bounds": 0,
  "complete_candidates": 0,
  "prediction": "NUMERICALLY_REFUTED_FOR_EXPLICIT_RESTRICTED_MODEL",
  "strict_proof_status": "NOT_EXPORTED",
  "UNKNOWN_solver_runs": 0,
  "method_count_note": "The min-dom source interface and producer belong to one construction record, not two methods",
  "F_component_types": {
    "P2": 18,
    "P3": 6,
    "P4": 9,
    "P6": 3
  },
  "exact_min_F_domination_number": 48,
  "forced_selected_count": 12,
  "binary_choice_pairs": 36,
  "min_dom_model_complete_without_search": true,
  "forced_selected_pins": [
    5,
    76,
    113,
    184,
    221,
    292,
    374,
    482,
    590,
    717,
    825,
    933
  ],
  "P3_centers_sorted_fixed_colors": [
    5,
    113,
    221,
    374,
    482,
    590
  ],
  "distinct_P3_center_colors_are_extra_restriction": true,
  "structure_interface_CPU_seconds": 0.0007080370000000016,
  "interface_BFS": 0,
  "interface_R2_matrix_recomputed": 0,
  "interface_solver_runs": 0,
  "interface_candidate_graphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PARENT_DESIGN.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PARENT_DESIGN.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/LP_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/LP_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/run.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/run.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/min_dom_model.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/min_dom_model.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/build_model.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/K6_free_dom_structure/build_model.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixedactual972 source. Sixclique helpers each8 oldpins; S is a minimum48dominating set of F108 paths. Complete minDom interface12forced+36pairchoices. SixsortedP3centers fixedtodistinctcolors0..5 is anexplicitadditionalrestriction, notWLOG. Noextraold-oldedges or otherhelpers.

**仍未完成：** No standalone strictinfeasibility certificate yet. Othercentercolorings, other S/helpergraphs/adjacencychanges and generalN(13,3) remain open; priorbuddy model remainsUNKNOWN.

**启发与重启依据：** A minimum dominating set and clique degreebudget fit exactly48pins, removing free-target difficulty by proof, but joint fulltarget/color restrictions still fail numerically. Distinctcentercolors is a realrestriction; do not generalize beyond it. Stop this rule, no K7/seed/budget or badtarget continuation; only explicit structural analysis or changedrule could justify another task.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

