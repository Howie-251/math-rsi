---
type: experiment
node_id: exp:ddp-d12-d4-four-rank3-packet65-20261027
title: "四rank3路线并非pencil：每源只65/81，改offset无救"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/bad4_packet_probe/REPORT.md; research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/bad4_packet_probe/RESULT.json"
added: 2026-10-27T18:32:57Z
tags: ["ddp", "method-ledger"]
---

# 四rank3路线并非pencil：每源只65/81，改offset无救

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-route-obstruction

**目标与阶数：** (12,4)；L=6156

**距目标的证据：** AABa/Abaa/Babb/BBAb在base0闭合；y9,m20使四路同到phase10。四法向量(0,1,2,2),(0,1,1,2),(1,0,1,2),(1,0,1,1)秩4而非2，全部81source的并恒65、缺16。

**其他指标（保持原计数类型）：**
```json
{
  "normals_rank": 4,
  "hyperplane_size": 27,
  "source_coordinates": 81,
  "union_size": 65,
  "missing": 16,
  "CPU": 0.007854,
  "BFS": 0,
  "graphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/bad4_packet_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/bad4_packet_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/bad4_packet_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/bad4_packet_probe/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** AABa/Abaa/Babb/BBAb在base0闭合；y9,m20使四路同到phase10。四法向量(0,1,2,2),(0,1,1,2),(1,0,1,2),(1,0,1,1)秩4而非2，全部81source的并恒65、缺16。

**仍未完成：** This finite result does not resolve generalgraph construction or completeLean.

**启发与重启依据：** 独立四法向量给仿射坐标双射，四平面补集为四坐标均非零的2^4点，故任何offset都不能让此四route包覆盖全fiber。不是没有四路，而是方向安排不形成共同pencil。只排此route包，不排其它pathunion/lifts。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

