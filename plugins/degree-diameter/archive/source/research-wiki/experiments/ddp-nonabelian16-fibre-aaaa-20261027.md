---
type: experiment
node_id: exp:ddp-nonabelian16-fibre-aaaa-20261027
title: "D8×C2非交换16纤维：960个统一自同构规则均无法满足AAAA"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/REPORT.md; research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/RESULT.json; research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/max12_fixture.json"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# D8×C2非交换16纤维：960个统一自同构规则均无法满足AAAA

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (8,4)；L=1100；条件性n=1152（未据此计纪录）

**距目标的证据：** Only the stated finite local model/coverage was checked; no complete newgraph.；960全部失败，覆盖最多12<16；任何g0均由归约覆盖，故这个统一Aut+two-shift纤维族不可用。没有1152图、没有重跑旧affine或转edge-local。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "fibre_size": 16,
  "automorphisms": 64,
  "nonidentity_h": 15,
  "complete_cases": 960,
  "max_AAAA_endpoints": 12,
  "required_AAAA_endpoints": 16,
  "CPU_seconds": 0.01654,
  "allsource_BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/REPORT.md](../../research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/REPORT.md)；[research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/RESULT.json](../../research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/RESULT.json)；[research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/max12_fixture.json](../../research/ddp/more_graphs_20261027/nonabelian16_fibre_preflight/max12_fixture.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** G=D8xC2,uniformR(x)={phi(x)g0,phi(x)g1}. Absorbg0 intoinnerautomorphism psi,enumerateall64trueAut and15nonidentityh;16binaryorbitproducts mustcoverG becausefixed72controller hasuniqueAAAA slots.

**仍未完成：** No result outside the exact stated scope is excluded.

**启发与重启依据：** Retain exact source and finite scope; no same-base restart or unbounded local-score optimization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

