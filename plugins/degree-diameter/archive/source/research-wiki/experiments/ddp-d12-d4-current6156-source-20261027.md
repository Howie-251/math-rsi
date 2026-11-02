---
type: experiment
node_id: exp:ddp-d12-d4-current6156-source-20261027
title: "(12,4)6156真实源：76×81成立，全12正则无增点接口"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d12_D4_current6156/REPORT.md; research/ddp/more_graphs_20261027/d12_D4_current6156/RESULT.json"
added: 2026-10-27T18:21:15Z
tags: ["ddp", "method-ledger"]
---

# (12,4)6156真实源：76×81成立，全12正则无增点接口

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,4)；L=6156；known_source_or_recovery n=6156

**距目标的证据：** 6156/36936全degree12、free0。76=4×19 controller，4底点permutations a=(0123),b=(0132)及Z19 voltages；F3^4每fiber81，152相邻fiberpairs每243边，每点四fibers各3neighbors，literal quotient匹配recipe，α/βorder76不是involutions。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 6156,
  "source_m": 36936,
  "degree12": 6156,
  "free_vertices": 0,
  "controller_n": 76,
  "fiber_n": 81,
  "fiber_pairs": 152,
  "edges_per_fiber_pair": 243,
  "profile_CPU": 0.067733,
  "BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d12_D4_current6156/REPORT.md](../../research/ddp/more_graphs_20261027/d12_D4_current6156/REPORT.md)；[research/ddp/more_graphs_20261027/d12_D4_current6156/RESULT.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 6156/36936全degree12、free0。76=4×19 controller，4底点permutations a=(0123),b=(0132)及Z19 voltages；F3^4每fiber81，152相邻fiberpairs每243边，每点四fibers各3neighbors，literal quotient匹配recipe，α/βorder76不是involutions。

**仍未完成：** No complete newgraph in this finite experiment; unrelatedrules and finalLean remain open.

**启发与重启依据：** 零free仅关闭固定cap12保全部旧边的连通增点。新80controller必须改变生成规则；作者已报告固定strict wordfilter的19..27voltage结果不原样复跑，但后续分析发现strict条件仅充分，不能自动上升为完整图族排除。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

