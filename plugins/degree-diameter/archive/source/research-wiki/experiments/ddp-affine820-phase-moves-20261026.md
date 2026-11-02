---
type: experiment
node_id: exp:ddp-affine820-phase-moves-20261026
title: "820点完整生成元相位与组成邻域"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, one worker per batch"
duration: "3.939126 CPU s plus0.006985 edgecomparison"
provenance: "research/ddp/m2_coset_tower/affine_cayley820_phase_moves/REPORT.md"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 820点完整生成元相位与组成邻域

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,3)；L=810；candidate_graph_or_family n=820

**距目标的证据：** 17starts43filteredscans26moves148681actualrootBFS;bestmiss34unchanged.



**既有原文指标：** 17starts43filteredscans26moves148681actualrootBFS;bestmiss34unchanged.



**原始证据：** [research/ddp/m2_coset_tower/affine_cayley820_phase_moves/REPORT.md](../../research/ddp/m2_coset_tower/affine_cayley820_phase_moves/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Finite capacity-surviving neighborhoods only. Finaledges exactly equal auditedsource; no repeatfinalBFS.

**启发与重启依据：** Finite capacity-surviving neighborhoods only. Finaledges exactly equal auditedsource; no repeatfinalBFS.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

