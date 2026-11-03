---
type: experiment
node_id: exp:ddp-d14-d5-complete-target-r4-cover-mip-20261028
title: "Actual94186 complete94186-target14-pin cover MILP: no returned incumbent,UNKNOWN at CPUguard"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/RESULT.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/MODEL_DIMENSIONS.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/checkpoint.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PROCESS_RECEIPT.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/worker.log; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/worker.py; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/run.py; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/generate.py; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PARENT_HANDLE.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/terminal.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/source94186.edges; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/degree14.u8.bin; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/RESULT.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/BINDING.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/BALLS_META.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/allfree_R4.u64le.bin; research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md; research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/REPORT.md"
added: 2026-10-28T01:03:45Z
tags: ["ddp", "method-ledger"]
---

# Actual94186 complete94186-target14-pin cover MILP: no returned incumbent,UNKNOWN at CPUguard

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** bounded-complete-static-MILP-variant

**目标与阶数：** (14,5)；L=94186；条件性n=94187（未据此计纪录）

**距目标的证据：** Full94187x3685 CSC/60337888nnz constructed in1.883178CPU,thenSciPy/HiGHS callentered. Workerexit-9 with90.206044observedCPU/configured90hard;no solvercallreturn,statusorincumbent. Parentwall150nottriggered. UNKNOWN,0newgraph/fullcandidateOR/newrootBFS;no infeasibilityclaim orstrictfamilyexclusion.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 94186,
  "source_m": 657452,
  "source_D_inherited": 5,
  "source_free_vertices": 3685,
  "source_free_slots": 3700,
  "source_minSatN_inherited": 9,
  "source_fullstar_scan_repeated": false,
  "source_proxy_scan_repeated": false,
  "complete_target_rows": 94186,
  "binary_variables": 3685,
  "cardinality_rows": 1,
  "matrix_rows": 94187,
  "cover_nonzeros": 60334203,
  "total_nonzeros": 60337888,
  "CSC_storage_bytes": 724069400,
  "prep_CPU_seconds": 1.883178,
  "solver_calls_started": 1,
  "solver_calls_returned": 0,
  "solver_status": null,
  "integer_incumbents_returned": 0,
  "solver_requested_time_limit_wall_seconds": 85.116627,
  "configured_worker_soft_CPU_seconds": 89,
  "configured_worker_hard_CPU_seconds": 90,
  "observed_worker_and_descendants_CPU_seconds": 90.20604399999999,
  "observed_parent_wall_seconds": 90.2728743776679,
  "parent_wall_limit_seconds": 150,
  "parent_wall_limit_triggered": false,
  "worker_exit_code": -9,
  "termination_cause": null,
  "source_BFS_count": 0,
  "ball_recomputation": 0,
  "candidate_cached_R4_OR_checks": 0,
  "newroot_BFS": 0,
  "new_graphs": 0,
  "LP_minimum_cardinality_computed": false,
  "infeasibility_certificate": null,
  "prediction": "UNKNOWN",
  "new_lower_bounds": 0,
  "older_partial_history": {
    "rows_started": [
      256,
      1229
    ],
    "returned_integer_candidate_missing_fulltargets": 6430,
    "terminal": "UNKNOWN_PROCESS_KILLED_DURING_SECOND_MODEL",
    "old_CPU_total": null,
    "old_termination_cause": null,
    "not_restarted_or_overwritten": true
  },
  "full_model_dimensions": {
    "variables": 3685,
    "binary_variables": 3685,
    "true_target_cover_rows": 94186,
    "cardinality_rows": 1,
    "rows": 94187,
    "cover_nonzeros": 60334203,
    "total_nonzeros": 60337888,
    "matrix_storage_bytes": 724069400,
    "CSC_data_dtype": "float64",
    "CSC_indices_dtype": "int32",
    "preparation_CPU_seconds": 1.8831779999999998,
    "preparation_wall_seconds": 1.883812490850687,
    "scipy_version": "1.15.3",
    "full_target_model": true,
    "source_BFS": 0,
    "ball_recomputation": 0
  },
  "ordinary_bad_count_units": "null;no newgraph/distance orcandidatecovermeasurements were produced"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/MODEL_DIMENSIONS.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/MODEL_DIMENSIONS.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/checkpoint.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/checkpoint.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PROCESS_RECEIPT.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PROCESS_RECEIPT.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/worker.log](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/worker.log)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/worker.py](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/worker.py)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/run.py](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/run.py)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/generate.py](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/generate.py)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PARENT_HANDLE.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/PARENT_HANDLE.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/terminal.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/complete_target_mip_20261028/terminal.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/source94186.edges](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/source94186.edges)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/degree14.u8.bin](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/degree14.u8.bin)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/BINDING.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/BINDING.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/BALLS_META.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/BALLS_META.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/allfree_R4.u64le.bin](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/allfree_R4.u64le.bin)；[research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actualfixed94186source,choose<=14distinct freevertices fromall3685 andappendonenewvertex adjacentonlytothosepins,retainalloldedges. All94186 cachedclosedR4 targetconstraints+cardinality inone staticMILP,zerofeasibilityobjective. One90CPUconfiguredworker,150wallparentguard;nooldpartialrowloop/LP/star/proxy/BFS/cache recomputation.

**仍未完成：** The fixedsource singlevertex coverquestion remainsunresolved. Noall94187graphs/generalN(14,5) orother augmentationruleisexcluded. Noexactinfeasibilitycertificate/LPbound was produced.

**启发与重启依据：** Buildingthefulltargetsystem is practical at724MB sparsebody and1.88CPU preparation,butthe singleboundedsolvercallprovided noexistenceorinfeasibility result. This differsfromold256/1229-rowUNKNOWN by itscompleteinformation,not by an extra seed. Stopthisbatch;do not converttermination/noincumbent intoUNSAT orautomaticallygrantmoretime. Source/star/proxy/cache resultsareinherited ratherthannewexperiments.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

