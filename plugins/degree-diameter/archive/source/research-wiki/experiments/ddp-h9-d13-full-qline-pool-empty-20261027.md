---
type: experiment
node_id: exp:ddp-h9-d13-full-qline-pool-empty-20261027
title: "(13,5)完整Q9-line：3640项全被满度pin挡住"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/terminal.json"
added: 2026-10-27T17:26:52Z
tags: ["ddp", "method-ledger"]
---

# (13,5)完整Q9-line：3640项全被满度pin挡住

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (13,5)；L=51417

**距目标的证据：** 3640条F3-defined fullQ9lines一次过滤全部degree阻断；7pin线1764条、10pin线1876条；16条四fixedpins全free的线仍各有3个满度非fixedpair pins，无单满pin删除实例。

**其他指标（保持原计数类型）：**
```json
{
  "lines": 3640,
  "feasible_pool": 0,
  "allfixed_free_lines": 16,
  "blocked_nonfixed_pins_on_each_of16": 3,
  "CPU_seconds": 0.089210711,
  "BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/terminal.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/qline_pool/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 3640条F3-defined fullQ9lines一次过滤全部degree阻断；7pin线1764条、10pin线1876条；16条四fixedpins全free的线仍各有3个满度非fixedpair pins，无单满pin删除实例。

**仍未完成：** No new complete graph in this probe; other parameters and mechanisms remain open.

**启发与重启依据：** 不能把Rédei/Baer空池自动外推Qline；已对更小邻域实际检查。此固定fullmandatory规则也空后停止，不从删2/3pins起机械续修。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

