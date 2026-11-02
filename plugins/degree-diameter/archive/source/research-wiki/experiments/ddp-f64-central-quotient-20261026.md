---
type: experiment
node_id: exp:ddp-f64-central-quotient-20261026
title: "循环F64剩余分支的中心商完整BB判定"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU worker"
duration: "16.739514 cumulative CPU seconds including profile and compilation"
provenance: "research/ddp/m2_coset_tower/d7_f64_two_pairs/REPORT.md; research/ddp/m2_coset_tower/d7_f64_two_pairs/SCOPE.md; research/ddp/m2_coset_tower/d7_f64_two_pairs/CENTRAL_QUOTIENT_CHECK.md"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "coset-tower", "central-quotient", "method-ledger"]
---

# 循环F64剩余分支的中心商完整BB判定

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** (7,5)；L=2810；条件性n=3200（未据此计纪录）

**距目标的证据：** 13127680 normalized projected inputs;7434370 HH failures;5693310 HH passers;0 BB passers;minimum18 missing blocks. No BH survivors or original C42 lifts evaluated. Saved profile12386-slot prefix continued without repetition.



**既有原文指标：** 13127680 normalized projected inputs;7434370 HH failures;5693310 HH passers;0 BB passers;minimum18 missing blocks. No BH survivors or original C42 lifts evaluated. Saved profile12386-slot prefix continued without repetition.



**原始证据：** [research/ddp/m2_coset_tower/d7_f64_two_pairs/REPORT.md](../../research/ddp/m2_coset_tower/d7_f64_two_pairs/REPORT.md)；[research/ddp/m2_coset_tower/d7_f64_two_pairs/SCOPE.md](../../research/ddp/m2_coset_tower/d7_f64_two_pairs/SCOPE.md)；[research/ddp/m2_coset_tower/d7_f64_two_pairs/CENTRAL_QUOTIENT_CHECK.md](../../research/ddp/m2_coset_tower/d7_f64_two_pairs/CENTRAL_QUOTIENT_CHECK.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Center fixes B/H and pairs leaves, so orbit quotient preserves all distances with fixed endpoints; independent saved-graph comparison confirms implementation. All projected multisets have legal original lifts, including duplicated pairs/involutions and identity projection. SCOPE.md proves full coverage. Exact BB obstruction closes all two-pair/two-involution inputs; combining prior other types closes the fixed cyclic3200 tower, not faithful semilinear or arbitrary graphs.

**启发与重启依据：** Center fixes B/H and pairs leaves, so orbit quotient preserves all distances with fixed endpoints; independent saved-graph comparison confirms implementation. All projected multisets have legal original lifts, including duplicated pairs/involutions and identity projection. SCOPE.md proves full coverage. Exact BB obstruction closes all two-pair/two-involution inputs; combining prior other types closes the fixed cyclic3200 tower, not faithful semilinear or arbitrary graphs.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

