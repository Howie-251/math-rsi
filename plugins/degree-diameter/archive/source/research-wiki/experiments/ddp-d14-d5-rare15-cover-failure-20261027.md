---
type: experiment
node_id: exp:ddp-d14-d5-rare15-cover-failure-20261027
title: "(14,5)稀有15点类：全部14子集无完整覆盖"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/RARE15_PREDICTION.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/RARE15_RESULT.json"
added: 2026-10-27T17:26:52Z
tags: ["ddp", "method-ledger"]
---

# (14,5)稀有15点类：全部14子集无完整覆盖

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (14,5)；L=94186；条件性n=94187（未据此计纪录）

**距目标的证据：** 15个degree12点中52155/85397为false twins；其余pairs无共同邻点。15次R4与15个留一子集全部完成，漏9754..11640；14个不同邻域代表与全15的并相同，仍漏9754。0新图。

**其他指标（保持原计数类型）：**
```json
{
  "R4_balls": 15,
  "fourteen_subsets": 15,
  "minimum_newroot_uncovered_old_vertices": 9754,
  "maximum_newroot_uncovered_old_vertices": 11640,
  "missing_vertex_degree_histogram": {
    "13": 409,
    "14": 9345
  },
  "prediction": "REFUTED",
  "CPU_including_compile": 1.499629988
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/RARE15_PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/RARE15_PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/RARE15_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/RARE15_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 15个degree12点中52155/85397为false twins；其余pairs无共同邻点。15次R4与15个留一子集全部完成，漏9754..11640；14个不同邻域代表与全15的并相同，仍漏9754。0新图。

**仍未完成：** No third-parameter complete record has been generated in these source/rareclass stages.

**启发与重启依据：** 稀有双余量不保证覆盖互补，false twins重复路线。停止这个固定子集，下一规则改全部free点并以全覆盖为唯一接受条件；不按漏点减少无限微调。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

