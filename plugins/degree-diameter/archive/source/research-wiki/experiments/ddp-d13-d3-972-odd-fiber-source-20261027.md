---
type: experiment
node_id: exp:ddp-d13-d3-972-odd-fiber-source-20261027
title: "Current972 source gap resolved:108 free vertices, minSatN10 and36 odd27 blocks"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/source_fetch_receipts.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/profile.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/source972.author.adjlist.txt; research/ddp/more_graphs_20261027/d13_D3_current972_source/source972.edges; research/ddp/more_graphs_20261027/d13_D3_chart_transfer/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_chart_transfer/SOURCE_FACTS.json"
added: 2026-10-27T21:17:06Z
tags: ["ddp", "method-ledger"]
---

# Current972 source gap resolved:108 free vertices, minSatN10 and36 odd27 blocks

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,3)；L=972；known_source_or_recovery n=972；条件性n=973（未据此计纪录）

**距目标的证据：** Author API now returned52470bytes/972rows. Actualn972/m6264, degree13:864/degree12:108,108free slots. minSatN10(36 prototypes), zero-/onefault0, maximum free-vs-full neighborhood overlap3. Every27-block has12 disjoint matching edges plus3 unmatched points, each vertex externaldegree12 in4 targetblocks×3.

**其他指标（保持原计数类型）：**
```json
{
  "source_reported_D": 3,
  "source_m": 6264,
  "degree_histogram": {
    "12": 108,
    "13": 864
  },
  "free_vertices": 108,
  "free_slots": 108,
  "minSatN": 10,
  "minSatN_count": 36,
  "onefault_count": 0,
  "free_proxy_max_neighbor_overlap": 3,
  "contiguous27_block_count": 36,
  "matching_edges_per_block": 12,
  "unmatched_vertices_per_block": 3,
  "external_degree_per_vertex": 12,
  "profile_CPU_seconds": 0.07901007200000001,
  "source_allroot_BFS": 0,
  "source_single_root_BFS": 0,
  "new_lower_bounds": 0,
  "source_gap": "RESOLVED",
  "odd_fiber_prediction": "SUPPORTED_WITH108_ACTUAL_SPARES",
  "method_count_note": "Update of preexisting source-gap record, not another independent method"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/source_fetch_receipts.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/source_fetch_receipts.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/profile.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/profile.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/source972.author.adjlist.txt](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/source972.author.adjlist.txt)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/source972.edges](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/source972.edges)；[research/ddp/more_graphs_20261027/d13_D3_chart_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_chart_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_chart_transfer/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d13_D3_chart_transfer/SOURCE_FACTS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** This upserts the existing source-gap node using the actual indexed972 literal. One degree/neighborhood/contiguous27-block profile only, no original source distance BFS or old952 replacement.

**仍未完成：** The complete local affine-line recipe and other adjacency-changing constructions are separate; source-profile results alone do not close general extensions.

**启发与重启依据：** The old odd-fiber parity lower bound36spares is supported and strengthened to108 actualspares. Near-star/close-neighborhood proxy intuition fails because minSatN10 and overlap<=3. Use the actual free-pin R2 matrix rather than assume free slots imply extendibility; the resulting fixed single-vertex test is recorded separately.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

