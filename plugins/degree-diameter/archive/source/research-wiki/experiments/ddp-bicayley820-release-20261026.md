---
type: experiment
node_id: exp:ddp-bicayley820-release-20261026
title: "解除820点Cayley层间约束的实际搜索"
idea_id: "idea:ddp-bicayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, one worker per bounded batch"
duration: "27.846856 profile/prep +0.008524168 exact final relabel CPU s"
provenance: "research/ddp/m2_coset_tower/bicayley820/REPORT.md"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 解除820点Cayley层间约束的实际搜索

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-bicayley-d3`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,3)；L=810；candidate_graph_or_family n=820

**距目标的证据：** 实际D=4，目标D=3；原报告bad（类型见详情）=13940；Existing Wiki Metrics; no experiment rerun；33starts297segments,634601legal evaluations/1269202rootBFS. Bestunchangedsource34/34,D4,bad13940.



**既有原文指标：** 33starts297segments,634601legal evaluations/1269202rootBFS. Bestunchangedsource34/34,D4,bad13940.



**原始证据：** [research/ddp/m2_coset_tower/bicayley820/REPORT.md](../../research/ddp/m2_coset_tower/bicayley820/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** IndependentA/B/T genuinelyrelaxCayleycoupling;fixedphasefamilynotexhausted. Finalgraphidentityinheritspriorall820rootcheck,nonewfullBFS.

**启发与重启依据：** IndependentA/B/T genuinelyrelaxCayleycoupling;fixedphasefamilynotexhausted. Finalgraphidentityinheritspriorall820rootcheck,nonewfullBFS.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

