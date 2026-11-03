---
type: experiment
node_id: exp:ddp-nonfaithful-remaining-20261026
title: "非忠实反射剩余三分支完整有限判定"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU worker"
duration: "49.78856 cumulative CPU seconds"
provenance: "research/ddp/m1_reflection_nonfaithful/remaining_search/SEARCH_REPORT.md"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "voltage", "finite-exclusion", "method-ledger"]
---

# 非忠实反射剩余三分支完整有限判定

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** graph_or_graph_family

**目标与阶数：** (5,5)；L=650；从属目标：[[5, 5]]

**距目标的证据：** 实际D=6，目标D=5；Existing Wiki Metrics; no experiment rerun；3332186 raw slots;3273316 legal inputs all scored. p17 mixed771341; p29 mixed1136191; p29 both1365784. Best graphs816/696/696 are independently simple connected5-regular,D6,bad9792/4350/4524.



**既有原文指标：** 3332186 raw slots;3273316 legal inputs all scored. p17 mixed771341; p29 mixed1136191; p29 both1365784. Best graphs816/696/696 are independently simple connected5-regular,D6,bad9792/4350/4524.

**从属变体：**
```json
[
  {
    "label": "p17 mixed",
    "target": [
      5,
      5
    ],
    "n": 816,
    "actualD": 6,
    "bad_pairs": 9792,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "p29 mixed",
    "target": [
      5,
      5
    ],
    "n": 696,
    "actualD": 6,
    "bad_pairs": 4350,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "p29 both",
    "target": [
      5,
      5
    ],
    "n": 696,
    "actualD": 6,
    "bad_pairs": 4524,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  }
]
```

**原始证据：** [research/ddp/m1_reflection_nonfaithful/remaining_search/SEARCH_REPORT.md](../../research/ddp/m1_reflection_nonfaithful/remaining_search/SEARCH_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Together with saved capacity exclusions and the prior p13 mixed completion, the declared double-reflection A mixed/both families for all three selected groups have no D5. No other A type/group excluded; no further queue.

**启发与重启依据：** Together with saved capacity exclusions and the prior p13 mixed completion, the declared double-reflection A mixed/both families for all three selected groups have no D5. No other A type/group excluded; no further queue.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

