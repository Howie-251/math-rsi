---
type: experiment
node_id: exp:ddp-d14-global-cover-mip-unknown-20261027
title: "(14,5)全局选边模型：一次incumbent失败，第二模型终止，UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/RESULT.json"
added: 2026-10-27T17:50:48Z
tags: ["ddp", "method-ledger"]
---

# (14,5)全局选边模型：一次incumbent失败，第二模型终止，UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** UNKNOWN-global-cover-MIP

**目标与阶数：** (14,5)；L=94186；条件性n=94187（未据此计纪录）

**距目标的证据：** 保留全部3685binary columns，Σx≤14；256真实target约束先得14pin incumbent，完整94186cache验缺6430，加973实际violatedcuts成1229约束。第二模型SIGKILL/137，未返回新incumbent。不是UNSAT或整族无解。

**其他指标（保持原计数类型）：**
```json
{
  "models_started": 2,
  "models_returned": 1,
  "integer_candidates_checked": 1,
  "first_candidate_missing": 6430,
  "added_original_constraints": 973,
  "final_active_constraints": 1229,
  "status": "UNKNOWN",
  "exitcode": 137,
  "solver_CPU_observed_lower_bound": 2.412668242,
  "whole_CPU_observed_lower_bound": 2.782928979,
  "solver_CPU_total": null,
  "whole_CPU_total": null,
  "budget_compliance": "NOT_ESTABLISHED",
  "strict_exclusion": false,
  "BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/global_cover_mip/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保留全部3685binary columns，Σx≤14；256真实target约束先得14pin incumbent，完整94186cache验缺6430，加973实际violatedcuts成1229约束。第二模型SIGKILL/137，未返回新incumbent。不是UNSAT或整族无解。

**仍未完成：** No general source-family maximality is claimed; final concrete Lean remains incomplete.

**启发与重启依据：** 全局协调与贪心不同，但此预算没有解决同时覆盖。停止此模型，不冷启。仅求解器time_limit不能保证进程CPU窗口；未来有具体理由重新实现时应把单次solver隔离在外部CPU guard下，不能伪报未回传累计CPU。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

