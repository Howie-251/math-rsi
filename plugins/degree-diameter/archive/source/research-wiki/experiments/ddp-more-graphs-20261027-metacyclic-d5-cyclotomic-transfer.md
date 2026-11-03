---
type: experiment
node_id: exp:ddp-more-graphs-20261027-metacyclic-d5-cyclotomic-transfer
title: "2810双轨道C5源的canonical cyclotomic迁移：p311四根完整端点检查失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/metacyclic_d5_transfer/REPORT.md; research/ddp/more_graphs_20261027/metacyclic_d5_transfer/RESULT.json; research/ddp/more_graphs_20261027/metacyclic_d5_transfer/SOURCE_AND_POLYNOMIALS.json; research/ddp/more_graphs_20261027/metacyclic_d5_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/metacyclic_d5_transfer/check.py"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# 2810双轨道C5源的canonical cyclotomic迁移：p311四根完整端点检查失败

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (7,5)；L=2810；条件性n=3110（未据此计纪录）；从属目标：[[7, 5]]

**距目标的证据：** No edgegraph generated or all-source BFS; exact reduced-word reachable endpoints only, two origins times10layers.；源并非C10 Cayley；自由形式每层最小949、固定低系数多项式最小899，容311。r=6/36/52/216各实际端点检查均失败，两root遗漏129/129、150/176、138/122、96/104。只有代表根端点缺项，不作普通无序坏对。

**其他指标（保持原计数类型）：**
```json
{
  "source_p": 281,
  "source_action_order": 5,
  "source_orbits": 2,
  "target_p": 311,
  "target_graph_order_hypothetical": 3110,
  "free_form_min_capacity": 949,
  "fixed_polynomial_min_capacity": 899,
  "representative_origin_sides": 2,
  "layers_per_origin": 10,
  "numeric_cases": 4,
  "CPU_seconds": 0.368844851,
  "new_graphs_generated": 0,
  "new_lower_bounds": 0,
  "old_source_BFS_repeated": false,
  "new_all_source_BFS": 0,
  "counts_are_not_ordinary_bad_pairs": true,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "id": "root6",
    "label": "p311,r6",
    "target": [
      7,
      5
    ],
    "target_Delta": 7,
    "target_D": 5,
    "savedL": 2810,
    "n": {
      "actual": null,
      "hypothetical": 3110
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "status": "EXACT_TWO_ORIGIN_TEN_LAYER_COVERAGE_FAILED",
    "parameters": {
      "b": 28,
      "s1": 192,
      "s2": 243,
      "s3": 175
    },
    "primitive_fifth_root": 6,
    "representative_root_missing_endpoints": [
      129,
      129
    ],
    "covered_counts_by_origin": [
      [
        295,
        298,
        297,
        297,
        298,
        299,
        299,
        299,
        299,
        300
      ],
      [
        299,
        300,
        299,
        299,
        299,
        295,
        297,
        298,
        298,
        297
      ]
    ],
    "first_missing_within5_witness": {
      "origin_side": 0,
      "target_side": 0,
      "target_phase": 0,
      "target_x": 14
    },
    "graph_generated": false,
    "scope": "This frozen canonical4polynomial lift, both origin sides,10 endpointlayers each, all reduced words oflength<=5; no ordinaryall-pairs BFS."
  },
  {
    "id": "root36",
    "label": "p311,r36",
    "target": [
      7,
      5
    ],
    "target_Delta": 7,
    "target_D": 5,
    "savedL": 2810,
    "n": {
      "actual": null,
      "hypothetical": 3110
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "status": "EXACT_TWO_ORIGIN_TEN_LAYER_COVERAGE_FAILED",
    "parameters": {
      "b": 236,
      "s1": 115,
      "s2": 241,
      "s3": 230
    },
    "primitive_fifth_root": 36,
    "representative_root_missing_endpoints": [
      150,
      176
    ],
    "covered_counts_by_origin": [
      [
        291,
        300,
        299,
        299,
        300,
        298,
        296,
        291,
        291,
        295
      ],
      [
        298,
        295,
        291,
        291,
        296,
        287,
        293,
        295,
        295,
        293
      ]
    ],
    "first_missing_within5_witness": {
      "origin_side": 0,
      "target_side": 0,
      "target_phase": 0,
      "target_x": 19
    },
    "graph_generated": false,
    "scope": "This frozen canonical4polynomial lift, both origin sides,10 endpointlayers each, all reduced words oflength<=5; no ordinaryall-pairs BFS."
  },
  {
    "id": "root52",
    "label": "p311,r52",
    "target": [
      7,
      5
    ],
    "target_Delta": 7,
    "target_D": 5,
    "savedL": 2810,
    "n": {
      "actual": null,
      "hypothetical": 3110
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "status": "EXACT_TWO_ORIGIN_TEN_LAYER_COVERAGE_FAILED",
    "parameters": {
      "b": 205,
      "s1": 192,
      "s2": 240,
      "s3": 80
    },
    "primitive_fifth_root": 52,
    "representative_root_missing_endpoints": [
      138,
      122
    ],
    "covered_counts_by_origin": [
      [
        297,
        303,
        290,
        290,
        303,
        297,
        295,
        300,
        302,
        295
      ],
      [
        297,
        295,
        302,
        300,
        295,
        293,
        304,
        299,
        299,
        304
      ]
    ],
    "first_missing_within5_witness": {
      "origin_side": 0,
      "target_side": 0,
      "target_phase": 0,
      "target_x": 31
    },
    "graph_generated": false,
    "scope": "This frozen canonical4polynomial lift, both origin sides,10 endpointlayers each, all reduced words oflength<=5; no ordinaryall-pairs BFS."
  },
  {
    "id": "root216",
    "label": "p311,r216",
    "target": [
      7,
      5
    ],
    "target_Delta": 7,
    "target_D": 5,
    "savedL": 2810,
    "n": {
      "actual": null,
      "hypothetical": 3110
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "status": "EXACT_TWO_ORIGIN_TEN_LAYER_COVERAGE_FAILED",
    "parameters": {
      "b": 151,
      "s1": 115,
      "s2": 202,
      "s3": 142
    },
    "primitive_fifth_root": 216,
    "representative_root_missing_endpoints": [
      96,
      104
    ],
    "covered_counts_by_origin": [
      [
        301,
        304,
        305,
        305,
        304,
        296,
        299,
        301,
        297,
        302
      ],
      [
        296,
        302,
        297,
        301,
        299,
        295,
        303,
        305,
        305,
        303
      ]
    ],
    "first_missing_within5_witness": {
      "origin_side": 0,
      "target_side": 0,
      "target_phase": 0,
      "target_x": 14
    },
    "graph_generated": false,
    "scope": "This frozen canonical4polynomial lift, both origin sides,10 endpointlayers each, all reduced words oflength<=5; no ordinaryall-pairs BFS."
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/metacyclic_d5_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/metacyclic_d5_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/metacyclic_d5_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/metacyclic_d5_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/metacyclic_d5_transfer/SOURCE_AND_POLYNOMIALS.json](../../research/ddp/more_graphs_20261027/metacyclic_d5_transfer/SOURCE_AND_POLYNOMIALS.json)；[research/ddp/more_graphs_20261027/metacyclic_d5_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/metacyclic_d5_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/metacyclic_d5_transfer/check.py](../../research/ddp/more_graphs_20261027/metacyclic_d5_transfer/check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed corrected source two-copyFp semidirectC5, internalphases1/2,crossphases0/2/3/1/0; canonicalgaugeA0/S4=1 and4 frozen minimumheight/L1/lex polynomials; exactlyp311 andall4primitivefifthroots.

**正向保证：** 保持合法C5 action、内部逆对与跨匹配结构；相位0跨电压0/1不同保证简单7regular。；左乘在每copy内传递，因此两个origin全覆盖可证明全图D≤5；此次四项均有明确缺项。

**仍未完成：** GeneralC5 two-orbitpattern and otherrepresentations/fields are open. Source低系数表达只在mod281拟合，不给模311全覆盖保证。

**启发与重启依据：** 形式数量够不代表求值覆盖；本批发生碰撞。固定四根已完成，不扩offset/prime队列；重开需新的源代数关系或实质全局覆盖依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

