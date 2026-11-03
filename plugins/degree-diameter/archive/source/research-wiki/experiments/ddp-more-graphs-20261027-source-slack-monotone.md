---
type: experiment
node_id: exp:ddp-more-graphs-20261027-source-slack-monotone
title: "当前D3/D4源的保边扩点：满度筛与极性65类覆盖界"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d3d4_transfer/REPORT.md; research/ddp/more_graphs_20261027/d3d4_transfer/RESULT.json; research/ddp/more_graphs_20261027/d3d4_transfer/SOURCES.json; research/ddp/more_graphs_20261027/d3d4_transfer/screen.py"
added: 2026-10-27T11:38:49Z
tags: ["ddp", "method-ledger"]
---

# 当前D3/D4源的保边扩点：满度筛与极性65类覆盖界

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** 多目标：D4 source104,Delta4→[4, 4]／L=104；D4 source252,Delta5→[5, 4]／L=252；D4 source441,Delta6→[6, 4]／L=441；D4 source684,Delta7→[7, 4]／L=684；D4 source1100,Delta8→[8, 4]／L=1100；D4 source1768,Delta9→[9, 4]／L=1768；D4 source2485,Delta10→[10, 4]／L=2485；D4 source3444,Delta11→[11, 4]／L=3444；D4 source5832,Delta12→[12, 4]／L=5832；D3 Delorme source585,Delta9→[9, 3]／L=585；D3 Delorme source650,Delta10→[10, 3]／L=650；D3 Delorme source715,Delta11→[11, 3]／L=715（逐变体，不合成一个距离）

**距目标的证据：** No augmented target graph generated. Existing source degree histograms/structural regularity and forced-class R2 covering numbers only.；D4 fixedsources全满度；实际D3 source650全10regular。585和715的eligible-R2 cover最优恰65，分别超过9/11pins预算；715虽全部eligible球的union=715，仍不能用11球覆盖。小互助块585 t≤7、715 t≤5也由65spokes下界排除。

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bounds": 0,
  "solver_calls": 0,
  "greedy_starts": 0,
  "new_all_source_BFS_calls": 0,
  "new_length2_walk_checks": 195,
  "native_screen_CPU_seconds": 0.037165033,
  "D3_source650_degree_histogram": {
    "10": 650
  },
  "D3_source715_degree_histogram": {
    "9": 130,
    "10": 65,
    "11": 520
  },
  "D3_source715_union_all_eligible_R2": 715,
  "D3_source715_minimum_eligible_cover": 65,
  "additional_regular_D3_representatives": [
    {
      "Delta": 4,
      "D": 3,
      "source_n": 41,
      "source_m": 82,
      "eligible_pins": 0
    },
    {
      "Delta": 5,
      "D": 3,
      "source_n": 72,
      "source_m": 180,
      "eligible_pins": 0
    },
    {
      "Delta": 12,
      "D": 3,
      "source_n": 810,
      "source_m": 4860,
      "eligible_pins": 0
    },
    {
      "Delta": 6,
      "D": 3,
      "source_n": 120,
      "source_m": 360,
      "eligible_pins": 0
    },
    {
      "Delta": 7,
      "D": 3,
      "source_n": 170,
      "source_m": 595,
      "eligible_pins": 0
    },
    {
      "Delta": 8,
      "D": 3,
      "source_n": 253,
      "source_m": 1012,
      "eligible_pins": 0
    }
  ],
  "counts_are_source_or_cover_metrics_not_candidate_bad_pairs": true,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "id": "D4-d4-source104-no-slack",
    "label": "D4 source104,Delta4",
    "target": [
      4,
      4
    ],
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 105
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 104,
    "known_source_m": 208,
    "known_source_degree_histogram": {
      "4": 104
    },
    "degree_evidence_kind": "reused existing raw-source verification",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Nishant Bhakar,2026-08-27;104c official source",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d5-source252-no-slack",
    "label": "D4 source252,Delta5",
    "target": [
      5,
      4
    ],
    "target_Delta": 5,
    "target_D": 4,
    "savedL": 252,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 253
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 252,
    "known_source_m": 630,
    "known_source_degree_histogram": {
      "5": 252
    },
    "degree_evidence_kind": "actual edge-degree histogram; no newBFS",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Rishabh Rajiv,2026-09-24;A7 orbit graph",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d6-source441-no-slack",
    "label": "D4 source441,Delta6",
    "target": [
      6,
      4
    ],
    "target_Delta": 6,
    "target_D": 4,
    "savedL": 441,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 442
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 441,
    "known_source_m": 1323,
    "known_source_degree_histogram": {
      "6": 441
    },
    "degree_evidence_kind": "actual edge-degree histogram; no newBFS",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Rishabh Rajiv,2026-09-24;PSU(3,3) orbit graph",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d7-source684-no-slack",
    "label": "D4 source684,Delta7",
    "target": [
      7,
      4
    ],
    "target_Delta": 7,
    "target_D": 4,
    "savedL": 684,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 685
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 684,
    "known_source_m": 2394,
    "known_source_degree_histogram": {
      "7": 684
    },
    "degree_evidence_kind": "actual edge-degree histogram; no newBFS",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Michel de Messieres,2026-10-05;two-base voltage lift",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d8-source1100-no-slack",
    "label": "D4 source1100,Delta8",
    "target": [
      8,
      4
    ],
    "target_Delta": 8,
    "target_D": 4,
    "savedL": 1100,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 1101
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 1100,
    "known_source_m": 4400,
    "known_source_degree_histogram": {
      "8": 1100
    },
    "degree_evidence_kind": "actual edge-degree histogram; no newBFS",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Eyal Loz,2006;official1100 source",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d9-source1768-no-slack",
    "label": "D4 source1768,Delta9",
    "target": [
      9,
      4
    ],
    "target_Delta": 9,
    "target_D": 4,
    "savedL": 1768,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 1769
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 1768,
    "known_source_m": 7956,
    "known_source_degree_histogram": {
      "9": 1768
    },
    "degree_evidence_kind": "derived from official construction counts and maximum degree9",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Francesc Comellas,2026-10-21;modified1700 source",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": "m=1700*9/2-191+497=7956=1768*9/2; every degree<=9 implies every degree=9",
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d10-source2485-no-slack",
    "label": "D4 source2485,Delta10",
    "target": [
      10,
      4
    ],
    "target_Delta": 10,
    "target_D": 4,
    "savedL": 2485,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 2486
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 2485,
    "known_source_m": 12425,
    "known_source_degree_histogram": {
      "10": 2485
    },
    "degree_evidence_kind": "actual edge-degree histogram; no newBFS",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Dharunish Yugeswardeenoo,2026-08-17;semidirect Cayley graph",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d11-source3444-no-slack",
    "label": "D4 source3444,Delta11",
    "target": [
      11,
      4
    ],
    "target_Delta": 11,
    "target_D": 4,
    "savedL": 3444,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 3445
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 3444,
    "known_source_m": 18942,
    "known_source_degree_histogram": {
      "11": 3444
    },
    "degree_evidence_kind": "official description explicitly11-regular; not re-downloaded",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Dharunish Yugeswardeenoo,2026-10-07;doubledW(9) incidence with spread twins",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D4-d12-source5832-no-slack",
    "label": "D4 source5832,Delta12",
    "target": [
      12,
      4
    ],
    "target_Delta": 12,
    "target_D": 4,
    "savedL": 5832,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 5833
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 5832,
    "known_source_m": 34992,
    "known_source_degree_histogram": {
      "12": 5832
    },
    "degree_evidence_kind": "official description explicitly12-regular route-chart lift; not re-downloaded",
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "eligible_pins": 0,
    "scope": "Keep all old edges at the same degree cap; every old vertex saturated, so no connected augmentation by any positive number of new vertices.",
    "source_credit": "Ryosuke Mizuno,2026-09-25;route-chart lift",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html",
    "derivation": null,
    "actual_D_scope": "No augmented target graph generated; these are known-source degree facts."
  },
  {
    "id": "D3-d9-source585-monotone",
    "label": "D3 Delorme source585,Delta9",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "target_D": 3,
    "savedL": 585,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 586
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 585,
    "known_source_m": 2600,
    "known_source_degree_histogram": {
      "8": 65,
      "9": 520
    },
    "eligible_pins": 65,
    "status": "CLOSED_ALL_BUDGETED_ELIGIBLE_R2_COVERS",
    "source_credit": "C.Delorme polarity/duplication construction; adjacency supplied byV.Pelekhaty; maintained byF.Comellas.",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n585d9k3.txt",
    "actual_D_scope": "No augmented target graph generated; this is a known-source degree/necessary-cover screen.",
    "eligible_target_classes": 65,
    "targets_per_class": 1,
    "classes_hit_by_each_eligible_R2": 1,
    "minimum_budgeted_eligible_R2_cover": 65,
    "new_vertex_pin_budget": 9,
    "small_cooperative_block_closed_through_size": 7,
    "scope": "All eligible pins, not only samples. Every class needs a spoke and each eligibleR2 hits one class; single-pinset cover number65>9. Any added block t<=7 also has at mostDelta*t<65spokes. Larger cooperative blocks not excluded."
  },
  {
    "id": "D3-d10-source650-monotone",
    "label": "D3 Delorme source650,Delta10",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "target_D": 3,
    "savedL": 650,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 651
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 650,
    "known_source_m": 3250,
    "known_source_degree_histogram": {
      "10": 650
    },
    "eligible_pins": 0,
    "status": "CLOSED_FIXED_SOURCE_NO_DEGREE_SLACK",
    "source_credit": "C.Delorme polarity/duplication construction; adjacency supplied byV.Pelekhaty; maintained byF.Comellas.",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n650d10k3.txt",
    "actual_D_scope": "No augmented target graph generated; this is a known-source degree/necessary-cover screen.",
    "scope": "The actual official650 source is10-regular, not the bare replication with unfilled degree slots; all connected monotone extensions are impossible at cap10."
  },
  {
    "id": "D3-d11-source715-monotone",
    "label": "D3 Delorme source715,Delta11",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "target_D": 3,
    "savedL": 715,
    "baseline_as_of": "2026-10-27",
    "n": {
      "actual": null,
      "hypothetical": 716
    },
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "known_source_n": 715,
    "known_source_m": 3770,
    "known_source_degree_histogram": {
      "9": 130,
      "10": 65,
      "11": 520
    },
    "eligible_pins": 195,
    "status": "CLOSED_ALL_BUDGETED_ELIGIBLE_R2_COVERS",
    "source_credit": "C.Delorme polarity/duplication construction; adjacency supplied byV.Pelekhaty; maintained byF.Comellas.",
    "source_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n715d11k3.txt",
    "actual_D_scope": "No augmented target graph generated; this is a known-source degree/necessary-cover screen.",
    "eligible_target_classes": 65,
    "targets_per_class": 3,
    "classes_hit_by_each_eligible_R2": 1,
    "minimum_budgeted_eligible_R2_cover": 65,
    "new_vertex_pin_budget": 11,
    "small_cooperative_block_closed_through_size": 5,
    "scope": "All eligible pins, not only samples. Every class needs a spoke and each eligibleR2 hits one class; single-pinset cover number65>11. Any added block t<=5 also has at mostDelta*t<65spokes. Larger cooperative blocks not excluded."
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d3d4_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d3d4_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d3d4_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d3d4_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d3d4_transfer/SOURCES.json](../../research/ddp/more_graphs_20261027/d3d4_transfer/SOURCES.json)；[research/ddp/more_graphs_20261027/d3d4_transfer/screen.py](../../research/ddp/more_graphs_20261027/d3d4_transfer/screen.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Current D4 degree4..12 records: no old degree slack. D3 q8 actual585/650/715 sources: all eligible pins, same cap, all old edges retained. Additional canonical regularD3 source histograms retained in evidence.

**正向保证：** 保留所有旧边可保持oldold近端覆盖，但新增点仍须完整R_(D-1)覆盖。；65个特殊类给出每类至少一pin的精确覆盖下界；不是把union覆盖误作有限budget覆盖。

**仍未完成：** Not a nonexistence theorem for arbitrary586/651/716 or D4 baseline+1 graphs; larger cooperative585/715 blocks, deleted/replaced old edges and genuinely new sources remain outside this scope.

**启发与重启依据：** 满度源立即止；有余量先看可选pins在全部必要目标类上的覆盖下界。只在获得有实际度余量的新非同构source或改变连接机制/全局路由规则时重开，不换seed或重编号重复闭族。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- STALE_715_PHASE69_TERMINAL_DELTA_20261101 -->
## 后续更强精确范围（2026-11-01，原结论保留）

原715单点及t≤5排除仍有效，以上为历史实验原文；不是把旧结论改为错误。后续实际715的65类core-R2新支持和owner-moment论证已排任意finite helperH，前提是旧诱导图固定；paper corollary允许各P3内部补leaf-leaf变K3，仍不允许跨原class新边或删改旧边。见[更强本scope节点](ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101.md)。没有sourceD3重验、solver/Lean或新图计数。
