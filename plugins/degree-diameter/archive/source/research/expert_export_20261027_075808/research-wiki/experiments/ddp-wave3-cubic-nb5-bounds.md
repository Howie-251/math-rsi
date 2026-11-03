---
type: experiment
node_id: exp:ddp-wave3-cubic-nb5-bounds
title: "三价exact-NB4/NB5控制器谱与计数界"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/REPORT.md; research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/RESULTS.json; research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/terminal.json"
added: 2026-10-27T07:55:16Z
tags: ["ddp", "method-ledger"]
---

# 三价exact-NB4/NB5控制器谱与计数界

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (?,?)；L=不适用／见变体

**距目标的证据：** NB4阶≤20；NB5阶≤44，42/44开放，不声称≤40。

**其他指标（保持原计数类型）：**
```json
{
  "controller_Delta": 3,
  "exact_NB4_order_bound": 20,
  "exact_NB5_order_bound": 44,
  "NB5_open_orders": [
    42,
    44
  ],
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/REPORT.md](../../research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/REPORT.md)；[research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/RESULTS.json](../../research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/RESULTS.json)；[research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/terminal.json](../../research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅cubic exact-NB4/5控制器，odd-label fiber chart尚未给出

**正向保证：** 自含有理谱与有限域算术检查

**仍未完成：** 未构造42/44图；不能自动映射到某个27格提升目标。

**启发与重启依据：** 有真实odd-label chart和控制器正向结构才继续。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

