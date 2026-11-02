---
type: experiment
node_id: exp:ddp-more-graphs-20261027-d4-two-involution-pattern
title: "两phase10对合+三逆对新规则：1815848项薄层仍不覆盖"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_two_involution_transfer/REPORT.md; research/ddp/more_graphs_20261027/d4_two_involution_transfer/RESULT.json; research/ddp/more_graphs_20261027/d4_two_involution_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d4_two_involution_transfer/CAPACITY.json; research/ddp/more_graphs_20261027/d4_two_involution_transfer/PROFILE1000.json; research/ddp/more_graphs_20261027/d4_two_involution_transfer/PROFILE_FORECAST.json; research/ddp/more_graphs_20261027/d4_two_involution_transfer/REMAINDER.json; research/ddp/more_graphs_20261027/d4_two_involution_transfer/enumerate.cpp"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# 两phase10对合+三逆对新规则：1815848项薄层仍不覆盖

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** complete-fixed-two-involution-pattern-screen

**目标与阶数：** (8,4)；L=1100；条件性n=1220（未据此计纪录）；从属目标：[[8, 4]]

**距目标的证据：** Oneorigin phase10only;zero necessarysurvivors,notallgraphbadpairs.；容量min85通过；>=1survivor预测被推翻，全1815848项phase10survivor0，max58/59。

**其他指标（保持原计数类型）：**
```json
{
  "cases": 1815848,
  "profile_cases": 1000,
  "profile_replayed": 0,
  "phase10_survivors": 0,
  "other19phase_checks": 0,
  "native_CPU_seconds": 0.33170900000000003,
  "new_graphs": 0,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "label": "r8",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 58
  },
  {
    "label": "r23",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 58
  },
  {
    "label": "r24",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 58
  },
  {
    "label": "r28",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 58
  },
  {
    "label": "r33",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 58
  },
  {
    "label": "r37",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 58
  },
  {
    "label": "r38",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 59
  },
  {
    "label": "r53",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "cases": 226981,
    "phase10_survivors": 0,
    "phase10_max": 59
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d4_two_involution_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/CAPACITY.json](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/CAPACITY.json)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/PROFILE1000.json](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/PROFILE1000.json)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/PROFILE_FORECAST.json](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/PROFILE_FORECAST.json)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/REMAINDER.json](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/REMAINDER.json)；[research/ddp/more_graphs_20261027/d4_two_involution_transfer/enumerate.cpp](../../research/ddp/more_graphs_20261027/d4_two_involution_transfer/enumerate.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** p61,all8primitive20actions,h0=(10,0),h1=(10,1),inversephases1/4/8,allA/B/CinF61.1000profile+1814848remainder,no replay.

**仍未完成：** NotallC61semidirectC20groups,nototherphasepatternsorall1220graphs.

**启发与重启依据：** Differentgeneratorcomposition stillnotcomplete;stopthisonlypattern,nophase/seed/prime/MIPextensions.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

