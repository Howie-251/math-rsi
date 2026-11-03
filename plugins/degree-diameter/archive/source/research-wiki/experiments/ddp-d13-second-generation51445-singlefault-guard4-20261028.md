---
type: experiment
node_id: exp:ddp-d13-second-generation51445-singlefault-guard4-20261028
title: "Newborn51445 partial-star extension: exact<=2guards fail; sole<=4guard MIP UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/ANALYSIS_PREDICTION.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/ANALYSIS_PREDICTION.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepared.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepared.masks.u64.bin; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mandatory.pins.txt; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/MIP_MODEL.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PREPARE_TERMINAL.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/MIP_TERMINAL.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/LIVE_HANDLE.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepare.log; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip.stdout; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip.stderr; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepare_once.py; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip_once.py; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/run_mip_once.py; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_PRED.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_TERMINAL.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/proxy_kernel.py"
added: 2026-10-28T04:19:15Z
tags: ["ddp", "method-ledger"]
---

# Newborn51445 partial-star extension: exact<=2guards fail; sole<=4guard MIP UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** new-prototype-variant-of-successful-extension-mechanism

**目标与阶数：** (13,5)；L=51417；条件性n=51458（未据此计纪录）

**距目标的证据：** mandatory9覆盖50707/51457，漏750；13115freeguards、13026unique nonzero masks，exact≤2完成0hit。唯一≤4MIP因CPUguard终止(exit−24)，0returned incumbent；主问题UNKNOWN。closedB1proxy余11邻目标中48762/50130无任何freeguard，cap4DP291states无解，只排proxy证书。0图/新下界/selectedR4验证/旧源全D5重验。

**其他指标（保持原计数类型）：**
```json
{
  "main_actual_counts": {
    "prototypes": 1,
    "mandatory_R4_checks": 1,
    "mandatory_covered_targets": 50707,
    "mandatory_missing_targets": 750,
    "eligible_guard_vertices": 13115,
    "unique_nonzero_masks": 13026,
    "exact_at_most_two_complete": true,
    "exact_at_most_two_hits": 0,
    "LP_calls": 0,
    "MIP_calls": 1,
    "returned_incumbents": 0,
    "selected_R4_verify_calls": 0,
    "candidate_graphs": 0,
    "new_lower_bounds": 0,
    "old_source_allroot_BFS": 0,
    "old91_retry": 0
  },
  "initial_batch_CPU_seconds": 29.384419797,
  "total_with_proxy_CPU_seconds": 29.651644798,
  "proxy_kernel": {
    "label": "after-MIP closedB1 full-pin proxy kernel",
    "status": "COMPLETE_PROXY_KERNEL_NO_AT_MOST_FOUR_GUARDS",
    "frozen_after_MIP_feedback": true,
    "full_pin": 35572,
    "Nf_targets_remaining_after_mandatory_B1": 11,
    "raw_kernel_labels": 141,
    "current_free_kernel_labels": 32,
    "nonzero_masks": 30,
    "zero_support_targets": [
      48762,
      50130
    ],
    "exact_cap4_DP_states": 291,
    "strict_closed_scope": "N(f) subset closedB1(mandatory union any currently free guards) is impossible; no assertion about unrestricted R4 four-guard covers.",
    "candidate_graphs": 0,
    "MIP_calls": 0,
    "R4_verify_calls": 0,
    "CPU_seconds": 0.267225001
  },
  "prototype": 51445,
  "source_n": 51457,
  "source_m": 324863,
  "main_current_R4_guard4_status": "UNKNOWN_NO_RETURNED_INCUMBENT",
  "same_source_fullstar_exclusion_not_repeated": true,
  "old91_retry": 0,
  "new_lower_bound_mathematically_verified": false,
  "method_count_note": "Newborn prototype and proxy-kernel variant of the already productive H9 prototype-neighborhood mechanism, not an independent method."
}
```



**从属变体：**
```json
[
  {
    "label": "exact_zero_one_two_guards",
    "status": "COMPLETE_NO_SOLUTION",
    "candidate_graphs": 0,
    "exact": true
  },
  {
    "label": "full_remaining_four_guard_model",
    "status": "UNKNOWN_CPU_GUARD_NO_RETURNED_INCUMBENT",
    "requested_solver_seconds": 25,
    "actual_observable_worker_CPU_seconds": 29.264401,
    "solver_exact_CPU_seconds": null,
    "exit_code": -24,
    "solver_infeasible_claim": false,
    "candidate_graphs": 0
  },
  {
    "label": "after-MIP closedB1 full-pin proxy kernel",
    "status": "COMPLETE_PROXY_KERNEL_NO_AT_MOST_FOUR_GUARDS",
    "frozen_after_MIP_feedback": true,
    "full_pin": 35572,
    "Nf_targets_remaining_after_mandatory_B1": 11,
    "raw_kernel_labels": 141,
    "current_free_kernel_labels": 32,
    "nonzero_masks": 30,
    "zero_support_targets": [
      48762,
      50130
    ],
    "exact_cap4_DP_states": 291,
    "strict_closed_scope": "N(f) subset closedB1(mandatory union any currently free guards) is impossible; no assertion about unrestricted R4 four-guard covers.",
    "candidate_graphs": 0,
    "MIP_calls": 0,
    "R4_verify_calls": 0,
    "CPU_seconds": 0.267225001
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/ANALYSIS_PREDICTION.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/ANALYSIS_PREDICTION.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/ANALYSIS_PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/ANALYSIS_PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepared.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepared.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepared.masks.u64.bin](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepared.masks.u64.bin)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mandatory.pins.txt](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mandatory.pins.txt)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/MIP_MODEL.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/MIP_MODEL.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PREPARE_TERMINAL.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PREPARE_TERMINAL.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/MIP_TERMINAL.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/MIP_TERMINAL.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/LIVE_HANDLE.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/LIVE_HANDLE.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepare.log](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepare.log)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip.stdout](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip.stdout)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip.stderr](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip.stderr)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepare_once.py](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/prepare_once.py)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip_once.py](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/mip_once.py)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/run_mip_once.py](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/run_mip_once.py)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_PRED.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_PRED.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_TERMINAL.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/PROXY_KERNEL_TERMINAL.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/proxy_kernel.py](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/second_generation_singlefault/proxy_kernel.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定已接受51457/324863当前图、新生prototype51445，省略满pin35572，9mandatory不变。实际全部eligibleguards masks完备≤2无解；唯一≤4cover MIP未返回incumbent为UNKNOWN。后置closedB1(full-pin-neighborhood)proxy kernel是另一个更强充分证书，严格被2个zero-support targets阻断，不等同整个R4四guard问题无解。

**正向保证：** The nine pins are current-free and leave four degree slots for guards.；Every missing target has at least one eligible guard coverer.；Old-old D5 is preserved by any legal append retaining all edges; full selected-R4 remains required before accepting a graph.；The full-pin closedB1 proxy is a sufficient whole-sourceR4 certificate; its complete local kernel here is blocked by two targets with no free one-step proxy.

**仍未完成：** 同9pins的任意3/4guard全R4完成仍UNKNOWN；closedB1更强proxy证书已排，不能外推一般51458图或其它源/协同规则。

**启发与重启依据：** 真实新generation与旧原91/fullstar池分开；≤2严格排除、≤4UNKNOWN和proxy子族严格阻断不得合成整族不存在。最新人工策略下本批停止，不续同MIP/guard预算/R2proxy/旧失败pool；若另有实质新结构由root另定。

**单独的重启条件：** No automatic continuation of the same solver, seed or prototype batch. The four-guard question is unresolved; a later decision would need substantive new structural reduction or an explicit reassessment.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

