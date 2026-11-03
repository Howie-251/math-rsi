---
type: experiment
node_id: exp:ddp-wave7-rajiv252-cell-structure
title: "Rajiv252七胞元完整组合坐标恢复"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md; research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/RESULT.json; research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/coordinate_tables.json; research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/recover.py; research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/regenerated252.edges"
added: 2026-10-27T07:55:18Z
tags: ["ddp", "method-ledger"]
---

# Rajiv252七胞元完整组合坐标恢复

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (5,4)；L=252

**距目标的证据：** 42+105+105点、630边按组合规则逐边重建完全相等。

**其他指标（保持原计数类型）：**
```json
{
  "known_source_n": 252,
  "reconstructed_edges": 630,
  "edge_equality": true,
  "new_BFS": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md](../../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md)；[research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/RESULT.json](../../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/RESULT.json)；[research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/coordinate_tables.json](../../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/coordinate_tables.json)；[research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/recover.py](../../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/recover.py)；[research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/regenerated252.edges](../../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/regenerated252.edges)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 从旧252边表恢复七K6胞元、35B三角形及pentad/syntheme坐标；不是新record

**正向保证：** 完整V/E生成规则已恢复；固定胞元/三角形模板D4要求胞元≤7

**仍未完成：** A7作者原生成元未恢复；该七胞元上限不限制一般(5,4)图。

**启发与重启依据：** 后续须改变模板的远端覆盖条件，不能只加第八胞元。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

