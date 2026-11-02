---
type: experiment
node_id: exp:ddp-current1141-seven-matching-cuts-onehub-milp-14d3-20261028
title: "Actual1141 seven-matching-cut endpoint hub: single60CPU MILP unknown without incumbent"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/REPORT.md; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/RESULT.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/MODEL_DIMENSIONS.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/LAST_SOLVER_RESULT.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/PROCESS_RECEIPT.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/COMPILE_RECEIPT.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/ANALYSIS_D3_CONSTRAINTS.md; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/ANALYSIS_D3_CONSTRAINTS.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/INCUMBENT_ROUNDS.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/LAZY_PAIR_CONSTRAINTS.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/worker.py; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/verify.cpp; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/run.py; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/terminal.json"
added: 2026-10-28T00:05:37Z
tags: ["ddp", "method-ledger"]
---

# Actual1141 seven-matching-cut endpoint hub: single60CPU MILP unknown without incumbent

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-global-MILP-construction-attempt

**目标与阶数：** (14,3)；L=1141；条件性n=1142（未据此计纪录）

**距目标的证据：** HiGHS status1/time limit/primal_status None; no incumbent and no infeasibility result. Initial9128binary/190229rows/986560nonzeros, including all173821 unique3 middle rows and14125 bounded singleton-first-loss rows.0actualmodifiedgraphs/BFS/lazyrounds. Necessary feasibility prediction remainsUNKNOWN.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 1141,
  "source_m": 7987,
  "source_degree": 14,
  "source_D_inherited": 3,
  "hypothetical_m": 7994,
  "binary_variables": 9128,
  "initial_constraint_rows": 190229,
  "initial_nonzeros": 986560,
  "critical_middle_rows": 173821,
  "first_loss_singleton_rows": 14125,
  "solver_calls": 1,
  "solver_status": 1,
  "solver_primal_status": "None",
  "incumbents": 0,
  "actual_modified_graphs": 0,
  "native_verifier_executions": 0,
  "modified_BFS_root_checks": 0,
  "source_distance_BFS_count": 0,
  "A2_A3_recomputation": 0,
  "lazy_bad_pairs_added": 0,
  "prediction": "UNKNOWN",
  "preparation_CPU_seconds": 0.815519,
  "worker_CPU_seconds_before_exit_snapshot": 59.491913000000004,
  "total_worker_and_all_descendants_CPU_seconds": 59.627412,
  "compile_CPU_seconds_separate": 0.7617419999999999,
  "hard_worker_CPU_seconds": 60,
  "worker_exit_code": 0,
  "new_lower_bounds": 0,
  "strict_infeasibility_certificate": null
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/MODEL_DIMENSIONS.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/MODEL_DIMENSIONS.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/LAST_SOLVER_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/LAST_SOLVER_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/PROCESS_RECEIPT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/PROCESS_RECEIPT.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/COMPILE_RECEIPT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/COMPILE_RECEIPT.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/ANALYSIS_D3_CONSTRAINTS.md](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/ANALYSIS_D3_CONSTRAINTS.md)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/ANALYSIS_D3_CONSTRAINTS.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/ANALYSIS_D3_CONSTRAINTS.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/INCUMBENT_ROUNDS.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/INCUMBENT_ROUNDS.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/LAZY_PAIR_CONSTRAINTS.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/LAZY_PAIR_CONSTRAINTS.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/worker.py](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/worker.py)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/verify.cpp](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/verify.cpp)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/run.py](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/run.py)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/terminal.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual1141 source, exactly7 disjoint oldedges deleted, newhub adjacent to all14 cut endpoints, every other oldedge retained. Single aggregate60CPU worker, at most10 incumbent/exactlazy rounds permitted; actual run only firstMILP round and0incumbents.

**仍未完成：** This exact seven-edge matching/hub family remainsopen. Other cut shapes,arbitrary1142graphs and generalN(14,3) are not excluded. A solver infeasibility status would still require its evidence level to be stated accurately; none occurred here.

**启发与重启依据：** Individual maximum-critical-matching bounds did not settle this source, so this batch coupled all seven cuts,endpointR2coverage and exact short-route necessities globally. The fixed budget supplied no feasible object or exclusion. Stop without automatic extra time,cutcount,helper/source changes; cached model and exactlazy proof remain reusable for a separately bounded substantive continuation.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

