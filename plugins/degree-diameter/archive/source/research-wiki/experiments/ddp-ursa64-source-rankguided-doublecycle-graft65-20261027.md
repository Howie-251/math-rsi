---
type: experiment
node_id: exp:ddp-ursa64-source-rankguided-doublecycle-graft65-20261027
title: "(16,4)URSA源abAB引导65-controller插点：新self满秩但12coarse点对失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/REPORT.md; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/PREDICTION.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/BINDING.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/CONTROLLER65.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/controller65.edges; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/COARSE_R4.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/RESULT.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/terminal.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/run.py; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/INTERFACE.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/WORD_IMAGES.json"
added: 2026-10-27T22:30:29Z
tags: ["ddp", "method-ledger"]
---

# (16,4)URSA源abAB引导65-controller插点：新self满秩但12coarse点对失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (16,4)；L=16384；条件性n=16640（未据此计纪录）

**距目标的证据：** No16640graph generated. Only actual65controller allroots radius4;controllerD≥5, exactcontrollerD unmeasured.；PredictionREFUTED. w64abAB64 isclosed/cachednoise rank4, yet controller24ordered/12unordered>4 (20orderedoldold+4newold); first0→11, w misses19/38. Actual16640n/D/badnull, 0largegraph/sourceBFS.

**其他指标（保持原计数类型）：**
```json
{
  "actual_controller_n": 65,
  "actual_controller_m": 130,
  "actual_controller_degree": 4,
  "controller_simple": true,
  "controller_inverse_types": [
    3,
    2,
    1,
    0
  ],
  "source_a_cycle_lengths": [
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8
  ],
  "source_b_cycle_lengths": [
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4
  ],
  "u": 0,
  "v": 16,
  "c": 48,
  "t": 46,
  "w": 64,
  "selected_word_types": [
    0,
    1,
    3,
    2
  ],
  "closed_word_trace": [
    64,
    16,
    57,
    46,
    64
  ],
  "cached_noise_rank": 4,
  "cached_noise_image_size": 256,
  "composite_linear_rank_different_metric": 2,
  "controller_R4_roots_checked": 65,
  "controller_bad_ordered_pairs": 24,
  "controller_bad_unordered_pairs": 12,
  "controller_oldold_bad_ordered": 20,
  "controller_newold_bad_ordered": 4,
  "neww_controller_missing": [
    19,
    38
  ],
  "controller_first_witness": [
    0,
    11
  ],
  "controller_exact_D": null,
  "controller_D_lower_bound": 5,
  "large_graphs_generated": 0,
  "source_BFS": 0,
  "rank4_certificate_stage_run": false,
  "actual_newfiber_R4_gate_run": false,
  "compile_CPU_seconds": 0,
  "worker_CPU_seconds": 0.007038141999999997,
  "hard_RLIMIT_CPU_seconds": 5,
  "baseline_date": "2026-10-27",
  "source_credit": "Official URSA16384 actualglobalGF4 interface inherited; sourceURL in originalSOURCE_FACTS."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/REPORT.md](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/REPORT.md)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/BINDING.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/BINDING.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/CONTROLLER65.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/CONTROLLER65.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/controller65.edges](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/controller65.edges)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/COARSE_R4.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/COARSE_R4.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/RESULT.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/RESULT.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/terminal.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/terminal.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/run.py](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/source_cycle_graft65/run.py)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/INTERFACE.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/INTERFACE.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/WORD_IMAGES.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/WORD_IMAGES.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ActualURSA64perms/charts inherited; one frozen abABrank4-guided lexu0 graft only. a0→16/b48→46 split throughw64, newinverseperms. Simple4reg65 controller all65R4 checked; coarsefailure stopsbeforechartcertificate/biggraph.

**仍未完成：** Other65controllers, source-aware insertion rules or general largerdegree16D4 graphs notexcluded.

**启发与重启依据：** Protecting one fullnoise selfloop islocal anddoesnotpreserve globalcontroller coverage aftercycleslengthen. Fixedskeleton coarseholes cannotbeoffset-repaired. Stopthisoneu/wordgraft, no automatic nextgraft oroldC19/974rerun.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

