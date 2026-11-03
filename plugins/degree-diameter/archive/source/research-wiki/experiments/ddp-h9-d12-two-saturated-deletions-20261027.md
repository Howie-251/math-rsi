---
type: experiment
node_id: exp:ddp-h9-d12-two-saturated-deletions-20261027
title: "两满度pin删除的29项两路核心修复：有限前缀无图"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d12_eightpin_two_saturated_deletions/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_eightpin_two_saturated_deletions/RESULT.json"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# 两满度pin删除的29项两路核心修复：有限前缀无图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (12,5)；L=42342；条件性n=42398（未据此计纪录）

**距目标的证据：** Only the stated finite local model/coverage was checked; no complete newgraph.；29项selectedprefix全部耗尽，two-core pair=0，故extras-tail调用0。0新图，不能写成所有4anchor无解。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "frozen_items": 29,
  "selected_core_pairs": 0,
  "extras_tail_calls": 0,
  "unknown_preparations": 0,
  "CPU_seconds": 5.928714208,
  "general_four_anchor_infeasible": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_d12_eightpin_two_saturated_deletions/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_two_saturated_deletions/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_eightpin_two_saturated_deletions/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_two_saturated_deletions/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Source42397;29full10pinsets with exactlytwo saturatedpins;removeboth,8pin+<=4anchors. Selectedfirst<=16rarecorecoverers andsecond<=8fullremainingcorecoverers,thenexacttwoextras tail only ifcorepairfound.

**仍未完成：** No result outside the exact stated scope is excluded.

**启发与重启依据：** Retain exact source and finite scope; no same-base restart or unbounded local-score optimization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

