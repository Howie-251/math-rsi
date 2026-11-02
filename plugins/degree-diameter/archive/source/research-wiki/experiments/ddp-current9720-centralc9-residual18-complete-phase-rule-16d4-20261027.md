---
type: experiment
node_id: exp:ddp-current9720-centralc9-residual18-complete-phase-rule-16d4-20261027
title: "Actual9720 fixedchart/C9:18 residual nonunit-a frames complete the allphase controller obstruction"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/REPORT.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/MODEL.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/probe.cpp; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/run.py; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/native.log; research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/terminal.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/ANALYSIS_PROOF.md"
added: 2026-10-27T22:30:29Z
tags: ["ddp", "method-ledger"]
---

# Actual9720 fixedchart/C9:18 residual nonunit-a frames complete the allphase controller obstruction

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (16,4)；L=16384；条件性n=17496（未据此计纪录）

**距目标的证据：** All18/18 newcontroller frames failR4, missing4..19/216 states. 0passers,0actualfibergraphs,0fiberBFS,0UNKNOWN/untested,0newlowerbounds. Togetherwith54inheritedframes andVALID normalization, thewholefixedm9phase rule is excluded, notgeneralN(16,4).

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 9720,
  "source_reported_D": 4,
  "hypothetical_graph_n": 17496,
  "hypothetical_degree": 16,
  "controller_n": 216,
  "new_coarse_frames": 18,
  "inherited_coarse_frames": 54,
  "new_controller_root_truncated_R4_BFS": 18,
  "coarse_missing_range": [
    4,
    19
  ],
  "new_planned_parity_lifts_excluded_by_projection": 72,
  "actual_graphs_constructed": 0,
  "fiber_root_BFS": 0,
  "source_all_roots_BFS_repeated": 0,
  "native_CPU_seconds": 0.000275,
  "compile_CPU_seconds": 1.123087,
  "total_parent_children_CPU_seconds": 1.1259290000000002,
  "prediction": "REFUTED",
  "UNKNOWN": 0,
  "untested_newframes": 0,
  "fixed_m9_allphase_rule_closed": true,
  "ordinary_bad_pair_scope": "Not measured; missing counts are controller states from identity."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/MODEL.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/MODEL.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/probe.cpp](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/probe.cpp)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/run.py](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/run.py)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/native.log](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/native.log)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/terminal.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/residual_phase_classes/terminal.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/ANALYSIS_PROOF.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 18 newframes only: A0/3/6,B1,two distinctprojectedplainclasses from1..4;4potentialfiberparitylifts each. Inherits54 earlierA1/Bfree frames without rerun. Paper normalization andminusI bounds extend the combined result toallA/Bmod9 for thefixedSL2 projections/sourcechart andtwo globalplain inverse-powerpairs; repeatedprojectedclasses/P9matching are separatelypaperexcluded.

**仍未完成：** Generaldegree16D4 graphs, othercentralorders, otherSL2 generators orchart rules/topologies are notexcluded. No actualglobalD orordinarybadpaircount was measured.

**启发与重启依据：** The nonunit-a gap was a genuine completeness issue and is now resolved by18 previously untested representativeframes. A missing projectedcontroller route cannotbe repaired by fiberparity or otherfiberparameters. Stop thefixedm9/sourceoperator rule; a future restart requires a substantively different controller/operator mechanism, notmorephase starts.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

