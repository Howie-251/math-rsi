---
type: experiment
node_id: exp:ddp-h9-d11-global-single-fault-20261027
title: "N11全几何单fault池17项：完整≤2anchor均失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d11_single_fault_global_pool/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_single_fault_global_pool/RESULT.json; research/ddp/more_graphs_20261027/h9_d11_single_fault_extensions/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_single_fault_extensions/RESULT.json"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# N11全几何单fault池17项：完整≤2anchor均失败

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (11,5)；L=37628；条件性n=37632（未据此计纪录）

**距目标的证据：** Only the stated finite local model/coverage was checked; no complete newgraph.；17/17完整exact≤2anchor无解，base始终37631，5410firstanchors穷尽，0UNKNOWN/未试/新图。这个严格singlefault族关闭，不排其它foldsizes/multiplefaults/rewiring。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "raw_Qlines": 5380830,
  "finite_actual_sets": 17,
  "exact_failures": 17,
  "CPU_seconds": 0.59671,
  "allsource_BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_d11_single_fault_global_pool/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_single_fault_global_pool/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_single_fault_global_pool/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d11_single_fault_global_pool/RESULT.json)；[research/ddp/more_graphs_20261027/h9_d11_single_fault_extensions/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_single_fault_extensions/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_single_fault_extensions/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d11_single_fault_extensions/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All5380830 nonH9Qlines atfixed37631; onlyfullfoldedimage10/exactlyone unique saturateddegree11 pin;deleteit to9pins,all17distinctsets. No overlapold240nearline scope.

**仍未完成：** No result outside the exact stated scope is excluded.

**启发与重启依据：** Retain exact source and finite scope; no same-base restart or unbounded local-score optimization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

