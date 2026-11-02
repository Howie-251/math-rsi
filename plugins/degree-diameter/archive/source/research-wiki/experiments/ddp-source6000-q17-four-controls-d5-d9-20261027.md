---
type: experiment
node_id: exp:ddp-source6000-q17-four-controls-d5-d9-20261027
title: "(5,9)6000源四F17显式嵌入：69360点四图均精确D10"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/REPORT.md; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/MODEL.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/terminal.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda2.RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda8.RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda9.RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda15.RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/run.py; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/construction.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/SOURCE_FACTS.json"
added: 2026-10-27T20:56:24Z
tags: ["ddp", "method-ledger"]
---

# (5,9)6000源四F17显式嵌入：69360点四图均精确D10

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,9)；L=60686；candidate_graph_or_family n=69360

**距目标的证据：** 实际D=10，目标D=9；All four actual simple connected 5regular controls; full BFS from both deck-orbit representatives per graph gives exact global diameter10.；4/4 actual69360/173400 simple connected5regular，全部exactD10，0D9hit/未试/UNKNOWN；预测REFUTED。代表根R9缺项分别914/986、173/173、531/507、202/195，不是全图无序坏对。

**其他指标（保持原计数类型）：**
```json
{
  "fixed_controls": 4,
  "actual_new_graphs": 4,
  "new_complete_orbit_root_BFS": 8,
  "deck_orbits": 2,
  "source_BFS": 0,
  "actual_source_graph_generated": 0,
  "positive_edge_exports": 0,
  "UNKNOWN": 0,
  "unattempted": 0,
  "normal_q": 17,
  "hypothesis_prediction": "REFUTED",
  "all_global_exact_D": 10,
  "alpha_order": 8,
  "beta_order": 3,
  "beta_eigenvalues_in_F17": 0,
  "positive_orders_Y_A_B_D": [
    8,
    30,
    8,
    30
  ],
  "compile_CPU_seconds": 0,
  "total_batch_CPU_seconds": 0.9784877750000001,
  "baseline_date": "2026-10-27",
  "baseline_provenance": "Parent supplied current (5,9)60686; this worker did not refresh the public table.",
  "source_credit": "Original public 6000-vertex two-base construction in f4t4nt/degree-diameter-graphs, graphs/deg5/dia7; local original README and construction retained."
}
```



**从属变体：**
```json
[
  {
    "lambda": 2,
    "n": {
      "actual": 69360,
      "hypothetical": null
    },
    "actual_D": 10,
    "actual_graph_Delta": 5,
    "m": 173400,
    "simple": true,
    "connected": true,
    "complete_representative_BFS": 2,
    "representative_roots": [
      0,
      34680
    ],
    "root_eccentricities": [
      10,
      10
    ],
    "root_R9_missing": [
      914,
      986
    ],
    "ordinary_bad_unordered_pairs": null,
    "CPU_seconds": 0.23618656700000001,
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda2.RESULT.json"
    ]
  },
  {
    "lambda": 8,
    "n": {
      "actual": 69360,
      "hypothetical": null
    },
    "actual_D": 10,
    "actual_graph_Delta": 5,
    "m": 173400,
    "simple": true,
    "connected": true,
    "complete_representative_BFS": 2,
    "representative_roots": [
      0,
      34680
    ],
    "root_eccentricities": [
      10,
      10
    ],
    "root_R9_missing": [
      173,
      173
    ],
    "ordinary_bad_unordered_pairs": null,
    "CPU_seconds": 0.23912313899999998,
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda8.RESULT.json"
    ]
  },
  {
    "lambda": 9,
    "n": {
      "actual": 69360,
      "hypothetical": null
    },
    "actual_D": 10,
    "actual_graph_Delta": 5,
    "m": 173400,
    "simple": true,
    "connected": true,
    "complete_representative_BFS": 2,
    "representative_roots": [
      0,
      34680
    ],
    "root_eccentricities": [
      10,
      10
    ],
    "root_R9_missing": [
      531,
      507
    ],
    "ordinary_bad_unordered_pairs": null,
    "CPU_seconds": 0.2540048650000001,
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda9.RESULT.json"
    ]
  },
  {
    "lambda": 15,
    "n": {
      "actual": 69360,
      "hypothetical": null
    },
    "actual_D": 10,
    "actual_graph_Delta": 5,
    "m": 173400,
    "simple": true,
    "connected": true,
    "complete_representative_BFS": 2,
    "representative_roots": [
      0,
      34680
    ],
    "root_eccentricities": [
      10,
      10
    ],
    "root_R9_missing": [
      202,
      195
    ],
    "ordinary_bad_unordered_pairs": null,
    "CPU_seconds": 0.23712621899999997,
    "report_paths": [
      "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda15.RESULT.json"
    ]
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/MODEL.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/MODEL.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/terminal.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/terminal.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda2.RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda2.RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda8.RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda8.RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda9.RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda9.RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda15.RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/lambda15.RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/run.py](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q17_D9_controls/run.py)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/construction.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/construction.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/SOURCE_FACTS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定原6000两底点/H24/z5/phase及VA=(0,1),VB=(1,-1),VD=(0,2)。F17 beta companion，alpha=lambda*K只取lambda2/8/9/15，4项全部实际生成完整邻接并以两个deck轨道根精确验全局直径。

**仍未完成：** Only these four explicit embeddings and fixed vectors are closed; arbitrary F17 normal voltages and general degree5 diameter9 graphs remain outside this scope.

**启发与重启依据：** 与特征3 F9相反，beta在F17不可约半单，且全部承重电压阶8/30/8/30保留，但完整D9覆盖仍失败。停止这四个固定控制，不按少漏点续向量/域/phase或修边；任何新族须新的具体结构理由与独立事前范围。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

