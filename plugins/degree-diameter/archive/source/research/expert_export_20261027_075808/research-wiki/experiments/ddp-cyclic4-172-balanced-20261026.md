---
type: experiment
node_id: exp:ddp-cyclic4-172-balanced-20261026
title: "172点平衡322底图有限构造"
idea_id: "idea:ddp-bicayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, one worker per batch"
duration: "11.849164041 CPU s includingfinal"
provenance: "research/ddp/m2_coset_tower/cyclic4_172_balanced/REPORT.md"
added: 2026-10-27T07:55:14Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 172点平衡322底图有限构造

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-bicayley-d3`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,3)；L=170；candidate_graph_or_family n=172

**距目标的证据：** 实际D=4，目标D=3；原报告bad（类型见详情）=258；Existing Wiki Metrics; no experiment rerun；64starts576segments994264evaluations3977056rootBFS;bestrootmiss2/5/3/2,D4,bad258.



**既有原文指标：** 64starts576segments994264evaluations3977056rootBFS;bestrootmiss2/5/3/2,D4,bad258.



**原始证据：** [research/ddp/m2_coset_tower/cyclic4_172_balanced/REPORT.md](../../research/ddp/m2_coset_tower/cyclic4_172_balanced/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Basecapacityminimum68vs63for421;wholefamilyopen. All602edges and172roots independentlycheckedonce.

**启发与重启依据：** Basecapacityminimum68vs63for421;wholefamilyopen. All602edges and172roots independentlycheckedonce.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

