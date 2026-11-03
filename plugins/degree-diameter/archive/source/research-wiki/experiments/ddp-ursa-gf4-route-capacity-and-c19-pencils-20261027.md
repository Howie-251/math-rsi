---
type: experiment
node_id: exp:ddp-ursa-gf4-route-capacity-and-c19-pencils-20261027
title: "URSA固定GF4 chart：96满秩四词、n≤120必要界与C19具体rank3洞"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/REPORT.md; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/PREDICTION.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/RESULT.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/C19_SLOT_ANALYSIS.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/WORD_IMAGES.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/FREE_REDUCTION_CLASSES.json"
added: 2026-10-27T18:59:15Z
tags: ["ddp", "method-ledger"]
---

# URSA固定GF4 chart：96满秩四词、n≤120必要界与C19具体rank3洞

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-route-obstruction

**目标与阶数：** (16,4)；L=16384；条件性n=19456（未据此计纪录）

**距目标的证据：** 安全总容量35201→controller≤137；freeclass union/common0给255n≤30753→n≤120，未封64以上。C19的30/32/42/47各唯一rank3四词故只64/256；R2slot61四个commoncore16超平面并208，self35词并217缺39。

**其他指标（保持原计数类型）：**
```json
{
  "all_words": 341,
  "reduced_words": 161,
  "reduced4_rank4": 96,
  "reduced4_rank3": 12,
  "all_canonical_M_ranks": [
    3,
    3,
    3,
    3
  ],
  "all_image_cardinality_sum": 35201,
  "free_class_union_sum": 30914,
  "controller_necessary_upper_bound": 120,
  "C19_firstroot_missing_targets": 963,
  "C19_metric_unit": "one fixed root missing target vertices, not unordered allpairs",
  "C19_match_all_native_fibers": true,
  "word_inventory_CPU": 0.10596401700000001,
  "cached_classification_CPU": 0.006314864999999996,
  "BFS": 0,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/REPORT.md)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/RESULT.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/RESULT.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/C19_SLOT_ANALYSIS.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/C19_SLOT_ANALYSIS.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/WORD_IMAGES.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/WORD_IMAGES.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/FREE_REDUCTION_CLASSES.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/route_capacity/FREE_REDUCTION_CLASSES.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅cached4全局线关系的341个<=4词代数（含回退），0source重parse/BFS。108reduced4中96rank4/12rank3，4canonicalM全rank3；free-reduction类仅归并actualimage并，不取消fiber回退。C19已有实验9slots/963单根缺项逐fiber全部匹配，不新建第二图/独立方法。

**仍未完成：** Generalcontrollers above64, other charts/affine offsets and completeLean remain open; C19 unique-route affine-offset obstruction only that fixedcontroller/linearparts.

**启发与重启依据：** GF4四超平面pencil不等于GF3全fiber；低秩路线仍必须实际取并，不能只reduced或rank4充分证书判actual失败。更大controller必须额外路由补齐deficient词，并同时保护self；不由容量余量直接开搜索。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

