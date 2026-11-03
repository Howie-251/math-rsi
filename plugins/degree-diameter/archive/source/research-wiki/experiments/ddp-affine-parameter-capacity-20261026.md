---
type: experiment
node_id: exp:ddp-affine-parameter-capacity-20261026
title: "六个固定仿射参数的必要容量比较"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, at most one worker per bounded batch"
duration: "0.662577227 CPU s"
provenance: "research/ddp/m2_coset_tower/axis_parameter_capacity/REPORT.md"
added: 2026-10-27T08:25:48Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 六个固定仿射参数的必要容量比较

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** 多目标：agl7_d4→[4, 3]／L=41；agl7_times_c2_d5→[5, 3]／L=72；agl13_d6→[6, 3]／L=120；agl11_times_c2_d7→[7, 3]／L=170；f11_c20_nonfaithful_d7→[7, 3]／L=170；agl19_d8→[8, 3]／L=253（逐变体，不合成一个距离）

**距目标的证据：** 2381fullpatterns,226plainpass;symbolicsurvivors0/0/0/4/0/1. No actualgraphs.



**既有原文指标：** 2381fullpatterns,226plainpass;symbolicsurvivors0/0/0/4/0/1. No actualgraphs.

**从属变体：**
```json
[
  {
    "label": "agl7_d4",
    "target": [
      4,
      3
    ],
    "savedL": 41,
    "n": 42,
    "n_role": "prospective group order; no graph searched in this note",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/axis_parameter_capacity/CAPACITY_RESULTS.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "agl7_times_c2_d5",
    "target": [
      5,
      3
    ],
    "savedL": 72,
    "n": 84,
    "n_role": "prospective group order; no graph searched in this note",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/axis_parameter_capacity/CAPACITY_RESULTS.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "agl13_d6",
    "target": [
      6,
      3
    ],
    "savedL": 120,
    "n": 156,
    "n_role": "prospective group order; no graph searched in this note",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/axis_parameter_capacity/CAPACITY_RESULTS.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "agl11_times_c2_d7",
    "target": [
      7,
      3
    ],
    "savedL": 170,
    "n": 220,
    "n_role": "prospective group order; no graph searched in this note",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/axis_parameter_capacity/CAPACITY_RESULTS.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "f11_c20_nonfaithful_d7",
    "target": [
      7,
      3
    ],
    "savedL": 170,
    "n": 220,
    "n_role": "prospective group order; no graph searched in this note",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/axis_parameter_capacity/CAPACITY_RESULTS.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "agl19_d8",
    "target": [
      8,
      3
    ],
    "savedL": 253,
    "n": 342,
    "n_role": "prospective group order; no graph searched in this note",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/axis_parameter_capacity/CAPACITY_RESULTS.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  }
]
```

**原始证据：** [research/ddp/m2_coset_tower/axis_parameter_capacity/REPORT.md](../../research/ddp/m2_coset_tower/axis_parameter_capacity/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Four fixedgroups fully excluded; directproduct220notsearched,342actualrunseparate. PureCayley lowdegree literature used only forselection.

**启发与重启依据：** Four fixedgroups fully excluded; directproduct220notsearched,342actualrunseparate. PureCayley lowdegree literature used only forselection.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

