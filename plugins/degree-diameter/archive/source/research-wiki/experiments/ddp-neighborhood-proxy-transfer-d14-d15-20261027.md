---
type: experiment
node_id: exp:ddp-neighborhood-proxy-transfer-d14-d15-20261027
title: "N13成功代理迁移：D14/D15每个原型仍缺8/9个代理"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/REPORT.md; research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/RESULT.json; research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json"
added: 2026-10-27T18:01:05Z
tags: ["ddp", "method-ledger"]
---

# N13成功代理迁移：D14/D15每个原型仍缺8/9个代理

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-proxy-eligibility-experiment

**目标与阶数：** 多目标：D14source→[14, 5]／L=94186；D15source→[15, 5]／L=100132（逐变体，不合成一个距离）

**距目标的证据：** D14找到1088个满pin有代理，D15找到205个满pin有代理（207pairs），但全部原型仍分别至少8/9个满pin无任何代理，故0投影候选、0R4检查、0图。不能登记badpairs或实际D。

**其他指标（保持原计数类型）：**
```json
{
  "prediction": "REFUTED_FOR_FIXED_RULE",
  "CPU_including_compile": 2.30092,
  "BFS": 0,
  "R4_recomputed": 0,
  "R4_candidate_checks": 0,
  "newgraphs": 0,
  "latest_public_15_D5": 102060,
  "latest_public_checked_UTC": "2026-10-27 17:59:33 UTC",
  "studied_D15_source_is_now_historical": true
}
```



**从属变体：**
```json
[
  {
    "label": "D14source",
    "target_Delta": 14,
    "target_D": 5,
    "savedL": 94186,
    "source_n": 94186,
    "source_m": 657452,
    "free_vertices": 3685,
    "wedges": 669198,
    "qualifying_pairs": 1088,
    "saturated_u_with_proxy": 1088,
    "minimum_unproxied_saturated_neighbors": 8,
    "projected_candidates": 0
  },
  {
    "label": "D15source",
    "target_Delta": 15,
    "target_D": 5,
    "savedL": 100132,
    "source_n": 100132,
    "source_m": 749732,
    "free_vertices": 2498,
    "wedges": 523529,
    "qualifying_pairs": 207,
    "saturated_u_with_proxy": 205,
    "minimum_unproxied_saturated_neighbors": 9,
    "projected_candidates": 0
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/near_neighborhood_proxy_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json](../../research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Two actualfixedsources94186/100132; fullu atdegreeDelta, freew with|N(u)\N(w)|<=3 and|N(w)\N(u)|<=1; deterministic maxcommon/mindegree/label proxy; alloldprototypefull-neighborhood projections.

**仍未完成：** Broaderproxyrelations, nonstar rules and arbitrary14/15graph extensions remain open; no newrecordhere.

**启发与重启依据：** 阈值和规则直接继承N13真实10core共有邻域/extra差异，理解确实改变了下一实验。此scope阻在代理存在性，改tie不能补无代理满pin；不放宽阈值逐层长尾，不泛排所有proxy或任意14/15点覆盖。只有不同route结构/新source有依据才重启。 最新17:59主表15,5为102060；100132源仅为历史控制对象，100133已不是纪录目标。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

