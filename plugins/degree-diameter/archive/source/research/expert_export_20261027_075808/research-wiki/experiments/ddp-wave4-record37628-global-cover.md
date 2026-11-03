---
type: experiment
node_id: exp:ddp-wave4-record37628-global-cover
title: "37628单点全部2504候选的全局覆盖MILP"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave4/record37628_global_cover/REPORT.md; research/ddp/breadth_20261027_wave4/record37628_global_cover/matrix_metadata.json; research/ddp/breadth_20261027_wave4/record37628_global_cover/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 37628单点全部2504候选的全局覆盖MILP

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** solver-UNKNOWN

**目标与阶数：** (11,5)；L=37628；条件性n=37629（未据此计纪录）

**距目标的证据：** CPU硬限终止，solver未返回，无incumbent/不可行证明，UNKNOWN。

**其他指标（保持原计数类型）：**
```json
{
  "variables": 2504,
  "coverage_rows": 37628,
  "cardinality_cap": 11,
  "solver_status": "UNKNOWN",
  "incumbent_returned": false,
  "solver_returned": false,
  "total_CPU_seconds": 59.066855350999994
}
```





**原始证据：** [research/ddp/breadth_20261027_wave4/record37628_global_cover/REPORT.md](../../research/ddp/breadth_20261027_wave4/record37628_global_cover/REPORT.md)；[research/ddp/breadth_20261027_wave4/record37628_global_cover/matrix_metadata.json](../../research/ddp/breadth_20261027_wave4/record37628_global_cover/matrix_metadata.json)；[research/ddp/breadth_20261027_wave4/record37628_global_cover/terminal.json](../../research/ddp/breadth_20261027_wave4/record37628_global_cover/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 全部37628覆盖行、2504二元变量、sum≤11；单solverhandle

**正向保证：** 模型含全部候选，不是只8候选；20260765非零覆盖关系已构建

**仍未完成：** 未找到覆盖不等于UNSAT；无新图/D。

**启发与重启依据：** 该solverhandle已停不重启；如有新结构证据再独立决定。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

