---
type: experiment
node_id: exp:ddp-source6000-q9-two-module-controls-d5-d8-20261027
title: "Two-base GF9 controls: both19440-vertex degree5 graphs have D9"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/REPORT.md; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/terminal.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/run.py"
added: 2026-10-27T20:53:05Z
tags: ["ddp", "method-ledger"]
---

# Two-base GF9 controls: both19440-vertex degree5 graphs have D9

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,8)；L=18810；candidate_graph_or_family n=19440

**距目标的证据：** 实际D=9，目标D=8；Both simple/connected5regular19440/48600, exact globalD9. Scalar4 representative R8 misses63/83; scalar8 misses71/77;2/2controls completed with0D8hit.

**其他指标（保持原计数类型）：**
```json
{
  "actual_new_graphs": 2,
  "inherited_graphs": 0,
  "new_complete_representative_BFS": 4,
  "deck_orbits": 2,
  "representative_root_ids": [
    0,
    9720
  ],
  "exact_global_D_per_control": [
    9,
    9
  ],
  "representative_R8_missing_per_control": [
    [
      63,
      83
    ],
    [
      71,
      77
    ]
  ],
  "source_D7_BFS_repeated": 0,
  "process_CPU_seconds": 0.131661777,
  "new_lower_bounds": 0,
  "prediction": "REFUTED",
  "UNKNOWN": 0,
  "untried": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/terminal.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/terminal.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/run.py](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_controls/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly two GF9 scalar embeddings4/8 of the source H24 module; all voltage phases/C5 coordinates fixed, B=(1,−1), D_normal=2A_normal. Two actual new graphs, two full deck-orbit representative BFS per graph.

**仍未完成：** Other field, action, voltage, phase and vector choices outside the stated finite family are not excluded. This is not a general degree/diameter upper bound.

**启发与重启依据：** Preserving normal-action order and projective source-vector ratios did not guarantee D8. The only related follow-up was the separately frozen free_B family, now also complete; no silent phase/field continuation.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

