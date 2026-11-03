---
type: experiment
node_id: exp:ddp-d15-d5-current102060-singlevertex-r4cover15-20261027
title: "Current102060完整810变量/102060行静态R4模型：LP时限、MIP未返回，UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/REPORT.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/PREDICTION.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/PREFLIGHT.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/LP_DIAGNOSTIC.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/CONSTRAINT_GENERATION_LOG.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/RESULT.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/BUDGET.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/cover.cpp; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/build_balls.py; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/solve.py; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/terminal.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/REPORT.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/PREDICTION.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RESULT.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/MODEL_DIMENSIONS.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/LP_RESULT.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/BUDGET_COMPLIANCE.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/checkpoint.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/terminal.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.executed.py; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/run.py; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.py; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/FUTURE_TIMER_FIX.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.json"
added: 2026-10-28T04:19:15Z
tags: ["ddp", "method-ledger"]
---

# Current102060完整810变量/102060行静态R4模型：LP时限、MIP未返回，UNKNOWN

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (15,5)；L=102060；条件性n=102061（未据此计纪录）

**距目标的证据：** 完整CSC19735920nnz建成，prep0.817543CPU。唯一LP返回TIME_LIMIT且objectiveNone；唯一MIP内部限70.91655但未返回，worker−9，aggregate128.110861<130。0incumbent/graph/BFS，不排完整族。95solver子预算无独立硬截止且实际超过，执行缺口如实保存，未renew。

**其他指标（保持原计数类型）：**
```json
{
  "inherited_constraint_generation_window": {
    "source_n": 102060,
    "source_m": 765045,
    "source_reported_D": 5,
    "eligible_pins": 810,
    "source_truncated_R4_roots": 810,
    "source_R4_layer_edge_expansion": "Only source layers0..3; no layer4edge scan",
    "scanned_arcs_layers0to3": 28114290,
    "all_eligible_R4_union": 102060,
    "ball_size_range": [
      24269,
      24414
    ],
    "target_support_range": [
      70,
      309
    ],
    "duplicate_ball_rows": 0,
    "unique_target_support_rows": 102060,
    "full_dense_binary_matrix_allocated": false,
    "initial_constraints": 256,
    "initial_nonzeros": 34312,
    "initial_subset_LP_minimum": 4.847825446878384,
    "MIP_calls": 2,
    "first_submodel_selection_count": 15,
    "first_submodel_fulltarget_missing": 3510,
    "first_submodel_selection_accepted": false,
    "new_true_counterexample_rows": 495,
    "final_constraints": 751,
    "final_nonzeros": 83204,
    "final_MIP_status": 1,
    "final_MIP_status_label": "TIME_LIMIT_NO_INCUMBENT",
    "source_allroot_diameter_BFS": 0,
    "candidate_newroot_BFS": 0,
    "new_lower_bounds": 0,
    "UNKNOWN": 1,
    "prediction": "UNRESOLVED_AT_SHARED_BUDGET",
    "phase1_CPU_seconds": 1.4231423669999999,
    "phase2_parent_children_CPU_seconds": 8.093057796,
    "total_shared_CPU_seconds": 9.516202857,
    "ordinary_bad_count_units": "Not measured:3510is one intermediate pinselection R4-complement, not graphunordered badpairs",
    "old100132_reused": false
  },
  "complete_static_window": {
    "name": "complete-static-102060targets-20261028",
    "status": "UNKNOWN_WORKER_LIMIT_OR_ERROR_NO_RETURN",
    "scope": "Exactly810 binary pin variables and all102060 actualtarget rows pluscardinality<=15",
    "full_target_rows": 102060,
    "matrix_shape": [
      102061,
      810
    ],
    "cover_nonzeros": 19735110,
    "total_nonzeros": 19735920,
    "LP_calls": 1,
    "MIP_calls": 1,
    "LP_raw_status": 1,
    "MIP_returned": false,
    "integer_incumbent_returned": false,
    "preparation_CPU_seconds": 0.8175429999999999,
    "execution_receipt": {
      "worker_exit_code": -9,
      "worker_child_CPU_seconds": 128.085535,
      "driver_CPU_seconds": 0.025324718999999996,
      "aggregate_CPU_seconds": 128.11086108799998,
      "wall_seconds": 128.76969941332936,
      "aggregate_CPU_budget_seconds": 130,
      "compile_CPU_seconds": 0,
      "workers": 1,
      "threads": 1,
      "retry_count": 0
    },
    "budget_compliance": {
      "aggregate_CPU_budget_seconds": 130,
      "actual_aggregate_CPU_seconds": 128.11086108799998,
      "aggregate_budget_respected": true,
      "preparation_CPU_limit_seconds": 25,
      "actual_preparation_CPU_seconds": 0.8175429999999999,
      "preparation_budget_respected": true,
      "LP_calls": 1,
      "MIP_calls": 1,
      "LP_configured_time_limit_seconds": 20.0,
      "MIP_configured_time_limit_seconds": 70.91655,
      "configured_solver_time_limit_sum_seconds": 90.91655,
      "solver_sub_budget_seconds": 95,
      "observed_LP_call_CPU_seconds": 24.083450000000003,
      "observed_CPU_after_MIP_checkpoint_until_exit": 103.16507099999998,
      "observed_LP_call_plus_MIP_running_phase_CPU_seconds": 127.24852099999998,
      "solver_sub_budget_externally_enforced_in_this_run": false,
      "execution_gap": "The native MIP call did not return at its internal limit; the95CPU solver-stage budget had no separate OS deadline. Aggregate130CPU was enforced, but this solver sub-budget was exceeded. No returned MIP status or incumbent is available.",
      "worker_exit_code": -9,
      "worker_soft_hard_CPU_limits": [
        127,
        128
      ],
      "workers": 1,
      "threads": 1,
      "retry_count": 0
    },
    "source_BFS": 0,
    "ball_recomputation": 0,
    "dedup_repeated": false,
    "constraint_generation": false,
    "actual_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "family_strictly_excluded": false,
    "report_paths": [
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/REPORT.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/PREDICTION.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RESULT.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/MODEL_DIMENSIONS.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/LP_RESULT.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/BUDGET_COMPLIANCE.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/checkpoint.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RUN_HANDLE.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/terminal.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.executed.py",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/run.py",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.py",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/FUTURE_TIMER_FIX.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.json"
    ]
  },
  "independent_method_count_increment": 0
}
```



**从属变体：**
```json
[
  {
    "name": "complete-static-102060targets-20261028",
    "status": "UNKNOWN_WORKER_LIMIT_OR_ERROR_NO_RETURN",
    "scope": "Exactly810 binary pin variables and all102060 actualtarget rows pluscardinality<=15",
    "full_target_rows": 102060,
    "matrix_shape": [
      102061,
      810
    ],
    "cover_nonzeros": 19735110,
    "total_nonzeros": 19735920,
    "LP_calls": 1,
    "MIP_calls": 1,
    "LP_raw_status": 1,
    "MIP_returned": false,
    "integer_incumbent_returned": false,
    "preparation_CPU_seconds": 0.8175429999999999,
    "execution_receipt": {
      "worker_exit_code": -9,
      "worker_child_CPU_seconds": 128.085535,
      "driver_CPU_seconds": 0.025324718999999996,
      "aggregate_CPU_seconds": 128.11086108799998,
      "wall_seconds": 128.76969941332936,
      "aggregate_CPU_budget_seconds": 130,
      "compile_CPU_seconds": 0,
      "workers": 1,
      "threads": 1,
      "retry_count": 0
    },
    "budget_compliance": {
      "aggregate_CPU_budget_seconds": 130,
      "actual_aggregate_CPU_seconds": 128.11086108799998,
      "aggregate_budget_respected": true,
      "preparation_CPU_limit_seconds": 25,
      "actual_preparation_CPU_seconds": 0.8175429999999999,
      "preparation_budget_respected": true,
      "LP_calls": 1,
      "MIP_calls": 1,
      "LP_configured_time_limit_seconds": 20.0,
      "MIP_configured_time_limit_seconds": 70.91655,
      "configured_solver_time_limit_sum_seconds": 90.91655,
      "solver_sub_budget_seconds": 95,
      "observed_LP_call_CPU_seconds": 24.083450000000003,
      "observed_CPU_after_MIP_checkpoint_until_exit": 103.16507099999998,
      "observed_LP_call_plus_MIP_running_phase_CPU_seconds": 127.24852099999998,
      "solver_sub_budget_externally_enforced_in_this_run": false,
      "execution_gap": "The native MIP call did not return at its internal limit; the95CPU solver-stage budget had no separate OS deadline. Aggregate130CPU was enforced, but this solver sub-budget was exceeded. No returned MIP status or incumbent is available.",
      "worker_exit_code": -9,
      "worker_soft_hard_CPU_limits": [
        127,
        128
      ],
      "workers": 1,
      "threads": 1,
      "retry_count": 0
    },
    "source_BFS": 0,
    "ball_recomputation": 0,
    "dedup_repeated": false,
    "constraint_generation": false,
    "actual_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "family_strictly_excluded": false,
    "report_paths": [
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/REPORT.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/PREDICTION.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RESULT.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/MODEL_DIMENSIONS.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/LP_RESULT.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/BUDGET_COMPLIANCE.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/checkpoint.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RUN_HANDLE.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/terminal.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.executed.py",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/run.py",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.py",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/FUTURE_TIMER_FIX.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.json",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.md",
      "research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.json"
    ]
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/REPORT.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/REPORT.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/PREDICTION.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/PREDICTION.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/PREFLIGHT.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/PREFLIGHT.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/LP_DIAGNOSTIC.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/LP_DIAGNOSTIC.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/CONSTRAINT_GENERATION_LOG.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/CONSTRAINT_GENERATION_LOG.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/RESULT.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/BUDGET.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/BUDGET.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/cover.cpp](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/cover.cpp)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/build_balls.py](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/build_balls.py)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/solve.py](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/solve.py)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/terminal.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/monotone_R4_cover/terminal.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/REPORT.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/REPORT.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/PREDICTION.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/PREDICTION.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RESULT.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/MODEL_DIMENSIONS.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/MODEL_DIMENSIONS.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/LP_RESULT.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/LP_RESULT.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/BUDGET_COMPLIANCE.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/BUDGET_COMPLIANCE.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/checkpoint.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/checkpoint.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/terminal.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/terminal.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.executed.py](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.executed.py)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/run.py](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/run.py)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.py](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/worker.py)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/FUTURE_TIMER_FIX.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/FUTURE_TIMER_FIX.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/full_static_R4_cover/CODE_REVIEW.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/CACHE_INTERFACE_REVIEW.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定实际102060/765045源，保旧边单加一点，至多15个当前degree14 pins。首次完整static810binary/102060coverrows+cap模型；不抽样/CG/已知行去重。旧751row试验保留为不同历史窗口。

**正向保证：** Sourceactualcurrent102060/765045andoldD5acceptanceareinherited;all810eligiblecurrentCSRdegrees14.；All102060targetrowsarepresentwithrowcountsmatchingcachedsupports;nosamplingorconstraintgeneration.；A truecandidatewouldrequireexactbinaryliteralpins,degreefreeandcompletecachedR4OR;nonewasreturned.

**仍未完成：** Complete<=15freepinR4coverremainsunresolved;nogeneralN(15,5)orfullmonotonefamilyexclusion.

**启发与重启依据：** 完整输入可在不到1CPU秒准备，但通用solver仍未给出整数结果；保完整模型。停止此批，不加时/换seed/重编码。以后若有不同结构性覆盖证据由parent另定，不把本UNKNOWN转成不存在。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

