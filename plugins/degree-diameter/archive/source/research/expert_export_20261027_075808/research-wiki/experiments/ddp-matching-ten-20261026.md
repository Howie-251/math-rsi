---
type: experiment
node_id: exp:ddp-matching-ten-20261026
title: "2810→2812六匹配扩张十个完整候选"
idea_id: "idea:ddp-matching-augmentation"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU"
duration: "7.344CPU s total"
provenance: "research/ddp/m1_matching_augmentation/INDEPENDENT_CHECK_REPORT.md; research/ddp/m1_matching_augmentation/ranked_results.json"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "augmentation", "no-new-bound", "method-ledger"]
---

# 2810→2812六匹配扩张十个完整候选

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-matching-augmentation`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,5)；L=2810；candidate_graph_or_family n=2812

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=364；Existing Wiki Metrics; no experiment rerun；Exactly10 simple connected7regular2812-vertex candidates checked from allroots; allD6. Bestcandidate02 has364badpairs=350old-old+14new-old. DeletedH has514old-oldbadpairs,164repaired. Generation,preprocess,independentcheck total7.344CPU seconds.



**既有原文指标：** Exactly10 simple connected7regular2812-vertex candidates checked from allroots; allD6. Bestcandidate02 has364badpairs=350old-old+14new-old. DeletedH has514old-oldbadpairs,164repaired. Generation,preprocess,independentcheck total7.344CPU seconds.



**原始证据：** [research/ddp/m1_matching_augmentation/INDEPENDENT_CHECK_REPORT.md](../../research/ddp/m1_matching_augmentation/INDEPENDENT_CHECK_REPORT.md)；[research/ddp/m1_matching_augmentation/ranked_results.json](../../research/ddp/m1_matching_augmentation/ranked_results.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only the predetermined10 candidates were tested, not an exhaustive augmentation search. Across all10 graphs, exact H-distance formulas agree for every old-old and new-old pair. Old-old deletion damage dominates; endpoint selection must combine coverage and path repair. No new bound or further queue.

**启发与重启依据：** Only the predetermined10 candidates were tested, not an exhaustive augmentation search. Across all10 graphs, exact H-distance formulas agree for every old-old and new-old pair. Old-old deletion damage dominates; endpoint selection must combine coverage and path repair. No new bound or further queue.

**单独的重启条件：** Endpoint choices must jointly handle deleted old-old paths and new-point coverage.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

