---
type: experiment
node_id: exp:ddp-m1-first-profile-20261026
title: "四个1+5电压候选的完整图与直径失败"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "4 single-thread CPU processes"
duration: "60 wall seconds per process"
provenance: "computations/ddp/m1/profile"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "finite-profile", "failed-candidates", "method-ledger"]
---

# 四个1+5电压候选的完整图与直径失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** graph_or_graph_family

**目标与阶数：** (6,3)；L=120；从属目标：[[6, 3]]

**距目标的证据：** 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；UT4(F2):n128,bad1024;D8xD8:n128,bad1536;HeisZ4:n128,bad800;C6xA4:n144,bad792. All simple6-regular connected diameter4; all-source BFS agrees with exact orbit scores.



**既有原文指标：** UT4(F2):n128,bad1024;D8xD8:n128,bad1536;HeisZ4:n128,bad800;C6xA4:n144,bad792. All simple6-regular connected diameter4; all-source BFS agrees with exact orbit scores.

**从属变体：**
```json
[
  {
    "label": "UT4(F2)",
    "target": [
      6,
      3
    ],
    "n": 128,
    "actualD": 4,
    "bad_pairs": 1024,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 120,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "D8xD8",
    "target": [
      6,
      3
    ],
    "n": 128,
    "actualD": 4,
    "bad_pairs": 1536,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 120,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "HeisZ4",
    "target": [
      6,
      3
    ],
    "n": 128,
    "actualD": 4,
    "bad_pairs": 800,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 120,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "C6xA4",
    "target": [
      6,
      3
    ],
    "n": 144,
    "actualD": 4,
    "bad_pairs": 792,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 120,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  }
]
```

**原始证据：** [computations/ddp/m1/profile](../../computations/ddp/m1/profile)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** No new(6,3) lower bound. Best values reached within0.02s and persisted for22–27million evaluated proposals. Change generating degree allocation to2+4/r4 rather than extending unchanged trajectories. This rejects saved candidates only.

**启发与重启依据：** No new(6,3) lower bound. Best values reached within0.02s and persisted for22–27million evaluated proposals. Change generating degree allocation to2+4/r4 rather than extending unchanged trajectories. This rejects saved candidates only.

**单独的重启条件：** Change internal/cross degree allocation to2+4/r4; do not extend the unchanged1+5 trajectories.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

