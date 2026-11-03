---
type: experiment
node_id: exp:ddp-h9-d11-ninepin-twoanchor-20261027
title: "(11,5)删一Q-line pin再补两anchor：240个受控变体无图"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/RESULT.json"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# (11,5)删一Q-line pin再补两anchor：240个受控变体无图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-controlled-variant-no-new-graph

**目标与阶数：** (11,5)；L=37628；条件性n=37632（未据此计纪录）

**距目标的证据：** 0新图。210个合法9pin集完整≤2anchor失败，无UNKNOWN、无未试；4.478133 CPU秒。没有把mandatory遗漏数当作整图坏对。

**其他指标（保持原计数类型）：**
```json
{
  "raw_variants": 240,
  "degree_blocked": 30,
  "exactly_processed": 210,
  "new_graphs_generated": 0,
  "CPU_seconds": 4.478133,
  "unknown_items": 0,
  "unattempted_items": 0,
  "family_excluded": false,
  "source_reaudited": false,
  "all_source_BFS_executed": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed current37631 graph,24 original ten-pin sets; delete one mandatory pin per set.240 distinct sets,30 degree-blocked,210 complete exact <=two eligible old-anchor checks.

**正向保证：** For two-anchor search a missing pivot must be covered by at least one of the two anchors; all its eligible coverers were enumerated, with exact second-anchor intersection.

**仍未完成：** This excludes only the240 saved deletions on current37631. Arbitrary nine-pin sets, rewiring and different bases remain untested.

**启发与重启依据：** Deleting one geometric pin and spending its degree slot on a second anchor does not help these concrete sets. Stop this frozen variant; do not enlarge by random seeds.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

