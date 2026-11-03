---
type: experiment
node_id: exp:ddp-d4-d6-flag-layer-absorption45568-20261027
title: "(4,6)单flag+单layer吸收45568全闭：新根170通过仍无完整图"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/REPORT.md; research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/RESULT.json; research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/PREDICTION.json; research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/first_oldpair_witness.json"
added: 2026-10-27T18:46:57Z
tags: ["ddp", "method-ledger"]
---

# (4,6)单flag+单layer吸收45568全闭：新根170通过仍无完整图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (4,6)；L=760；条件性n=761（未据此计纪录）

**距目标的证据：** 固定45568=1424现存coreflag×32现存layeredge，删两disjoint边，新x邻四端点，假设761/1522/4reg。45398 newrootR5失败；170 newroot完整通过但各有旧旧>6反例，0图/未试/UNKNOWN。

**其他指标（保持原计数类型）：**
```json
{
  "candidates_total": 45568,
  "candidates_closed": 45568,
  "newroot_R5_failures": 45398,
  "newroot_D6_passers": 170,
  "oldpair_D6_failures": 170,
  "modified_root_BFS_runs": 1015,
  "maximum_executed_roots_per_failed_candidate": 12,
  "theoretical_complete_root_bound": 69,
  "source_endpoint_R5_cache_roots": 760,
  "source_R2_snapshots_same_R5_run": 760,
  "source_D6_allBFS_revalidation": 0,
  "graphs_exported": 0,
  "unattempted": 0,
  "UNKNOWN": 0,
  "native_CPU_seconds": 0.066705,
  "total_CPU_seconds": 2.468014226,
  "CPU_budget_seconds": 20,
  "first_witness": {
    "ordinal": 2,
    "F": [
      [
        0,
        364
      ],
      [
        729,
        730
      ]
    ],
    "S": [
      0,
      364,
      729,
      730
    ],
    "old_badpair": [
      0,
      733
    ],
    "distance_greater_than": 6
  },
  "negative_scope": "One existing coreflag plus oneexisting layeredge, forcedfour-endpoint neighbor set onfixed760source; noextracuts."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/RESULT.json](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/RESULT.json)；[research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/first_oldpair_witness.json](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/production/first_oldpair_witness.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定45568=1424现存coreflag×32现存layeredge，删两disjoint边，新x邻四端点，假设761/1522/4reg。45398 newrootR5失败；170 newroot完整通过但各有旧旧>6反例，0图/未试/UNKNOWN。

**仍未完成：** Only this complete frozenfamily isexcluded; arbitrary761graphs andotherdeletions remainopen.

**启发与重启依据：** F端点全入S给sourceR5精确newroot gate；完整旧pair根集为sourceR2(T)+x（≤69），不是D4的R1或对称抽样。只闭当前source固定两edge族，不按新badpair增加flag/layeredge。重启需新连接机制或不同source。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

