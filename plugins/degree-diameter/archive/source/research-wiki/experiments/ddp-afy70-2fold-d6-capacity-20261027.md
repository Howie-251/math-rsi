---
type: experiment
node_id: exp:ddp-afy70-2fold-d6-capacity-20261027
title: "(3,6)AFY70的2重cover：短闭路/路线容量均匀排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/cubic_D6_twofold70/REPORT.md; research/ddp/more_graphs_20261027/cubic_D6_twofold70/RESULT.json"
added: 2026-10-27T17:50:48Z
tags: ["ddp", "method-ledger"]
---

# (3,6)AFY70的2重cover：短闭路/路线容量均匀排除

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-capacity-obstruction

**目标与阶数：** (3,6)；L=132；条件性n=140（未据此计纪录）

**距目标的证据：** 固定官方AFY70源70/105，在D=6内70个diagonal槽均只有identity路径，另有不同点容量1槽；全部4900端点槽检查，1204槽只有1个raw NBroute/form，不能覆盖2sheets。0电压赋值/线性求解/BFS/新图。

**其他指标（保持原计数类型）：**
```json
{
  "base_n": 70,
  "base_m": 105,
  "cover_fibers": 2,
  "ordered_slots": 4900,
  "capacity_one_slots": 1204,
  "diagonal_identity_only": 70,
  "voltage_assignments": 0,
  "linear_system_run": false,
  "CPU_seconds": 0.02555,
  "strict_scope_excluded": true,
  "arbitrary_graph_excluded": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/cubic_D6_twofold70/REPORT.md](../../research/ddp/more_graphs_20261027/cubic_D6_twofold70/REPORT.md)；[research/ddp/more_graphs_20261027/cubic_D6_twofold70/RESULT.json](../../research/ddp/more_graphs_20261027/cubic_D6_twofold70/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定官方AFY70源70/105，在D=6内70个diagonal槽均只有identity路径，另有不同点容量1槽；全部4900端点槽检查，1204槽只有1个raw NBroute/form，不能覆盖2sheets。0电压赋值/线性求解/BFS/新图。

**仍未完成：** No general source-family maximality is claimed; final concrete Lean remains incomplete.

**启发与重启依据：** 先检查同fiber短闭路和端点路线数，避免盲扫电压。任何此source普通2重cover都不能D≤6（或不连通），不排其它70source/新基图/任意degree3图。D6结果促使有依据查D7，D7仍失败后停止该机制，不续D8长尾。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

