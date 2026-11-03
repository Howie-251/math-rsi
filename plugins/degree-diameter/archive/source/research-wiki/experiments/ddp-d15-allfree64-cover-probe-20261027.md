---
type: experiment
node_id: exp:ddp-d15-allfree64-cover-probe-20261027
title: "(15,5)全2498可接点：64个完整15pin方案无命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/allfree_cover_probe/REPORT.md; research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/allfree_cover_probe/RESULT.json; research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json"
added: 2026-10-27T18:01:05Z
tags: ["ddp", "method-ledger"]
---

# (15,5)全2498可接点：64个完整15pin方案无命中

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (15,5)；L=100132；条件性n=100133（未据此计纪录）

**距目标的证据：** 复用20球、一次补2478球，完整allfree union全盖100132，每target支持364..651。冻结64方案全部完成，0hit，漏1848..2064。0新图/0source全BFS。

**其他指标（保持原计数类型）：**
```json
{
  "candidates": 2498,
  "reused_R4_balls": 20,
  "new_R4_balls": 2478,
  "allfree_union_missing": 0,
  "target_support_min": 364,
  "target_support_max": 651,
  "frozen_candidates": 64,
  "evaluated": 64,
  "hits": 0,
  "newroot_uncovered_targets_min": 1848,
  "newroot_uncovered_targets_max": 2064,
  "CPU_including_compile": 4.066048549,
  "operation_prediction": "REFUTED",
  "global_existence": "UNRESOLVED",
  "BFS": 0,
  "cache_bytes": 31274960,
  "latest_public_15_D5": 102060,
  "latest_public_checked_UTC": "2026-10-27 17:59:33 UTC",
  "studied_D15_source_is_now_historical": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/allfree_cover_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/allfree_cover_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/allfree_cover_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/allfree_cover_probe/RESULT.json)；[research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json](../../research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 复用20球、一次补2478球，完整allfree union全盖100132，每target支持364..651。冻结64方案全部完成，0hit，漏1848..2064。0新图/0source全BFS。

**仍未完成：** No general source-family maximality is claimed; final concrete Lean remains incomplete.

**启发与重启依据：** 局部球比例提高获支持，但同一有限离散选择仍未共同cover；停止该规则，不按1848少于3705续算。所有31MB球缓存保留。任意≤15cover存在性仍UNRESOLVED，不能把64无命中登记为整族无望。 最新17:59主表15,5为102060；100132源仅为历史控制对象，100133已不是纪录目标。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

