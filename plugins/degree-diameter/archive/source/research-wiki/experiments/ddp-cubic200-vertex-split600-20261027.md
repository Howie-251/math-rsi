---
type: experiment
node_id: exp:ddp-cubic200-vertex-split600-20261027
title: "(3,7)200→201全部600标号拆分：恰D8，0完整D7命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/PREDICTION.json; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/RESULT.json; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/terminal.json; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/cases.tsv; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/probe.cpp; research/ddp/more_graphs_20261027/cubic_D7_vertex_split/run.py"
added: 2026-10-27T18:55:02Z
tags: ["ddp", "method-ledger"]
---

# (3,7)200→201全部600标号拆分：恰D8，0完整D7命中

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (3,7)；L=200；条件性n=201（未据此计纪录）

**距目标的证据：** 实际D=8，目标D=7；全部600实际内存候选：每项为source的一条边细分，继承sourceD7给D≤8；各项已保存>7见证给D≥8。没有选定/导出代表完整边表，也没有逐项全源BFS。；事前至少一项D7的预测REFUTED。所有600候选恰D8；这是上界证明与反例结合，不是全图坏对计数。首个newroot通过者ordinal360/v120/singleton0，新根完整R7覆盖，但旧0→41>7。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 200,
  "source_m": 300,
  "candidate_n": 201,
  "candidate_m": 301,
  "candidate_degree_histogram": {
    "2": 1,
    "3": 200
  },
  "labelled_scope": 600,
  "structurally_unique_edge_subdivisions": 300,
  "visited": 600,
  "unattempted": 0,
  "UNKNOWN": 0,
  "newroot_fail": 520,
  "newroot_pass": 80,
  "newroot_pass_oldpair_fail": 80,
  "modified_graph_root_BFS": 715,
  "source_R3_search_roots": 200,
  "source_full_diameter_BFS": 0,
  "derived_all_candidate_D": 8,
  "derived_D_upper_bound_reason": "One edge subdivision increases every old distance by at most one; newpoint-to-old distance is at most one plus an old endpoint distance.",
  "derived_D_lower_bound_reason": "Every candidate has a saved root/target witness with distance greater than seven.",
  "first_newroot_pass_oldpair_witness": {
    "ordinal": 360,
    "vertex": 120,
    "singleton": 0,
    "first_bad_root": 0,
    "first_bad_target": 41,
    "distance_lower_bound": 8
  },
  "witness_root_membership": "0 is a source neighbor of split vertex120, hence lies in R1_G(120)⊆R3_G(120); verified from literal edge0-120 without BFS.",
  "native_CPU_seconds": 0.006137,
  "compile_CPU_seconds": 0.86158,
  "total_CPU_seconds": 0.869739975,
  "new_lower_bound_graphs": 0,
  "source_author": "Nishant Bhakar",
  "baseline_date": "2026-10-27"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/REPORT.md)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/PREDICTION.json](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/PREDICTION.json)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/RESULT.json](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/RESULT.json)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/terminal.json](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/terminal.json)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/cases.tsv](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/cases.tsv)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/probe.cpp](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/probe.cpp)；[research/ddp/more_graphs_20261027/cubic_D7_vertex_split/run.py](../../research/ddp/more_graphs_20261027/cubic_D7_vertex_split/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 全部200旧点×3 singleton选择=600标号1+2相邻拆分，对应全部300旧边细分各两种标号。删去v至非singleton的两边，新点接这两个旧邻点及v；旧v度2，其余度3，201/301。全部600已测、0未试/UNKNOWN/导出；520新根失败，80新根通过但全有旧旧反例。

**仍未完成：** 固定source与固定操作的结论不排除其它连接机制、其它source或一般目标阶数图；没有新增下界或Lean实例。

**启发与重启依据：** connector的两圈路线与块内路线可让新根覆盖，却未保护全部旧旧路线。此固定source全部单边细分已闭；不按失败点追加edgepair、删边或局部修补。重启需实质不同的连接机制或新source。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

