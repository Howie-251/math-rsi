---
type: experiment
node_id: exp:ddp-d15-d4-literal15552-k8-shared64-backbone-20261030
title: "Literal15552(15,4) K8共同64端口骨架：完整支持诊断与必要整数门UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-30"
hardware: "Single-thread HiGHS feasibility call, one45s window; whole batch cap90CPU."
duration: "Diagnostic.143200583+prepare.354100389+process47.296332646=47.793633618CPU;solver47.065159115CPU."
provenance: "research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/HANDLE.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/PORT_MULTIPLICITIES.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/PREDICTION_AND_SCOPE.md; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R2_TRIPLES.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R3_BLOCK_SIGNATURES.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R3_COUNT_SIGNATURES.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/REPORT.md; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/RESULT.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/SUPPORT_INTERFACE.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/TERMINAL.json; research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/run_once.py; research/ddp/refresh_20261029/d15_K8_backbone_integer/INPUT_SCOPE.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/MODEL.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/MODEL_CODE.md; research/ddp/refresh_20261029/d15_K8_backbone_integer/PREDICTION_AND_BUDGET.md; research/ddp/refresh_20261029/d15_K8_backbone_integer/PREPARE_HANDLE.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/PREPARE_TERMINAL.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/SELECTOR_MAP.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/SOLVER_HANDLE.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/SOLVER_TERMINAL.json; research/ddp/refresh_20261029/d15_K8_backbone_integer/prepare.py; research/ddp/refresh_20261029/d15_K8_backbone_integer/solve_backbone_once.py"
added: 2026-10-30T03:29:48Z
tags: ["ddp", "method-ledger"]
---

# Literal15552(15,4) K8共同64端口骨架：完整支持诊断与必要整数门UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (15,4)；L=15552；条件性n=15560（未据此计纪录）

**距目标的证据：** Cached diagnostic:5184 sparse R2 targets reduce to648 literal provider triples, each port lies in3 triples and covers24 sparse targets, so any64-pin T leaves at least3648 sparse targets requiring8-color R3 coverage. Triples are actual affine lines in3 independent directions;72 R3 block/count signatures do not permit merging distinct literal supports. Diagnostic0.143200583CPU,0BFS/balls/source read. Full backbone648binary variables/15553rows/1497528nnz, constraints sumT=64 and R3count+7R2count>=8 for every target, prepared0.354100389CPU. Actual sole HiGHS45s window returned raw1/Status13 time limit: UNKNOWN_NO_ACCEPTED_BACKBONE, solver47.065159115/process47.296332646CPU, aggregate47.793633618CPU including both prior stages.0accepted T/0coloringcalls/0newgraphs; stop, not K8 exclusion.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 15552,
  "source_m": 116316,
  "ports": 648,
  "spare_per_port": 1,
  "helper_count": 8,
  "pins_per_helper": 8,
  "common_T_size": 64,
  "conditional_n": 15560,
  "sparse_R2_targets": 5184,
  "literal_R2_provider_triples": 648,
  "sparse_targets_per_port": 24,
  "uncovered_sparse_targets_lower_bound": 3648,
  "R3_block_signatures": 72,
  "R3_count_signatures": 72,
  "literal_R3_supports_not_merged": true,
  "diagnostic_CPU_seconds": 0.143200583,
  "prepare_CPU_seconds": 0.354100389,
  "binary_variables": 648,
  "rows": 15553,
  "target_rows": 15552,
  "matrix_nnz": 1497528,
  "complete_all_ports": true,
  "complete_all_targets": true,
  "backbone_model_is_necessary_not_complete_graph_model": true,
  "actual_solver_status": "UNKNOWN_NO_ACCEPTED_BACKBONE",
  "raw_HiGHS_status": 1,
  "raw_HiGHS_model_status": 13,
  "solver_calls": 1,
  "solver_CPU_seconds": 47.065159115,
  "process_CPU_seconds": 47.296332646,
  "whole_batch_CPU_seconds": 47.793633618,
  "accepted_backbones": 0,
  "coloring_solver_calls": 0,
  "source_only_coloring_executed": false,
  "source_graph_reads": 0,
  "BFS_runs": 0,
  "new_graphs": 0,
  "current_running": false,
  "pending": [],
  "K8_family_excluded": false,
  "automatic_continuation": false,
  "new_record": false,
  "external_static_review_status": "NOT_YET_RECORDED"
}
```



**从属变体：**
```json
[
  {
    "label": "cached5184_sparse_target_literal_triples_and_R3_shared_signature_diagnostic_20261030",
    "status": "COMPLETE_CACHED_SUPPORT_DIAGNOSTIC",
    "targets": 5184,
    "triples": 648,
    "each_port_sparse_target_multiplicity": 24,
    "at_least3648_sparse_targets_still_need_coloring": true,
    "same_fiber_one_color_restriction_rejected": true,
    "literal_R3_support_rows_not_merged": true,
    "CPU_seconds": 0.143200583,
    "source_reads": 0,
    "BFS_runs": 0,
    "solver_calls": 0
  },
  {
    "label": "full648_by15552_uncolored_K8_backbone_integer_single45window_20261030",
    "status": "UNKNOWN_NO_ACCEPTED_BACKBONE",
    "variables": 648,
    "rows": 15553,
    "matrix_nnz": 1497528,
    "exact_binary_constraint": "R3count+7R2count>=8; sumT=64",
    "model_scope": "Necessary uncolored T gate only; not sufficient for8-color construction",
    "actual_solver_calls": 1,
    "raw_status": 1,
    "raw_HiGHS_status": 13,
    "solver_CPU_seconds": 47.065159115,
    "process_CPU_seconds": 47.296332646,
    "whole_batch_CPU_seconds": 47.793633618,
    "candidates": 0,
    "coloring_solver_calls": 0,
    "new_graphs": 0,
    "source_only_coloring_script_executed": false,
    "K8_family_excluded": false,
    "running": false,
    "pending": []
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/HANDLE.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/HANDLE.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/PORT_MULTIPLICITIES.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/PORT_MULTIPLICITIES.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/PREDICTION_AND_SCOPE.md](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/PREDICTION_AND_SCOPE.md)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R2_TRIPLES.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R2_TRIPLES.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R3_BLOCK_SIGNATURES.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R3_BLOCK_SIGNATURES.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R3_COUNT_SIGNATURES.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/R3_COUNT_SIGNATURES.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/REPORT.md](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/REPORT.md)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/RESULT.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/RESULT.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/SUPPORT_INTERFACE.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/SUPPORT_INTERFACE.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/TERMINAL.json](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/TERMINAL.json)；[research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/run_once.py](../../research/ddp/refresh_20261029/d15_K8_shared_backbone_gate/run_once.py)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/INPUT_SCOPE.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/INPUT_SCOPE.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/MODEL.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/MODEL.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/MODEL_CODE.md](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/MODEL_CODE.md)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/PREDICTION_AND_BUDGET.md](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/PREDICTION_AND_BUDGET.md)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/PREPARE_HANDLE.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/PREPARE_HANDLE.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/PREPARE_TERMINAL.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/PREPARE_TERMINAL.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/SELECTOR_MAP.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/SELECTOR_MAP.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/SOLVER_HANDLE.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/SOLVER_HANDLE.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/SOLVER_TERMINAL.json](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/SOLVER_TERMINAL.json)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/prepare.py](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/prepare.py)；[research/ddp/refresh_20261029/d15_K8_backbone_integer/solve_backbone_once.py](../../research/ddp/refresh_20261029/d15_K8_backbone_integer/solve_backbone_once.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Preserve all edges of the accepted literal15552 degree15/D4 source. Add8 mutually adjacent helpers, each attached to8 distinct degree14 old ports; all8 groups disjoint, forming64-port T. Filling groups to8 loses no solution because648 spare1 ports are available. K8 maximizes h(16-h) common pins in this degree15 clique rule. Whole648 columns and15552 targets encoded; no LP pool/fiber-color/line/symmetry restriction. The current model decides only the necessary uncolored T gate, not full8-color graph feasibility.

**正向保证：** All literal target rows and648 ports retained; R2 subset R3 checked before exact binary OR inequality encoding.；If R2(T) misses a target, every one of8 helper colors needs its own selected R3 provider; uncolored count>=8 is necessary only.；A future accepted T would still require8-color disjoint groups and complete graph acceptance; no T was returned in this run.；Source-only coloring code was not executed and is not counted as a failed experiment.

**仍未完成：** K8 extension remains UNKNOWN. No accepted T, no coloring call, no15560 graph. Exact8-color feasibility is unresolved and unexecuted; a source-only coloring script is not a failed full model. Existing K2 UNKNOWN is separate.

**启发与重启依据：** Shared R2 skeleton geometry has real redundancy but64 ports cannot remove8-color requirements for at least3648 sparse targets. Preserve literal mixed-fiber colors. The complete necessary backbone model stopped at its sole time limit with no T; do not infer infeasibility or extend timer/seed/clique-size ladder. A materially new coverage or integrality fact is needed to reopen this batch.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

