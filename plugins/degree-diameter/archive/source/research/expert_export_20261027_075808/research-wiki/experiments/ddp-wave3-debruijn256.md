---
type: experiment
node_id: exp:ddp-wave3-debruijn256
title: "无向4字母4位状态移位图256及补边障碍"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/debruijn256/REPORT.md; research/ddp/breadth_20261027_wave3/debruijn256/obstruction.json; research/ddp/breadth_20261027_wave3/debruijn256/source.edges; research/ddp/breadth_20261027_wave3/debruijn256/source_check.json; research/ddp/breadth_20261027_wave3/debruijn256/source_distances.json; research/ddp/breadth_20261027_wave3/debruijn256/terminal.json"
added: 2026-10-27T07:55:16Z
tags: ["ddp", "method-ledger"]
---

# 无向4字母4位状态移位图256及补边障碍

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,3)；L=253；candidate_graph_or_family n=256；条件性n=256（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=12354；saved_explicit_graph；实际D4/12354；(27,73)到全部亏度点各至少2步，新增边路线≥5，所有单调补边失败。

**其他指标（保持原计数类型）：**
```json
{
  "edges": 1014,
  "degree_histogram": {
    "6": 4,
    "7": 12,
    "8": 240
  },
  "deficit_vertices": 16,
  "deficit_slots": 20
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/debruijn256/REPORT.md](../../research/ddp/breadth_20261027_wave3/debruijn256/REPORT.md)；[research/ddp/breadth_20261027_wave3/debruijn256/obstruction.json](../../research/ddp/breadth_20261027_wave3/debruijn256/obstruction.json)；[research/ddp/breadth_20261027_wave3/debruijn256/source.edges](../../research/ddp/breadth_20261027_wave3/debruijn256/source.edges)；[research/ddp/breadth_20261027_wave3/debruijn256/source_check.json](../../research/ddp/breadth_20261027_wave3/debruijn256/source_check.json)；[research/ddp/breadth_20261027_wave3/debruijn256/source_distances.json](../../research/ddp/breadth_20261027_wave3/debruijn256/source_distances.json)；[research/ddp/breadth_20261027_wave3/debruijn256/terminal.json](../../research/ddp/breadth_20261027_wave3/debruijn256/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定x--(4x+a)mod256去loops/duplicates；全部旧边保留的Δ8补边

**正向保证：** 真实入边恢复反向邻居，不用模256除4；固定源connected

**仍未完成：** 不排删边重连或其他state图。

**启发与重启依据：** 必须改变旧边保留约束，不能填度余量继续搜。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

