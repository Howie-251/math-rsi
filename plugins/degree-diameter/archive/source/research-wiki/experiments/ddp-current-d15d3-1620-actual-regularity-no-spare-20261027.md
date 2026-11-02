---
type: experiment
node_id: exp:ddp-current-d15d3-1620-actual-regularity-no-spare-20261027
title: "(15,3)current1620实际全15正则：五外部线路，无odd-cell free入口"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d15_D3_current1620_source/REPORT.md; research/ddp/more_graphs_20261027/d15_D3_current1620_source/PREDICTION.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/SOURCE_FACTS.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/RESULT.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/terminal.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/PRIMARY_RECEIPTS.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/README.author.md; research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json; research/ddp/more_graphs_20261027/d15_D3_current1620_source/source1620.author.edges.txt; research/ddp/more_graphs_20261027/d15_D3_current1620_source/source1620.header.edges; research/ddp/more_graphs_20261027/d15_D3_current1620_source/profile.py"
added: 2026-10-27T21:21:43Z
tags: ["ddp", "method-ledger"]
---

# (15,3)current1620实际全15正则：五外部线路，无odd-cell free入口

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (15,3)；L=1620；known_source_or_recovery n=1620

**距目标的证据：** Published sourceD3 inherited; this worker only profiled the complete actual1620 literal, without any ordinary BFS.；metadata-based全regular预测SUPPORTED，free0/slots0/minSatN15/zero及onefault0；0旧BFS/R2/solver/新图。s的base semi-edge经Z20电压10连不同cells，不是odd27内部involution；不能沿972 fixedpoint空位技巧迁移。

**其他指标（保持原计数类型）：**
```json
{
  "source_n_actual": 1620,
  "source_m_actual": 12150,
  "source_bytes": 105809,
  "source_degree_histogram_actual": {
    "15": 1620
  },
  "free_vertices": 0,
  "free_slots": 0,
  "minSatN": 15,
  "zero_fault_count": 0,
  "onefault_count": 0,
  "fiber_blocks_actual": 60,
  "fiber_size_actual": 27,
  "internal_edges_actual": 0,
  "quotient_degree_actual": 5,
  "edges_per_adjacent_block": 81,
  "per_vertex_neighbors_in_each_adjacent_block": 3,
  "source_BFS": 0,
  "R2_cache": 0,
  "solver_runs": 0,
  "candidate_graphs": 0,
  "profile_CPU_seconds": 0.023142106999999995,
  "baseline_date": "2026-10-27",
  "baseline_provenance": "Parent main-table refresh21:10 current1620; this worker did not refresh main table.",
  "source_credit": "Nishant Bhakar f4t4nt/degree-diameter-graphs graphs/deg15/dia3; primary README/construction and actualedgefile locally retained."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d15_D3_current1620_source/REPORT.md](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/REPORT.md)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/SOURCE_FACTS.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/RESULT.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/terminal.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/terminal.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/PRIMARY_RECEIPTS.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/PRIMARY_RECEIPTS.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/README.author.md](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/README.author.md)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/source1620.author.edges.txt](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/source1620.author.edges.txt)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/source1620.header.edges](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/source1620.header.edges)；[research/ddp/more_graphs_20261027/d15_D3_current1620_source/profile.py](../../research/ddp/more_graphs_20261027/d15_D3_current1620_source/profile.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一当前Bhakar1620 actual literal和完整recipe。一次105809byte下载，实际1620/12150，全15reg；60independent27cells，五external符号各给3邻居。保全部旧边max15加点/助手组无任何oldpin。

**仍未完成：** Degree-releasing deletions, different source constructions and general larger(15,3)graphs are not excluded.

**启发与重启依据：** 奇纤维本身不蕴含free；必须先恢复实际内部/外部度预算。停止本源保边star/proxy，不因无空位而称一般1621图不可能；其它操作需改变旧连接机制并另定范围。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

