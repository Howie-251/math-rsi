---
type: experiment
node_id: exp:ddp-michel684-three-crossmatching-deletions-6d4-20261028
title: "Michel684 degree7-to6: all3 literal crossmatching deletions fail rootR4"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/REPORT.md; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/MODEL_SCOPE.md; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/PREDICTION.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/RESULT.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/SOURCE_INPUT.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/CASES.jsonl; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_0.edges; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_1.edges; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_2.edges; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_0_root_0.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_1_root_0.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_2_root_0.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/controls.py; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/run.py; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/checkpoint.json; research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/terminal.json; research/ddp/m1_sources/684_recovered_construction.json"
added: 2026-10-28T03:01:36Z
tags: ["ddp", "method-ledger"]
---

# Michel684 degree7-to6: all3 literal crossmatching deletions fail rootR4

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,4)；L=441；candidate_graph_or_family n=684

**距目标的证据：** 3complete/0untested/0hit. Root0R4misses103/147/114; firstmissing14=(side0,n1,p5),9=(0,1,0),4=(0,0,4). Eachfirstrootrejectsitscontrol, so no secondroot/globalDcheck. NegativeglobalD/connectivity/ordinarybadpairsnull.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 684,
  "source_degree_inherited": 7,
  "source_D_inherited": 4,
  "actual_candidate_graphs": 3,
  "actual_n_per_candidate": 684,
  "actual_m_per_candidate": 2052,
  "removed_matching_edges_per_candidate": 342,
  "controls_completed": 3,
  "controls_untested": 0,
  "actual_identity_R4_checks": 3,
  "second_root_checks": 0,
  "fullglobalD_BFS": 0,
  "old_source_BFS": 0,
  "solver_calls": 0,
  "new_lower_bounds": 0,
  "root_state_missing_counts": [
    103,
    147,
    114
  ],
  "thin_minimum_phase_image_sizes": [
    27,
    26,
    26
  ],
  "phase_slot_target_count": 38,
  "root_state_count_type": "one-root endpoints; notordinaryunorderedpairs",
  "worker_CPU_seconds": 0.037271,
  "driver_CPU_seconds": 0.000599593999999995,
  "compile_CPU_seconds": 0,
  "workers": 1
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/REPORT.md](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/REPORT.md)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/MODEL_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/MODEL_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/RESULT.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/RESULT.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/SOURCE_INPUT.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/SOURCE_INPUT.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/CASES.jsonl](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/CASES.jsonl)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_0.edges](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_0.edges)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_1.edges](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_1.edges)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_2.edges](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_2.edges)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_0_root_0.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_0_root_0.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_1_root_0.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_1_root_0.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_2_root_0.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/case_2_root_0.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/controls.py](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/controls.py)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/run.py](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/run.py)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/checkpoint.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/checkpoint.json)；[research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/terminal.json](../../research/ddp/more_graphs_20261027/small_d6_D4_michel684_cross_matching_deletion/terminal.json)；[research/ddp/m1_sources/684_recovered_construction.json](../../research/ddp/m1_sources/684_recovered_construction.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly the3 deletions ofone entireoriginal0-to1 crossmatching at unchanged Michelm38/n9/r23, allotheredgesretained. Threeactual684/2052simple6regulargraphs, not arbitrary6regular684graphs or other voltage/action/phase/deletion families.

**仍未完成：** Other degree6graphs or materiallydifferentsource surgery remainunexcluded; general(6,4)unresolved. Oldp43freevoltageclosure isdistinct andnotrepeated.

**启发与重启依据：** No originalcrossmatching is redundant for four-stepcoverage under this fixed deletionrule. Keepingthetwo-orbit groupaction helps exactverification but doesnotpreserve diameterafterremovingwhole routeclasses. Stopall3controls; do nottunephasemodulus/voltage/seed fromthedeficits.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

