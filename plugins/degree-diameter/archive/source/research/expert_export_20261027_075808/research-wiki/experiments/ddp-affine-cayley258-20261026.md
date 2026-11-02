---
type: experiment
node_id: exp:ddp-affine-cayley258-20261026
title: "258阶四反射轨道完整检查失败"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, at most one worker per bounded batch"
duration: "4.095573 production/prep +0.004713864 independent CPU s"
provenance: "research/ddp/m2_coset_tower/affine_cayley258/REPORT.md"
added: 2026-10-27T07:55:13Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 258阶四反射轨道完整检查失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,3)；L=253；candidate_graph_or_family n=258

**距目标的证据：** 实际D=4，目标D=3；原报告bad（类型见详情）=1935；Existing Wiki Metrics; no experiment rerun；35→18→3 modes;74 reflectionorbits;410478raw,6364illegal,404114legal full rootBFS;noD3. Best258/8/D4,bad1935.



**既有原文指标：** 35→18→3 modes;74 reflectionorbits;410478raw,6364illegal,404114legal full rootBFS;noD3. Best258/8/D4,bad1935.



**原始证据：** [research/ddp/m2_coset_tower/affine_cayley258/REPORT.md](../../research/ddp/m2_coset_tower/affine_cayley258/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** AGL1(43) four-set orbit normalization preserves all4reflections, pairfields enumerateall43². Old10.5m bound never run. All258root unique final done.

**启发与重启依据：** AGL1(43) four-set orbit normalization preserves all4reflections, pairfields enumerateall43². Old10.5m bound never run. All258root unique final done.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

