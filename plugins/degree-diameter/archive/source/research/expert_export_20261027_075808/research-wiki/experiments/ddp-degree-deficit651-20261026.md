---
type: experiment
node_id: exp:ddp-degree-deficit651-20261026
title: "651点图移动唯一度数缺口的有限邻域"
idea_id: "idea:ddp-matching-augmentation"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU per task"
duration: "9.425 CPU s +7.679 selected lookahead"
provenance: "research/ddp/degree_deficit651/REPORT.md; research/ddp/degree_deficit651/LOOKAHEAD.md"
added: 2026-10-27T07:55:14Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# 651点图移动唯一度数缺口的有限邻域

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-matching-augmentation`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=651

**距目标的证据：** 59坏对图的全部3230合法单步：min61、median109、max138，无改善/中性。两个61最优邻居各自3230步均唯一改善回原59图，其余均>61。



**既有原文指标：** 59坏对图的全部3230合法单步：min61、median109、max138，无改善/中性。两个61最优邻居各自3230步均唯一改善回原59图，其余均>61。



**原始证据：** [research/ddp/degree_deficit651/REPORT.md](../../research/ddp/degree_deficit651/REPORT.md)；[research/ddp/degree_deficit651/LOOKAHEAD.md](../../research/ddp/degree_deficit651/LOOKAHEAD.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只检查源单步及两个指定邻居，不是全部二步或全图排除。精确bitset评分经已知650正例、651源和实际moves全BFS对照；未运行退火。固定源修复暂时停下。

**启发与重启依据：** 只检查源单步及两个指定邻居，不是全部二步或全图排除。精确bitset评分经已知650正例、651源和实际moves全BFS对照；未运行退火。固定源修复暂时停下。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

