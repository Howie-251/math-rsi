---
type: experiment
node_id: exp:ddp-d10-d7-current624690-source-recovery-20261027
title: "(10,7)624690真实CRT源与规范化恢复：faithful90 prime迁移暂列备用"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d10_D7_current624690_source/REPORT.md; research/ddp/more_graphs_20261027/d10_D7_current624690_source/SOURCE_FACTS.json; research/ddp/more_graphs_20261027/d10_D7_current624690_source/ARITHMETIC.json; research/ddp/more_graphs_20261027/d10_D7_current624690_source/AUTHOR_construction.json; research/ddp/more_graphs_20261027/d10_D7_current624690_source/AUTHOR_README.md; research/ddp/more_graphs_20261027/d10_D7_current624690_source/source_arithmetic.py"
added: 2026-10-27T23:03:52Z
tags: ["ddp", "method-ledger"]
---

# (10,7)624690真实CRT源与规范化恢复：faithful90 prime迁移暂列备用

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (10,7)；L=624690；条件性n=680490（未据此计纪录）

**距目标的证据：** Primary source reports624690/D7; only small recipe and arithmetic recovered; no actual large edgefile or BFS.；Source recovered: global action order90, CRT component orders10/45,11 involutions. Minimum larger faithful90 prime7561 yields hypothetical680490(+8.93%), greater relative jump than active degree8 transfer; primefield involution class changes to7561.

**其他指标（保持原计数类型）：**
```json
{
  "source_author_reported_n": 624690,
  "source_N": 6941,
  "source_M": 90,
  "source_r": 316,
  "source_D_author_reported": 7,
  "source_Delta_author_reported": 10,
  "source_graph_downloaded": false,
  "source_BFS": 0,
  "new_graphs": 0,
  "embedding_evaluations": 0,
  "action_orders": {
    "mod11": 10,
    "mod631": 45,
    "mod6941": 90
  },
  "normalized_source_generators": [
    [
      0,
      1
    ],
    [
      1,
      5
    ],
    [
      2847,
      35
    ],
    [
      3471,
      52
    ],
    [
      3355,
      67
    ]
  ],
  "baseline_date": "2026-10-27",
  "source_credit": "Nishant Bhakar f4t4nt/degree-diameter-graphs graphs/deg10/dia7 primary recipe/README"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d10_D7_current624690_source/REPORT.md](../../research/ddp/more_graphs_20261027/d10_D7_current624690_source/REPORT.md)；[research/ddp/more_graphs_20261027/d10_D7_current624690_source/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d10_D7_current624690_source/SOURCE_FACTS.json)；[research/ddp/more_graphs_20261027/d10_D7_current624690_source/ARITHMETIC.json](../../research/ddp/more_graphs_20261027/d10_D7_current624690_source/ARITHMETIC.json)；[research/ddp/more_graphs_20261027/d10_D7_current624690_source/AUTHOR_construction.json](../../research/ddp/more_graphs_20261027/d10_D7_current624690_source/AUTHOR_construction.json)；[research/ddp/more_graphs_20261027/d10_D7_current624690_source/AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d10_D7_current624690_source/AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d10_D7_current624690_source/source_arithmetic.py](../../research/ddp/more_graphs_20261027/d10_D7_current624690_source/source_arithmetic.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Unique primary N6941/M90/r316 five-pair source; exact group law/gauge/action and CRT kernel arithmetic only. No embedding/parameter search.

**仍未完成：** No larger graph ruled out, no new-field action/offset family tested.

**启发与重启依据：** Preserve source CRT relations and explain a new complete-route rule before any numerical transfer; merely changing group order does not preserve coverage. Parent separately owns C90-to-C180 central lift; this worker did not enumerate its words or graph.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

