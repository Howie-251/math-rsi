---
type: experiment
node_id: exp:ddp-hierarchical676-insertion-20261026
title: "676点唯一层次插入候选：完整图D6"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU"
duration: "0.5312 CPU s"
provenance: "research/ddp/m2_hierarchical676/REPORT.md; research/ddp/m2_hierarchical676/DISTANCE_RULES.md"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# 676点唯一层次插入候选：完整图D6

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=676

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=2172；Existing Wiki Metrics; no experiment rerun；676 vertices1690 edges,simple connected5regular,D6,2172badpairs. HH0,HB6,HL170,BB14,BL776,LL1206; old-old1309,new-old863,new-new0.



**既有原文指标：** 676 vertices1690 edges,simple connected5regular,D6,2172badpairs. HH0,HB6,HL170,BB14,BL776,LL1206; old-old1309,new-old863,new-new0.



**原始证据：** [research/ddp/m2_hierarchical676/REPORT.md](../../research/ddp/m2_hierarchical676/REPORT.md)；[research/ddp/m2_hierarchical676/DISTANCE_RULES.md](../../research/ddp/m2_hierarchical676/DISTANCE_RULES.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** The40 removed edges are a matching and all group-head pairs are covered, but other necessary routes fail. One deterministic candidate only; no exclusion of the general mechanism.

**启发与重启依据：** The40 removed edges are a matching and all group-head pairs are covered, but other necessary routes fail. One deterministic candidate only; no exclusion of the general mechanism.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

