---
type: experiment
node_id: exp:ddp-current9720-bphase54-centralc9-controller-synthesis-16d4-20261027
title: "Actual9720 chart: all54 a-phase1/b-variable C9 controller frames failR4 before fiber construction"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/REPORT.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/MODEL.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/probe.cpp; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/run.py; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/native.log; research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/terminal.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/input.txt"
added: 2026-10-27T22:30:28Z
tags: ["ddp", "method-ledger"]
---

# Actual9720 chart: all54 a-phase1/b-variable C9 controller frames failR4 before fiber construction

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (16,4)；L=16384；条件性n=17496（未据此计纪录）

**距目标的证据：** All54/54 controller frames fail identity-root R4, missing5..30 of216 controller states. Consequently all216 planned parity lifts fail D4 by path projection. 0 coarse passers,0 actual17496 graphs,0 fiber-root BFS,0 UNKNOWN/unattemptedframes,0 newlowerbounds.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 9720,
  "source_reported_D": 4,
  "source_degree": 14,
  "controller_n": 216,
  "coarse_frames_total": 54,
  "coarse_frames_checked": 54,
  "coarse_passers": 0,
  "controller_R4_missing_range": [
    5,
    30
  ],
  "controller_root_truncated_R4_BFS": 54,
  "planned_actual_lifts": 216,
  "planned_lifts_excluded_by_projection": 216,
  "actual_graphs_constructed": 0,
  "actual_fiber_root_BFS": 0,
  "source_all_roots_BFS_repeated": 0,
  "native_CPU_seconds": 0.000372,
  "compile_CPU_seconds": 1.0885299999999998,
  "total_parent_children_CPU_seconds": 1.0911919999999997,
  "prediction": "REFUTED",
  "ordinary_bad_pair_scope": "Not measured; reported counts are missing controller states at one root.",
  "UNKNOWN": 0,
  "untested_coarse_frames": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/MODEL.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/MODEL.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/probe.cpp](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/probe.cpp)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/run.py](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/run.py)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/native.log](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/native.log)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/terminal.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/bphase_route_synthesis/terminal.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/input.txt](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m9_degree16_transfer/input.txt)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual9720 SL2(3) generators and GF3^4 charts, centralC9, a-phase1, b-phase0..8. Two distinct projected plain inverse-pair classes chosen from1..4:54 frames, each representing4 global gamma-power parity lifts (216 total). Fullcontroller R4 only; no fiber graph generated.

**仍未完成：** No assertion about nonunit a phases, other central moduli, otherSL2 generators or generalN(16,4). Repeated projected pair classes and P9matching cases are not actual frames in this numeric batch; any exclusion of them belongs to separately saved paper analysis.

**启发与重启依据：** Changing b phase genuinely changes the distribution of wide routes, but every frozen frame still lacks controller endpoints. Fiber matrices, offsets or parity choices cannot repair a missing projected route within these fixed frames. Stop this54-frame family; any future work needs an explicitly different controller rule, not a continuation chosen by missing counts.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

