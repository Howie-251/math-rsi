---
type: experiment
node_id: exp:ddp-m3-control-capacity-20261026
title: "仿射线控制器的必要覆盖与实际失败范围"
idea_id: "idea:ddp-m3-affine-line-cover"
verdict: partial
confidence: high
date: "2026-10-26"
hardware: "CPU bounded profiles; standard-library and NumPy independent checks"
duration: ""
provenance: "research/ddp/second_mechanism/DERIVATION_PACKAGE.md; research/ddp/m3_capacity_independent.md"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "affine", "counterexample", "method-ledger"]
---

# 仿射线控制器的必要覆盖与实际失败范围

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-m3-affine-line-cover`

## Metrics
**对象层级：** controller

**目标与阶数：** (4,3)；L=不适用／见变体；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': None, 'graph_generated': False}

**距目标的证据：** Recovered810 known edges exactly. Ternary4regular controller needs A³>0 and n≤39. Cyclic3layer m11..17 capacity enumeration0survivors; second implementation agrees. Unrestricted n31/32/33 profiles120s each have4/8/14 zeroentries. Direct binary lifts252×16 and441×16 fail unique3route counterexamples.

**其他指标（保持原计数类型）：**
```json
{
  "intended_final_target": {
    "Delta": 12,
    "D": 3,
    "savedL": 810,
    "n_if_full_lift_valid": null,
    "graph_generated": false
  }
}
```

**既有原文指标：** Recovered810 known edges exactly. Ternary4regular controller needs A³>0 and n≤39. Cyclic3layer m11..17 capacity enumeration0survivors; second implementation agrees. Unrestricted n31/32/33 profiles120s each have4/8/14 zeroentries. Direct binary lifts252×16 and441×16 fail unique3route counterexamples.



**原始证据：** [research/ddp/second_mechanism/DERIVATION_PACKAGE.md](../../research/ddp/second_mechanism/DERIVATION_PACKAGE.md)；[research/ddp/m3_capacity_independent.md](../../research/ddp/m3_capacity_independent.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Capacity is necessary, never complete fiber coverage. General31–39 controllers remain open. No new lower bound. Latest binary6regularF2³ alternative changes field/degree and must use its own capacity and same-fiber triangle condition.

**启发与重启依据：** Capacity is necessary, never complete fiber coverage. General31–39 controllers remain open. No new lower bound. Latest binary6regularF2³ alternative changes field/degree and must use its own capacity and same-fiber triangle condition.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

