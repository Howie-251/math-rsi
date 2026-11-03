---
type: experiment
node_id: exp:ddp-h9-d12-ninepin-coreguard-20261027
title: "N12九pin先修核心再补外围：120项0图，预测被反驳"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/RESULT.json"
added: 2026-10-27T14:08:26Z
tags: ["ddp", "method-ledger"]
---

# N12九pin先修核心再补外围：120项0图，预测被反驳

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-controlled-variant-no-new-graph

**目标与阶数：** (12,5)；L=42342；条件性n=42398（未据此计纪录）

**距目标的证据：** 96项无单coreguard；24项有guard，其中19项全部guard+exacttwo尾穷尽无解、5项限时UNKNOWN。0图，120项全访问，计时22.6116父+child CPU，初始NumPyimport未计入。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "source_n": 42397,
  "scope_items": 120,
  "no_coreguard": 96,
  "exact_restricted_nohit": 19,
  "limited_unknown": 5,
  "prediction_supported": false,
  "unattempted": 0,
  "all_three_anchor_family_excluded": false,
  "allsource_BFS_executed": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed42397,120 degreelegal saturatedpin deletions after skipping acceptedpool43 and5degreeblocked. Firstanchor mustcoverevery missingcore vertex<41356; remaining at mosttwoanchors coverextras.

**正向保证：** No-coreguard only rejects this restricted generationrule, not cooperative three-anchor corecoverage.；P at leastone completehit was actually tested and refuted.

**仍未完成：** Five guarded cases remain time-limited; all-three-anchor feasibility is not excluded for any no-guard case.

**启发与重启依据：** The successful42397witness does not generalize to a productive coreguard-first batch. Stop thisrestrictedrule; do not renew a timer or declare the entire three-anchor family impossible.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

