---
type: experiment
node_id: exp:ddp-sign-quarterturn108-all3066-4d4-20261028
title: "Gminus sign quarterturn108: complete3066-set controlled comparison has no D4 hit"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/REPORT.md; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/GROUP_PROOF.md; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/CANONICAL_CASES.json; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/RESULT.json; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/CASES.jsonl; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/ORBIT_COUNTS.json; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/GROUP_TABLE.json; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/search.py; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/run.py; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/checkpoint.json; research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/terminal.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.json"
added: 2026-10-28T01:49:22Z
tags: ["ddp", "method-ledger"]
---

# Gminus sign quarterturn108: complete3066-set controlled comparison has no D4 hit

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,4)；L=104；candidate_graph_or_family n=108

**距目标的证据：** 0 hit;3066 complete;0 untested. C4 labelled-path gate rejected1500;1566 passers yielded1134 actual disconnected closures and432 connected actual radius4 failures. Three canonical cases were extracted from the existing log without a new graph or BFS.

**其他指标（保持原计数类型）：**
```json
{
  "total_sets": 3066,
  "tested_sets": 3066,
  "untested_sets": 0,
  "hits": 0,
  "types": {
    "two_pairs": 1176,
    "one_pair_two_involutions": 1764,
    "four_involutions": 126
  },
  "stats": {
    "processed": 3066,
    "phase_raw_gate_rejects": 1500,
    "phase_gate_passes": 1566,
    "actual108_profiles": 1566,
    "actual108_disconnected": 1134,
    "actual108_connected": 432,
    "actual108_R4checks": 432,
    "actual108_R4fail": 432
  },
  "canonical_profiles": [
    {
      "k": 0,
      "ordinal": 237,
      "generator_ids": [
        10,
        20,
        27,
        81
      ],
      "status": "ACTUAL108_R4_FAIL",
      "R4_missing": 42,
      "phase_rawcounts": [
        35,
        38,
        50,
        38
      ]
    },
    {
      "k": 1,
      "ordinal": 555,
      "generator_ids": [
        27,
        37,
        81,
        93
      ],
      "status": "STRICT_C4_RAW_GATE_REJECT",
      "R4_missing": null,
      "phase_rawcounts": [
        65,
        20,
        56,
        20
      ]
    },
    {
      "k": 2,
      "ordinal": 573,
      "generator_ids": [
        27,
        64,
        73,
        81
      ],
      "status": "ACTUAL108_R4_FAIL",
      "R4_missing": 34,
      "phase_rawcounts": [
        39,
        38,
        46,
        38
      ]
    }
  ],
  "source_BFS": 0,
  "new_lower_bounds": 0,
  "worker_CPU_seconds": 0.164381,
  "driver_CPU_seconds": 0.0007637299999999972,
  "compile_CPU_seconds": 0,
  "workers": 1
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/REPORT.md](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/REPORT.md)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/GROUP_PROOF.md](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/GROUP_PROOF.md)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/CANONICAL_CASES.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/CANONICAL_CASES.json)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/CASES.jsonl](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/CASES.jsonl)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/ORBIT_COUNTS.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/ORBIT_COUNTS.json)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/GROUP_TABLE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/GROUP_TABLE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/search.py](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/search.py)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/run.py](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/run.py)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/checkpoint.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/checkpoint.json)；[research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/terminal.json](../../research/ddp/more_graphs_20261027/small_d4_D4_sign_quarterturn108_20261028/terminal.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly Gminus=F3^3 semidirect diag(J,-1) C4, all3066 inverse-closed four-element nonidentity connection sets. Same comparison family as Gplus, with separate execution counts. No other group, phase or seed.

**仍未完成：** Other groups of order108 and general graphs in the(4,4) cell are outside this computation. Negative global diameter and ordinary bad-pair counts remain null.

**启发与重启依据：** The sign change removes the C12 abelian quotient but does not give simultaneous complete108-point radius4 coverage. Both specified representations stop here. A later materially different question must cite this complete scope; existing quartic Cayley census knowledge is being checked by the parent, with no novelty claim here.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

