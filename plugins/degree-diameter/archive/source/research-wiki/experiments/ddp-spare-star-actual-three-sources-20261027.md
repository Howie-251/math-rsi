---
type: experiment
node_id: exp:ddp-spare-star-actual-three-sources-20261027
title: "完整邻域复制三源检查：N13最少1满邻点，N14最少9，均无直接twin"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md; research/ddp/more_graphs_20261027/spare_star_transfer/RESULT.json"
added: 2026-10-27T17:50:48Z
tags: ["ddp", "method-ledger"]
---

# 完整邻域复制三源检查：N13最少1满邻点，N14最少9，均无直接twin

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** 多目标：source13→[13, 5]／L=51417；source14→[14, 5]／L=94186；source15→[15, 5]／L=100132（逐变体，不合成一个距离）

**距目标的证据：** 实际51417/94186源逐v完整N(v)扫描均无合法fullstar；最少满邻点分别1（91 prototypes）和9（20 prototypes）。D15源到后同一native扫描100132个v也无fullstar。0BFS/新图。

**其他指标（保持原计数类型）：**
```json
{
  "source13_minimum_saturated_neighbors": 1,
  "source13_minimum_attainers": 91,
  "source14_minimum_saturated_neighbors": 9,
  "source14_minimum_attainers": 20,
  "source15_prototypes_scanned": 100132,
  "fullstar_hits": 0,
  "source13_14_CPU_seconds": 0.67839,
  "BFS": 0
}
```



**从属变体：**
```json
[
  {
    "label": "source13",
    "target_Delta": 13,
    "target_D": 5,
    "savedL": 51417
  },
  {
    "label": "source14",
    "target_Delta": 14,
    "target_D": 5,
    "savedL": 94186
  },
  {
    "label": "source15",
    "target_Delta": 15,
    "target_D": 5,
    "savedL": 100132
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/spare_star_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/spare_star_transfer/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际51417/94186源逐v完整N(v)扫描均无合法fullstar；最少满邻点分别1（91 prototypes）和9（20 prototypes）。D15源到后同一native扫描100132个v也无fullstar。0BFS/新图。

**仍未完成：** No general source-family maximality is claimed; final concrete Lean remains incomplete.

**启发与重启依据：** N13恰1满邻点提示可以有依据删1并修复私有路线；N14至少9不适合照搬单缺口规则。完整N(v)保边复制失败不排near-neighborhood修复。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

