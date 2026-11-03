---
type: experiment
node_id: exp:ddp-exoo72-critical-route-intuition-20261027
title: "Exoo72紧路线与两类halfturn删边限制：强预测仅部分成立"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/REPORT.md; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/RESULT.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CRITICAL_MATCHING_CERTIFICATES.json"
added: 2026-10-27T15:27:58Z
tags: ["ddp", "method-ledger"]
---

# Exoo72紧路线与两类halfturn删边限制：强预测仅部分成立

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (5,3)；L=72；known_source_or_recovery n=72

**距目标的证据：** 实际D=3，目标D=3；KnownpublicExoo72source;targetedshortpathsupportdiagnosis,no repeated sourceBFS.；无3/4圈，1080个唯一三步距离3点对。所有edge都有6-disjoint-critical-pairs的预测被反驳，仅两个内部halfturn轨道成立，其余matching3..5。

**其他指标（保持原计数类型）：**
```json
{
  "unique_distance3_pairs": 1080,
  "vertex_orbits": 6,
  "edge_orbits": 16,
  "uniform_six_critical_pair_prediction": "REFUTED",
  "source_BFS": 0,
  "CPU_seconds": 0.146835983
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/REPORT.md](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/REPORT.md)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/RESULT.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/RESULT.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CRITICAL_MATCHING_CERTIFICATES.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CRITICAL_MATCHING_CERTIFICATES.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ActualExoo72source;allshortsimplepath supports andsixC12vertexorbits/16edgeorbits. No sourceBFS/candidategraphgrid.

**仍未完成：** 一般(5,3)超过72仍未解；此受限范围不是全题，完整Lean实例0。

**启发与重启依据：** 新root三步修复旧旧对必须有端点在S，故S要vertexcover所有被删边critical pairs；只将实际有6-matching证书的边排除，不把其它轨道自动关掉。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

