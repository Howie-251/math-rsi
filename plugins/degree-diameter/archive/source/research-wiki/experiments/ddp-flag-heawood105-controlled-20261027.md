---
type: experiment
node_id: exp:ddp-flag-heawood105-controlled-20261027
title: "同旗规则Heawood105实例：AA预测验中，其它类型仍失盖，实际D6"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/PREDICTION.json; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/construct.py; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/RESULT.json; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/graph105.edges"
added: 2026-10-27T16:02:06Z
tags: ["ddp", "method-ledger"]
---

# 同旗规则Heawood105实例：AA预测验中，其它类型仍失盖，实际D6

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,4)；L=104；candidate_graph_or_family n=105

**距目标的证据：** 实际D=6，目标D=4；普通无序坏对=735；All105roots ordinary BFS ofnewcandidate byproducer; failurediagnostic, no repeated source verification.；完整105点189边simpleconnected图，max4/min3，D6，普通无序>4对735。按AA/AB/AC/BB/BC/CC分别0/84/42/21/336/252；首次markedflag A0-C63距6。保住AA预测得到支持，CC失盖预测也支持。

**其他指标（保持原计数类型）：**
```json
{
  "new_record": false,
  "bad_by_types": {
    "AA": 0,
    "AB": 84,
    "AC": 42,
    "BB": 21,
    "BC": 336,
    "CC": 252
  },
  "old_source_BFS": 0,
  "CPU_seconds": 0.007502339
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/construct.py](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/construct.py)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/RESULT.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/RESULT.json)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/graph105.edges](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/thin_heawood105/graph105.edges)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactlyone(s2,t1)geometry:21edges/14vertexstars ofFanoHeawood,applycompleteflagoperator. All105candidate roots examined,no oldsourceBFS orrepair.

**仍未完成：** 本轮没有产生新的验收通过纪录；一般图及未明示范围仍开放，Lean完整实例0。

**启发与重启依据：** incidence距离必要界过线不代表各类同时覆盖；薄t1缺第三条line，不能靠相同规则加helper或局部改漏点。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

