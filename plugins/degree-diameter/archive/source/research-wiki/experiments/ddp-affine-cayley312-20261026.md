---
type: experiment
node_id: exp:ddp-affine-cayley312-20261026
title: "312阶仿射直积群完整失败"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, at most one worker per bounded batch"
duration: "5.220701 production/prep +0.006707408 independent CPU s"
provenance: "research/ddp/m2_coset_tower/affine_cayley312/REPORT.md"
added: 2026-10-27T08:25:48Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 312阶仿射直积群完整失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,3)；L=253；candidate_graph_or_family n=312

**距目标的证据：** 实际D=4，目标D=3；原报告bad（类型见详情）=3900；Existing Wiki Metrics; no experiment rerun；4060→370 modes;252258 raw;238440 legal full root BFS;noD3. Best312/8/D4,bad3900.



**既有原文指标：** 4060→370 modes;252258 raw;238440 legal full root BFS;noD3. Best312/8/D4,bad3900.



**原始证据：** [research/ddp/m2_coset_tower/affine_cayley312/REPORT.md](../../research/ddp/m2_coset_tower/affine_cayley312/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Full fixedgroup S8 scope; later symbolic filter370→12 is explanatory and not the actual search count.

**启发与重启依据：** Full fixedgroup S8 scope; later symbolic filter370→12 is explanatory and not the actual search count.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

