---
type: experiment
node_id: exp:ddp-wave6-metacyclic78-degree5
title: "78阶degree5 Cayley入口文献止损"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/metacyclic78_degree5/REPORT.md; research/ddp/breadth_20261027_wave6/metacyclic78_degree5/SOURCE_SCOPE.json; research/ddp/breadth_20261027_wave6/metacyclic78_degree5/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# 78阶degree5 Cayley入口文献止损

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** literature-scout

**目标与阶数：** (5,3)；L=72；条件性n=78（未据此计纪录）

**距目标的证据：** 拟定16887集合枚举实际0；不是本地新UNSAT。

**其他指标（保持原计数类型）：**
```json
{
  "planned_sets": 16887,
  "actual_sets": 0,
  "literature_reported_pure_Cayley_optimum": 60,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave6/metacyclic78_degree5/REPORT.md](../../research/ddp/breadth_20261027_wave6/metacyclic78_degree5/REPORT.md)；[research/ddp/breadth_20261027_wave6/metacyclic78_degree5/SOURCE_SCOPE.json](../../research/ddp/breadth_20261027_wave6/metacyclic78_degree5/SOURCE_SCOPE.json)；[research/ddp/breadth_20261027_wave6/metacyclic78_degree5/terminal.json](../../research/ddp/breadth_20261027_wave6/metacyclic78_degree5/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 所读文献报告pureCayley(5,3)最优60；本地未独立复核原分类证明

**仍未完成：** 原始最优性证明未在本地重验；一般非Cayley图不受限制。

**启发与重启依据：** 只有可信反例或机制转到非Cayley才值得继续，不重证旧分类。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

