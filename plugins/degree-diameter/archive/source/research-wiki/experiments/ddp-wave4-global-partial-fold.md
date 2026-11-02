---
type: experiment
node_id: exp:ddp-wave4-global-partial-fold
title: "H9全局三态三起点固定单点退火"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave4/global_partial_fold/REPORT.md; research/ddp/breadth_20261027_wave4/global_partial_fold/batch_result.json; research/ddp/breadth_20261027_wave4/global_partial_fold/best_legal.states; research/ddp/breadth_20261027_wave4/global_partial_fold/best_legal_state.json; research/ddp/breadth_20261027_wave4/global_partial_fold/build_metrics.json; research/ddp/breadth_20261027_wave4/global_partial_fold/degree_check.json; research/ddp/breadth_20261027_wave4/global_partial_fold/execution_metrics.json; research/ddp/breadth_20261027_wave4/global_partial_fold/input.txt; research/ddp/breadth_20261027_wave4/global_partial_fold/preset.json; research/ddp/breadth_20261027_wave4/global_partial_fold/search_log.jsonl; research/ddp/breadth_20261027_wave4/global_partial_fold/start0_anneal_end.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start0_best_legal.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start0_final.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start1_anneal_end.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start1_best_legal.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start1_final.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start2_anneal_end.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start2_best_legal.states; research/ddp/breadth_20261027_wave4/global_partial_fold/start2_final.states; research/ddp/breadth_20261027_wave4/global_partial_fold/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# H9全局三态三起点固定单点退火

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-profile-partial-state

**目标与阶数：** (12,5)；L=42342；条件性n=42343（未据此计纪录）

**距目标的证据：** 最好合法核心38383/S4986；另两终态1068/1124实际点度13，不能当Δ12图。

**其他指标（保持原计数类型）：**
```json
{
  "partial_state_core_order": 38383,
  "best_legal_S": 4986,
  "fixed_copies": 0,
  "starts": 3,
  "search_CPU_seconds": 150.021963
}
```





**原始证据：** [research/ddp/breadth_20261027_wave4/global_partial_fold/REPORT.md](../../research/ddp/breadth_20261027_wave4/global_partial_fold/REPORT.md)；[research/ddp/breadth_20261027_wave4/global_partial_fold/batch_result.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/batch_result.json)；[research/ddp/breadth_20261027_wave4/global_partial_fold/best_legal.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/best_legal.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/best_legal_state.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/best_legal_state.json)；[research/ddp/breadth_20261027_wave4/global_partial_fold/build_metrics.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/build_metrics.json)；[research/ddp/breadth_20261027_wave4/global_partial_fold/degree_check.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/degree_check.json)；[research/ddp/breadth_20261027_wave4/global_partial_fold/execution_metrics.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/execution_metrics.json)；[research/ddp/breadth_20261027_wave4/global_partial_fold/input.txt](../../research/ddp/breadth_20261027_wave4/global_partial_fold/input.txt)；[research/ddp/breadth_20261027_wave4/global_partial_fold/preset.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/preset.json)；[research/ddp/breadth_20261027_wave4/global_partial_fold/search_log.jsonl](../../research/ddp/breadth_20261027_wave4/global_partial_fold/search_log.jsonl)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start0_anneal_end.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start0_anneal_end.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start0_best_legal.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start0_best_legal.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start0_final.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start0_final.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start1_anneal_end.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start1_anneal_end.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start1_best_legal.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start1_best_legal.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start1_final.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start1_final.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start2_anneal_end.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start2_anneal_end.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start2_best_legal.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start2_best_legal.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/start2_final.states](../../research/ddp/breadth_20261027_wave4/global_partial_fold/start2_final.states)；[research/ddp/breadth_20261027_wave4/global_partial_fold/terminal.json](../../research/ddp/breadth_20261027_wave4/global_partial_fold/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 全部33033generic自由三态，copies固定0；三starts各50CPU秒

**正向保证：** 允许先删后增，不再固定作者S；合法state的D≤5仍由原几何定理提供

**仍未完成：** 未越逐点degree能垒；未证明全局模型不行；没有展开大图。

**启发与重启依据：** 本单点惩罚profile停止，需结构变化非追加时限。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

