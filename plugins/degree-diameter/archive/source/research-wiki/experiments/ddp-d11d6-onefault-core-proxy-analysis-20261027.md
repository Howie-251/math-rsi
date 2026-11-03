---
type: experiment
node_id: exp:ddp-d11d6-onefault-core-proxy-analysis-20261027
title: "186033的core-proxy预测被实际邻域推翻：所有freeguard最大共享1点"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D6_current186033/FREE_PIN_PROXY_ANALYSIS.json; research/ddp/more_graphs_20261027/d11_D6_current186033/POSITIVE_OVERLAP_GUARDS.json; research/ddp/more_graphs_20261027/d11_D6_current186033/free_pin_proxy_analysis.py; research/ddp/more_graphs_20261027/d11_D6_current186033/PROBE_TRANSFER_NOTES.md; research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/REPORT.md; research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/RESULT.json; research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/PREDICTION.json; research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/TARGETED_NEIGHBORS.json; research/ddp/more_graphs_20261027/d11_D6_current186033/MANDATORY_R5.json"
added: 2026-10-27T19:05:32Z
tags: ["ddp", "method-ledger"]
---

# 186033的core-proxy预测被实际邻域推翻：所有freeguard最大共享1点

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (11,6)；L=186033；candidate_graph_or_family n=186033；条件性n=186034（未据此计纪录）

**距目标的证据：** 24660guards与N78477共享0，16人共享1，最大overlap1；无先前13D5那种10个共同core邻点代理。debruijn预测满pin有少于11个old-layer邻居被推翻：11个全在old182618，degree≤10的freeguard更不可能容纳其全部11邻集。最小普通N对称差18反而来自3个degree7且0共享的点，不能机械当好proxy。0新图，这个负结果不排metric R5互补guard。

**其他指标（保持原计数类型）：**
```json
{
  "own_analysis_status": "COMPLETE_PROXY_PREMISE_REFUTED_METRIC_RULE_SELECTED",
  "prototype": 19161,
  "deleted_saturated_pin": 78477,
  "deleted_pin_neighbors": [
    1274,
    9088,
    19161,
    24157,
    28380,
    36035,
    43458,
    51104,
    53063,
    63302,
    141164
  ],
  "all11_deleted_pin_neighbors_in_old182618": true,
  "verified_geometric_core_label_map": false,
  "eligible_guards_excluding_mandatory": 24676,
  "shared_neighbor_histogram": {
    "0": 24660,
    "1": 16
  },
  "max_shared_neighbors": 1,
  "ten_shared_neighbor_proxy_exists": false,
  "minimum_N_symmetric_difference": 18,
  "minimum_attaining_degree7_vertices": [
    182711,
    182724,
    182873
  ],
  "all_positive_overlap_guard_ids": [
    69536,
    77955,
    78476,
    78481,
    78482,
    83405,
    84767,
    87433,
    97501,
    100817,
    101908,
    106380,
    116049,
    121730,
    123074,
    128104
  ],
  "proxy_analysis_CPU_seconds": 0.040363706,
  "positive_list_CPU_seconds": 0.0010641219999999972,
  "raw_source_reparses": 0,
  "BFS": 0,
  "radius_balls_here": 0,
  "candidate_generation_here": 0,
  "inherited_mandatory_R5_missing_targets": 4201,
  "metric_unit": "fixed mandatorypinset uncoveredtargets, not fullgraphbadpairs",
  "guard_production_status": "Separate in-progress producer at row request; this own-analysis terminal does not adjudicate it"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D6_current186033/FREE_PIN_PROXY_ANALYSIS.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/FREE_PIN_PROXY_ANALYSIS.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/POSITIVE_OVERLAP_GUARDS.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/POSITIVE_OVERLAP_GUARDS.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/free_pin_proxy_analysis.py](../../research/ddp/more_graphs_20261027/d11_D6_current186033/free_pin_proxy_analysis.py)；[research/ddp/more_graphs_20261027/d11_D6_current186033/PROBE_TRANSFER_NOTES.md](../../research/ddp/more_graphs_20261027/d11_D6_current186033/PROBE_TRANSFER_NOTES.md)；[research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/RESULT.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/PREDICTION.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/PREDICTION.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/TARGETED_NEIGHBORS.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/core_mechanism/TARGETED_NEIGHBORS.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/MANDATORY_R5.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/MANDATORY_R5.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只读现成CSR/degree及继承debruijn core_mechanism报告，未重rawparse、未跑球/BFS或候选。删去的新邻集满pin78477的11个实际邻居全部在旧182618前缀；该前缀只标legacy来源，未绑定为H9几何core。对除mandatory9外24676freeguards完整逆邻索引＋零重合排序，得到全局N重合/差集事实。

**仍未完成：** Separate bounded guard production and general(11,6)construction remain open; these rows do not decide the producer terminal or completeLean.

**启发与重启依据：** 不要凭数字前缀称几何core，或把低阶N相似当长半径覆盖必要条件。此处应让独立producer用4201真实mandatoryholes上的完整R5 coverage masks决定0/1/2guard；16个共享1的点只可作有限优先序，失败不排余下guards。不要重开邻域proxy搜索或据此判全任务失败。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

