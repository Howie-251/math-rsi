---
type: experiment
node_id: exp:ddp-current9720-centralc9-two-plainpower-controls-16d4-20261027
title: "Actual9720 chart transferred to C9 with plain±2/±3: both17496 degree16 models failfirstR4"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/REPORT.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/MODEL.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power2_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power3_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power2_missing_states.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power3_missing_states.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/SL2_ELEMENTS.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/input.txt; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/probe.cpp; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/run.py; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/terminal.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/ANALYSIS_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/PHASE_OBSTRUCTION_PREDICTION.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/PHASE_OBSTRUCTION_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/phase_obstruction.py"
added: 2026-10-27T22:11:50Z
tags: ["ddp", "method-ledger"]
---

# Actual9720 chart transferred to C9 with plain±2/±3: both17496 degree16 models failfirstR4

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (16,4)；L=16384；candidate_graph_or_family n=17496

**距目标的证据：** Bothactual17496/139968/simple16regular/reciprocal graphs failroot0R4: missing4052/4548; samefirsttarget82=(SL2I,central1,fiber1). PergraphglobalDnull/connectivityunverifiedbeyondR4, noordinarybadpairs orfailededgeexports. Bothmodelscomplete0D4hit,0unknown/unattempted;80additionalfiberrootspercase skippedafterdecisivefirstfail.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 9720,
  "source_reported_D": 4,
  "source_degree": 14,
  "new_controller_states": 216,
  "new_central_order": 9,
  "fiber": "GF3^4",
  "actual_graphs_constructed": 2,
  "actual_graph_n": 17496,
  "actual_graph_m": 139968,
  "degree": 16,
  "simple_undirected": true,
  "line_source_centered_integer_phases": [
    1,
    -1,
    2,
    -2
  ],
  "extra_power_controls": [
    2,
    3
  ],
  "plain_fiber_gamma_order": 2,
  "true_extra_power2_fiber": "identity",
  "true_extra_power3_fiber": "gamma",
  "firstroot_R4_missing_per_control": [
    4052,
    4548
  ],
  "firstmissing_vertex_per_control": [
    82,
    82
  ],
  "firstmissing_controller": 1,
  "firstmissing_central": 1,
  "firstmissing_fiber": 1,
  "R4_representatives_checked": 2,
  "additional_fiber_representatives_skipped_after_failure": 160,
  "global_D_scope": "Notmeasured,firstrootR4alreadyfails",
  "source9720_BFS_repeated": 0,
  "ordinary_bad_pair_count_units": "Notmeasured;reportedmissingareone-rootstates",
  "native_CPU_seconds": 0.009521,
  "compile_and_driver_CPU_seconds": 1.038899267,
  "total_parent_children_CPU_seconds": 1.050549445,
  "new_lower_bounds": 0,
  "prediction": "REFUTED_FOR_TWO_FROZEN_CONTROLS",
  "models_unattempted": 0,
  "UNKNOWN": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/MODEL.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/MODEL.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power2_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power2_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power3_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power3_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power2_missing_states.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power2_missing_states.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power3_missing_states.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/power3_missing_states.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/SL2_ELEMENTS.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/SL2_ELEMENTS.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/input.txt](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/input.txt)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/probe.cpp](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/probe.cpp)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/run.py](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/run.py)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/terminal.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/terminal.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/ANALYSIS_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/PHASE_OBSTRUCTION_PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/PHASE_OBSTRUCTION_PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/PHASE_OBSTRUCTION_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/PHASE_OBSTRUCTION_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/phase_obstruction.py](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/route_analysis/phase_obstruction.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactlyactual9720fourGF3^4linecharts andSL2parts, frozen sourcecentralphases1,-1,2,-2, newC9directcentralfactor. RetainP±1 plustrueP±2 ortrueP±3. Twoactualfulladjacency models only; firstfailing representative stops each, nooldGF4/C19family expansion.

**仍未完成：** Othercentralmoduli/phasepatterns/plainpowers/charts andgeneralN(16,4) are notexcluded. No exactglobalD claimed.

**启发与重启依据：** Degreebudgetchange via truepowers compresses differentplainwalks, but doesnot preserve sourceD4 when centralmodulus changes. Freezeoldpositiveintegerphases beforetaking newinverses. Aplaincontrollercycle neednot haveidentityfiberholonomy forlocalgraphlegality. These twofinitefailures stop; no powers4/newm/offset/coeff/seed continuation frommissingcounts.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

