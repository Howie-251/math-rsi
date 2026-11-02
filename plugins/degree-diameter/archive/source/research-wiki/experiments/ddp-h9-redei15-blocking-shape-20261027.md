---
type: experiment
node_id: exp:ddp-h9-redei15-blocking-shape-20261027
title: "Rédei15新覆盖形状：5固定点+5共轭对，10+s pins"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md; research/ddp/more_graphs_20261027/h9_redei15/SHAPE.json; reviews/ddp/redei15_20261027.DISPOSITION.md"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# Rédei15新覆盖形状：5固定点+5共轭对，10+s pins

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-theorem

**目标与阶数：** (12,5)；L=42342

**距目标的证据：** f(x)=x^5的9个图点加6方向点阻塞PG2(F9)全部91条线；最小阻塞、无完整Q-line/Baer13子集。5个Frobenius固定点和5对给10+s pins。极化论证给bare-core R4覆盖。

**其他指标（保持原计数类型）：**
```json
{
  "raw_points": 15,
  "fixed_points": 5,
  "conjugate_pairs": 5,
  "fully_folded_pins": 10,
  "lines_blocked": 91
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md](../../research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md)；[research/ddp/more_graphs_20261027/h9_redei15/SHAPE.json](../../research/ddp/more_graphs_20261027/h9_redei15/SHAPE.json)；[reviews/ddp/redei15_20261027.DISPOSITION.md](../../reviews/ddp/redei15_20261027.DISPOSITION.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** f(x)=x^5的9个图点加6方向点阻塞PG2(F9)全部91条线；最小阻塞、无完整Q-line/Baer13子集。5个Frobenius固定点和5对给10+s pins。极化论证给bare-core R4覆盖。

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 新覆盖邻域允许保住旧核心同时给extras留最多2个anchors；这是改变连接规则的数学依据。actual degree/extras仍须检查，不把局部定理作完整新图。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

