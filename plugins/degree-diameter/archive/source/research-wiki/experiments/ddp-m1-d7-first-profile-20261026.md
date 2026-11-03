---
type: experiment
node_id: exp:ddp-m1-d7-first-profile-20261026
title: "同一电压机制在(7,4)的702/720点候选"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "2 single-threadCPU processes"
duration: "120s each"
provenance: "computations/ddp/m1/d7_profile"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "candidate-failed", "method-ledger"]
---

# 同一电压机制在(7,4)的702/720点候选

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** graph_or_graph_family

**目标与阶数：** (7,4)；L=684；从属目标：[[7, 4]]

**距目标的证据：** 实际D=5，目标D=4；Existing Wiki Metrics; no experiment rerun；702vertices,2457edges,degree7,diameter5,1404badpairs;720vertices,2520edges,degree7,diameter5,2700badpairs. Full-source BFS from edge lists.



**既有原文指标：** 702vertices,2457edges,degree7,diameter5,1404badpairs;720vertices,2520edges,degree7,diameter5,2700badpairs. Full-source BFS from edge lists.

**从属变体：**
```json
[
  {
    "label": "702 candidate",
    "target": [
      7,
      4
    ],
    "n": 702,
    "actualD": 5,
    "bad_pairs": 1404,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 684,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "720 candidate",
    "target": [
      7,
      4
    ],
    "n": 720,
    "actualD": 5,
    "bad_pairs": 2700,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 684,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  }
]
```

**原始证据：** [computations/ddp/m1/d7_profile](../../computations/ddp/m1/d7_profile)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Both exceed record684 in order but fail diameter4, so neither is a new bound. Recovered684 baseline all-source regression passed. Analyze actual distance5 failures before local repair or changed quotient.

**启发与重启依据：** Both exceed record684 in order but fail diameter4, so neither is a new bound. Recovered684 baseline all-source regression passed. Analyze actual distance5 failures before local repair or changed quotient.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

