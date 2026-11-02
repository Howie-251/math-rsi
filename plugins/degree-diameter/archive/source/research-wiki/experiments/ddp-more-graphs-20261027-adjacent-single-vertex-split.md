---
type: experiment
node_id: exp:ddp-more-graphs-20261027-adjacent-single-vertex-split
title: "同一相邻单点拆分跨D3/D4/D5：固定八源完整范围无命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d3_vertex_split/REPORT.md; research/ddp/more_graphs_20261027/d3_vertex_split/RESULT.json; research/ddp/more_graphs_20261027/d3_vertex_split/PROPOSITION.md; research/ddp/more_graphs_20261027/d3_vertex_split/PREDICTION.json; research/ddp/more_graphs_20261027/d3_vertex_split/terminal.json; research/ddp/more_graphs_20261027/d4_vertex_split/REPORT.md; research/ddp/more_graphs_20261027/d4_vertex_split/RESULT.json; research/ddp/more_graphs_20261027/d4_vertex_split/PROPOSITION.md; research/ddp/more_graphs_20261027/d4_vertex_split/PREDICTION.json; research/ddp/more_graphs_20261027/d4_vertex_split/terminal.json; research/ddp/more_graphs_20261027/d5_vertex_split/REPORT.md; research/ddp/more_graphs_20261027/d5_vertex_split/RESULT.json; research/ddp/more_graphs_20261027/d5_vertex_split/PROPOSITION.md; research/ddp/more_graphs_20261027/d5_vertex_split/PREDICTION.json; research/ddp/more_graphs_20261027/d5_vertex_split/terminal.json"
added: 2026-10-27T11:38:49Z
tags: ["ddp", "method-ledger"]
---

# 同一相邻单点拆分跨D3/D4/D5：固定八源完整范围无命中

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** complete-fixed-operation-finite-enumeration-with-capacity-prefilters

**目标与阶数：** 多目标：D3,Delta8,source253→[8, 3]／L=253；D3,Delta12,source810→[12, 3]／L=810；D4,Delta4,source104→[4, 4]／L=104；D4,Delta6,source441→[6, 4]／L=441；D4,Delta7,source684→[7, 4]／L=684；D5,Delta5,source650→[5, 5]／L=650；D5,Delta6,source1518→[6, 5]／L=1518；D5,Delta7,source2810→[7, 5]／L=2810（逐变体，不合成一个距离）

**距目标的证据：** No successful full target candidate. Eight variant counts are sourcevertices/partitions/necessary-root failures, not ordinary badpairs. Calibration metrics remain inside each variant.；八源共1981530无序分割，其中容量拒1321591、精确新根检查659939，全部规范S侧新根已失败，0完整候选。D5虽NB容量全过，首步geodesic singleton阻碍说明走步数余量不能替代两侧路线互补。

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bounds": 0,
  "fixed_source_variant_count": 8,
  "independent_method_count": 1,
  "all_vertex_scope_complete": true,
  "raw_unordered_partitions": 1981530,
  "capacity_rejections": 1321591,
  "exact_newroot_condition_evaluations": 659939,
  "all_newroot_checks_failed": true,
  "exported_successful_candidate_graphs": 0,
  "producer_success_graphs": 0,
  "calibration_only": {
    "D3_full_graphs": 2,
    "D4_two_root_graphs": 3,
    "D5_two_root_graphs": 3,
    "not_best_candidates": true
  },
  "native_CPU_per_batch": {
    "D3": 0.238373,
    "D4": 0.094959,
    "D5": 0.757271
  },
  "CPU_scope": "native runtime only; each one worker;prep/compile separate.",
  "paper_capacity_exclusions": {
    "D3_degree_targets": [
      4,
      5,
      6,
      7,
      9,
      10,
      11
    ],
    "D3_capacity_maxima": [
      36,
      59,
      113,
      159,
      339,
      507,
      623
    ],
    "D4_degree5": {
      "maximum_capacity": 235,
      "target_n": 253,
      "enumerations": 0
    },
    "D5_degree4": {
      "maximum_capacity": 324,
      "target_n": 365,
      "enumerations": 0
    }
  },
  "counts_are_not_ordinary_bad_pairs": true,
  "random_starts": 0,
  "bad_pair_optimization_moves": 0,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "id": "D3-d8-source253-adjacent-split",
    "label": "D3,Delta8,source253",
    "target": [
      8,
      3
    ],
    "target_Delta": 8,
    "target_D": 3,
    "savedL": 253,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 254
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 253,
    "known_source_m": 1012,
    "known_source_degree_histogram": {
      "8": 253
    },
    "source_credit": "F.Comellas and M.Mitjana,1994;official semidirect Cayley source.",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 253,
      "raw_unordered_nonempty_partitions": 32131,
      "capacity_rejected": 23276,
      "root_conditions_evaluated": 8855,
      "canonical_S_newroot_rejected": 8855,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "canonical_mask": 15,
        "S": [
          33,
          39,
          49,
          103
        ],
        "T": [
          163,
          224,
          234,
          241
        ],
        "source_vertex0_reused_as_S_vertex": true,
        "new_T_vertex": 253,
        "split_new_degrees": [
          5,
          5
        ]
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "One complete expanded calibration graph/allsource BFS; entire predicted ordinary badpair set matched.",
      "scope": "Only this fixed calibration, no optimization.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d3_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d3_vertex_split/d8_RESULT.json",
      "research/ddp/more_graphs_20261027/d3_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d3_vertex_split/enumerate.cpp"
    ]
  },
  {
    "id": "D3-d12-source810-adjacent-split",
    "label": "D3,Delta12,source810",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "target_D": 3,
    "savedL": 810,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 811
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 810,
    "known_source_m": 4860,
    "known_source_degree_histogram": {
      "12": 810
    },
    "source_credit": "Dharunish Yugeswardeenoo,2026-10-07;current official3-base affine-voltage source.",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 810,
      "raw_unordered_nonempty_partitions": 1658070,
      "capacity_rejected": 1283850,
      "root_conditions_evaluated": 374220,
      "canonical_S_newroot_rejected": 374220,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "canonical_mask": 63,
        "S": [
          270,
          282,
          294,
          405,
          415,
          425
        ],
        "T": [
          567,
          581,
          592,
          756,
          761,
          763
        ],
        "source_vertex0_reused_as_S_vertex": true,
        "new_T_vertex": 810,
        "split_new_degrees": [
          7,
          7
        ]
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "One complete expanded calibration graph/allsource BFS; entire predicted ordinary badpair set matched.",
      "scope": "Only this fixed calibration, no optimization.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d3_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d3_vertex_split/d12_RESULT.json",
      "research/ddp/more_graphs_20261027/d3_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d3_vertex_split/enumerate.cpp"
    ]
  },
  {
    "id": "D4-d4-source104-adjacent-split",
    "label": "D4,Delta4,source104",
    "target": [
      4,
      4
    ],
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 105
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 104,
    "known_source_m": 208,
    "known_source_degree_histogram": {
      "4": 104
    },
    "source_credit": "Nishant Bhakar,2026-08-27;104c official source",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 104,
      "raw_unordered_nonempty_partitions": 728,
      "capacity_rejected": 416,
      "root_conditions_evaluated": 312,
      "canonical_S_newroot_rejected": 312,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "S": [
          24,
          25
        ],
        "T": [
          26,
          27
        ],
        "source_vertex_reused_as_S_root": 0,
        "T_root_new_label": 104
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "Two new-root radius4 checks only; no wholegraph diameter/badpair measurement.",
      "scope": "Only both new-root miss sets of fixed firstpartition.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d4_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d4_vertex_split/d4_RESULT.json",
      "research/ddp/more_graphs_20261027/d4_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d4_vertex_split/enumerate.cpp"
    ]
  },
  {
    "id": "D4-d6-source441-adjacent-split",
    "label": "D4,Delta6,source441",
    "target": [
      6,
      4
    ],
    "target_Delta": 6,
    "target_D": 4,
    "savedL": 441,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 442
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 441,
    "known_source_m": 1323,
    "known_source_degree_histogram": {
      "6": 441
    },
    "source_credit": "Rishabh Rajiv,2026-09-24;PSU(3,3) orbit graph",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 441,
      "raw_unordered_nonempty_partitions": 13671,
      "capacity_rejected": 9261,
      "root_conditions_evaluated": 4410,
      "canonical_S_newroot_rejected": 4410,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "S": [
          117,
          170,
          194
        ],
        "T": [
          197,
          208,
          227
        ],
        "source_vertex_reused_as_S_root": 0,
        "T_root_new_label": 441
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "Two new-root radius4 checks only; no wholegraph diameter/badpair measurement.",
      "scope": "Only both new-root miss sets of fixed firstpartition.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d4_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d4_vertex_split/d6_RESULT.json",
      "research/ddp/more_graphs_20261027/d4_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d4_vertex_split/enumerate.cpp"
    ]
  },
  {
    "id": "D4-d7-source684-adjacent-split",
    "label": "D4,Delta7,source684",
    "target": [
      7,
      4
    ],
    "target_Delta": 7,
    "target_D": 4,
    "savedL": 684,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 685
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 684,
    "known_source_m": 2394,
    "known_source_degree_histogram": {
      "7": 684
    },
    "source_credit": "Michel de Messieres,2026-10-05;two-base voltage lift",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 684,
      "raw_unordered_nonempty_partitions": 43092,
      "capacity_rejected": 4788,
      "root_conditions_evaluated": 38304,
      "canonical_S_newroot_rejected": 38304,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "S": [
          40,
          77
        ],
        "T": [
          228,
          267,
          362,
          366,
          561
        ],
        "source_vertex_reused_as_S_root": 0,
        "T_root_new_label": 684
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "Two new-root radius4 checks only; no wholegraph diameter/badpair measurement.",
      "scope": "Only both new-root miss sets of fixed firstpartition.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d4_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d4_vertex_split/d7_RESULT.json",
      "research/ddp/more_graphs_20261027/d4_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d4_vertex_split/enumerate.cpp"
    ]
  },
  {
    "id": "D5-d5-source650-adjacent-split",
    "label": "D5,Delta5,source650",
    "target": [
      5,
      5
    ],
    "target_Delta": 5,
    "target_D": 5,
    "savedL": 650,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 651
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 650,
    "known_source_m": 1625,
    "known_source_degree_histogram": {
      "5": 650
    },
    "source_credit": "Rithwik Gupta,2026-09-08;official650 D5 source, different fromDelorme650 D3.",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 650,
      "raw_unordered_nonempty_partitions": 9750,
      "capacity_rejected": 0,
      "root_conditions_evaluated": 9750,
      "canonical_S_newroot_rejected": 9750,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "S": [
          246
        ],
        "T": [
          251,
          260,
          292,
          500
        ],
        "S_root_label": 0,
        "new_T_root_label": 650
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "Two new-root radius5 checks only; no wholegraph diameter/badpair measurement.",
      "scope": "Only both new-root miss sets of fixed firstpartition.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d5_vertex_split/d5_RESULT.json",
      "research/ddp/more_graphs_20261027/d5_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d5_vertex_split/enumerate.cpp"
    ],
    "geodesic_first_step_obstruction": {
      "source_vertex": 0,
      "exclusive_first_neighbor": 246,
      "example_far_target": 55,
      "number_of_targets_with_this_exclusive_first_neighbor": 11,
      "source_distance_to_each_target": 5,
      "H_distance_from_exclusive_neighbor_to_each_target": 4,
      "other_first_neighbors_H_distance_to_targets": ">4",
      "scope": "Uniqueness of first step, not uniqueness of the entire geodesic; derived from saved calibration plus known sourceD<=5, no new BFS."
    }
  },
  {
    "id": "D5-d6-source1518-adjacent-split",
    "label": "D5,Delta6,source1518",
    "target": [
      6,
      5
    ],
    "target_Delta": 6,
    "target_D": 5,
    "savedL": 1518,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 1519
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 1518,
    "known_source_m": 4554,
    "known_source_degree_histogram": {
      "6": 1518
    },
    "source_credit": "Rishabh Rajiv,2026-08-24;PSL(2,23) coset source fromofficialSageMath sparse6.",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 1518,
      "raw_unordered_nonempty_partitions": 47058,
      "capacity_rejected": 0,
      "root_conditions_evaluated": 47058,
      "canonical_S_newroot_rejected": 47058,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "S": [
          329
        ],
        "T": [
          435,
          533,
          776,
          967,
          981
        ],
        "S_root_label": 0,
        "new_T_root_label": 1518
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "Two new-root radius5 checks only; no wholegraph diameter/badpair measurement.",
      "scope": "Only both new-root miss sets of fixed firstpartition.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d5_vertex_split/d6_RESULT.json",
      "research/ddp/more_graphs_20261027/d5_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d5_vertex_split/enumerate.cpp"
    ],
    "geodesic_first_step_obstruction": {
      "source_vertex": 0,
      "exclusive_first_neighbor": 329,
      "example_far_target": 38,
      "number_of_targets_with_this_exclusive_first_neighbor": 20,
      "source_distance_to_each_target": 5,
      "H_distance_from_exclusive_neighbor_to_each_target": 4,
      "other_first_neighbors_H_distance_to_targets": ">4",
      "scope": "Uniqueness of first step, not uniqueness of the entire geodesic; derived from saved calibration plus known sourceD<=5, no new BFS."
    }
  },
  {
    "id": "D5-d7-source2810-adjacent-split",
    "label": "D5,Delta7,source2810",
    "target": [
      7,
      5
    ],
    "target_Delta": 7,
    "target_D": 5,
    "savedL": 2810,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 2811
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "actual_D_scope": "No accepted full target candidate. Partition/newroot rejection counts only; calibration object explicitly separated.",
    "known_source_n": 2810,
    "known_source_m": 9835,
    "known_source_degree_histogram": {
      "7": 2810
    },
    "source_credit": "Dharunish Yugeswardeenoo,2026-10-07;two-copy semidirect voltage source.",
    "status": "COMPLETE_FIXED_SOURCE_ALL_VERTICES_AND_UNORDERED_PARTITIONS_NO_HIT",
    "counts": {
      "all_source_vertices": 2810,
      "raw_unordered_nonempty_partitions": 177030,
      "capacity_rejected": 0,
      "root_conditions_evaluated": 177030,
      "canonical_S_newroot_rejected": 177030,
      "both_newroots_pass": 0,
      "complete_passers": 0
    },
    "calibration": {
      "purpose": "Fixed firstpartition model calibration only; not best graph or accepted new candidate.",
      "parameters": {
        "split_source_vertex": 0,
        "S": [
          1176
        ],
        "T": [
          1379,
          1405,
          1450,
          1591,
          1817,
          2743
        ],
        "S_root_label": 0,
        "new_T_root_label": 2810
      },
      "actual_full_candidate_n": null,
      "actual_full_candidate_D": null,
      "ordinary_candidate_bad_unordered_pairs": null,
      "type": "Two new-root radius5 checks only; no wholegraph diameter/badpair measurement.",
      "scope": "Only both new-root miss sets of fixed firstpartition.",
      "exact_set_match": true
    },
    "whole_target_candidate_exported": false,
    "scope": "All source vertices, all nonempty unordered partitions ofN(v); exact cap filter counted; adjacent splitpoints, disjoint fullneighbor assignment, every other oldedge retained.",
    "restart_condition": "This fixed operation/source is complete. Requires a genuinely new nonisomorphic source or a changed connection/routing mechanism, not seed/label changes.",
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_vertex_split/REPORT.md",
      "research/ddp/more_graphs_20261027/d5_vertex_split/d7_RESULT.json",
      "research/ddp/more_graphs_20261027/d5_vertex_split/PROPOSITION.md",
      "research/ddp/more_graphs_20261027/d5_vertex_split/enumerate.cpp"
    ],
    "geodesic_first_step_obstruction": {
      "source_vertex": 0,
      "exclusive_first_neighbor": 1176,
      "example_far_target": 254,
      "number_of_targets_with_this_exclusive_first_neighbor": 15,
      "source_distance_to_each_target": 5,
      "H_distance_from_exclusive_neighbor_to_each_target": 4,
      "other_first_neighbors_H_distance_to_targets": ">4",
      "scope": "Uniqueness of first step, not uniqueness of the entire geodesic; derived from saved calibration plus known sourceD<=5, no new BFS."
    }
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d3_vertex_split/REPORT.md](../../research/ddp/more_graphs_20261027/d3_vertex_split/REPORT.md)；[research/ddp/more_graphs_20261027/d3_vertex_split/RESULT.json](../../research/ddp/more_graphs_20261027/d3_vertex_split/RESULT.json)；[research/ddp/more_graphs_20261027/d3_vertex_split/PROPOSITION.md](../../research/ddp/more_graphs_20261027/d3_vertex_split/PROPOSITION.md)；[research/ddp/more_graphs_20261027/d3_vertex_split/PREDICTION.json](../../research/ddp/more_graphs_20261027/d3_vertex_split/PREDICTION.json)；[research/ddp/more_graphs_20261027/d3_vertex_split/terminal.json](../../research/ddp/more_graphs_20261027/d3_vertex_split/terminal.json)；[research/ddp/more_graphs_20261027/d4_vertex_split/REPORT.md](../../research/ddp/more_graphs_20261027/d4_vertex_split/REPORT.md)；[research/ddp/more_graphs_20261027/d4_vertex_split/RESULT.json](../../research/ddp/more_graphs_20261027/d4_vertex_split/RESULT.json)；[research/ddp/more_graphs_20261027/d4_vertex_split/PROPOSITION.md](../../research/ddp/more_graphs_20261027/d4_vertex_split/PROPOSITION.md)；[research/ddp/more_graphs_20261027/d4_vertex_split/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_vertex_split/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_vertex_split/terminal.json](../../research/ddp/more_graphs_20261027/d4_vertex_split/terminal.json)；[research/ddp/more_graphs_20261027/d5_vertex_split/REPORT.md](../../research/ddp/more_graphs_20261027/d5_vertex_split/REPORT.md)；[research/ddp/more_graphs_20261027/d5_vertex_split/RESULT.json](../../research/ddp/more_graphs_20261027/d5_vertex_split/RESULT.json)；[research/ddp/more_graphs_20261027/d5_vertex_split/PROPOSITION.md](../../research/ddp/more_graphs_20261027/d5_vertex_split/PROPOSITION.md)；[research/ddp/more_graphs_20261027/d5_vertex_split/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_vertex_split/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_vertex_split/terminal.json](../../research/ddp/more_graphs_20261027/d5_vertex_split/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** One fixed operation: split sourcev into adjacentu,w; disjoint nonempty parts ofcompleteN(v), no other oldedge change. Eight actualsources acrossD3/D4/D5; every sourcevertex and unorderedpart completed. Separate capacity proof excludes specifiedotherdegree targets without fake enumeration.

**正向保证：** 旧点度不变，新两点度由part大小+1精确控制。；newroot条件只作必要筛；若通过才检查oldold和producer全图BFS，不冒充整图成功。；完整规则和数值预筛在各PROPOSITION中给出；D5受影响旧对可限于R1_H(N)端点，但本批无新根通过，后阶段未执行。

**仍未完成：** Other nonisomorphic253/810/104/441/684/650/1518/2810sources and general targetorder graphs remain open. Multi-split, overlapping attachments and other oldedge changes are different mechanisms, not excluded here.

**启发与重启依据：** 按NB根容量选择参数，容量过线后还要每个最远层目标能从两侧首步到达。当前实际源存在独占首步远目标，邻集不能仅靠相邻两点分开。按约暂停该方向；只在明确改变连接机制或取得有不同覆盖结构的新source时重开，不续seed/局部bad优化或自动跨case。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

