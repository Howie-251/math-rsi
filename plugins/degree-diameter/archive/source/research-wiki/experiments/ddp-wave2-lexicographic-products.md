---
type: experiment
node_id: exp:ddp-wave2-lexicographic-products
title: "全部27格均匀lexicographic产品阶数界"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/lexicographic_products/REPORT.md; research/ddp/breadth_20261027_wave2/lexicographic_products/RESULTS.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 全部27格均匀lexicographic产品阶数界

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** parameter/capacity

**目标与阶数：** (?,?)；L=不适用／见变体

**距目标的证据：** 330个参数对的Moore/degree数值上界筛；无可越线入口。

**其他指标（保持原计数类型）：**
```json
{
  "parameter_pairs": 330,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/lexicographic_products/REPORT.md](../../research/ddp/breadth_20261027_wave2/lexicographic_products/REPORT.md)；[research/ddp/breadth_20261027_wave2/lexicographic_products/RESULTS.json](../../research/ddp/breadth_20261027_wave2/lexicographic_products/RESULTS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** G[H]，connected|G|≥2、任意simple|H|≥2；含均匀independent blowup

**正向保证：** Δ(G[H])=|H|Δ(G)+Δ(H)；D由base及局部replacement约束

**仍未完成：** 不含非均匀blowup或任意replacement。

**启发与重启依据：** 必须改变均匀产品模板，不能换seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

