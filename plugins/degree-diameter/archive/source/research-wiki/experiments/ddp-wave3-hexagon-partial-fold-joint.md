---
type: experiment
node_id: exp:ddp-wave3-hexagon-partial-fold-joint
title: "H9四预定region联合S/c/copies MILP"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/REPORT.md; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/best_loads.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/best_state.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/current_state.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_candidate.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_result.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_stderr.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_stdout.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_candidate.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_result.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_stderr.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_stdout.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_candidate.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_result.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_stderr.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_stdout.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_candidate.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_result.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_stderr.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_stdout.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/regions.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/root_state_identity.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# H9四预定region联合S/c/copies MILP

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-local-optimization

**目标与阶数：** (12,5)；L=42342；条件性n=42343（未据此计纪录）

**距目标的证据：** 四区均Optimal gap0，gain0；best核心41636且state未变。

**其他指标（保持原计数类型）：**
```json
{
  "partial_state_core_order": 41636,
  "solver_statuses": [
    "Optimal",
    "Optimal",
    "Optimal",
    "Optimal"
  ],
  "objective_gain": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/REPORT.md](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/REPORT.md)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/best_loads.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/best_loads.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/best_state.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/best_state.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/current_state.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/current_state.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_candidate.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_candidate.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_result.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_result.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_stderr.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_stderr.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_stdout.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_0_stdout.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_candidate.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_candidate.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_result.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_result.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_stderr.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_stderr.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_stdout.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_1_stdout.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_candidate.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_candidate.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_result.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_result.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_stderr.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_stderr.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_stdout.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_2_stdout.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_candidate.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_candidate.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_result.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_result.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_stderr.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_stderr.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_stdout.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/region_3_stdout.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/regions.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/regions.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/root_state_identity.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/root_state_identity.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/terminal.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 四预定region、域外固定，freegeneric820/820/899/901；copy变量1/1/28/28

**正向保证：** 允许删除/加split、重染、改copies；边界外degree约束完整纳入；所有逐点degree通过

**仍未完成：** 仅局部子问题optimal，不排全局部分折叠；没有展开大图。

**启发与重启依据：** 不扩大旧区域；须新的全局结构步骤。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

