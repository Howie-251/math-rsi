---
type: experiment
node_id: exp:ddp-mobius108-schreier-20261027
title: "Möbius置换的Schreier图有限试验"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: "local CPU, one worker per profile"
duration: "1.214109 CPU seconds; final check separately recorded"
provenance: "research/ddp/breadth_20261027/mobius108_schreier/REPORT.md"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "construction", "method-ledger"]
---

# Möbius置换的Schreier图有限试验

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,4)；L=104；candidate_graph_or_family n=108

**距目标的证据：** 实际D=6，目标D=4；原报告bad（类型见详情）=784；Existing Wiki Metrics; no experiment rerun；n=108, degree cap=4, target D=4; independently checked D=6, bad pairs=784.



**既有原文指标：** n=108, degree cap=4, target D=4; independently checked D=6, bad pairs=784.



**原始证据：** [research/ddp/breadth_20261027/mobius108_schreier/REPORT.md](../../research/ddp/breadth_20261027/mobius108_schreier/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 30000个矩阵对；断连样本也计入。有限采样完成；整个作用图族仍开放；未声称任意图不存在或取得新下界。

**启发与重启依据：** 30000个矩阵对；断连样本也计入。有限采样完成；整个作用图族仍开放；未声称任意图不存在或取得新下界。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

