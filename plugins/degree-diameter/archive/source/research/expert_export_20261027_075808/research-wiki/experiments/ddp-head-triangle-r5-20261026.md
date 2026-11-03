---
type: experiment
node_id: exp:ddp-head-triangle-r5-20261026
title: "7203点三角头固定r5塔：必要商过滤与完整BB失败"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU worker"
duration: "7.828042 CPU seconds including independent checks; small math tables separately recorded"
provenance: "research/ddp/m2_coset_tower/d8_head_triangles/REPORT.md; research/ddp/m2_coset_tower/d8_head_triangles/STRUCTURE_SCOPE.md; research/ddp/m2_coset_tower/d8_head_triangles/QUOTIENT_BB_CHECK.md; research/ddp/m2_coset_tower/d8_head_triangles/production.terminal.json; research/ddp/m2_coset_tower/d8_head_triangles/best.independent_verify.json"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "triangle-head", "finite-scope", "negative", "method-ledger"]
---

# 7203点三角头固定r5塔：必要商过滤与完整BB失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,5)；L=5334；candidate_graph_or_family n=7203

**距目标的证据：** 实际D=7，目标D=5；原报告bad（类型见详情）=2508408；Existing Wiki Metrics; no experiment rerun；CompleteHHscope28894320; quotientrejected28663824; actualoriginalBB230496; originalBBpass0; one minBB diagnosticD7,2508408badpairs,BB31.



**既有原文指标：** CompleteHHscope28894320; quotientrejected28663824; actualoriginalBB230496; originalBBpass0; one minBB diagnosticD7,2508408badpairs,BB31.



**原始证据：** [research/ddp/m2_coset_tower/d8_head_triangles/REPORT.md](../../research/ddp/m2_coset_tower/d8_head_triangles/REPORT.md)；[research/ddp/m2_coset_tower/d8_head_triangles/STRUCTURE_SCOPE.md](../../research/ddp/m2_coset_tower/d8_head_triangles/STRUCTURE_SCOPE.md)；[research/ddp/m2_coset_tower/d8_head_triangles/QUOTIENT_BB_CHECK.md](../../research/ddp/m2_coset_tower/d8_head_triangles/QUOTIENT_BB_CHECK.md)；[research/ddp/m2_coset_tower/d8_head_triangles/production.terminal.json](../../research/ddp/m2_coset_tower/d8_head_triangles/production.terminal.json)；[research/ddp/m2_coset_tower/d8_head_triangles/best.independent_verify.json](../../research/ddp/m2_coset_tower/d8_head_triangles/best.independent_verify.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** AllHH inputs are covered by the safe normalization and necessary quotient. Quotient pass is not original BB pass. Every remaining original input fails exact BB. All failures after quotientpass lie onfixedaxis v0. Diagnostic is not a global bestbadpair graph.

**启发与重启依据：** AllHH inputs are covered by the safe normalization and necessary quotient. Quotient pass is not original BB pass. Every remaining original input fails exact BB. All failures after quotientpass lie onfixedaxis v0. Diagnostic is not a global bestbadpair graph.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

