---
type: experiment
node_id: exp:propertyb35-paper-principal-trace-degree-prefix-20261020
title: "实际主子集Gram与稳定LOW19共同degree-prefix缩减"
idea_id: "idea:propertyb36-40-structural-diagnosis"
verdict: partial
confidence: high
date: "2026-10-20"
hardware: ""
duration: ""
provenance: "context/propertyb35-paper/round01/middle/a1_incidence_rank_subset_20261020/DERIVATION.md;middle/a1_independent_set_degree_prefix_20261020/LOW19_RESULT.json;LOW19_VERIFY.json;middle/a1_chordal_triangle_repair_20261020/CAPACITY_FILTER.json;round01/reviews/REVIEW_RECONCILIATION.md"
added: 2026-10-20T04:26:39Z
tags: ["propertyb", "m5-ge36", "a1", "principal-gram", "low19", "partial"]
---

# 实际主子集Gram与稳定LOW19共同degree-prefix缩减

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:propertyb36-40-structural-diagnosis`

## Metrics
完整21615 moment tuples->25，root实际.430333CPU；最终LOW19全部19(E,t)/25alloc双DP且root重编频数实跑PASS.451305CPU；稳定3aggregate P12876/12812/12905,L2725680/2723280/2730180,margin2960/560/7460。

## Reasoning
root原创/25和24独立核A1删1/2及低块low<=20/19；root最终全链实跑已确认。Grok/Gemini通用principal-trace有效静态审仅通用1-3.1，未执行/未审后来A1cuts；cell940后续定点双审pending。三个aggregate非H类，A1/21/36未闭，不追加同类DP。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

