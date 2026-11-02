---
type: experiment
node_id: exp:ddp-wave6-tensor-product-screen
title: "保存因子的普通categorical tensor产品筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/tensor_product_screen/REPORT.md; research/ddp/breadth_20261027_wave6/tensor_product_screen/RESULTS.json; research/ddp/breadth_20261027_wave6/tensor_product_screen/screen.py; research/ddp/breadth_20261027_wave6/tensor_product_screen/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 保存因子的普通categorical tensor产品筛

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** parameter/capacity

**目标与阶数：** (?,?)；L=不适用／见变体；从属目标：[{'Delta': 4, 'D': 3, 'savedL': 41}, {'Delta': 6, 'D': 3, 'savedL': 120}, {'Delta': 8, 'D': 3, 'savedL': 253}, {'Delta': 12, 'D': 3, 'savedL': 810}]

**距目标的证据：** 7个数值越线组合全部同步walk/奇偶障碍，D4/D5无数值越线组合。

**其他指标（保持原计数类型）：**
```json
{
  "two_factor_rows": 90,
  "three_factor_rows": 40,
  "numerical_exceeders": 7,
  "graphs_generated": 0
}
```



**从属变体：**
```json
[
  {
    "factors": [
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      }
    ],
    "factor_count": 2,
    "degree_bound": 4,
    "target_diameter": 3,
    "order": 49,
    "baseline_at_degree_bound": 41,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "C7 has no triangle, hence no closed3walk at any vertex.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order7>Moore(2,2)=5, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 4,
    "target_baseline": 41
  },
  {
    "factors": [
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 3,
        "diameter": 3,
        "order": 20,
        "kind": "saved_maintainer_source"
      }
    ],
    "factor_count": 2,
    "degree_bound": 6,
    "target_diameter": 3,
    "order": 140,
    "baseline_at_degree_bound": 120,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "C7 has no triangle, hence no closed3walk at any vertex.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order20>Moore(3,2)=10, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 6,
    "target_baseline": 120
  },
  {
    "factors": [
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 4,
        "diameter": 3,
        "order": 41,
        "kind": "saved_maintainer_source"
      }
    ],
    "factor_count": 2,
    "degree_bound": 8,
    "target_diameter": 3,
    "order": 287,
    "baseline_at_degree_bound": 253,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "C7 has no triangle, hence no closed3walk at any vertex.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order41>Moore(4,2)=17, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 8,
    "target_baseline": 253
  },
  {
    "factors": [
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      }
    ],
    "factor_count": 3,
    "degree_bound": 8,
    "target_diameter": 3,
    "order": 343,
    "baseline_at_degree_bound": 253,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "C7 has no triangle, hence no closed3walk at any vertex.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order7>Moore(2,2)=5, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 8,
    "target_baseline": 253
  },
  {
    "factors": [
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 6,
        "diameter": 3,
        "order": 120,
        "kind": "saved_maintainer_source"
      }
    ],
    "factor_count": 2,
    "degree_bound": 12,
    "target_diameter": 3,
    "order": 840,
    "baseline_at_degree_bound": 810,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "C7 has no triangle, hence no closed3walk at any vertex.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order120>Moore(6,2)=37, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 12,
    "target_baseline": 810
  },
  {
    "factors": [
      {
        "degree": 3,
        "diameter": 3,
        "order": 20,
        "kind": "saved_maintainer_source"
      },
      {
        "degree": 4,
        "diameter": 3,
        "order": 41,
        "kind": "saved_maintainer_source"
      }
    ],
    "factor_count": 2,
    "degree_bound": 12,
    "target_diameter": 3,
    "order": 820,
    "baseline_at_degree_bound": 810,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "A subcubic graph with a triangle has at most1+3+4+8=16 vertices within3 of a triangle vertex; order20 and diameter3 force trianglefree.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order41>Moore(4,2)=17, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 12,
    "target_baseline": 810
  },
  {
    "factors": [
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 2,
        "diameter": 3,
        "order": 7,
        "kind": "cycleC7"
      },
      {
        "degree": 3,
        "diameter": 3,
        "order": 20,
        "kind": "saved_maintainer_source"
      }
    ],
    "factor_count": 3,
    "degree_bound": 12,
    "target_diameter": 3,
    "order": 980,
    "baseline_at_degree_bound": 810,
    "numerically_exceeds_baseline": true,
    "walk_obstruction": {
      "triangle_free_factor_index": 0,
      "triangle_free_reason": "C7 has no triangle, hence no closed3walk at any vertex.",
      "distance3_factor_index": 1,
      "distance3_existence_reason": "order7>Moore(2,2)=5, while source diameter3",
      "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
      "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
      "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."
    },
    "target_degree_cap": 12,
    "target_baseline": 810
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave6/tensor_product_screen/REPORT.md](../../research/ddp/breadth_20261027_wave6/tensor_product_screen/REPORT.md)；[research/ddp/breadth_20261027_wave6/tensor_product_screen/RESULTS.json](../../research/ddp/breadth_20261027_wave6/tensor_product_screen/RESULTS.json)；[research/ddp/breadth_20261027_wave6/tensor_product_screen/screen.py](../../research/ddp/breadth_20261027_wave6/tensor_product_screen/screen.py)；[research/ddp/breadth_20261027_wave6/tensor_product_screen/terminal.json](../../research/ddp/breadth_20261027_wave6/tensor_product_screen/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保存source orders及oddcycles，2/3因子、目标27格；不含未知因子或修补产品

**正向保证：** n为因子阶乘积，degree为因子degree乘积；完整同步walk条件

**仍未完成：** 一般产品修补和未知更大因子未排。

**启发与重启依据：** 只有新因子或改变同步路线规则才值得重启。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

