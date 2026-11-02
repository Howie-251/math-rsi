---
type: experiment
node_id: exp:ddp-affine4-shared-slope-20261027
title: "两个四轨道底图共同仿射斜率障碍"
idea_id: "idea:ddp-bicayley-d3"
verdict: no
confidence: high
date: "2026-10-27"
hardware: "localCPU up to4workers,within8total"
duration: "1.585976602CPU"
provenance: "research/ddp/m2_coset_tower/affine_four_orbit_matching_cover/AFFINE_MATCHING_COVER.md"
added: 2026-10-27T08:25:48Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 两个四轨道底图共同仿射斜率障碍

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-bicayley-d3`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** 多目标：shared-slope base→[6, 3]／L=120；shared-slope base→[7, 3]／L=170（逐变体，不合成一个距离）

**距目标的证据：** 27000+74088triples finitecheck;124survivortriples symboliccomposition;0translations0graphs0BFS.



**既有原文指标：** 27000+74088triples finitecheck;124survivortriples symboliccomposition;0translations0graphs0BFS.

**从属变体：**
```json
[
  {
    "label": "shared-slope base",
    "target": [
      6,
      3
    ],
    "n": 124,
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/affine_four_orbit_matching_cover/terminal.json conclusion D<=3",
    "savedL": 120,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "shared-slope base",
    "target": [
      7,
      3
    ],
    "n": 172,
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/affine_four_orbit_matching_cover/terminal.json conclusion D<=3",
    "savedL": 170,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  }
]
```

**原始证据：** [research/ddp/m2_coset_tower/affine_four_orbit_matching_cover/AFFINE_MATCHING_COVER.md](../../research/ddp/m2_coset_tower/affine_four_orbit_matching_cover/AFFINE_MATCHING_COVER.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Self-containedHamiltonclassification andmissingline/interpolation proof forceflat;noveltynotclaimed;notindependent-slope irregulargraphs.

**启发与重启依据：** Self-containedHamiltonclassification andmissingline/interpolation proof forceflat;noveltynotclaimed;notindependent-slope irregulargraphs.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

