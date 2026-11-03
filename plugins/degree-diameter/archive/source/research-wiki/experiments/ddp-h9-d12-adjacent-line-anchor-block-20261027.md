---
type: experiment
node_id: exp:ddp-h9-d12-adjacent-line-anchor-block-20261027
title: "N12相邻Q-line双点各加anchor：冻结32对精确无完整块"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d12_adjacent_line_anchor_block/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_adjacent_line_anchor_block/RESULT.json"
added: 2026-10-27T14:08:26Z
tags: ["ddp", "method-ledger"]
---

# N12相邻Q-line双点各加anchor：冻结32对精确无完整块

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-controlled-variant-no-new-graph

**目标与阶数：** (12,5)；L=42342；条件性n=42399（未据此计纪录）

**距目标的证据：** 32对全部精确无hit；全13895oldanchors及444077个a角色已作exactb交集，0候选图。其余59290兼容pair未算；native0.81731CPU秒。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "source_n": 42397,
  "degreecompatible_pairs": 59322,
  "exact_pairs_checked": 32,
  "unattempted_pairs": 59290,
  "general_family_excluded": false,
  "native_CPU_seconds": 0.81731,
  "allsource_BFS_executed": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_d12_adjacent_line_anchor_block/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_adjacent_line_anchor_block/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_adjacent_line_anchor_block/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_adjacent_line_anchor_block/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed42397;346 degreelegal tenpinlines,59322 degreecompatible pairs. Freeze32pairs by actualbuddy-root residualsupport before coupledoneanchor-per-newpoint check.

**正向保证：** For adjacentnewz/w, exactnew-old distances are min(1+d_B(S,x),2+d_B(T,x)); bothrootcoverconditions and actualoldload constraints were included.

**仍未完成：** Only32 frozenpairs closed. The rest of the compatiblepair family remains untested.

**启发与重启依据：** A buddyvertex can in principle replace an oldanchor through R3, but these selectedcoupled roles cannot be jointly realized. Stop the fixedbatch; no newseed or thirdpoint.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

