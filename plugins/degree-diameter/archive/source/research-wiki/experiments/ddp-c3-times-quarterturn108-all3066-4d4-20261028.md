---
type: experiment
node_id: exp:ddp-c3-times-quarterturn108-all3066-4d4-20261028
title: "G+ C3timesquarterturn108: all3066 four-generator sets failD4"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/REPORT.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/GROUP_PROOF.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/RESULT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/CONTROL_RESULT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/CASES.jsonl; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ORBIT_COUNTS.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/GROUP_TABLE.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/search.py; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/run.py; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/checkpoint.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/terminal.json"
added: 2026-10-28T01:49:02Z
tags: ["ddp", "method-ledger"]
---

# G+ C3timesquarterturn108: all3066 four-generator sets failD4

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,4)；L=104；candidate_graph_or_family n=108

**距目标的证据：** 0hit/3066complete/0untested. Quotientrawgate rejects2580;486passers give54 disconnected and432connected actual108R4 failures. Controlledframe separatelyprofiled once with exactD8/hist.

**其他指标（保持原计数类型）：**
```json
{
  "family_sets": 3066,
  "types": {
    "two_pairs": 1176,
    "one_pair_two_involutions": 1764,
    "four_involutions": 126
  },
  "stats": {
    "processed": 3066,
    "control_full_BFS": 1,
    "actual108_profiles": 487,
    "actual108_connected_profiled": 433,
    "actual108_R4checks": 433,
    "quotient_gate_rejects": 2580,
    "quotient_R4_rejects": 1689,
    "quotient_raw_below9_rejects": 2580,
    "quotient_disconnected_implies_full_disconnected": 1545,
    "control_R4_fail": 1,
    "quotient_only_rejects_without108_profile": 2579,
    "quotient_gate_passes": 486,
    "actual108_disconnected_profiled": 54,
    "actual108_R4_fail": 432
  },
  "control_exact_D": 8,
  "control_histogram": [
    1,
    4,
    10,
    20,
    22,
    18,
    17,
    12,
    4
  ],
  "control_R4missing": 51,
  "source_BFS": 0,
  "worker_CPU_seconds": 0.21600100000000003,
  "driver_CPU_seconds": 0.0006930309999999967,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/REPORT.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/REPORT.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/GROUP_PROOF.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/GROUP_PROOF.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/CONTROL_RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/CONTROL_RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/CASES.jsonl](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/CASES.jsonl)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ORBIT_COUNTS.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ORBIT_COUNTS.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/GROUP_TABLE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/GROUP_TABLE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/search.py](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/search.py)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/run.py](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/run.py)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/checkpoint.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/checkpoint.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/terminal.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ExactlyG+=C3x(F3²semidirect_JC4),all3066 inverseclosed4element nonidentity connectionsets. No othergroup orphasegrid.

**仍未完成：** Otherorder108groups or generalN(4,4) areunexcluded. All negativeglobaldiameters exceptthecontrolledframe areunknown.

**启发与重启依据：** CentralC3 creates aC12quotient and label-route bottlenecks;centre-onlycoverage isinsufficient. This fixedgroup family isclosed. A sign-action change is a separateauthorized control,not a seed or missedpairoptimization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

