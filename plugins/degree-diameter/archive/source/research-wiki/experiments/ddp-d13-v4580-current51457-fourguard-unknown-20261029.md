---
type: experiment
node_id: exp:ddp-d13-v4580-current51457-fourguard-unknown-20261029
title: "Current51457 v4580：自然重叠整块充分域阴性，真正四guard R4仍UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-29"
hardware: ""
duration: ""
provenance: "research/ddp/refresh_20261029/d13_joint_capacity_read/READ_SCOPE.json; research/ddp/refresh_20261029/d13_joint_capacity_read/REPORT.md; research/ddp/refresh_20261029/d13_joint_capacity_read/ANALYSIS.json; research/ddp/refresh_20261029/d13_joint_capacity_read/CURRENT_LITERAL_CAPACITY.json; research/ddp/refresh_20261029/d13_v4580_fourguard/PREDICTION.json; research/ddp/refresh_20261029/d13_v4580_fourguard/prepared.json; research/ddp/refresh_20261029/d13_v4580_fourguard/MODEL.json; research/ddp/refresh_20261029/d13_v4580_fourguard/RESULT.json; research/ddp/refresh_20261029/d13_v4580_fourguard/TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_fourguard/PREPARE_TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_fourguard/SAT_TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_fourguard/HANDLE.json; research/ddp/refresh_20261029/d13_v4580_fourguard/mandatory.pins.txt; research/ddp/refresh_20261029/d13_v4580_fourguard/run_once.py; research/ddp/refresh_20261029/d13_v4580_fractional_gate/PREDICTION.md; research/ddp/refresh_20261029/d13_v4580_fractional_gate/RESULT.json; research/ddp/refresh_20261029/d13_v4580_fractional_gate/HANDLE.json; research/ddp/refresh_20261029/d13_v4580_fractional_gate/lp_once.py; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/frozen91.json; research/ddp/refresh_20261029/SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md; research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/FROZEN_POOL.json; research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/PREDICTION.json; research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/REPORT.md; research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/RESULT.json; research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/TERMINAL.json; research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/run_once.py; research/ddp/refresh_20261029/Q8_CYCLIC_D13_KERNEL_WIKI_REPORT.md; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/ALL_BLOCK_OWNERSHIP_RESULT.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/ALL_BLOCK_OWNERSHIP_TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/BLOCKS.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/GUARD_BLOCK_MASKS.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/HARD_BLOCK_READOUT.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_DP_STATES.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_RESULT.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_UNION_READOUT.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/PREDICTION.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/REPORT.md; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/RESULT.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/run_once.py; research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/run_overlap_once.py; research/ddp/refresh_20261029/Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_REPORT.md; research/ddp/refresh_20261029/d13_v4580_column_dominance/PREDICTION.md; research/ddp/refresh_20261029/d13_v4580_column_dominance/REPORT.md; research/ddp/refresh_20261029/d13_v4580_column_dominance/RESULT.json; research/ddp/refresh_20261029/d13_v4580_column_dominance/TERMINAL.json; research/ddp/refresh_20261029/d13_v4580_column_dominance/check.cpp; research/ddp/refresh_20261029/d13_v4580_column_dominance/run_once.py; research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md"
added: 2026-10-29T21:49:56Z
tags: ["ddp", "method-ledger"]
---

# Current51457 v4580：自然重叠整块充分域阴性，真正四guard R4仍UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** complete-current-target-single-prototype-cover-model

**目标与阶数：** (13,5)；L=51457；条件性n=51458（未据此计纪录）

**距目标的证据：** No candidate graph or global diameter computed; source51457 D5 accepted earlier.；一次完整2755target/13057column SAT60秒UNKNOWN、code0，无模型；aggregate68.829465935CPU。另一次同完整矩阵fractional LP20秒limit UNKNOWN、无primal/dual下界证书，22.439896875CPU；合91.269362810CPU。0新图/全源BFS，不续timer。；后续38池强proxy kernel中v4580只复用已证明至少5guards的强证书下界，未重跑该单例DP；完整R4仍UNKNOWN。；新路线块13个B3中11非空，13057当前guard列产生9种整块mask；正确接受条件是≤4guards取得的完整块目标并集覆盖全部2755，而非所有11块各有负责人。256states/1170transitions完整失败，总CPU0.403699516；只闭该自然整块充分域，真正R4仍UNKNOWN。；全部2755-target guard列的严格包含过滤完成，13057→12961，仅删96约0.74%；96个保留superset见证全精确校验，0.768575CPU，0图读/新球/solver。原四guard存在性仍UNKNOWN。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 51457,
  "source_m": 324863,
  "prototype": 4580,
  "omitted_saturated_pin": 45089,
  "mandatory_pins": [
    4628,
    9574,
    14663,
    20519,
    26997,
    33721,
    37436,
    40798,
    44310
  ],
  "mandatory_count": 9,
  "missing_current_targets": 2755,
  "eligible_current_guards": 13115,
  "unique_nonzero_guard_masks": 13057,
  "guard_budget": 4,
  "SAT_variables": 65285,
  "SAT_clauses": 120260,
  "SAT_calls": 1,
  "SAT_status": "UNKNOWN",
  "SAT_child_CPU_seconds": 60.23667,
  "SAT_aggregate_CPU_seconds": 68.829465935,
  "LP_calls": 1,
  "LP_status": "UNKNOWN_NO_CERTIFICATE",
  "LP_nnz": 8105259,
  "LP_CPU_seconds": 22.439896875000002,
  "combined_CPU_seconds": 91.26936281,
  "source_allroot_BFS": 0,
  "new_candidate_graphs": 0,
  "incumbent": null,
  "LP_primal_certificate": null,
  "LP_dual_certificate": null,
  "current_mandatory_free_prototypes": 38,
  "current_mandatory_blocked_prototypes": 13,
  "old_static_51417_target_count": 2752,
  "do_not_mix_old_masks": true,
  "old51445_problem_is_distinct": true,
  "overlap_aware_whole_route_blocks_status": "COMPLETE_OVERLAP_AWARE_WHOLE_ROUTE_BLOCK_NEGATIVE",
  "whole_route_block_DP_states": 256,
  "whole_route_block_DP_transitions": 1170,
  "whole_route_block_CPU_seconds": 0.403699516,
  "whole_route_block_new_graphs": 0,
  "unrestricted_four_guard_R4_excluded": false,
  "strict_dominance_complete": true,
  "strict_dominance_retained_columns": 12961,
  "strict_dominance_removed_columns": 96,
  "strict_dominance_superset_checks": 96,
  "strict_dominance_new_solver_calls": 0,
  "actual_four_guard_R4_existence_status": "UNKNOWN"
}
```



**从属变体：**
```json
[
  {
    "label": "strong_closedB1_proxy_certificate_only",
    "sufficient_certificate": "N(45089) subset closedB1(mandatory union guards)",
    "guard_lower_bound": 5,
    "available_guard_budget": 4,
    "five_disjoint_supports": [
      {
        "target": 137,
        "old_free_closed_B1_coverers": [
          6209,
          50795,
          50889
        ]
      },
      {
        "target": 577,
        "old_free_closed_B1_coverers": [
          5619
        ]
      },
      {
        "target": 1254,
        "old_free_closed_B1_coverers": [
          10136,
          50901
        ]
      },
      {
        "target": 50015,
        "old_free_closed_B1_coverers": [
          47095,
          47679,
          48482,
          49163,
          49460,
          49879,
          50584,
          51298,
          51323
        ]
      },
      {
        "target": 50828,
        "old_free_closed_B1_coverers": [
          39121,
          42510
        ]
      }
    ],
    "current_graph_extension_argument": "The five listed targets all have original degree13 and no accepted40 step can attach to them. Their closed neighborhoods are unchanged in current51457; current free support can only shrink. Thus this strong one-step proxy cannot work with<=4 guards, but unrestricted R4 cover is not excluded.",
    "excludes_full_R4_model": false
  },
  {
    "label": "fixed38_pool_v4580_reuse_20261029",
    "status": "REUSED_PROVED_STRONG_LOWER_BOUND_EXCEEDS_BUDGET",
    "available_guard_budget": 4,
    "strong_guard_lower_bound": 5,
    "new_v4580_DP_runs": 0,
    "actual_R4_model_excluded": false,
    "related_existing_experiment": "exp:ddp-d13-singlefault-star-family-51457-20261027"
  },
  {
    "label": "natural_overlap_aware_whole_route_block_proxy_v4580_20261029",
    "status": "COMPLETE_OVERLAP_AWARE_WHOLE_ROUTE_BLOCK_NEGATIVE",
    "source_n": 51457,
    "source_m": 324863,
    "missing_targets": 2755,
    "guard_representatives": 13057,
    "guard_cap": 4,
    "local_radius3_expansions": 13,
    "nonempty_blocks": 11,
    "unique_nonzero_block_masks": 9,
    "useful_guards": 53,
    "acceptance": "Union of actual targets in the complete route blocks covered by at most4 guards equals all2755 targets.",
    "DP_states": 256,
    "DP_transitions": 1170,
    "initial_all11_block_ownership_model": "Stricter condition; preserved as history, not used as natural-overlap conclusion.",
    "hard_block": 50828,
    "hard_block_targets": 21,
    "maximum_single_guard_coverage": 18,
    "all_hard_block_targets_have_other_block_membership": true,
    "all_coverable_blocks_union_equals_all2755": true,
    "complete_graphs_generated": 0,
    "source_allroot_BFS": 0,
    "new_selected_R4_BFS": 0,
    "solver_calls": 0,
    "CPU_seconds": 0.403699516,
    "corrected_DP_CPU_seconds": 0.018247001,
    "stopped_no_refinement": true,
    "unrestricted_four_guard_R4_excluded": false
  },
  {
    "label": "complete2755_target_strict_column_dominance_13057_to12961_20261029",
    "status": "COMPLETE_STRICT_COLUMN_DOMINANCE",
    "source_n": 51457,
    "prototype": 4580,
    "mandatory_count": 9,
    "guard_budget": 4,
    "unit_cost": true,
    "conflicts": false,
    "complete_targets": 2755,
    "input_unique_columns": 13057,
    "processed_columns": 13057,
    "retained_inclusion_maximal_columns": 12961,
    "removed_columns": 96,
    "removed_fraction_about": "0.74%",
    "exact_saved_superset_witness_checks": 96,
    "equivalence": "Everydeleted guard can be replaced by a retainedproper superset atunit cost; ifalreadyselected, dropdeletedguard. Retained solutionsareoriginalsolutions.",
    "actual_cover_existence_decided": false,
    "source_graph_reads": 0,
    "new_balls": 0,
    "solver_calls": 0,
    "new_graphs": 0,
    "worker_CPU_seconds": 0.161755,
    "aggregate_compile_run_CPU_seconds": 0.768575,
    "stopped_no_solver_due_small_reduction": true
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/d13_joint_capacity_read/READ_SCOPE.json](../../research/ddp/refresh_20261029/d13_joint_capacity_read/READ_SCOPE.json)；[research/ddp/refresh_20261029/d13_joint_capacity_read/REPORT.md](../../research/ddp/refresh_20261029/d13_joint_capacity_read/REPORT.md)；[research/ddp/refresh_20261029/d13_joint_capacity_read/ANALYSIS.json](../../research/ddp/refresh_20261029/d13_joint_capacity_read/ANALYSIS.json)；[research/ddp/refresh_20261029/d13_joint_capacity_read/CURRENT_LITERAL_CAPACITY.json](../../research/ddp/refresh_20261029/d13_joint_capacity_read/CURRENT_LITERAL_CAPACITY.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/PREDICTION.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/PREDICTION.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/prepared.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/prepared.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/MODEL.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/MODEL.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/RESULT.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/RESULT.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/PREPARE_TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/PREPARE_TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/SAT_TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/SAT_TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/HANDLE.json](../../research/ddp/refresh_20261029/d13_v4580_fourguard/HANDLE.json)；[research/ddp/refresh_20261029/d13_v4580_fourguard/mandatory.pins.txt](../../research/ddp/refresh_20261029/d13_v4580_fourguard/mandatory.pins.txt)；[research/ddp/refresh_20261029/d13_v4580_fourguard/run_once.py](../../research/ddp/refresh_20261029/d13_v4580_fourguard/run_once.py)；[research/ddp/refresh_20261029/d13_v4580_fractional_gate/PREDICTION.md](../../research/ddp/refresh_20261029/d13_v4580_fractional_gate/PREDICTION.md)；[research/ddp/refresh_20261029/d13_v4580_fractional_gate/RESULT.json](../../research/ddp/refresh_20261029/d13_v4580_fractional_gate/RESULT.json)；[research/ddp/refresh_20261029/d13_v4580_fractional_gate/HANDLE.json](../../research/ddp/refresh_20261029/d13_v4580_fractional_gate/HANDLE.json)；[research/ddp/refresh_20261029/d13_v4580_fractional_gate/lp_once.py](../../research/ddp/refresh_20261029/d13_v4580_fractional_gate/lp_once.py)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/frozen91.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/frozen91.json)；[research/ddp/refresh_20261029/SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md](../../research/ddp/refresh_20261029/SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md)；[research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/FROZEN_POOL.json](../../research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/FROZEN_POOL.json)；[research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/PREDICTION.json](../../research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/PREDICTION.json)；[research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/REPORT.md](../../research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/REPORT.md)；[research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/RESULT.json](../../research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/RESULT.json)；[research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/TERMINAL.json](../../research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/TERMINAL.json)；[research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/run_once.py](../../research/ddp/refresh_20261029/d13_remaining_strong_proxy_kernel/run_once.py)；[research/ddp/refresh_20261029/Q8_CYCLIC_D13_KERNEL_WIKI_REPORT.md](../../research/ddp/refresh_20261029/Q8_CYCLIC_D13_KERNEL_WIKI_REPORT.md)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/ALL_BLOCK_OWNERSHIP_RESULT.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/ALL_BLOCK_OWNERSHIP_RESULT.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/ALL_BLOCK_OWNERSHIP_TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/ALL_BLOCK_OWNERSHIP_TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/BLOCKS.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/BLOCKS.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/GUARD_BLOCK_MASKS.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/GUARD_BLOCK_MASKS.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/HARD_BLOCK_READOUT.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/HARD_BLOCK_READOUT.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_DP_STATES.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_DP_STATES.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_RESULT.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_RESULT.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_UNION_READOUT.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/OVERLAP_UNION_READOUT.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/PREDICTION.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/PREDICTION.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/REPORT.md](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/REPORT.md)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/RESULT.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/RESULT.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/run_once.py](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/run_once.py)；[research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/run_overlap_once.py](../../research/ddp/refresh_20261029/d13_v4580_routeblock_proxy/run_overlap_once.py)；[research/ddp/refresh_20261029/Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_REPORT.md](../../research/ddp/refresh_20261029/Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_REPORT.md)；[research/ddp/refresh_20261029/d13_v4580_column_dominance/PREDICTION.md](../../research/ddp/refresh_20261029/d13_v4580_column_dominance/PREDICTION.md)；[research/ddp/refresh_20261029/d13_v4580_column_dominance/REPORT.md](../../research/ddp/refresh_20261029/d13_v4580_column_dominance/REPORT.md)；[research/ddp/refresh_20261029/d13_v4580_column_dominance/RESULT.json](../../research/ddp/refresh_20261029/d13_v4580_column_dominance/RESULT.json)；[research/ddp/refresh_20261029/d13_v4580_column_dominance/TERMINAL.json](../../research/ddp/refresh_20261029/d13_v4580_column_dominance/TERMINAL.json)；[research/ddp/refresh_20261029/d13_v4580_column_dominance/check.cpp](../../research/ddp/refresh_20261029/d13_v4580_column_dominance/check.cpp)；[research/ddp/refresh_20261029/d13_v4580_column_dominance/run_once.py](../../research/ddp/refresh_20261029/d13_v4580_column_dominance/run_once.py)；[research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md](../../research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 当前51457固定prototype4580，删去唯一sat pin45089后的mandatory9全free；全部2755个当前缺项、13057个非零不同guard列、独立guard数<=4。不是旧51445/750目标四guardMIP，也不是41helper joint packing。；后续只做全列严格dominance等价预处理，没有重启原SAT/LP或变更目标/eligibility。

**正向保证：** Source/current target/column绑定完整；mandatory9确有余量，SAT目标是精确guard联合覆盖，不是old2752目标缓存的拼接。；旧40邻点集均只用原51417标签，旧51失败原型中38个mandatory在final仍全free，13个blocked；不能把前38个失败归因于贪心端口锁。；五个两两互斥closedB1支持组只证明强一阶proxy至少5guards；不能否定允许长R4路线的完整四guard域。

**仍未完成：** 固定v4580/current51457真正<=4guard的完整R4覆盖仍UNKNOWN；closedB1强proxy与自然重叠whole-block充分规则已各完整阴性，均不是完整R4的必要条件。一般partial-star、其它mandatory与共同容量问题未排。

**启发与重启依据：** 本完整SAT与LP预算均终止，UNKNOWN保持开放，不能用五组强proxy否定替代R4模型；不恢复51445旧MIP或给本例自动加时。Joint重排需真实原base静态覆盖池，当前40项动态接受证据不能反向当作此池。；50828块21目标单guard最多18，且每目标都在其它块中，不能凭该块零完整支持排重叠联合。实际正确overlap验收也完整阴性，整块规则停止；一般四guard允许分裂目标，未被排除，不追加块细分或旧timer。；完整strict dominance缩减不足1%，不构成续算理由，本批停止，无新solver。原真正四guard问题保持UNKNOWN；不能将等价预处理当阴性证明。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

