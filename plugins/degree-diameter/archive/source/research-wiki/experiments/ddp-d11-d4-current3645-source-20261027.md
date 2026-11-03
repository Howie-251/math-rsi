---
type: experiment
node_id: exp:ddp-d11-d4-current3645-source-20261027
title: "(11,4)3645新源恢复：W9双图+201吸收插入，非45×81"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D4_current3645/REPORT.md; research/ddp/more_graphs_20261027/d11_D4_current3645/RESULT.json"
added: 2026-10-27T18:21:15Z
tags: ["ddp", "method-ledger"]
---

# (11,4)3645新源恢复：W9双图+201吸收插入，非45×81

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (11,4)；L=3645；known_source_or_recovery n=3645

**距目标的证据：** 实际3645/20044，3638个degree11和7个degree10，free=[3456,3489,3564,3571,3583,3603,3643]均在201插入层。作者源为3444点W9 incidence-double+164spreadtwins，非45×81纤维；81分组不equitable。minSatN9，单满点模式不适用。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 3645,
  "source_m": 20044,
  "degree10": 7,
  "degree11": 3638,
  "min_saturated_neighbors": 9,
  "naive81fibers_prediction": "REFUTED",
  "profile_CPU": 0.04171,
  "BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D4_current3645/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际3645/20044，3638个degree11和7个degree10，free=[3456,3489,3564,3571,3583,3603,3643]均在201插入层。作者源为3444点W9 incidence-double+164spreadtwins，非45×81纤维；81分组不equitable。minSatN9，单满点模式不适用。

**仍未完成：** No complete newgraph in this finite experiment; unrelatedrules and finalLean remain open.

**启发与重启依据：** 先由source证据推翻因子分解猜测，转实际point-copy/line-copy/twin吸收路线。当前3444诱导已有457原边被删，不能把旧几何覆盖直接继承为current图覆盖。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

