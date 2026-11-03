---
type: experiment
node_id: exp:ddp-m1-d5-prunings-20261026
title: "已有电压图删逆对后对(5,5)的直接迁移"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "CPU; each search single-thread"
duration: "8 explicit candidates"
provenance: "research/ddp/m1_degree5_transfer/REPORT.md"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "candidate-failed", "scoped-evidence", "method-ledger"]
---

# 已有电压图删逆对后对(5,5)的直接迁移

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=702

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=9477；Existing Wiki Metrics; no experiment rerun；702/720两图各4种逆对删边，8张完整五正则图均D6或D7；最佳702图D6，9477坏对。两根与独立全根距离谱相符。



**既有原文指标：** 702/720两图各4种逆对删边，8张完整五正则图均D6或D7；最佳702图D6，9477坏对。两根与独立全根距离谱相符。



**原始证据：** [research/ddp/m1_degree5_transfer/REPORT.md](../../research/ddp/m1_degree5_transfer/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 更长路线允许同机制检验新参数；直接删边尚未成功。下一步用F13共同共轭及缩放降维，有限覆盖完整2+3赋值，不能只从8张子图否定该族。

**启发与重启依据：** 更长路线允许同机制检验新参数；直接删边尚未成功。下一步用F13共同共轭及缩放降维，有限覆盖完整2+3赋值，不能只从8张子图否定该族。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

