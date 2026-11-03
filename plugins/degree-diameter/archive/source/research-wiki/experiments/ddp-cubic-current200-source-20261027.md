---
type: experiment
node_id: exp:ddp-cubic-current200-source-20261027
title: "(3,7)200真实源：五个Wagner块与四条20cycle的40群电压提升"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/SOURCE.json; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/source200.edges; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/README.author.md; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/construction.author.json"
added: 2026-10-27T18:55:02Z
tags: ["ddp", "method-ledger"]
---

# (3,7)200真实源：五个Wagner块与四条20cycle的40群电压提升

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (3,7)；L=200；known_source_or_recovery n=200

**距目标的证据：** 实际D=7，目标D=7；沿用作者公开source验证；本轮只读实际边表和配方，没有source全直径BFS。；恢复了实际source及其路线结构；无空余度。source恢复不计新图或独立构造方法。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 200,
  "source_m": 300,
  "degree_histogram": {
    "3": 200
  },
  "free_vertices": 0,
  "fibres": 5,
  "fibre_size": 40,
  "source_allBFS": 0,
  "source_author": "Nishant Bhakar",
  "source_URL": "https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg3/dia7",
  "source_saved_date": "2026-10-27",
  "source_reported_D": 7,
  "is_new_lower_bound": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/SOURCE.json](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/SOURCE.json)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/source200.edges](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/source200.edges)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/README.author.md](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/README.author.md)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/construction.author.json](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/construction.author.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 作者当前repo实际200/300全三正则；5个40点纤维，G=C5⋊_4C8。底图恒等电压0-1/0-2/0-3/1-4，1→2电压y，2处半边y^4，3/4处环xy²/x²y²。五个细分Wagner块经四条20圈连接。

**仍未完成：** 固定source与固定操作的结论不排除其它连接机制、其它source或一般目标阶数图；没有新增下界或Lean实例。

**启发与重启依据：** 同一source作有明确操作的路线保持检验；不重验已公开D7，不将旧AFY70普通cover失败外推到此source。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

