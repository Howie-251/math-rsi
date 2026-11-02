---
type: experiment
node_id: exp:ddp-more-graphs-20261027-michel684-prime43-transfer
title: "Michel684七电压的p43迁移：全部形式容量通过，两个固定lift跨层预测失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/REPORT.md; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/SOURCE.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/CAPACITY.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/RESULT.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/terminal.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/check.py"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# Michel684七电压的p43迁移：全部形式容量通过，两个固定lift跨层预测失败

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (7,4)；L=684；条件性n=774（未据此计纪录）；从属目标：[[7, 4]]

**距目标的证据：** No graph edge table or ordinary BFS. Two root-orbit endpoint coverage for exactly two fixed polynomial lifts; missing counts are root-state deficits, not ordinary unordered bad pairs.；全部36槽自由形式容量最小61>43；两个固定lift均无满跨侧槽，预测REFUTED。r6两root漏116/122，r36漏87/83。0完整774命中，0新图。

**其他指标（保持原计数类型）：**
```json
{
  "capacity_roots": 2,
  "slots_per_root": 18,
  "minimum_freeform_capacity": 61,
  "canonical_lifts_evaluated": 2,
  "prediction_verdict": "REFUTED",
  "complete_cross_side_slots": 0,
  "full_hits": 0,
  "new_graphs": 0,
  "all_source_BFS": 0,
  "source_reverified": false,
  "capacity_CPU_seconds": 0.011896338,
  "canonical_lifts_CPU_seconds": 0.0023553470000000007,
  "total_process_CPU_seconds": 0.016325184,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "label": "canonical-r6-order3",
    "target": [
      7,
      4
    ],
    "savedL": 684,
    "n": {
      "actual": null,
      "hypothetical": 774
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "fixed_voltage_translations": [
      35,
      6,
      0,
      6,
      2,
      2,
      5
    ],
    "root_endpoint_missing_counts": [
      116,
      122
    ],
    "metric_scope": "Two identity-orbit roots; endpoint missing states, not whole-graph ordinary bad pairs. No graph edge table or BFS.",
    "complete_cross_side_slots": 0,
    "full_hit": false
  },
  {
    "label": "canonical-r36-order3",
    "target": [
      7,
      4
    ],
    "savedL": 684,
    "n": {
      "actual": null,
      "hypothetical": 774
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "fixed_voltage_translations": [
      5,
      36,
      0,
      36,
      2,
      2,
      35
    ],
    "root_endpoint_missing_counts": [
      87,
      83
    ],
    "metric_scope": "Two identity-orbit roots; endpoint missing states, not whole-graph ordinary bad pairs. No graph edge table or BFS.",
    "complete_cross_side_slots": 0,
    "full_hit": false
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/SOURCE.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/SOURCE.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/CAPACITY.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/CAPACITY.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/terminal.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/terminal.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/check.py](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** p43,C9 quotient, roots6/36 of order3; fixed Michel684 phases internal0=4/3,internal1=1/6,cross=2/6/3. All7 free-translation linear-form capacity checked; numerical tests only the single predeclared source-derived polynomial lift at the two roots.

**正向保证：** 精确恢复的七个源电压与乘法约定直接复用，没有旧source重验。；全部7变量自由形式容量支持43，但尚不保证同赋值联合覆盖。

**仍未完成：** The entire seven-free-translation fixed-phase pattern remains open. No four-variable normalized enumeration has been executed; no other roots, primes or phases tested.

**启发与重启依据：** 固定整数/低系数迁移未能保留跨层覆盖；不能把容量通过当命中，也不能把两个lift失败外推全部自由电压。仅在同一结构有具体联合路线依据及主线程新有限范围决定时重启；不按bad下降续seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

