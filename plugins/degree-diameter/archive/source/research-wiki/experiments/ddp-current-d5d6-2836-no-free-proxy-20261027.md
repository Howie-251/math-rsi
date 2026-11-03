---
type: experiment
node_id: exp:ddp-current-d5d6-2836-no-free-proxy-20261027
title: "(5,6)2836实际全5正则：保边star/proxy增点无接口"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D6_current2836/REPORT.md; research/ddp/more_graphs_20261027/d5_D6_current2836/RESULT.json; research/ddp/more_graphs_20261027/d5_D6_current2836/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D6_current2836/profile.py"
added: 2026-10-27T18:51:36Z
tags: ["ddp", "method-ledger"]
---

# (5,6)2836实际全5正则：保边star/proxy增点无接口

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (5,6)；L=2836；known_source_or_recovery n=2836；条件性n=2837（未据此计纪录）

**距目标的证据：** 原图每点已满度5；保所有旧边且maxdegree5时不存在任何old-new边，故任意正数量新点均与oldsource断开。完整关闭此fixedsource保边连接增广机制，不是order2837一般不存在。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 2836,
  "source_m": 7090,
  "source_reported_D": 6,
  "source_D6_reused": true,
  "degree5_vertices": 2836,
  "free_vertices": 0,
  "free_slots": 0,
  "minSatN": 5,
  "saturated_neighbor_histogram": {
    "5": 2836
  },
  "layer_count": 106,
  "profile_CPU": 0.014542602000000002,
  "BFS": 0,
  "candidate_graphs": 0,
  "anchors_searched": 0,
  "prediction": "SUPPORTED_NO_FREE_ACTUAL_VERTICES"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_D6_current2836/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D6_current2836/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D6_current2836/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D6_current2836/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D6_current2836/profile.py](../../research/ddp/more_graphs_20261027/d5_D6_current2836/profile.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Bhakar current actual2836/7090/simple，全部degree5，free0/slots0/minSatN5。106layer每点1point+1line+3layer，6719baseflags/212cross/159layer。只一遍literal degree/near-star profile，0BFS/候选。

**仍未完成：** Source-edge deletion/rewiring, other sources, general degree5 diameter6 graphs; no claim of optimality or Lean completion.

**启发与重启依据：** 几何增广layer也可能已经用满所有容量；应先实际free/minSatN，而非因106新增点猜有proxy余量。仅有效改变删边/rewiring或另有真实free源时重启，不在此源上开anchors或helpers。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

