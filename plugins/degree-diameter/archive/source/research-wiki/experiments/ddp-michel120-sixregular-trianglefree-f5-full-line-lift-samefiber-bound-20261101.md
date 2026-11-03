---
type: experiment
node_id: exp:ddp-michel120-sixregular-trianglefree-f5-full-line-lift-samefiber-bound-20261101
title: "Michel120无三角：F5³同层最多25点，full-line lift首门停止"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/PRED.json; research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/PROOF.md; research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/RESULT.json; research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/TERMINAL.json"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# Michel120无三角：F5³同层最多25点，full-line lift首门停止

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (30,3)；L=不适用／见变体；controller n=120

**距目标的证据：** 实际D=3，目标D=3；固定Michel120控制器、每incidentedge五个仿射线邻点、F5³、无intrafiber边、真逆；不是所有6度D3controller或允许intrafiber模型。；已存Michel120字面controller：120点6regular／360边，triangle0、所有120点不在三角。任意trueinverse affineoffset的full5line/nointrafiber lift同层R3至多1+6*(5−1)=25<125，不能D3。0.001604957CPU，0quotient/fiber/BFS/solver/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "controller_n": 120,
  "triangle_count": 0,
  "samefiber_R3_upper": 25,
  "fiber_size": 125,
  "fiber_graphs": 0,
  "CPU": 0.001604957
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/PRED.json](../../research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/PRED.json)；[research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_c120_f5_conic6/TERMINAL.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定Michel120控制器、每incidentedge五个仿射线邻点、F5³、无intrafiber边、真逆；不是所有6度D3controller或允许intrafiber模型。

**仍未完成：** 其他source／内层连接开放；不声称一般30D3不可解。

**启发与重启依据：** 先检三角而非先找charts：缺三角不能由offset/矩阵补同层125覆盖。停止此source，不自动转119/111数字梯子；为Schreier b三角直觉提供必要条件。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

