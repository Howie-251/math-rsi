---
type: experiment
node_id: exp:ddp-d11-d4-free7-monotone-barrier-20261027
title: "(11,4)七空余点R3缺743core：全部保边增点类关闭"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D4_current3645/REPORT.md; research/ddp/more_graphs_20261027/d11_D4_current3645/RESULT.json; research/ddp/more_graphs_20261027/d11_D4_current3645/COVER_PREDICTION.json; research/ddp/more_graphs_20261027/d11_D4_current3645/COVER_RESULT.json"
added: 2026-10-27T18:21:15Z
tags: ["ddp", "method-ledger"]
---

# (11,4)七空余点R3缺743core：全部保边增点类关闭

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-port-obstruction

**目标与阶数：** (11,4)；L=3645；条件性n=3646（未据此计纪录）

**距目标的证据：** all7free的source R3覆盖2902/3645，遗漏743全属原3444core，layer201全覆盖；首witness6到全部7free距离4。故任意新点到6的≤4路最后一条新增edge落在originalfree port，余source路径必须≤3而实际均4，矛盾。

**其他指标（保持原计数类型）：**
```json
{
  "ports": 7,
  "R3_covered": 2902,
  "R3_missing": 743,
  "missing_layer201": 0,
  "witness": 6,
  "CPU_seconds": 0.01014,
  "newgraphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D4_current3645/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/RESULT.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/COVER_PREDICTION.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/COVER_PREDICTION.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/COVER_RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/COVER_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** all7free的source R3覆盖2902/3645，遗漏743全属原3444core，layer201全覆盖；首witness6到全部7free距离4。故任意新点到6的≤4路最后一条新增edge落在originalfree port，余source路径必须≤3而实际均4，矛盾。

**仍未完成：** No complete newgraph in this finite experiment; unrelatedrules and finalLean remain open.

**启发与重启依据：** 这排除保全部source旧边、max11下任意数量helpers，甚至新增old-old port边的扩张；不排删边吸收。实际障碍是新点缺旧core入口，不是七点子集选择或坏对微调。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

