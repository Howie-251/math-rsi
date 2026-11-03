---
type: experiment
node_id: exp:ddp-stale-d4d8-loz69-f139-shared4-normalized-endpoints-20261101
title: "4D8旧Loz规则迁移：raw160/coeff159两次必要门预测被推翻，19462归一参数全失败且最大image117<139"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/FORM_MODEL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/PREPARATION_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NORMALIZATION_BINDING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/ALL_REPRESENTATIVE_COVERAGES.csv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/BEST_CRITICAL_SLOT_COVERAGE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/parameter_gate_normalization_review.md"
added: 2026-11-01T18:12:35Z
tags: ["ddp", "method-ledger"]
---

# 4D8旧Loz规则迁移：raw160/coeff159两次必要门预测被推翻，19462归一参数全失败且最大image117<139

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_route_or_local_counting_gate

**目标与阶数：** (4,8)；L=3243；条件性n=9591（未据此计纪录）

**距目标的证据：** No new full target graph; finite local premise or route-image gate only；固定69-state=3bases×23phases。raw≤8NB最小160≥139、distinctcoeff最小159≥139，两个“容量不足”预测均REFUTED，只是必要PASS。随后gauge c→c+(6^a−1)d置c2=0，再非零scale置首非零1，P²(F139)+zero全19462代表均在tight46→52漏端点；实际image最大117、至少缺22/139，best(1,102,0,128)。所有159form的gauge-offset绑定通过。未造9591图，未用sourceBFS或旧失败singlecontrol冒新排除。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 13121,
  "located_baseline": 3243,
  "Moore_space": 9878,
  "hypothetical_target": 9591,
  "target_below_Moore_by": 3530,
  "Moore_gap_is_not_constructibility": true,
  "accepted_source": {
    "actual_order": 3243,
    "actual_edges": 6486,
    "degree_histogram": {
      "4": 3243
    },
    "D_inherited": 8,
    "girth_inherited": 10,
    "literal_path": "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source3243.raw_adj.txt",
    "recipe_path": "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_FACTS.json",
    "prior_directed_arc_binding": 12972,
    "source_legality": "INHERITED_NOT_REVERIFIED",
    "Cayley": false,
    "vertex_transitive": false
  },
  "inherited_stops": [
    {
      "scope": "Keep all old edges, cap4, any connected append",
      "status": "EXACT_NO_OLD_DEGREE_SLACK",
      "source": "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/REPORT.md"
    },
    {
      "scope": "Any nontrivial ordinary graph cover of this exact3243 source with D<=9, hence D8",
      "status": "EXACT_NO_BY_PUBLISHED_GIRTH10_AND_UNIQUE_WALK_LIFT",
      "source": "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/REPORT.md"
    }
  ],
  "inherited_single_control": {
    "status": "SINGLE_FIXED_CONTROL_REFUTED",
    "n": 9591,
    "target_D": 9,
    "first_orbit_root_eccentricity": 10,
    "first_orbit_root_R9_missing": 245,
    "all_three_root_BFS_complete": false,
    "actual_global_D": null,
    "scope": "F139,r6,stored centered offsets only, not all translation assignments",
    "recipe": "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/CONTROL_RECIPE.json",
    "result": "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/CONTROL_RESULT.json"
  },
  "raw_gate": {
    "status": "NECESSARY_CAPACITY_PASS_NO_GRAPH_OR_FIELD_CONSTRUCTION",
    "prediction": "REFUTED_MINIMUM_AT_LEAST139",
    "ordered_slots": 4761,
    "minimum_words": 160,
    "tight_pair": [
      46,
      52
    ],
    "required_endpoints": 139
  },
  "coefficient_gate": {
    "status": "NECESSARY_DISTINCT_FORM_CAPACITY_PASS_PARAMETERS_UNSOLVED",
    "prediction": "REFUTED_ALL_DISTINCT_FORM_CAPACITIES_AT_LEAST139",
    "minimum_distinct_forms": 159,
    "all4761_slots_computed": true
  },
  "normalized_gate": {
    "parameter_representatives_evaluated": 19462,
    "complete_normalized_parameter_domain": true,
    "critical_slot": [
      46,
      52
    ],
    "critical_slot_survivor_count": 0,
    "maximum_actual_image_cardinality": 117,
    "required_image_cardinality": 139,
    "best_representative": [
      1,
      102,
      0,
      128
    ],
    "gauge_binding_all159": true,
    "all_representatives_have_saved_first_missing_endpoint": true
  },
  "phase_coordinate": "Z23; 69 is total controller-state count, not phase modulus",
  "normalization_review": "same-slot affine endpoint bijection; no false fixed-normal0-root premise",
  "cumulative_charged_CPU_seconds": 1.7118444500000003,
  "CPU_budget_seconds": 20.0,
  "actual_new_parameter_evaluation_CPU_seconds": 0.45503052,
  "prior_and_failed_preparation_charges_preserved": true,
  "no_timer_reset": true,
  "source_graph_BFS": 0,
  "old_word_or_form_recounts": 0,
  "solver_Lean_review_runs": 0,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/phase69_capacity_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/FORM_MODEL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/coefficient_alias_gate/FORM_MODEL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/PREPARATION_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/PREPARATION_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NORMALIZATION_BINDING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NORMALIZATION_BINDING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/ALL_REPRESENTATIVE_COVERAGES.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/ALL_REPRESENTATIVE_COVERAGES.csv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/BEST_CRITICAL_SLOT_COVERAGE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/BEST_CRITICAL_SLOT_COVERAGE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/parameter_gate_normalization_review.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/parameter_gate_normalization_review.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed69-state three-base/23-phase controller; r6 on F139; four shared translations with two identity-cross translations0; true inverse darts; diameter at most8. One mechanism node combines raw NB capacity, shared coefficient aliasing and complete normalized parameter evaluation. Not a repeat of the old3243 ordinary-cover or fixed centered-control checks; not all4D8 graphs.

**仍未完成：** General target parameter remains open; only the explicitly fixed source/rule is closed.

**启发与重启依据：** STOP this exact fixed phase/r6/F139 four-shared-translation family. Raw/per-form necessary passes do not guarantee simultaneous endpoint coverage. Do not restart the19462 domain or prior ordinary-cover/girth10/centered-control scopes; other phases, per-phase maps or arbitrary permutation lifts require genuinely changed premises and remain outside this finiteNO.

**单独的重启条件：** STOP this exact fixed phase/r6/F139 four-shared-translation family. Raw/per-form necessary passes do not guarantee simultaneous endpoint coverage. Do not restart the19462 domain or prior ordinary-cover/girth10/centered-control scopes; other phases, per-phase maps or arbitrary permutation lifts require genuinely changed premises and remain outside this finiteNO.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

