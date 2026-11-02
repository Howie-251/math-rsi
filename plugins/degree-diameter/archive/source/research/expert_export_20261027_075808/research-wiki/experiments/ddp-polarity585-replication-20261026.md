---
type: experiment
node_id: exp:ddp-polarity585-replication-20261026
title: "585完全复制扩张的精确阶数上限"
idea_id: "idea:ddp-polarity585-complete-replication"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, at most one worker per bounded batch"
duration: "0.016055331 partitioncheck CPU s; paper derivation"
provenance: "research/ddp/polarity585_replication/DERIVATION_PACKAGE.md"
added: 2026-10-27T07:55:16Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 585完全复制扩张的精确阶数上限

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-polarity585-complete-replication`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** 多目标：complete-replication bound→[10, 3]／L=650；complete-replication bound→[11, 3]／L=715；complete-replication bound→[12, 3]／L=810（逐变体，不合成一个距离）；条件性n=585（未据此计纪录）

**距目标的证据：** A65/B520;everyvertex has8neighborsB;8N≤520Delta;N≤65Delta sharp. No graphsearch orBFS.



**既有原文指标：** A65/B520;everyvertex has8neighborsB;8N≤520Delta;N≤65Delta sharp. No graphsearch orBFS.

**从属变体：**
```json
[
  {
    "label": "complete-replication bound",
    "target": [
      10,
      3
    ],
    "n": null,
    "actualD": null,
    "bad_pairs": null,
    "theoretical_order_upper_bound": 650,
    "count_type": null,
    "evidence": "research/ddp/polarity585_replication/DERIVATION_PACKAGE.md:6-17",
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "complete-replication bound",
    "target": [
      11,
      3
    ],
    "n": null,
    "actualD": null,
    "bad_pairs": null,
    "theoretical_order_upper_bound": 715,
    "count_type": null,
    "evidence": "research/ddp/polarity585_replication/DERIVATION_PACKAGE.md:6-17",
    "savedL": 715,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "complete-replication bound",
    "target": [
      12,
      3
    ],
    "n": null,
    "actualD": null,
    "bad_pairs": null,
    "theoretical_order_upper_bound": 780,
    "count_type": null,
    "evidence": "research/ddp/polarity585_replication/DERIVATION_PACKAGE.md:6-17",
    "savedL": 810,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  }
]
```

**原始证据：** [research/ddp/polarity585_replication/DERIVATION_PACKAGE.md](../../research/ddp/polarity585_replication/DERIVATION_PACKAGE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** EveryBclassmustremain; originalcompletecrossconnections retained; allowsnonuniformweights,deletedAclassesandextraedges. Nooriginalityclaim.

**启发与重启依据：** EveryBclassmustremain; originalcompletecrossconnections retained; allowsnonuniformweights,deletedAclassesandextraedges. Nooriginalityclaim.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

