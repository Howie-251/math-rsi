---
type: experiment
node_id: exp:ddp-f5-clone-fixed16-old-router-engineering-pilot-20261101
title: "F5克隆三图固定16旧路由器静态pilot：负载分流与端点槽分别记账"
idea_id: "idea:ddp-network-expansion-value-pilot"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: "Declared unit-capacity static fluid model; no hardware measurements"
duration: "CPU0.50115918;48 routing-source BFS in already completed pilot"
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/ASSUMPTIONS.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/PREDICTION.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/REPORT.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/run_once.py"
added: 2026-11-01T04:07:00Z
tags: ["ddp", "engineering-diagnostic", "fixed-workload", "not-throughput-measurement"]
---

# F5克隆三图固定16旧路由器静态pilot：负载分流与端点槽分别记账

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-network-expansion-value-pilot`

## Metrics
非数学有限工程pilot：固定16个旧路由器17+233i，240个不同有序需求各1/15，总需求16。三图仅各16源路由BFS，共48次，CPU0.50115918；无旧3750 D3复验。全最短路径等权流体分流，有向容量1，新增路由器不注入。

|图|n/m|r24剩余端点槽|峰值有向负载|平均跳数|任意新边流量比例|新边hop-volume比例|
|---|---|---:|---:|---:|---:|---:|
|source|3750/37500|15000|0.266667|2.941667|0|0|
|clone150|3900/40500|12600|0.266667|2.941667|3.40278%|2.31350%|
|clone375|4125/45000|9000|0.213333|2.941667|11.19643%|7.61230%|

r32/48仅计数slot；成本只按设备/边数量。RMS/均方以全部2m有向边含零负载平均，分母随图改变。没有故障、布局、功耗、队列或吞吐实测。本工程节点不进入数学method ledger，不增加合法图或Lean数。

## Reasoning
在这一固定流量/等完整最短路径规则下，3900峰值不变、4125峰值降低20%，但r24端点槽分别减少2400/6000。完整邻域clone可折叠回原型，故全部旧旧最短距离严格不变，而路径数量可增使分流负载变化。旧端点只占全图少量，不能外推全网络/全部新端点同时注入。该结果是有限静态模型诊断，非工业收益或实测吞吐。批次已停止，不追加新指标或平台。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

