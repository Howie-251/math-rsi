---
type: experiment
node_id: exp:ddp-current12654-fixed342-f43-allprojective-controls-7d6-20261028
title: "Current12654 fixed342-controller transfer toF43: all3786 projective/action cases fail D6"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d7_D6_current12654_field43/REPORT.md; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/PREDICTION.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/RESULT.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/EXECUTION_MODEL.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/CASES.jsonl; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/THIN_COEFFICIENTS_action7.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/THIN_COEFFICIENTS_action37.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_ARITHMETIC.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/PRIMARY_RECEIPTS.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/AUTHOR_construction.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/AUTHOR_README.md; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/controller_capacity/REPORT.md; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/controller_capacity/RESULT.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/probe.cpp; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/run.py; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/terminal.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_NORMALIZATION.md; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_NORMALIZATION.json; research/ddp/more_graphs_20261027/d7_D6_current12654_field43/SOURCE_BINDING.json"
added: 2026-10-28T00:09:53Z
tags: ["ddp", "method-ledger"]
---

# Current12654 fixed342-controller transfer toF43: all3786 projective/action cases fail D6

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,6)；L=12654；candidate_graph_or_family n=14706

**距目标的证据：** Complete3786:2539 exactthin-image rejections and1247 actualimplicit14706/51471/simple7regular Cayley graphs,each identityR6fail.0hits/unknown/untested. All negative globaldiameters null because R6 checks were not extended. Source-control(1,18,-4):action7image43 then163R6miss;action37image40 no actualgraph.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 12654,
  "source_D_inherited": 6,
  "target_m": 51471,
  "controller_states": 342,
  "capacity_prefixes": 65318,
  "minimum_raw_routes": 152,
  "selected_thin_slot": {
    "id": 126,
    "phase": 6,
    "normal19": 12
  },
  "distinct_thin_coefficient_triples_per_action": [
    132,
    132
  ],
  "objects": 3786,
  "objects_unique": 3786,
  "objects_processed": 3786,
  "strict_image_rejections": 2539,
  "actual_implicit_graphs": 1247,
  "actual_identity_R6_checks": 1247,
  "complete_identity_full_diameter_BFS": 0,
  "rejected_by_actions7_37": [
    1272,
    1267
  ],
  "actualgraphs_by_actions7_37": [
    621,
    626
  ],
  "source_control_normal43": [
    1,
    18,
    39
  ],
  "source_control_outcomes": [
    {
      "candidate_ordinal": 0,
      "action43": 7,
      "normal43": [
        1,
        18,
        39
      ],
      "inherited_source_control": true,
      "thin_image_size": 43,
      "actual_graph": true,
      "simple": true,
      "max_degree": 7,
      "identity_R6_reached": 14543,
      "identity_R6_missing": 163,
      "first_R6_missing_vertex": 18,
      "R6_distance_histogram": [
        1,
        7,
        42,
        252,
        1450,
        6066,
        6725
      ],
      "status": "ACTUAL_IDENTITY_R6_FAILURE",
      "actual_global_D": null,
      "connected_by_this_truncated_check": null,
      "first_R6_missing_state": {
        "phase": 0,
        "normal19": 0,
        "normal43": 18
      }
    },
    {
      "candidate_ordinal": 1,
      "action43": 37,
      "normal43": [
        1,
        18,
        39
      ],
      "inherited_source_control": true,
      "thin_image_size": 40,
      "status": "STRICT_THIN_IMAGE_REJECTION",
      "missing_thin_field": 6,
      "actual_graph": false,
      "actual_global_D": null,
      "thin_missing_controller_state": {
        "phase": 6,
        "normal19": 12,
        "normal43": 6
      }
    }
  ],
  "thin_image_size_histogram": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    4,
    2,
    6,
    0,
    6,
    0,
    4,
    4,
    4,
    0,
    12,
    3,
    6,
    8,
    6,
    11,
    19,
    18,
    20,
    30,
    31,
    49,
    55,
    129,
    274,
    617,
    1217,
    1247
  ],
  "prediction": "REFUTED",
  "source_BFS_count": 0,
  "solver_calls": 0,
  "new_lower_bounds": 0,
  "untested": 0,
  "UNKNOWN": 0,
  "native_CPU_seconds": 0.584382,
  "production_native_process_plus_driver_CPU_seconds": 0.5877651580000002,
  "compile_CPU_seconds_separate": 1.0510429999999997,
  "per_candidate_CPU_measured": false,
  "ordinary_bad_count_units": "null; truncated single-root R6 misses and strict thin-slot residues are separate units"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d7_D6_current12654_field43/REPORT.md](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/REPORT.md)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/PREDICTION.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/PREDICTION.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/RESULT.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/RESULT.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/EXECUTION_MODEL.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/EXECUTION_MODEL.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/CASES.jsonl](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/CASES.jsonl)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/THIN_COEFFICIENTS_action7.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/THIN_COEFFICIENTS_action7.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/THIN_COEFFICIENTS_action37.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/THIN_COEFFICIENTS_action37.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_ARITHMETIC.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_ARITHMETIC.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/PRIMARY_RECEIPTS.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/PRIMARY_RECEIPTS.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/AUTHOR_construction.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/AUTHOR_construction.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/controller_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/controller_capacity/REPORT.md)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/controller_capacity/RESULT.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/controller_capacity/RESULT.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/probe.cpp](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/probe.cpp)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/run.py](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/run.py)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/terminal.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/terminal.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_NORMALIZATION.md](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_NORMALIZATION.md)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_NORMALIZATION.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/ANALYSIS_NORMALIZATION.json)；[research/ddp/more_graphs_20261027/d7_D6_current12654_field43/SOURCE_BINDING.json](../../research/ddp/more_graphs_20261027/d7_D6_current12654_field43/SOURCE_BINDING.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed source C18/Z19 controller,action9,positive phases17/13/10,normals17/11/17,involution(9,0). TargetF43 only,actions7/37,allP2(F43)1893positive-normal triples peraction after field involution centering/common scaling.3786objects complete; zero triple disconnected. No othercontroller/phase/prime/action/seed.

**仍未完成：** Othercontrollers,phases,fieldactions/orders,primefields or generalN(7,6) graphs are not excluded. Exactnegative globaldiameters/ordinaryunorderedbadpairs were not measured.

**启发与重启依据：** Rawcapacity152>=43 and even fullthinimage43 are only necessary. Full projective normal enumeration removes vector choice as an escape for this fixed342controller/twoaction family. Any next reuse needs a materially different controller/phase/rule, not continued normals,nextprime or first-missing-phase tuning.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

