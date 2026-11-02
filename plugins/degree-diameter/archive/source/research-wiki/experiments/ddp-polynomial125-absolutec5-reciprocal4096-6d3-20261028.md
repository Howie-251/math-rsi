---
type: experiment
node_id: exp:ddp-polynomial125-absolutec5-reciprocal4096-6d3-20261028
title: "Polynomial125 absoluteC5: fourtarget repair works; all4096 tests fail, antipodal topology uniformly excluded"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/REPORT.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/MODEL_SCOPE.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREDICTION.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREDICTION_DISPOSITION.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PRED_CONTROL.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/RESULT.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/CASES.jsonl; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SOURCE_RECIPE.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/source125.edges; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SCOUT_SCOPE_ANALYSIS.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SCOUT_SCOPE_ANALYSIS.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ROUTES.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ROUTES.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/producer.cpp; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/run.py; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/RUN_RECEIPT.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREPARATION_STATE.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREPARATION_STATE_BEFORE_EXECUTION.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/checkpoint.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/terminal.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SAVED_FIRST_WITNESS_SUMMARY.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ANTIPODAL_OBSTRUCTION.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ANTIPODAL_OBSTRUCTION.json"
added: 2026-10-28T03:07:56Z
tags: ["ddp", "method-ledger"]
---

# Polynomial125 absoluteC5: fourtarget repair works; all4096 tests fail, antipodal topology uniformly excluded

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,3)；L=120；candidate_graph_or_family n=125

**距目标的证据：** 4096complete/0untested/0hit;4096actualgraphs and4096root0R3failures. Canonical4frozenpaths allpresent and4verticaltargets alldistance3; canonical stillmissing18 withfirstID2=(a0,y2,h0). NegativeglobalD/conn/ordinarybadpairsnull. All4096 saved first_missing fields equalID2=(0,2,0). A shortpath algebraic proof excludes thispair forany such antipodalshift, beyondthe4096reciprocal subset; noextra graph/BFS.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 125,
  "source_m": 310,
  "absolute_vertices": 5,
  "nonabsolute_vertices": 120,
  "new_absolute_C5_edges": 5,
  "new_matching_edges": 60,
  "candidate_n": 125,
  "candidate_m": 375,
  "actual_candidate_graphs": 4096,
  "complete_kappa_settings": 4096,
  "untested": 0,
  "representative_root_R3_checks": 4096,
  "failed_first_root_histogram": {
    "0": 4096
  },
  "extra_control_BFS": 0,
  "other24_representative_roots_checked": 0,
  "fullglobalD_BFS": 0,
  "old_source_BFS": 0,
  "solver_calls": 0,
  "new_lower_bounds": 0,
  "control_tuple": [
    1,
    1,
    1,
    1,
    4,
    1
  ],
  "control_tuple_index": 12,
  "direction_order": [
    [
      0,
      1
    ],
    [
      1,
      0
    ],
    [
      1,
      1
    ],
    [
      1,
      2
    ],
    [
      1,
      3
    ],
    [
      1,
      4
    ]
  ],
  "four_target_path_prediction": "SUPPORTED_ACTUAL",
  "four_vertical_distances": [
    3,
    3,
    3,
    3
  ],
  "canonical_R3_missing": 18,
  "canonical_first_missing_coordinates": [
    0,
    2,
    0
  ],
  "common_missing_intersection_computed": false,
  "common_missing_targets": null,
  "native_body_CPU_seconds": 0.024836,
  "compiler_process_CPU_seconds": 1.161616,
  "native_process_CPU_seconds": 0.025958999999999843,
  "driver_CPU_seconds": 0.002271770999999999,
  "measured_run_total_CPU_seconds": 1.1898467709999998,
  "workers": 1,
  "exec_session_id": 40310,
  "saved_first_missing_id_histogram": {
    "2": 4096
  },
  "common_saved_first_witness": [
    0,
    2,
    0
  ],
  "paper_excluded_antipodal_shift_assignments": 16777216,
  "additional_graphs_or_BFS_for_paper": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/REPORT.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/REPORT.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/MODEL_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/MODEL_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREDICTION_DISPOSITION.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREDICTION_DISPOSITION.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PRED_CONTROL.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PRED_CONTROL.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/RESULT.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/RESULT.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/CASES.jsonl](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/CASES.jsonl)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SOURCE_RECIPE.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SOURCE_RECIPE.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/source125.edges](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/source125.edges)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SCOUT_SCOPE_ANALYSIS.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SCOUT_SCOPE_ANALYSIS.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SCOUT_SCOPE_ANALYSIS.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SCOUT_SCOPE_ANALYSIS.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ROUTES.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ROUTES.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ROUTES.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ROUTES.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/producer.cpp](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/producer.cpp)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/run.py](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/run.py)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/RUN_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/RUN_RECEIPT.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREPARATION_STATE.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREPARATION_STATE.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREPARATION_STATE_BEFORE_EXECUTION.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/PREPARATION_STATE_BEFORE_EXECUTION.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/checkpoint.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/checkpoint.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/terminal.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/terminal.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SAVED_FIRST_WITNESS_SUMMARY.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/SAVED_FIRST_WITNESS_SUMMARY.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ANTIPODAL_OBSTRUCTION.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ANTIPODAL_OBSTRUCTION.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ANTIPODAL_OBSTRUCTION.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_absoluteC5_reciprocal_matching/ANALYSIS_ANTIPODAL_OBSTRUCTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly fixedq5polynomialsource, alloldedgesretained, absolutea-step1 C5, nonabsolute(a,v)->(a+kappa_L/scalar,-v), sixdirections kappa inF5*. All4096 literalsettings tested. Not all C5equivariantmatchings, allpreserved-edgeaugmentations or all125graphs. Postexperiment independent paper proof further excludes all a-independent nonzero antipodal shifts tau(-v)=-tau(v),4^12 assignments withoutenumeratingthem. Doesnotexcludeotherorbitpartner topologies.

**正向保证：** The actualloop-deleted polynomialsource has125vertices/310edges, five degree4 absolutes and120degree5 nonabsolute vertices.；The newabsoluteC5 and reciprocalmatching are genuine nonedges and give everytestedcandidate simple6regularity with375edges.；a-translation is an explicit C5automorphism with25v-indexedorbits; all25representatives would suffice for a positive, while anyrootfailure is definitive negative.；Allfour frozen canonical old-coordinate paths are present in the actualgraph, and allfour targetedvertical vertices have actualdistance3.；The canonicaltuple iscountedonce and all4096 literalparameter settings were tested withoutseed/field/rule extensions.

**仍未完成：** Other C5-equivariant matchingpartner topologies, other source-preserving augmentations and general125/max6/D3 graphs remainopen. Fulluncovered-set intersection was notcomputed; a common savedfirstwitness and independent uniformproof suffice for stated exclusion.

**启发与重启依据：** The four predicted oldvertical routes were repaired. The remaining commonwitness is forced by the antipodal partner topology, so changing kappa or reciprocalexponent within thattopology cannot repairit. Stop all nonzeroantipodalshift rules; other partner topologies remain untested, not automaticnext experiments.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

