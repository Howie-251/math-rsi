---
type: experiment
node_id: exp:ddp-old6641680-small-factor13-core-gates-20261028
title: "Old6641680 factor61-to13: both core gates pass but all450 normalized target objects fail"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/REPORT.md; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/CORE_INPUT.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/RESULT.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree6_D10_remove_h.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree7_D9_keep_h.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/RAW_COUNTS_SCHEMA.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree6_D10_remove_h_rawcounts.u64le.bin; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree7_D9_keep_h_rawcounts.u64le.bin; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/core_gate.cpp; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/run.py; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/checkpoint.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/terminal.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ANALYSIS_GATE_METHOD.md; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ANALYSIS_GATE_METHOD.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ROOT_QUESTION_NOT_EXECUTED.md; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/SOURCE_NOTES.md; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/PROVENANCE.json; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/VERSION_GAP.md; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/OLD6641680_ARITHMETIC.json; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/construction.json; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/README.md; research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/verification.txt; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/PARAMETERS.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/RESULT.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/REPORT.md; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/ROUTE_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/CASES.jsonl; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/TERMINAL.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/WORKER_RESULT.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/LIVE_HANDLE.json; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/search.cpp; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/run.py; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/generate_edges.py; research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/prepare.py"
added: 2026-10-28T04:21:02Z
tags: ["ddp", "method-ledger"]
---

# Old6641680 factor61-to13: both core gates pass but all450 normalized target objects fail

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** 多目标：degree6_D10_small13→[6, 10]／L=1394189；degree7_D9_small13→[7, 9]／L=1332774（逐变体，不合成一个距离）；known_source_or_recovery n=1415440

**距目标的证据：** Both inherited core gates pass. Actual450 implicit target graphs all fail assigned R_D:225 degree6D10 and225 degree7D9.0unvisited/UNKNOWN/hit. Thinfull34/48 is not wholegraph coverage;396 first witnesses lie inidentitycore,54 do not.

**其他指标（保持原计数类型）：**
```json
{
  "old_seed_n": 6641680,
  "current_main7D10_n": 6645690,
  "current_source_recipe_bound": false,
  "source_normal_modulus": 83021,
  "source_normal_factors": [
    61,
    1361
  ],
  "source_phase_modulus": 80,
  "source_action": 4400,
  "core_n": 108880,
  "core_action": 317,
  "target_small_prime": 13,
  "paper_F13actors": [
    1,
    12,
    5,
    8
  ],
  "normal_forms_per_rule": 225,
  "trivial_actor_projective_classes": 183,
  "nontrivial_actor_classes_each": 14,
  "target_rules": 2,
  "target_settings_executed": 450,
  "target_graphs": 450,
  "source_BFS_count": 0,
  "core_BFS_count": 2,
  "target_BFS_count": 450,
  "module_image_evaluations": 0,
  "wordlists": 0,
  "native_CPU_seconds": 0.0543235,
  "native_process_CPU_seconds": 0.05609700000000023,
  "compile_CPU_seconds": 1.02735,
  "driver_CPU_seconds": 0.0023974949999999995,
  "total_CPU_budget_seconds": 120,
  "native_CPU_hard_limit_seconds": 28,
  "new_lower_bounds": 0,
  "target_graph_type": "implicit finite Cayley graph, no failed-edge export",
  "target_BFS_this_batch": 450,
  "core_BFS_this_batch": 0,
  "core_BFS_count_note": "Historical inherited two core traversals only",
  "worker_CPU_seconds": 13.2292,
  "target_batch_aggregate_CPU_seconds": 17.606401823,
  "target_batch_compile_CPU_seconds": 4.369663,
  "historical_core_gate_timing_note": "native_CPU_seconds/native_process_CPU_seconds/compile_CPU_seconds/driver_CPU_seconds above are inherited core-gate timings; target batch has its separately named worker/compile/aggregate fields.",
  "independent_method_count_increment": 0
}
```



**从属变体：**
```json
[
  {
    "title": "degree6_D10_remove_h",
    "target_Delta": 6,
    "target_D": 10,
    "savedL": 1394189,
    "n": {
      "actual": 1415440,
      "hypothetical": null
    },
    "actual_D": null,
    "actual_graph_Delta": 6,
    "core_n": 108880,
    "core_exact_D": 9,
    "core_radius_missing": 0,
    "minimum_source_label_raw_count": 67,
    "first_minimum_slot": 23532,
    "first_minimum_phase": 17,
    "first_minimum_normal1361": 395,
    "raw_prefix_count": 14648437,
    "necessary_gate_passed": true,
    "paper_target_normal_representatives": 225,
    "target_settings_executed": 225,
    "target_status": "COMPLETE225_NO_HIT",
    "target_radius_failures": 225,
    "target_unknown": 0,
    "target_unvisited": 0,
    "firstthin_full13": 34,
    "first_missing_identity_core": 195,
    "first_missing_outside_identity_core": 30,
    "label": "degree6_D10_small13",
    "target": [
      6,
      10
    ]
  },
  {
    "title": "degree7_D9_keep_h",
    "target_Delta": 7,
    "target_D": 9,
    "savedL": 1332774,
    "n": {
      "actual": 1415440,
      "hypothetical": null
    },
    "actual_D": null,
    "actual_graph_Delta": 7,
    "core_n": 108880,
    "core_exact_D": 8,
    "core_radius_missing": 0,
    "minimum_source_label_raw_count": 81,
    "first_minimum_slot": 42875,
    "first_minimum_phase": 31,
    "first_minimum_normal1361": 684,
    "raw_prefix_count": 14108774,
    "necessary_gate_passed": true,
    "paper_target_normal_representatives": 225,
    "target_settings_executed": 225,
    "target_status": "COMPLETE225_NO_HIT",
    "target_radius_failures": 225,
    "target_unknown": 0,
    "target_unvisited": 0,
    "firstthin_full13": 48,
    "first_missing_identity_core": 201,
    "first_missing_outside_identity_core": 24,
    "label": "degree7_D9_small13",
    "target": [
      7,
      9
    ]
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/CORE_INPUT.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/CORE_INPUT.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree6_D10_remove_h.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree6_D10_remove_h.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree7_D9_keep_h.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree7_D9_keep_h.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/RAW_COUNTS_SCHEMA.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/RAW_COUNTS_SCHEMA.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree6_D10_remove_h_rawcounts.u64le.bin](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree6_D10_remove_h_rawcounts.u64le.bin)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree7_D9_keep_h_rawcounts.u64le.bin](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/degree7_D9_keep_h_rawcounts.u64le.bin)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/core_gate.cpp](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/core_gate.cpp)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/run.py](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/run.py)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/checkpoint.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/checkpoint.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/terminal.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/core_from_old6641680/terminal.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ANALYSIS_GATE_METHOD.md](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ANALYSIS_GATE_METHOD.md)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ANALYSIS_GATE_METHOD.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ANALYSIS_GATE_METHOD.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ROOT_QUESTION_NOT_EXECUTED.md](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/ROOT_QUESTION_NOT_EXECUTED.md)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/SOURCE_NOTES.md](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/SOURCE_NOTES.md)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/PROVENANCE.json](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/PROVENANCE.json)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/VERSION_GAP.md](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/VERSION_GAP.md)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/OLD6641680_ARITHMETIC.json](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/OLD6641680_ARITHMETIC.json)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/construction.json](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/construction.json)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/README.md](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/README.md)；[research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/verification.txt](../../research/ddp/more_graphs_20261027/d7_D10_current6645690_source/old6641680_primary/verification.txt)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/PARAMETERS.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/PARAMETERS.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/ROUTE_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/ROUTE_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/CASES.jsonl](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/CASES.jsonl)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/TERMINAL.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/TERMINAL.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/WORKER_RESULT.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/WORKER_RESULT.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/LIVE_HANDLE.json](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/LIVE_HANDLE.json)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/search.cpp](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/search.cpp)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/run.py](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/run.py)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/generate_edges.py](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/generate_edges.py)；[research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/prepare.py](../../research/ddp/more_graphs_20261027/d6_D10_factor_reduction_from6645690/small13_two_rule_family/prepare.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All connected source-projection-preserving F13 small-component assignments in the proved225-normal-form family, for each of the two fixed rules.

**正向保证：** Actual primary oldseed and both core gates/normalization inherited.；All225 source-projection-preserving connected small-coordinate classes per rule are covered.；Exact identity R_D decides the radius bound globally by Cayley transitivity; every failed object has a decoded endpoint witness.

**仍未完成：** Other projections, phases, fields, modules, connection sets and arbitrary graphs remain open; current6645690 recipe still unbound.

**启发与重启依据：** Enough projected words, a full preselected13point fiber and even fullidentityreturn fiber do not guarantee simultaneous coverage of all target endpoints. This complete fixed small13 family stops; do not continue fields/phases/normals or missing-score tuning.

**单独的重启条件：** StopthecompletefixedF13two-rulefamily;noautomaticfield/seed/translationcontinuation. Othermechanisms remainoutsideitsclosure.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

