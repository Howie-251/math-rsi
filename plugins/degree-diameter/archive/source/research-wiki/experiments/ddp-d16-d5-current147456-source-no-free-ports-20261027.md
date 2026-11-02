---
type: experiment
node_id: exp:ddp-d16-d5-current147456-source-no-free-ports-20261027
title: "Current147456 source is16regular: keep-all-edges extension has no free port"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d16_D5_current147456_source/REPORT.md; research/ddp/more_graphs_20261027/d16_D5_current147456_source/SOURCE.json; research/ddp/more_graphs_20261027/d16_D5_current147456_source/PREDICTION.json; research/ddp/more_graphs_20261027/d16_D5_current147456_source/RESULT.json"
added: 2026-10-27T21:07:17Z
tags: ["ddp", "method-ledger"]
---

# Current147456 source is16regular: keep-all-edges extension has no free port

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (16,5)；L=147456；known_source_or_recovery n=147456；条件性n=147457（未据此计纪录）

**距目标的证据：** Primary author Theorem2.1 states all16regular; current maintainer order147456/m1179648 and degreehist match. Therefore free vertices0, slots0, minSatN16 and onefault0. These are theorem deductions, not numerical profile/BFS. No graph downloaded, constructed or new lower bound.

**其他指标（保持原计数类型）：**
```json
{
  "source_reported_D": 5,
  "source_degree_histogram": {
    "16": 147456
  },
  "source_m": 1179648,
  "free_vertices": 0,
  "free_slots": 0,
  "minSatN": 16,
  "onefault_prototypes": 0,
  "all_counts_basis": "Primary all16regular theorem, not graph profile",
  "raw_header_read": false,
  "source_literal_downloads": 0,
  "numerical_degree_profiles": 0,
  "source_BFS_roots": 0,
  "candidate_graphs": 0,
  "CPU_profile_executed": false,
  "new_lower_bounds": 0,
  "source_degree_evidence": "Mizuno Theorem2.1 and LemmaA.8; maintainedD5 degreehist",
  "different_from_16D4_source": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d16_D5_current147456_source/REPORT.md](../../research/ddp/more_graphs_20261027/d16_D5_current147456_source/REPORT.md)；[research/ddp/more_graphs_20261027/d16_D5_current147456_source/SOURCE.json](../../research/ddp/more_graphs_20261027/d16_D5_current147456_source/SOURCE.json)；[research/ddp/more_graphs_20261027/d16_D5_current147456_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D5_current147456_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D5_current147456_source/RESULT.json](../../research/ddp/more_graphs_20261027/d16_D5_current147456_source/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed published Mizuno147456 graph. Any connected max16 extension adding one or more vertices while retaining every original edge. n.hypothetical147457 represents the first larger order; the obstruction applies to every N>147456 within this preserve-edge scope.

**仍未完成：** General N(16,5), non-preserving-edge surgery and other controller/graph families remain open.

**启发与重启依据：** Check actual regularity before spare-star/proxy or cover optimization. Every old endpoint is saturated, so arbitrary helpers cannot attach without violating max16. Only a separately justified change deleting/rewiring old edges or changing source/controller could reopen a construction problem; none is run here.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

