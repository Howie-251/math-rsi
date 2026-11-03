---
type: experiment
node_id: exp:ddp-f5-fixed3750-restricted-noise-d10d4-two100-families-20261029
title: "Fixed F5 matrices, degree10/D4: global-port100 and triangle/external100 full root gates fail"
idea_id: "idea:ddp-q3-three-step-plane-pencil31"
verdict: no
confidence: high
date: "2026-10-29"
hardware: ""
duration: ""
provenance: "research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/PREDICTION.md; research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/RESULT.json; research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/INPUT_PARAMETERS.json; research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/CASES.jsonl; research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/prepare.py; research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/run.cpp; research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/HANDLE.json; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/PREDICTION.md; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/RESULT.json; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/INPUT_PARAMETERS.json; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/CASES.jsonl; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/prepare.py; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/run.cpp; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/HANDLE.json; research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/LOCAL_PREDICTION_CHECK.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PREDICTION.md; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/INITIAL_ANALYSIS_RESULT.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze_initial.py; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/SECOND_PREDICTION.md; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/RESULT.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze.py; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/LOCAL_SHAPE_CASES.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/ALL_TRIANGLE_LOCAL_CASES.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_RESULT.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_SHAPES.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/triangle_complement.py; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_PREDICTION.md; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_RESULT.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/cycle_gate.py; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_0.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_20.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_28.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_22.json; research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_9.json; reviews/ddp/f5_d10_oddcycle_20261029.response.json; reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md; reviews/ddp/f5_d10_oddcycle_20261029.prompt.md; research/ddp/refresh_20261029/f5_flat_conic_local/PREDICTION.md; research/ddp/refresh_20261029/f5_flat_conic_local/INPUT.json; research/ddp/refresh_20261029/f5_flat_conic_local/RESULT.json; research/ddp/refresh_20261029/f5_flat_conic_local/REPORT.md; research/ddp/refresh_20261029/f5_flat_conic_local/TERMINAL.json; research/ddp/refresh_20261029/f5_flat_conic_local/check_local.py; research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_0.json; research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_20.json; research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_28.json; research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_22.json; research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_9.json; research/ddp/refresh_20261029/F5_STRUCTURAL_TURN_RESULT.json"
added: 2026-10-29T17:51:01Z
tags: ["ddp", "method-ledger"]
---

# Fixed F5 matrices, degree10/D4: global-port100 and triangle/external100 full root gates fail

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-q3-three-step-plane-pencil31`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (10,4)；L=2485；candidate_graph_or_family n=3750；从属目标：[[10, 4]]

**距目标的证据：** Each actual3750/18750 simple10regular candidate checked to first complete-root R4 counterexample; all200 fail atroot0. No exact global D/allpairs reported.；两域分别100/100全失败、0未试，nativeCPU0.082468/0.087869。旧global对称首例root layers[1,10,86,708,2474]，首漏26；新type首例[1,10,84,682,2471]，首漏6。type局部预测另真实10个triangle集×全部external选择覆盖100项：往返word[0,1,2,3]均得25点平面并修复旧26/52，CPU0.000858224、0新增图/BFS；局部SUPPORTED而globalexistenceREFUTED。普通无序坏对及exactglobalD未算。 后续从原200项样本升级为数学统一排除：固定旧controller/矩阵/方向、每条边独立选择且不随x变化的triangle3/external2系数，全部10^60字面赋值不能D4；依据五根完整局部短闭路线及奇五环差集交替矛盾，最终有限检查CPU4.40427237，实际全图枚举0。一次Gemini实际SUCCESS/SOUND AS STATED，静态审阅不冒新数值或Lean。 一次实质改矩阵对照另列：全部T改I、唯一proper6color圆锥方向和对称3/2系数，同fiber五根仅111/111/107/111/105，root0位移(0,2,0)不可≤4；CPU.019305658、0展开图/BFS。仅关该一控制，不用旧矩阵奇环命题冒排所有平移提升。

**其他指标（保持原计数类型）：**
```json
{
  "actual_candidate_graphs_generated": 200,
  "actual_graph_n": 3750,
  "actual_graph_m": 18750,
  "actual_graph_degree": 10,
  "graph_counts_by_variant": {
    "global_port": 100,
    "triangle_external": 100
  },
  "first_root_failures": 200,
  "source_BFS": 0,
  "solver_calls": 0,
  "untested": 0,
  "native_CPU_seconds_sum": 0.17033700000000002,
  "local_saved_rule_check_CPU_seconds": 0.0008582240000000012,
  "CPU_scope": "Saved native worker timings; prepare/compile costs not reconstructed.",
  "actual_global_D": null,
  "ordinary_bad_unordered_pairs": null,
  "new_lower_bound_mathematically_verified": false,
  "same_affine_family_not_independent_methods": true,
  "edgewise_tri3_ext2_obstruction": {
    "mathematically_accepted": true,
    "literal_parameter_settings": "10^60",
    "actual_full_settings_enumerated": 0,
    "new_graphs": 0,
    "new_BFS": 0,
    "formalized_in_Lean": false,
    "new_Lean_instances": 0,
    "fixed_controller_and_matrices": true,
    "coefficients_independent_of_fiber_coordinate": true,
    "review_status": "SUCCESS",
    "review_verdict": "SOUND AS STATED",
    "review_disposition": "reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md",
    "final_cycle_CPU_seconds": 4.40427237
  },
  "changed_matrix_single_control": {
    "H_identity": true,
    "local_prediction": "REFUTED",
    "same_fiber_counts": [
      111,
      111,
      107,
      111,
      105
    ],
    "actual_full_graphs": 0,
    "BFS": 0,
    "global_D": null,
    "CPU_seconds": 0.019305658000000003
  }
}
```



**从属变体：**
```json
[
  {
    "label": "global_inverse_port_pairs_2_and_3",
    "target_Delta": 10,
    "target_D": 4,
    "target": [
      10,
      4
    ],
    "savedL": 2485,
    "n": {
      "actual": 3750,
      "hypothetical": null
    },
    "m": 18750,
    "degree": 10,
    "actual_candidate_graphs": 100,
    "complete_cases": 100,
    "untested": 0,
    "complete_target_passes": 0,
    "first_failed_root": 0,
    "all_cases_root0_failed": true,
    "actual_global_D": null,
    "ordinary_bad_unordered_pairs": null,
    "native_CPU_seconds": 0.082468,
    "first_case_first_missing": 26,
    "first_case_root_layers": [
      1,
      10,
      86,
      708,
      2474
    ],
    "joint_existence_prediction": "REFUTED",
    "source_BFS": 0,
    "exported_positive_graphs": 0,
    "new_solver_calls": 0
  },
  {
    "label": "triangle3_externalC5_2",
    "target_Delta": 10,
    "target_D": 4,
    "target": [
      10,
      4
    ],
    "savedL": 2485,
    "n": {
      "actual": 3750,
      "hypothetical": null
    },
    "m": 18750,
    "degree": 10,
    "actual_candidate_graphs": 100,
    "complete_cases": 100,
    "untested": 0,
    "complete_target_passes": 0,
    "first_failed_root": 0,
    "all_cases_root0_failed": true,
    "actual_global_D": null,
    "ordinary_bad_unordered_pairs": null,
    "native_CPU_seconds": 0.087869,
    "first_case_first_missing": 6,
    "first_case_root_layers": [
      1,
      10,
      84,
      682,
      2471
    ],
    "joint_existence_prediction": "REFUTED",
    "source_BFS": 0,
    "exported_positive_graphs": 0,
    "new_solver_calls": 0,
    "local_prediction": "SUPPORTED",
    "local_word": [
      0,
      1,
      2,
      3
    ],
    "local_controller_walk": [
      0,
      18,
      0,
      2,
      0
    ],
    "repaired_old_labels": [
      26,
      52
    ],
    "local_endpoint_plane_size": 25,
    "triangle_sets_checked": 10,
    "total_literal_cases_covered": 100,
    "local_check_new_graph_generation": 0,
    "local_check_new_BFS": 0,
    "local_check_CPU_seconds": 0.0008582240000000012
  },
  {
    "label": "edgewise_independent_tri3_ext2_fixed_matrices_oddC5_obstruction_20261029",
    "status": "MATHEMATICALLY_ACCEPTED_FIXED_EDGEWISE_FAMILY_D4_EXCLUDED",
    "review_status": "SUCCESS",
    "review_disposition": "reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md",
    "object_level": "finite_exact_algebra_over_fixed_rules_not_generated_graph_batch",
    "source_controller_vertices": 30,
    "fiber_size": 125,
    "hypothetical_graph_n": 3750,
    "hypothetical_graph_degree": 10,
    "target_D": 4,
    "parameter_domain": "One independent3-subset per30 triangle edges and one independent2-subset per30 external edges of F5, reverse set negated, fixedT and directions, independent of x.",
    "literal_parameter_settings": "10^60",
    "actual_full_settings_enumerated": 0,
    "actual_candidate_graphs_generated": 0,
    "new_BFS_runs": 0,
    "new_solver_calls": 0,
    "external_odd_cycle": [
      0,
      20,
      28,
      22,
      9
    ],
    "each_root_closed_word_counts": {
      "0": 1,
      "1": 0,
      "2": 4,
      "3": 2,
      "4": 28
    },
    "external_shapes_per_root": 256,
    "triangle_set_triples_per_root": 1000,
    "all_source_holonomy_image_sizes": [
      5,
      25,
      25,
      25,
      5
    ],
    "relaxed_shape_pass_counts": [
      16,
      16,
      4,
      4,
      6
    ],
    "necessary_root_external_gap_pairs": [
      [
        1,
        2
      ],
      [
        2,
        1
      ]
    ],
    "prediction": "SUPPORTED_BY_FINAL_EXACT_CERTIFICATES_AND_ACCEPTED_SCOPED_PROOF",
    "proof_mechanism": "All-source same-fiber coverage; union over triangle choices is a necessary relaxation; opposite two gap shapes at all five roots would2-edge-color an odd5cycle.",
    "correction": "Initial code used one difference set for traversing one edge fourtimes; corrected to two difference-set sums before finalcycle. Correct root0 has8 fullbacktrack shapes; backtrack fullness is not a necessary condition.",
    "final_five_root_cycle_CPU_seconds": 4.40427237,
    "formalized_in_Lean": false,
    "new_Lean_graph_instances": 0,
    "excluded_only_after_review": null,
    "not_excluded": [
      "coordinate-dependent coefficient rules",
      "changed matrices or controller",
      "different branch allocations",
      "general3750-point degree10/D4 graphs"
    ],
    "evidence_paths": [
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PREDICTION.md",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/INITIAL_ANALYSIS_RESULT.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze_initial.py",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/SECOND_PREDICTION.md",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/RESULT.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze.py",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/LOCAL_SHAPE_CASES.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/ALL_TRIANGLE_LOCAL_CASES.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_RESULT.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_SHAPES.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/triangle_complement.py",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_PREDICTION.md",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_RESULT.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/cycle_gate.py",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_0.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_20.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_28.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_22.json",
      "research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_9.json",
      "reviews/ddp/f5_d10_oddcycle_20261029.response.json",
      "reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md",
      "reviews/ddp/f5_d10_oddcycle_20261029.prompt.md"
    ],
    "review_verdict": "SOUND AS STATED (NO FLAWS FOUND)",
    "review_response": "reviews/ddp/f5_d10_oddcycle_20261029.response.json",
    "review_model": "gemini-3.8-flash-high",
    "review_effort": "high",
    "review_thread": "9c43feb5-a0d1-4b36-a9ae-e041ee7f2559",
    "review_code_execution": false,
    "review_new_BFS": false,
    "accepted_closed_scope": "All10^60 literal fixed per-controller-edge3/2 subset assignments with the old fixed matrices/directions and no dependence on fiber coordinate.",
    "proof_status": "mathematically_accepted_finite_exact_algebra_not_Lean"
  },
  {
    "label": "one_flat_identity_matrix_proper6color_conic_control_20261029",
    "status": "SINGLE_CONIC_LOCAL_PREDICTION_REFUTED",
    "prediction": "REFUTED",
    "target_Delta": 10,
    "target_D": 4,
    "n": {
      "actual": null,
      "hypothetical": 3750
    },
    "actual_expanded_graph": null,
    "rule": "All matrices I; conic vectors(1,t,t^2),t inF5,and(0,0,1); one canonical proper6edge-coloring; triangle{0,1,-1},external{1,-1}.",
    "changed_matrices": true,
    "covered_by_old_matrix_oddcycle_proof": false,
    "exact_scope": "One deterministic conic coloring with symmetric3/2 coefficients; not all identity-map lifts/direction assignments.",
    "literal_candidate_rules": 1,
    "roots": [
      0,
      20,
      28,
      22,
      9
    ],
    "same_fiber_endpoint_counts": [
      111,
      111,
      107,
      111,
      105
    ],
    "all_source_coordinates_equivalent_by_translation": true,
    "exact_counterexample": {
      "controller": 0,
      "source_fiber_coordinate": [
        0,
        0,
        0
      ],
      "target_fiber_displacement": [
        0,
        2,
        0
      ],
      "reachable_within4": false
    },
    "actual_global_D": null,
    "connectivity": null,
    "ordinary_bad_unordered_pairs": null,
    "whole_graphs_expanded": 0,
    "new_BFS": 0,
    "new_solver_calls": 0,
    "new_controller_word_enumerations": 0,
    "coloring_searches": 0,
    "CPU_seconds": 0.019305658000000003,
    "new_Lean_instances": 0,
    "evidence_paths": [
      "research/ddp/refresh_20261029/f5_flat_conic_local/PREDICTION.md",
      "research/ddp/refresh_20261029/f5_flat_conic_local/INPUT.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/RESULT.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/REPORT.md",
      "research/ddp/refresh_20261029/f5_flat_conic_local/TERMINAL.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/check_local.py",
      "research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_0.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_20.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_28.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_22.json",
      "research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_9.json"
    ]
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/PREDICTION.md](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/PREDICTION.md)；[research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/RESULT.json](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/RESULT.json)；[research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/INPUT_PARAMETERS.json](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/INPUT_PARAMETERS.json)；[research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/CASES.jsonl](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/CASES.jsonl)；[research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/prepare.py](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/prepare.py)；[research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/run.cpp](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/run.cpp)；[research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/HANDLE.json](../../research/ddp/refresh_20261029/f5_restricted_noise_d10_D4/HANDLE.json)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/PREDICTION.md](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/PREDICTION.md)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/RESULT.json](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/RESULT.json)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/INPUT_PARAMETERS.json](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/INPUT_PARAMETERS.json)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/CASES.jsonl](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/CASES.jsonl)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/prepare.py](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/prepare.py)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/run.cpp](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/run.cpp)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/HANDLE.json](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/HANDLE.json)；[research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/LOCAL_PREDICTION_CHECK.json](../../research/ddp/refresh_20261029/f5_triangle_noise_d10_D4/LOCAL_PREDICTION_CHECK.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PREDICTION.md](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PREDICTION.md)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/INITIAL_ANALYSIS_RESULT.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/INITIAL_ANALYSIS_RESULT.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze_initial.py](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze_initial.py)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/SECOND_PREDICTION.md](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/SECOND_PREDICTION.md)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/RESULT.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/RESULT.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze.py](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/analyze.py)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/LOCAL_SHAPE_CASES.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/LOCAL_SHAPE_CASES.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/ALL_TRIANGLE_LOCAL_CASES.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/ALL_TRIANGLE_LOCAL_CASES.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_RESULT.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_RESULT.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_SHAPES.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/COMPLEMENT_SHAPES.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/triangle_complement.py](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/triangle_complement.py)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_PREDICTION.md](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_PREDICTION.md)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_RESULT.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_RESULT.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/cycle_gate.py](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/cycle_gate.py)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_0.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_0.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_20.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_20.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_28.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_28.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_22.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_22.json)；[research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_9.json](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/CYCLE_ROOT_9.json)；[reviews/ddp/f5_d10_oddcycle_20261029.response.json](../../reviews/ddp/f5_d10_oddcycle_20261029.response.json)；[reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md](../../reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md)；[reviews/ddp/f5_d10_oddcycle_20261029.prompt.md](../../reviews/ddp/f5_d10_oddcycle_20261029.prompt.md)；[research/ddp/refresh_20261029/f5_flat_conic_local/PREDICTION.md](../../research/ddp/refresh_20261029/f5_flat_conic_local/PREDICTION.md)；[research/ddp/refresh_20261029/f5_flat_conic_local/INPUT.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/INPUT.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/RESULT.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/RESULT.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/REPORT.md](../../research/ddp/refresh_20261029/f5_flat_conic_local/REPORT.md)；[research/ddp/refresh_20261029/f5_flat_conic_local/TERMINAL.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/TERMINAL.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/check_local.py](../../research/ddp/refresh_20261029/f5_flat_conic_local/check_local.py)；[research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_0.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_0.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_20.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_20.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_28.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_28.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_22.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_22.json)；[research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_9.json](../../research/ddp/refresh_20261029/f5_flat_conic_local/ROOT_9.json)；[research/ddp/refresh_20261029/F5_STRUCTURAL_TURN_RESULT.json](../../research/ddp/refresh_20261029/F5_STRUCTURAL_TURN_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原30controller、F5^3与四真逆矩阵固定。域一A0二元/A1取负、A2三元/A3取负，共100；域二真实triangle边三元、externalC5边二元，每无向边按u<v同类型集合、反向取负，共100。实际200个3750/18750/simple10regular图，未声称非同构；不是controller设置。每项首root0 R4失败即停该图，无导出positive。

**正向保证：** 真逆与系数取负保证无向，四目标controller互异保证simple；两域每点度10，新增真实噪声约束不继承full20度D3。；type域与global域分支分配实质不同；任三元Atri差集F5给两次triangle往返的25点平面，旧26/52全100项实际修复。；局部修复不能替代其余同fiber/跨fiber的共同R4覆盖；每项完整首root反例足以否定D4。

**仍未完成：** 已接受的统一排除只作用于固定旧controller/四矩阵/方向且系数逐边固定、不随x变化的3/2域。新增T=I对照仅单规则失败；一般平移提升、coordinate-dependent系数、其它branch或控制器和一般3750点10度D4不排。

**启发与重启依据：** 停止旧固定矩阵全部edgewise/x-independent3/2系数域，不按seed或缺点分数续算；改变矩阵后单个flat-conic控制仍失败，亦停止该具体规则。不同矩阵、coordinate-dependent系数、不同branch分配和一般(10,4)仍开放；本批无下一搜索自动授权。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

