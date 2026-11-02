---
type: experiment
node_id: exp:ddp-more-graphs-20261027-small120-cayley-d4
title: "S5与SL2(F5)全部四元逆闭Cayley集：29542项完整0命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small120_cayley_d4/REPORT.md; research/ddp/more_graphs_20261027/small120_cayley_d4/RESULT.json; research/ddp/more_graphs_20261027/small120_cayley_d4/PREDICTION.json; research/ddp/more_graphs_20261027/small120_cayley_d4/GROUPS.json; research/ddp/more_graphs_20261027/small120_cayley_d4/ENUMERATION.json; research/ddp/more_graphs_20261027/small120_cayley_d4/prepare.py; research/ddp/more_graphs_20261027/small120_cayley_d4/enumerate.cpp; research/ddp/more_graphs_20261027/small120_cayley_d4/group_elements.json; research/ddp/more_graphs_20261027/small120_cayley_d4/group_tables.txt; research/ddp/more_graphs_20261027/small120_cayley_d4/COMPILE.json; research/ddp/more_graphs_20261027/small120_cayley_d4/terminal.json"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# S5与SL2(F5)全部四元逆闭Cayley集：29542项完整0命中

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** complete-two-fixed-groups-quartic-Cayley-screen

**目标与阶数：** (4,4)；L=104；条件性n=120（未据此计纪录）；从属目标：[[4, 4]]

**距目标的证据：** One exact identity-root breadth expansion throughdepth4 per generator set using concrete120x120 multiplication tables. No separate fullgraph all-source BFS, no new graph edge tables, no best ordinary badpair score or localrepair.；S5全部27831和SL2(F5)全部1711项0命中，预测REFUTED。SL2商60已四步全满的项数也是0，未得到商已满但sheet缺的例子。

**其他指标（保持原计数类型）：**
```json
{
  "generator_sets_total": 29542,
  "S5_sets": 27831,
  "SL2F5_sets": 1711,
  "full_hits": 0,
  "central_quotient60_full_sets": 0,
  "quotient60_full_but120_notfull": 0,
  "new_graphs": 0,
  "independent_120graph_checks": 0,
  "best_badpairs_saved": false,
  "preparation_CPU_seconds": 0.016816636999999995,
  "native_CPU_seconds": 0.011523,
  "compile_user_CPU_seconds": 1.31966,
  "compile_system_CPU_seconds": 0.103222,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "label": "S5-all-quartic-inverseclosed",
    "target": [
      4,
      4
    ],
    "savedL": 104,
    "n": {
      "actual": null,
      "hypothetical": 120
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "generator_sets_enumerated": 27831,
    "four_involution_sets": 12650,
    "two_involutions_onepair_sets": 14100,
    "two_pair_sets": 1081,
    "full120_hits": 0,
    "central_quotient60_full_sets": null,
    "metric_scope": "Counts of generator sets and exact identityroot endpoint coverage, not wholegraph ordinary badpairs."
  },
  {
    "label": "SL2F5-all-quartic-inverseclosed",
    "target": [
      4,
      4
    ],
    "savedL": 104,
    "n": {
      "actual": null,
      "hypothetical": 120
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "generator_sets_enumerated": 1711,
    "four_involution_sets": 0,
    "two_involutions_onepair_sets": 0,
    "two_pair_sets": 1711,
    "full120_hits": 0,
    "central_quotient60_full_sets": 0,
    "metric_scope": "Counts of generator sets and exact identityroot endpoint coverage, not wholegraph ordinary badpairs."
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/small120_cayley_d4/REPORT.md](../../research/ddp/more_graphs_20261027/small120_cayley_d4/REPORT.md)；[research/ddp/more_graphs_20261027/small120_cayley_d4/RESULT.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/RESULT.json)；[research/ddp/more_graphs_20261027/small120_cayley_d4/PREDICTION.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/PREDICTION.json)；[research/ddp/more_graphs_20261027/small120_cayley_d4/GROUPS.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/GROUPS.json)；[research/ddp/more_graphs_20261027/small120_cayley_d4/ENUMERATION.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/ENUMERATION.json)；[research/ddp/more_graphs_20261027/small120_cayley_d4/prepare.py](../../research/ddp/more_graphs_20261027/small120_cayley_d4/prepare.py)；[research/ddp/more_graphs_20261027/small120_cayley_d4/enumerate.cpp](../../research/ddp/more_graphs_20261027/small120_cayley_d4/enumerate.cpp)；[research/ddp/more_graphs_20261027/small120_cayley_d4/group_elements.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/group_elements.json)；[research/ddp/more_graphs_20261027/small120_cayley_d4/group_tables.txt](../../research/ddp/more_graphs_20261027/small120_cayley_d4/group_tables.txt)；[research/ddp/more_graphs_20261027/small120_cayley_d4/COMPILE.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/COMPILE.json)；[research/ddp/more_graphs_20261027/small120_cayley_d4/terminal.json](../../research/ddp/more_graphs_20261027/small120_cayley_d4/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All inverseclosed subsets of4 distinct nonidentity elements in the concrete groups S5 andSL2(F5), no conjugacy/orbit reduction and no connectedness prescreen. Nongenerating sets are included and naturally fail rootcoverage.

**正向保证：** 完整逆闭类别划分不漏集合，非生成集保留。；群乘法/元素/逆直接由具体排列和模5矩阵生成，无旧source复验。

**仍未完成：** Only two fixed groups and quartic Cayleysets are excluded. Arbitrary120vertexgraph existence, other groups and other mechanisms remain open.

**启发与重启依据：** S5纯even不能跨奇偶，纯odd二分容量不足；mixed亦完整失败。SL2的失败已在中心商路线层发生。停止两群固定scope，不按best坏对修补或自动换群；改变机制须有新的全局覆盖依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

