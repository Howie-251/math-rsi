---
type: experiment
node_id: exp:ddp-wave3-hexagon-partial-fold-greedy
title: "H9逐点解除orbit常值：四序greedy与单调闭包"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/REPORT.md; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/best_loads.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/best_state.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/blocking_stats.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/monotone_closure_witness.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/root_monotone_closure.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# H9逐点解除orbit常值：四序greedy与单调闭包

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-profile-plus-monotone-exclusion

**目标与阶数：** (12,5)；L=42342；条件性n=42343（未据此计纪录）

**距目标的证据：** 四序新增0；root强迫闭包禁全部25074 merged，故该指定单调cone任何真S超集不可能。

**其他指标（保持原计数类型）：**
```json
{
  "partial_state_core_order": 41636,
  "split_fibers": 7959,
  "copies": 280,
  "merged_forbidden": 25074,
  "actual_D_measured": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/REPORT.md](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/REPORT.md)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/best_loads.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/best_loads.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/best_state.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/best_state.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/blocking_stats.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/blocking_stats.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/monotone_closure_witness.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/monotone_closure_witness.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/root_monotone_closure.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/root_monotone_closure.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/terminal.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原S固定为子集、H3 copies固定280；任意重染也包含在root后续闭包排除内

**正向保证：** 合法状态仍有几何D≤5保证；逐点degree精确维护与独立重算

**仍未完成：** 允许删除旧split或改变copies仍开放；未展开新大图。

**启发与重启依据：** 必须做结构交换，不再加批量split或重染。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

