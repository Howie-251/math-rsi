---
type: experiment
node_id: exp:ddp-d13-d3-actual972-k6-unfixed-center-lp-control-20261027
title: "K6 color restriction ablation: removing P3 center fixing still LP-infeasible"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/LP_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/run.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/ANALYSIS_PROOF.md"
added: 2026-10-27T21:38:45Z
tags: ["ddp", "method-ledger"]
---

# K6 color restriction ablation: removing P3 center fixing still LP-infeasible

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controlled-ablation

**目标与阶数：** (13,3)；L=972；条件性n=978（未据此计纪录）

**距目标的证据：** LPstatus2 infeasible, objnull,1.337638892CPU. Prediction that freeingcenters restoresLP feasibility is numericallyrefuted. Conditional newMIP notentered;0MIP/balls/candidates/newrootBFS/newlowerbound. No exactinfeasibility certificate exported.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 972,
  "source_m": 6264,
  "source_reported_D": 3,
  "variables": 648,
  "fulltarget_cover_rows": 5184,
  "disjoint_rows": 108,
  "equality_rows": 54,
  "P3_center_color_restrictions": false,
  "pin5_colorfix_in_LP": false,
  "LP_calls": 1,
  "LP_status": 2,
  "LP_objective": null,
  "MIP_calls": 0,
  "conditional_MIP_executed": false,
  "source_allroot_BFS": 0,
  "candidate_newroot_BFS": 0,
  "cached_R2_balls_recomputed": 0,
  "new_lower_bounds": 0,
  "process_CPU_seconds": 1.337638892,
  "prediction": "NUMERICALLY_REFUTED",
  "strict_proof_status": "NOT_EXPORTED",
  "original_restricted_experiment_overwritten": false,
  "method_count_note": "Single controlledvariant of the existingK6 mechanism, not a newindependentmethod"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/LP_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/LP_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/run.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/run.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/unfixed_color_LP_control/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/k6_dominating_extension/ANALYSIS_PROOF.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Same actual972 minimum48F-domination K6model as parent, but removeall6P3center colorfix bounds. LP retains648vars/5184cover/108disjoint/54equalities/forbiddenpins. No center-distinct restriction and no pin5fix in this LP. Only this single restriction control wasexecuted.

**仍未完成：** StrictLP contradiction certificate notexported. K6 models without minimumSdomination, otherhelpergraphs, rewiring and generalN(13,3) remainopen.

**启发与重启依据：** DistinctP3colors was anextraassumption but isnot the sole numericalobstruction: the same minimum-domination K6relaxation remainsinfeasible withoutit. Stop thissingleablation, notK7 or aseed/time continuation. Anystrictclosure needs a separate exactcertificate; anynew construction must change a coverage-relevant assumption beyond centercoloring.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

