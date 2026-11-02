---
type: experiment
node_id: exp:ddp-h3-364-single-port-barrier-20261027
title: "自然H3/364源：28个独立端口要求排除单点增广"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/REPORT.md; research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/RESULT.json"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# 自然H3/364源：28个独立端口要求排除单点增广

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (4,5)；L=364；条件性n=365（未据此计纪录）

**距目标的证据：** 源364点714边，有28个degree3 ports；R4(p)与port集仅交{p}，28个R2球划分全部364点。最小port R4 cover恰28，故≤4 pins的新点不可能；均匀排除20475项，实际枚举0。

**其他指标（保持原计数类型）：**
```json
{
  "source_m": 714,
  "ports": 28,
  "exact_port_cover": 28,
  "combinations_excluded": 20475,
  "combinations_evaluated": 0,
  "CPU_seconds": 0.039194522
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/RESULT.json](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 源364点714边，有28个degree3 ports；R4(p)与port集仅交{p}，28个R2球划分全部364点。最小port R4 cover恰28，故≤4 pins的新点不可能；均匀排除20475项，实际枚举0。

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 端口彼此距离5决定失败；不能靠同一host换4个pins修复。与全4regular的Delorme364源不同，不混用源。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

