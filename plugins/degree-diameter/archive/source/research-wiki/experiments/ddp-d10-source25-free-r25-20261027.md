---
type: experiment
node_id: exp:ddp-d10-source25-free-r25-20261027
title: "C25/F101/r25固定作用的完整射影连接系数检验"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d10_dhar2485_transfer/REPORT.md; research/ddp/more_graphs_20261027/d10_dhar2485_transfer/free_translation_r25/RESULT.json; research/ddp/more_graphs_20261027/d10_dhar2485_transfer/free_translation_r25/PREDICTION.json"
added: 2026-10-27T15:27:57Z
tags: ["ddp", "method-ledger"]
---

# C25/F101/r25固定作用的完整射影连接系数检验

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-cayley-route-coverage-no-accepted-graph

**目标与阶数：** (10,4)；L=2485；条件性n=2525（未据此计纪录）

**距目标的证据：** 全部1040604项结束，未试0、UNKNOWN0、完整命中0；17711项修好薄phase10却在其它层失败。总编译/运行4.083CPU秒。无新图，无普通坏对或实际D数值。

**其他指标（保持原计数类型）：**
```json
{
  "status": "COMPLETE_NO_HIT",
  "complete_space": true,
  "total_projective_charts": 1040604,
  "evaluated_candidates": 1040604,
  "untested_candidates": 0,
  "cursor_next_ordinal": 1040605,
  "thin_phase": 10,
  "thin_phase_full": 17711,
  "full_hits": 0,
  "first_failed_phase_counts": [
    11735,
    5492,
    456,
    23,
    4,
    1,
    0,
    0,
    0,
    0,
    1022893,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  "first_failure_witness_by_phase": [
    {
      "ordinal": 1136,
      "chart": "E1",
      "coefficients_BCDE": [
        0,
        11,
        24,
        1
      ],
      "phase": 0,
      "endpoint_count": 99,
      "missing": [
        34,
        67
      ]
    },
    {
      "ordinal": 2895,
      "chart": "E1",
      "coefficients_BCDE": [
        0,
        28,
        66,
        1
      ],
      "phase": 1,
      "endpoint_count": 95,
      "missing": [
        13,
        21,
        55,
        80,
        82,
        99
      ]
    },
    {
      "ordinal": 10789,
      "chart": "E1",
      "coefficients_BCDE": [
        1,
        5,
        82,
        1
      ],
      "phase": 2,
      "endpoint_count": 93,
      "missing": [
        3,
        4,
        12,
        29,
        66,
        71,
        75,
        84
      ]
    },
    {
      "ordinal": 31047,
      "chart": "E1",
      "coefficients_BCDE": [
        3,
        4,
        39,
        1
      ],
      "phase": 3,
      "endpoint_count": 99,
      "missing": [
        2,
        18
      ]
    },
    {
      "ordinal": 72614,
      "chart": "E1",
      "coefficients_BCDE": [
        7,
        11,
        95,
        1
      ],
      "phase": 4,
      "endpoint_count": 97,
      "missing": [
        33,
        35,
        67,
        69
      ]
    },
    {
      "ordinal": 868877,
      "chart": "E1",
      "coefficients_BCDE": [
        85,
        17,
        74,
        1
      ],
      "phase": 5,
      "endpoint_count": 99,
      "missing": [
        47,
        80
      ]
    },
    null,
    null,
    null,
    null,
    {
      "ordinal": 1,
      "chart": "E1",
      "coefficients_BCDE": [
        0,
        0,
        0,
        1
      ],
      "phase": 10,
      "endpoint_count": 55,
      "missing": [
        2,
        5,
        7,
        8,
        10,
        11,
        14,
        15,
        22,
        28,
        29,
        34,
        35,
        36,
        39,
        40,
        41,
        42,
        46,
        47,
        48,
        50,
        51,
        52,
        53,
        54,
        55,
        57,
        60,
        67,
        68,
        73,
        75,
        76,
        77,
        80,
        82,
        83,
        84,
        89,
        90,
        91,
        93,
        94,
        99,
        100
      ]
    },
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
  ],
  "first_thin_phase_passer": {
    "ordinal": 1136,
    "chart": "E1",
    "coefficients_BCDE": [
      0,
      11,
      24,
      1
    ],
    "phase": 10,
    "endpoint_count": 101,
    "missing": []
  },
  "CPU_seconds": 2.817479,
  "preparation_CPU_seconds": 0.004095,
  "profile1000_scan_CPU_seconds": 0.00252,
  "profile_projected_native_CPU_seconds": 2.62641708,
  "native_budget_CPU_seconds": 57.987277577,
  "actual_graph_order": null,
  "actual_diameter": null,
  "old_source_BFS": 0,
  "prediction_thin_phase_supported": true,
  "full_graphs_generated": 0,
  "independent_new_graph_checks": 0,
  "total_compile_parent_child_CPU_seconds": 4.083046161,
  "source_baseline_order": 2485,
  "target_Delta": 10,
  "target_D": 4,
  "hypothetical_graph_order": 2525,
  "ordinary_bad_unordered_pairs": null,
  "continuation": "Stop this complete fixed-action/fixed-phase projective scope; no other action or phasepattern was searched."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d10_dhar2485_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d10_dhar2485_transfer/free_translation_r25/RESULT.json](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/free_translation_r25/RESULT.json)；[research/ddp/more_graphs_20261027/d10_dhar2485_transfer/free_translation_r25/PREDICTION.json](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/free_translation_r25/PREDICTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** FixedC25/F101/r25andphases1/3/6/7/9;A0bycommonconjugation,nonzeroB/C/D/Eup-to-common-scalar. Exactscope/result in rawJSON.

**仍未完成：** 未取得此参数的完整新纪录；其它作用、相位及一般图未由此排除。完整Lean实例仍0。

**启发与重启依据：** 按固定全范围终态重新评估；不自动扩其它作用/商/seed，也不把未知或有限未命中扩大为整个构造族不存在。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

