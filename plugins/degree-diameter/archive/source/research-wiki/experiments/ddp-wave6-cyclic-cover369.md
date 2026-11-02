---
type: experiment
node_id: exp:ddp-wave6-cyclic-cover369
title: "Allwright41(1a)普通C9电压覆盖"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/cyclic_cover369/REPORT.md; research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges; research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_check.json; research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_distances.json; research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_source.adjlist.txt; research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.independent_check.json; research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.json; research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.py; research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity_witness.json; research/ddp/breadth_20261027_wave6/cyclic_cover369/terminal.json; research/ddp/breadth_20261027_wave6/cyclic_cover369/tree_gauge.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# Allwright41(1a)普通C9电压覆盖

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (4,5)；L=364；条件性n=369（未据此计纪录）

**距目标的证据：** 根0 self≤5只有{0,±T,±P}五种形式，5<9；整个固定投影不可能。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 41,
  "source_known_D": 3,
  "capacity": 5,
  "required_states": 9,
  "starts": 0,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave6/cyclic_cover369/REPORT.md](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/REPORT.md)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_check.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_check.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_distances.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_distances.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_source.adjlist.txt](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/base41_source.adjlist.txt)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.independent_check.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.independent_check.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.py](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity.py)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity_witness.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/capacity_witness.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/terminal.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/terminal.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover369/tree_gauge.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover369/tree_gauge.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定Allwright41(1a)全部C9电压赋值；树gauge无损

**正向保证：** 源41实际simple4regularD3已首次检查；ordinary cover保持degree4

**仍未完成：** 不排其他41底图或非普通cover；未生成369图。

**启发与重启依据：** 只有改变base闭路容量才值得继续。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

