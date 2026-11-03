---
type: experiment
node_id: exp:ddp-affine930-capacity-20261026
title: "930阶十一与十二度完整必要容量比较"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, one worker per bounded batch"
duration: "2.764555 CPU s"
provenance: "research/ddp/m2_coset_tower/affine_cayley930_capacity/REPORT.md"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 930阶十一与十二度完整必要容量比较

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** 多目标：degree11 necessary capacity→[11, 3]／L=715；degree12 necessary capacity→[12, 3]／L=810（逐变体，不合成一个距离）；条件性n=930（未据此计纪录）

**距目标的证据：** d11:15504→1509→78;d12:54264→16642→5944. Zero fieldassignments/graphs/BFS.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family.

**其他指标（保持原计数类型）：**
```json
{
  "superseding_existing_wiki": [
    {
      "path": "research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md",
      "note": "Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family."
    }
  ]
}
```

**既有原文指标：** d11:15504→1509→78;d12:54264→16642→5944. Zero fieldassignments/graphs/BFS.

**从属变体：**
```json
[
  {
    "label": "degree11 necessary capacity",
    "target": [
      11,
      3
    ],
    "savedL": 715,
    "n": 930,
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/affine_cayley930_capacity/metadata.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "degree12 necessary capacity",
    "target": [
      12,
      3
    ],
    "savedL": 810,
    "n": 930,
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/affine_cayley930_capacity/metadata.json",
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  }
]
```

**原始证据：** [research/ddp/m2_coset_tower/affine_cayley930_capacity/REPORT.md](../../research/ddp/m2_coset_tower/affine_cayley930_capacity/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Necessary phase/form capacities only;d12 theoretical191303804004 inputs notrun.

**启发与重启依据：** Necessary phase/form capacities only;d12 theoretical191303804004 inputs notrun.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

