---
type: experiment
node_id: exp:ddp-d4-d6-current760-source-20261027
title: "(4,6)760真实源：728incidence+32flag层，三个cycle8/8/16"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D6_flag760_extension/REPORT.md; research/ddp/more_graphs_20261027/d4_D6_flag760_extension/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d4_D6_flag760_extension/RECIPE_BINDING.json; research/ddp/more_graphs_20261027/d4_D6_flag760_extension/PROOF.md"
added: 2026-10-27T18:46:57Z
tags: ["ddp", "method-ledger"]
---

# (4,6)760真实源：728incidence+32flag层，三个cycle8/8/16

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (4,6)；L=760；known_source_or_recovery n=760

**距目标的证据：** 实际760/1520全4regular、free0；728个H3 incidence原顶点+32flag-subdivision。当前coreflags1424/cross64/layer32，layer cycles8,8,16。作者D6沿用，无source全BFS；冻结1424×32单flag/单layer吸收候选。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 760,
  "source_m": 1520,
  "degree4": 760,
  "free_vertices": 0,
  "original_incidence_vertices": 728,
  "layer_vertices": 32,
  "core_flag_edges": 1424,
  "cross_edges": 64,
  "layer_edges": 32,
  "layer_cycle_lengths": [
    8,
    8,
    16
  ],
  "source_allBFS": 0,
  "frozen_candidates": 45568,
  "prepare_CPU_seconds": 0.098789662,
  "source_author": "Nishant Bhakar; classicalH3 incidence foundation",
  "baseline_date": "2026-10-27"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D6_flag760_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D6_flag760_extension/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d4_D6_flag760_extension/RECIPE_BINDING.json](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/RECIPE_BINDING.json)；[research/ddp/more_graphs_20261027/d4_D6_flag760_extension/PROOF.md](../../research/ddp/more_graphs_20261027/d4_D6_flag760_extension/PROOF.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际760/1520全4regular、free0；728个H3 incidence原顶点+32flag-subdivision。当前coreflags1424/cross64/layer32，layer cycles8,8,16。作者D6沿用，无source全BFS；冻结1424×32单flag/单layer吸收候选。

**仍未完成：** Knownsource recovery is not a newlowerbound. General761 constructions andcompleteLean remainopen.

**启发与重启依据：** 源无空余度，保旧边增点没有接口；可恢复原flag-subdivision+layer2factor机制，再冻结精确吸收操作。未把32layer误作单C32，不重验已知D6。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

