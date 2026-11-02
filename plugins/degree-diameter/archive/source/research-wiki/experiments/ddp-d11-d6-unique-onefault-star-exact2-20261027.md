---
type: experiment
node_id: exp:ddp-d11-d6-unique-onefault-star-exact2-20261027
title: "(11,6)186033→186034唯一9pin+≤2guard：完整精确无解"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D6_current186033/REPORT.md; research/ddp/more_graphs_20261027/d11_D6_current186033/RESULT.json; research/ddp/more_graphs_20261027/d11_D6_current186033/PROBE_PREDICTION.json; research/ddp/more_graphs_20261027/d11_D6_current186033/MANDATORY_R5.json; research/ddp/more_graphs_20261027/d11_D6_current186033/EXACT_RESULT.json; research/ddp/more_graphs_20261027/d11_D6_current186033/TARGET_SUPPORTS.json; research/ddp/more_graphs_20261027/d11_D6_current186033/FREE_PIN_PROXY_ANALYSIS.json; research/ddp/more_graphs_20261027/d11_D6_current186033/exact_guard.cpp; research/ddp/more_graphs_20261027/d11_D6_current186033/run_exact.py"
added: 2026-10-27T19:05:32Z
tags: ["ddp", "method-ledger"]
---

# (11,6)186033→186034唯一9pin+≤2guard：完整精确无解

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (11,6)；L=186033；条件性n=186034（未据此计纪录）

**距目标的证据：** 覆盖预测REFUTED。所有固定扩张条件式恰D7（旧源D6给≤7、完整R5失败给≥7），但未导出代表完整边表，不把4201缺点或pairscope写成图坏对。

**其他指标（保持原计数类型）：**
```json
{
  "prototype": 19161,
  "prototype_degree": 10,
  "deleted_saturated_pin": 78477,
  "mandatory_count": 9,
  "guard_cap": 2,
  "mandatory_R5_covered": 181832,
  "mandatory_R5_missing": 4201,
  "mandatory_multisource_R5_traversals": 1,
  "reverse_closed_neighborhood_rounds": 5,
  "eligible_guards": 24676,
  "distinct_nonzero_masks": 24676,
  "single_guard_solutions": 0,
  "two_guard_solutions": 0,
  "unordered_guard_pair_scope": 304440150,
  "pair_first_masks_processed": 24676,
  "target_support_min": 8662,
  "target_support_max": 14747,
  "derived_fixed_family_D": 7,
  "source_allBFS": 0,
  "new_graphs": 0,
  "UNKNOWN": 0,
  "native_CPU_seconds": 0.907972,
  "compile_CPU_seconds": 1.1439020579999997,
  "tracked_run_exact_CPU_seconds": 2.0586063169999997,
  "budget_accounted_CPU_seconds": 2.4186063169999996,
  "budget_accounting_note": "Budget accounting includes0.36CPU reserve for the earlier measure compilation/native call; this reserve was not a separately measured compiler CPU value."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D6_current186033/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D6_current186033/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D6_current186033/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/RESULT.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/PROBE_PREDICTION.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/PROBE_PREDICTION.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/MANDATORY_R5.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/MANDATORY_R5.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/EXACT_RESULT.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/EXACT_RESULT.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/TARGET_SUPPORTS.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/TARGET_SUPPORTS.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/FREE_PIN_PROXY_ANALYSIS.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/FREE_PIN_PROXY_ANALYSIS.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/exact_guard.cpp](../../research/ddp/more_graphs_20261027/d11_D6_current186033/exact_guard.cpp)；[research/ddp/more_graphs_20261027/d11_D6_current186033/run_exact.py](../../research/ddp/more_graphs_20261027/d11_D6_current186033/run_exact.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一v19161删去满pin78477，固定9个free旧邻点；全部24676其它freeguards选≤2。mandatoryR5漏4201；24676个非零不同mask全无singlefull，所有24676first-mask交集处理完整排除304440150unorderedpairs。0图/UNKNOWN/未试；普通坏对总数未算。

**仍未完成：** Only the fixedsource/fixedstar rule is closed. Other mechanisms andgeneral186034 constructions remainopen.

**启发与重启依据：** directNproxy不存在：所有freeguard与被删满pin的邻域最多共享1点；完整R5又排除任意两guard同时补齐。停止此source唯一onefaultstar，不追加satN2/更多guards/坏点修补；重启需实质不同连接规则。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

