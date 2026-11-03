---
type: experiment
node_id: exp:ddp-h9-d12-eightpin-rare-prefix-20261027
title: "两项八pin稀有目标首选补全：限时UNKNOWN，0新图"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d12_eightpin_rare_target/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_eightpin_rare_target/RESULT.json"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# 两项八pin稀有目标首选补全：限时UNKNOWN，0新图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-controlled-variant-no-new-graph

**目标与阶数：** (12,5)；L=42342；条件性n=42397（未据此计纪录）

**距目标的证据：** 两项均到时UNKNOWN；10.3142父+child CPU，0图，不排除四anchor可行性。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "limited_unknown": 2,
  "unattempted": 0,
  "general_four_anchor_family_excluded": false,
  "allsource_BFS_executed": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_d12_eightpin_rare_target/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_rare_target/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_eightpin_rare_target/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_rare_target/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixedcurrent42396,pools103/577;firstmask mustcoverrarest missingtarget;32x16 bounded prefixes andexacttwo-tail,5CPU peritem.

**正向保证：** No same-base ten-pin pool repeated; no MIP or extra seed.

**仍未完成：** Neither fullfour-anchor feasibility nor the selected32x16prefix class was exhausted.

**启发与重启依据：** Changing prefix bias did not produce a graph in the bounded experiment. Stop this run; do not renew the time limit without a different coverage rule.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

