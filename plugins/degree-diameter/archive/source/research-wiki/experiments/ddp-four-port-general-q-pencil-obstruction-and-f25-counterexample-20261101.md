---
type: experiment
node_id: exp:ddp-four-port-general-q-pencil-obstruction-and-f25-counterexample-20261101
title: "四端口三维一般q路线：精确pencil障碍与F25单点反例，未生成新图"
idea_id: "idea:ddp-q3-three-step-plane-pencil31"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/PREDICTION.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/READ_SCOPE.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/ALL_CONTROLLER_ROUTE_CLASSES.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/EXTERNAL_EDGE_0_20.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/FOUR_PORT_PROJECTIVE_TRIPLES.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/F25_COUNTEREXAMPLE_PREDICTION.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/F25_COUNTEREXAMPLE.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/check_once.py; research/ddp/two_successful_methods_20261101/affine_field_conditions/check_F25_counterexample.py; research/ddp/two_successful_methods_20261101/reviews/A_AND_Q_BOUND_GEMINI_RAW.json; research/ddp/two_successful_methods_20261101/reviews/A_AND_Q_BOUND_DISPOSITION.md"
added: 2026-11-01T04:07:00Z
tags: ["ddp", "method-ledger"]
---

# 四端口三维一般q路线：精确pencil障碍与F25单点反例，未生成新图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-q3-three-step-plane-pencil31`

## Metrics
**对象层级：** symbolic_route_obstruction_and_single_point_counterexample

**目标与阶数：** (100,3)；L=不适用／见变体；条件性n=468750（未据此计纪录）；从属目标：[[100, 3]]

**距目标的证据：** No actual lifted graph or graph diameter measured; complete symbolic route obstruction bound to C30, one F25 target checked；四方向frame下每有向边坏turn恰k=|A∩B|，不同pencil平面6−k，并集q+(6−k)(q²−q)；全turn满秩且pencil全覆仅q5。原C30有30条无triangle/C4外边，沿此边pencil穷尽全部≤3路线，因此q>5实际不可能D3，允许逐边逆相容矩阵/常量位移。F25只验(0,0)→(20,(0,1,alpha))六法向量均非零，目标不可达；缺12000/15625是已证公式值，不是大图BFS坏对数。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_Lean_instances": 0,
  "lifted_graphs_generated": 0,
  "source_graph_BFS_runs": 0,
  "controller_ordered_pairs": 900,
  "raw_controller_words_0_to3": 2550,
  "route_class_counts": {
    "same_layer": 30,
    "nonadjacent": 750,
    "triangle_adjacent": 60,
    "external_adjacent": 60
  },
  "external_undirected_edges": 30,
  "symbolic_identities": {
    "bad_turns_per_directed_edge": "k=|A intersect B|",
    "different_backtrack_planes": "6-k",
    "pencil_union": "q+(6-k)*(q*q-q)",
    "full_pencil_iff": "k=5-q",
    "all_good_turns_and_full_pencil_iff_field_size": 5
  },
  "q_gt5_minimum_missing_per_target_fibre": "q(q-1)(q-5)",
  "q_lt5_excluded": false,
  "global_q_family_claimed_successful": false,
  "hypothetical_F25_order": 468750,
  "hypothetical_F25_degree": 100,
  "F25_counterexample": {
    "source_controller": 0,
    "source_coordinate": [
      0,
      0,
      0
    ],
    "target_controller": 20,
    "target_coordinate": "(0,1,alpha)",
    "field": "F5[alpha]/(alpha^2-2)",
    "target_fibre_size": 15625,
    "reachable_by_proved_formula": 3625,
    "missing_by_proved_formula": 12000,
    "actual_graph_generated": false,
    "BFS": false
  },
  "numeric_CPU_seconds": 0.03933034,
  "field_values_enumerated": [
    5
  ],
  "single_F25_target_check": true,
  "matrix_search": false,
  "full_field_scan": false,
  "static_review_status": "SUCCESS",
  "formalized_in_Lean": false,
  "later_r5_F7_C60_gate": "SEPARATE_F7_KNOWN_NONRECORD_AND_F4_EDGE_DEPENDENT_ACCEPTED_INSTANCES",
  "independent_construction_framework_claimed": false,
  "static_review_model": "gemini-3.8-flash-high",
  "static_review_effort": "high",
  "static_review_selectedModelLabel": "Gemini 3.8 Flash (High)",
  "static_review_thread": "7548e5af-769d-4736-a7d2-0ae080f78318",
  "static_review_scope": "A original-clone/transverse-plane capacity; B four-port q identity, fixedC30 q>5 obstruction and F25 point only; excludes laterF7 chart.",
  "static_review_correction": "Pins cover radius2; newroot reaches targets within3, not2.",
  "static_review_code_execution": false
}
```



**从属变体：**
```json
[
  {
    "label": "general_symbolic_q_gt5_fixedC30_obstruction",
    "actual_n": null,
    "hypothetical_n": null,
    "actual_D": null,
    "scope": "General finite field order q>5 under exact four-port full-line hypotheses"
  },
  {
    "label": "F25_single_target_counterexample",
    "target": [
      100,
      3
    ],
    "actual_n": null,
    "hypothetical_n": 468750,
    "actual_D": null,
    "actual_graph_generated": false,
    "BFS": false
  }
]
```

**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/PREDICTION.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/PREDICTION.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/READ_SCOPE.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/READ_SCOPE.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/ALL_CONTROLLER_ROUTE_CLASSES.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/ALL_CONTROLLER_ROUTE_CLASSES.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/EXTERNAL_EDGE_0_20.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/EXTERNAL_EDGE_0_20.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/FOUR_PORT_PROJECTIVE_TRIPLES.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/FOUR_PORT_PROJECTIVE_TRIPLES.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/F25_COUNTEREXAMPLE_PREDICTION.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/F25_COUNTEREXAMPLE_PREDICTION.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/F25_COUNTEREXAMPLE.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/F25_COUNTEREXAMPLE.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/check_once.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/check_once.py)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/check_F25_counterexample.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/check_F25_counterexample.py)；[research/ddp/two_successful_methods_20261101/reviews/A_AND_Q_BOUND_GEMINI_RAW.json](../../research/ddp/two_successful_methods_20261101/reviews/A_AND_Q_BOUND_GEMINI_RAW.json)；[research/ddp/two_successful_methods_20261101/reviews/A_AND_Q_BOUND_DISPOSITION.md](../../research/ddp/two_successful_methods_20261101/reviews/A_AND_Q_BOUND_DISPOSITION.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Complete Fq^3 fibres, simple4regular controller with shared four-direction projective frame; invertible edge-dependent matrices, true inverse reverse edges, direction-line compatibility, full one-dimensional noise. Actual q>5 exclusion requires at least one controller edge in neither a triangle nor a4cycle (fixedC30 has30). Certificate-only uniqueness q5 is distinct from actual q>5 exclusion. F25 literal embedding is one concrete counterexample, not a generated468750-point graph.

**正向保证：** 一般q恒等式为纸面推导，绑定到全部900控制点对/2550个0..3端口词及四port交数0。；F5字面数据36turn满秩与pencil覆盖继承；单点F25域嵌入保持逆与非零行列式，仍出现实际短路遗漏。；q<5的partial-rank/多路线联合与其它控制器/端口数/维数/非直线或非uniform fibre不被排除。

**仍未完成：** 一般q结论尚未Lean；首批Gemini实际SUCCESS，支持限定推导，不覆盖后续F7/F4。F7/C60已独验20580、明确非纪录；F4 global纯linear域严格失败后，150逐边独立chart的新域SAT得到3840终图并全3840根独验PASS，另节点保存，不是旧global域被推翻。

**启发与重启依据：** 保行列式不保短路线互补；原C30仅换q>5或逐边矩阵已无用，需增加相邻层短控制路线或实质改变端口/层关系。下一生成方向必须离开承重假设，不自动扩字段或重跑已闭q3模板。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

