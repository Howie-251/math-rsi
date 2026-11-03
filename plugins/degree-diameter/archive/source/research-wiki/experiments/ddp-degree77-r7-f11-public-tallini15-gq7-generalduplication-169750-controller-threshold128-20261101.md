---
type: experiment
node_id: exp:ddp-degree77-r7-f11-public-tallini15-gq7-generalduplication-169750-controller-threshold128-20261101
title: "77度公开门已更正181450：primary W(7)33，H132目标少5758，原169750仅历史"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101_scalar_check.py; research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png"
added: 2026-11-01T09:53:52Z
tags: ["ddp", "method-ledger"]
---

# 77度公开门已更正181450：primary W(7)33，H132目标少5758，原169750仅历史

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (77,3)；L=不适用／见变体

**距目标的证据：** 已发表机制的标量代入和可核推论；0controller/图/BFS/Lean。；此前Tallini15组合169750及Hmin128保留为检索历史。实际读Cimráková–Fack2007 p140 Table5：W(7)33点/#1，p131明确symplectic W(3,q)，非upper43或Q(4,7)partialovoid。当前160000+13*(33*50)=181450，条件175692少5758；1331H纯点数min137，7regular偶Hmin138，三baseevenm46/H138、四base3|m36/H144仅条件尺度，无新搜索授权。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "full_graphs_generated": 0,
  "BFS_runs": 0,
  "Lean_compilations": 0,
  "best_located_derived_guarantee": 181450,
  "source_n": 160000,
  "source_degree": 64,
  "public_partial_ovoid": 33,
  "spread_lines": 50,
  "centers": 1650,
  "replications": 13,
  "center_matching_edges": 528,
  "center_isolates": 594,
  "PolarStarIQ_legal_cases": 684,
  "PolarStarPaley_legal_cases": 417,
  "PolarStarIQmax": 137424,
  "PolarStarPaleymax": 129903,
  "minimumH": 137,
  "minimum_threebase_evenH": 138,
  "minimum_threebase_evenm": 46,
  "scalar_CPU_seconds": 0.020526023,
  "primary_query_batches": 1,
  "queries": 4,
  "unpublished_local_graph_used_as_public": false,
  "global_record_or_priority_certified": false,
  "historical_pre_primary33": {
    "best_located_derived_guarantee": 169750,
    "public_partial_ovoid": 15,
    "centers": 750,
    "minimumH": 128,
    "minimum_threebase_evenH": 132,
    "minimum_threebase_evenm": 44
  },
  "minimum7regular_evenH": 138,
  "minimum_fourbase_H": 144,
  "minimum_fourbase_m": 36,
  "current_H132_target_minus_public": -5758,
  "public33_source_report": "research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101_scalar_check.py](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101_scalar_check.py)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 已读primary33计算例存在性＋继承公开GQ7/spread/一般§7复制的直接推论；没有独立公开181450数值边表或全球维护表。旧15门不再当前；合法PolarStar窗口原值保留，无重算。

**正向保证：** 2007原始计算表明确给W(7)33点，作者报告为穷尽最大及1等价类；本门只需要实际计算下界，未重跑该计算。；一般Delorme复制含matching新新边，使用原公开160000源和50spread，不用本地160050/O22。；本次推论不产独立公开数值边表，也不认证全局纪录；H阈值不证明controller存在。

**仍未完成：** H132/175692竞争目标已明确被更大公开方法推论阻断，不再只写partialovoid未穷尽。未认证全局图最优/优先权；无新controller/图。

**启发与重启依据：** 针对明确25阈值的primary小q表找到33，实际停止m33作为新纪录目的的派发；转公开33对象的坐标复现及现有filled源连接接口小实验，复现不记新纪录。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

