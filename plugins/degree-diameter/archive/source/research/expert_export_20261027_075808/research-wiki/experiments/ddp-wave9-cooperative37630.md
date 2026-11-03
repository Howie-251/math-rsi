---
type: experiment
node_id: exp:ddp-wave9-cooperative37630
title: "37628→37630：互连双新点的联合半径覆盖"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave9/cooperative37630/REPORT.md; research/ddp/breadth_20261027_wave9/cooperative37630/terminal.json; research/ddp/breadth_20261027_wave9/cooperative37630/search_result.json; research/ddp/breadth_20261027_wave9/cooperative37630/best.edges; research/ddp/breadth_20261027_wave9/cooperative37630/best_parameters.json; research/ddp/breadth_20261027_wave9/cooperative37630/best.independent_check.json; research/ddp/breadth_20261027_wave9/cooperative37630/first_coordinate_calibration.json; research/ddp/breadth_20261027_wave9/cooperative37630/coverage_cache.json; research/ddp/breadth_20261027_wave9/cooperative37630/search.cpp; research/ddp/breadth_20261027_wave9/cooperative37630/run.py"
added: 2026-10-27T07:55:18Z
tags: ["ddp", "method-ledger"]
---

# 37628→37630：互连双新点的联合半径覆盖

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (11,5)；L=37628；candidate_graph_or_family n=37630；条件性n=37630（未据此计纪录）

**距目标的证据：** 新旧坏对=25，只验新根；two_new_root_eccentricities_only:6,6;source_old_D5_reused;whole_graph_all_pairs_BFS_not_performed；明确生成37630/205317/simple/max11图。两新根独立完整BFS均偏心率6，分别遗漏10、15个旧点，25个新旧坏对逐点MATCH，故候选D5失败；未全图all-pairs，不填全图ordinary坏对数。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "finalgraph",
  "graph_generated": true,
  "graph_edges": 205317,
  "source_n": 37628,
  "source_edges": 205296,
  "source_old_D5_fact_reused": true,
  "source_all_root_BFS_rerun": false,
  "eligible_vertices": 2504,
  "shareable_vertices": 315,
  "effective_spoke_capacity": 2819,
  "new_vertices": [
    37628,
    37629
  ],
  "new_degrees": [
    11,
    11
  ],
  "A": [
    22207,
    16383,
    30245,
    34099,
    475,
    3760,
    27391,
    15017,
    35172,
    7935
  ],
  "B": [
    13143,
    19858,
    26357,
    843,
    4640,
    33358,
    36740,
    33676,
    31376,
    1754
  ],
  "shared_pins": [],
  "newroot_eccentricities": [
    6,
    6
  ],
  "new_old_bad_target_D": 5,
  "new_old_bad_pairs": 25,
  "newroot_missing_counts": {
    "37628": 10,
    "37629": 15
  },
  "newroot_missing_vertices": {
    "37628": [
      7554,
      9638,
      13575,
      15696,
      19789,
      30950,
      31354,
      31937,
      32781,
      36098
    ],
    "37629": [
      3517,
      7388,
      7566,
      10888,
      11018,
      22459,
      31423,
      31620,
      31700,
      33045,
      33334,
      34481,
      34503,
      35156,
      35828
    ]
  },
  "newroot_missing_distance": 6,
  "newroot_missing_sets_independently_match": true,
  "whole_graph_all_pairs_BFS_performed": false,
  "whole_graph_ordinary_bad_pairs_measured": false,
  "certified_diameter_lower_bound": 6,
  "starts": 2,
  "initial_joint_missing": [
    25,
    351
  ],
  "final_joint_missing": [
    25,
    340
  ],
  "complete_coordinate_sweeps": [
    1,
    2
  ],
  "second_start_sweep_scores": [
    351,
    341,
    340
  ],
  "best_stage": "start0 initialization_complete",
  "removed_old_single_pin": 3814,
  "greedy_candidate_scores": 99818,
  "coordinate_candidate_scores": 149320,
  "first_formal_coordinate_calibration": "MATCH:all37628x2 bits;retained old22207,no strict replacement;formal proposal reused",
  "closed_R3_R4_preparation_roots": 2504,
  "coverage_cache_bytes_each": 11778816,
  "production_total_CPU_seconds": 3.113637224,
  "root_check_CPU_seconds": 0.647212327,
  "CPU_budget_seconds": 30,
  "workers": 1,
  "old_single_actual_pin_budget": 11,
  "old_eight_meant_fixed_starts_not_pins": true
}
```





**原始证据：** [research/ddp/breadth_20261027_wave9/cooperative37630/REPORT.md](../../research/ddp/breadth_20261027_wave9/cooperative37630/REPORT.md)；[research/ddp/breadth_20261027_wave9/cooperative37630/terminal.json](../../research/ddp/breadth_20261027_wave9/cooperative37630/terminal.json)；[research/ddp/breadth_20261027_wave9/cooperative37630/search_result.json](../../research/ddp/breadth_20261027_wave9/cooperative37630/search_result.json)；[research/ddp/breadth_20261027_wave9/cooperative37630/best.edges](../../research/ddp/breadth_20261027_wave9/cooperative37630/best.edges)；[research/ddp/breadth_20261027_wave9/cooperative37630/best_parameters.json](../../research/ddp/breadth_20261027_wave9/cooperative37630/best_parameters.json)；[research/ddp/breadth_20261027_wave9/cooperative37630/best.independent_check.json](../../research/ddp/breadth_20261027_wave9/cooperative37630/best.independent_check.json)；[research/ddp/breadth_20261027_wave9/cooperative37630/first_coordinate_calibration.json](../../research/ddp/breadth_20261027_wave9/cooperative37630/first_coordinate_calibration.json)；[research/ddp/breadth_20261027_wave9/cooperative37630/coverage_cache.json](../../research/ddp/breadth_20261027_wave9/cooperative37630/coverage_cache.json)；[research/ddp/breadth_20261027_wave9/cooperative37630/search.cpp](../../research/ddp/breadth_20261027_wave9/cooperative37630/search.cpp)；[research/ddp/breadth_20261027_wave9/cooperative37630/run.py](../../research/ddp/breadth_20261027_wave9/cooperative37630/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定37628源保留全部旧边，添加互连a-b，各≤10旧pins；共享仅原deficit≥2。两个指定确定性初态，每start最多两轮完整20位置坐标扫描；一完整轮无严格改善即停。

**正向保证：** 所有205296条源边保留，因此旧旧距离不增加；原图D5沿用作者/Comellas来源事实，未重复全旧源BFS。；新增根覆盖条件精确为R4(A)∪R3(B)=V且R4(B)∪R3(A)=V。；显式图简单连通、最大度11，新点均degree11，新增21边恰为a-b和20条指定spokes。

**仍未完成：** 最佳A仍有10个、B仍有15个旧点距离6；两固定profile失败不排除一般双点互助模板、协同多pin替换或其他初态。

**启发与重启依据：** 复用旧高覆盖A10再贪心补B10在本批优于从空平衡联合贪心；最佳对合法单pin严格替换已停滞。此profile已收束，不追加坐标轮/MILP/node数/source；后续需新的覆盖结构依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

