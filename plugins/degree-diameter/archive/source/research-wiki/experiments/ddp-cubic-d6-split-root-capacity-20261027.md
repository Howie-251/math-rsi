---
type: experiment
node_id: exp:ddp-cubic-d6-split-root-capacity-20261027
title: "(3,6)132→133同一拆分：度二根六步容量127先验止损"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/PREDICTION.json"
added: 2026-10-27T18:55:02Z
tags: ["ddp", "method-ledger"]
---

# (3,6)132→133同一拆分：度二根六步容量127先验止损

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity-screen

**目标与阶数：** (3,6)；L=132；条件性n=133（未据此计纪录）

**距目标的证据：** 容量不足已均匀排除这个操作的目标133/Δ3/D6，不将必要容量写成生成图直径或普通坏对数。

**其他指标（保持原计数类型）：**
```json
{
  "newroot_max_degree": 2,
  "ambient_max_degree": 3,
  "radius": 6,
  "radius_capacity_upper_bound": 127,
  "required_order": 133,
  "capacity_deficit": 6,
  "candidate_graphs": 0,
  "source_BFS": 0,
  "candidate_BFS": 0,
  "baseline_date": "2026-10-27",
  "baseline_provenance": "当前父任务给定132；本条没有独立fresh table或literal source132绑定。"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/PREDICTION.json](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/PREDICTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅同一相邻1+2拆分操作。新图必含度二点，最大度3时其R6容量≤1+2+4+8+16+32+64=127<133；未下载或重验132源，未生成133候选，未运行枚举或BFS。

**仍未完成：** 固定source与固定操作的结论不排除其它连接机制、其它source或一般目标阶数图；没有新增下界或Lean实例。

**启发与重启依据：** 先按新低度根容量选择可试直径，D7容量255才允许实际600项。D6重启须改变使新图含度二点的连接机制，非增加split枚举。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

