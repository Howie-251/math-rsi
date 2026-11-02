---
type: experiment
node_id: exp:ddp-wave11-new-route-scout
title: "norm5/PSL2(F11)固定算术候选：937短词漏132单位根目标"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave11/new_route_scout/REPORT.md; research/ddp/breadth_20261027_wave11/new_route_scout/RESULT.json; research/ddp/breadth_20261027_wave11/new_route_scout/PROBE.json; research/ddp/breadth_20261027_wave11/new_route_scout/probe.py; research/ddp/breadth_20261027_wave11/new_route_scout/root_witness_check.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# norm5/PSL2(F11)固定算术候选：937短词漏132单位根目标

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** fixed-arithmetic-word-endpoint-screen

**目标与阶数：** (6,4)；L=441；条件性n=660（未据此计纪录）

**距目标的证据：** No ordinary graph BFS;complete reducedwords<=4 unit-root endpoint screen disproves this fixed D4 candidate;one missing witness independently confirmed.；937个约化词只覆盖528/660类，漏132个单位根目标。w=[[0,1],[10,1]]为显式遗漏；root另用37个R2端点的S2分解独立确认此一个w不能≤4到达，没有重枚举937词或全源BFS。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "fixed_arithmetic_endpoint_filter",
  "defined_group_order": 660,
  "defined_degree": 6,
  "defined_edges": 1980,
  "raw_reduced_words_by_length": [
    1,
    6,
    30,
    150,
    750
  ],
  "total_reduced_words": 937,
  "cumulative_distinct_endpoints": [
    1,
    7,
    37,
    184,
    528
  ],
  "unit_root_R4_covered": 528,
  "unit_root_missing_targets": 132,
  "producer_missing_witness": [
    0,
    1,
    10,
    1
  ],
  "root_confirmed_missing_witness_count": 1,
  "root_R2_endpoint_count": 37,
  "root_S2_factorization_test_empty": true,
  "root_repeated937_enumeration": false,
  "source_full_graph_adjacency_generated": false,
  "BFS_count": 0,
  "producer_CPU_seconds": 0.004563325,
  "root_witness_CPU_seconds": 0.003219645
}
```





**原始证据：** [research/ddp/breadth_20261027_wave11/new_route_scout/REPORT.md](../../research/ddp/breadth_20261027_wave11/new_route_scout/REPORT.md)；[research/ddp/breadth_20261027_wave11/new_route_scout/RESULT.json](../../research/ddp/breadth_20261027_wave11/new_route_scout/RESULT.json)；[research/ddp/breadth_20261027_wave11/new_route_scout/PROBE.json](../../research/ddp/breadth_20261027_wave11/new_route_scout/PROBE.json)；[research/ddp/breadth_20261027_wave11/new_route_scout/probe.py](../../research/ddp/breadth_20261027_wave11/new_route_scout/probe.py)；[research/ddp/breadth_20261027_wave11/new_route_scout/root_witness_check.json](../../research/ddp/breadth_20261027_wave11/new_route_scout/root_witness_check.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅模11、六个整数四元数norm5的射影矩阵生成类；定义660点6reg、理论1980边，不改q或S。完整单位根长度0..4 reduced words，非群/生成集搜索。

**正向保证：** 六矩阵互异、非单位、实际逆封闭；右Cayley图由左平移把单位根覆盖等价为全图D4条件。；所有最短路可约掉相邻逆元，因此937 reduced words覆盖全部≤4单位根端点可能。

**仍未完成：** 只否定这一个六生成元候选D4，不排PSL2(F11)其它S或其它算术路由；未测实际D、连通性或全图ordinary无序坏对。132不是全图无序坏对。

**启发与重启依据：** 局部近树增长与算术/谱扩张不保证四步模投影覆盖。该固定候选必要条件已失败，停止；不能仅换群名/模数当新机制续跑。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

