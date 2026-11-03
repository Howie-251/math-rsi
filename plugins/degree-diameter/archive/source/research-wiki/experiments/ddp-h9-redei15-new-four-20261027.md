---
type: experiment
node_id: exp:ddp-h9-redei15-new-four-20261027
title: "Rédei15已产四图：42399–42402，固定池终态"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_redei15/production/continuation/REPORT.md; research/ddp/more_graphs_20261027/h9_redei15/production/continuation/RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json; research/ddp/more_graphs_20261027/h9_redei15/production/independent_newroot42399.json; reviews/ddp/redei15_20261027.DISPOSITION.md"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# Rédei15已产四图：42399–42402，固定池终态

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,5)；L=42342；candidate_graph_or_family n=42402

**距目标的证据：** 实际D=5，目标D=5；85项once-policy全部终态：4成功、23当时degree阻断、58当时coverage失败，0UNKNOWN。四图完整新增degree与actual-current R4遗漏均0；最强42402/m245937/max12/D5。

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bound_mathematically_verified": true,
  "example_orders": [
    42399,
    42400,
    42401,
    42402
  ],
  "example_count": 4,
  "strongest_n": 42402,
  "strongest_m": 245937,
  "accepted": 4,
  "degree_blocked": 23,
  "coverage_fail": 58,
  "UNKNOWN": 0,
  "full_Lean_instances": 0,
  "review_status": "ACCEPTED_WITH_ARITHMETIC_CORRECTION",
  "actual_reviewer_model": "gemini-3.8-flash-high"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_redei15/production/continuation/REPORT.md](../../research/ddp/more_graphs_20261027/h9_redei15/production/continuation/REPORT.md)；[research/ddp/more_graphs_20261027/h9_redei15/production/continuation/RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/production/continuation/RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json](../../research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json)；[research/ddp/more_graphs_20261027/h9_redei15/production/independent_newroot42399.json](../../research/ddp/more_graphs_20261027/h9_redei15/production/independent_newroot42399.json)；[reviews/ddp/redei15_20261027.DISPOSITION.md](../../reviews/ddp/redei15_20261027.DISPOSITION.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 85项once-policy全部终态：4成功、23当时degree阻断、58当时coverage失败，0UNKNOWN。四图完整新增degree与actual-current R4遗漏均0；最强42402/m245937/max12/D5。

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 新阻塞规则预测得到支持，已交付四个完整阶数。停止已完成固定池；早期失败属于当时基图，不声称最终42402静态不可扩张。当前数学主力迁往其他参数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

