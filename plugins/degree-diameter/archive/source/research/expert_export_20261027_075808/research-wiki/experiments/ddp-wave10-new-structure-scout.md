---
type: experiment
node_id: exp:ddp-wave10-new-structure-scout
title: "线性码Hamming商图：全局covering-radius路由，但27格阶数界均不足"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave10/new_structure_scout/REPORT.md; research/ddp/breadth_20261027_wave10/new_structure_scout/RESULT.json; research/ddp/breadth_20261027_wave10/new_structure_scout/terminal.json; research/ddp/breadth_20261027_wave10/new_structure_scout/screen.py"
added: 2026-10-27T07:58:08Z
tags: ["ddp", "method-ledger"]
---

# 线性码Hamming商图：全局covering-radius路由，但27格阶数界均不足

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** 多目标：变体→[4, 3]／L=41；变体→[4, 4]／L=104；变体→[4, 5]／L=364；变体→[5, 3]／L=72；变体→[5, 4]／L=252；变体→[5, 5]／L=650；变体→[6, 3]／L=120；变体→[6, 4]／L=441；变体→[6, 5]／L=1518；变体→[7, 3]／L=170；变体→[7, 4]／L=684；变体→[7, 5]／L=2810；变体→[8, 3]／L=253；变体→[8, 4]／L=1100；变体→[8, 5]／L=5334；变体→[9, 3]／L=585；变体→[9, 4]／L=1768；变体→[9, 5]／L=9020；变体→[10, 3]／L=650；变体→[10, 4]／L=2485；变体→[10, 5]／L=33397；变体→[11, 3]／L=715；变体→[11, 4]／L=3444；变体→[11, 5]／L=37628；变体→[12, 3]／L=810；变体→[12, 4]／L=5832；变体→[12, 5]／L=42342（逐变体，不合成一个距离）

**距目标的证据：** no_new_graph_generated；独立推导diam等于ker(H) covering radius；可交换短词合并为至多D个方向的非零线性组合，n=q^r≤sum binom(s,j)(q-1)^j。有限495项q/s/目标比较覆盖27格，存活0；没有矩阵赋值、码搜索或图。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "theoretical_family_order_bound",
  "graph_generated": false,
  "matrix_assignments": 0,
  "codes_generated": 0,
  "field_direction_comparisons": 495,
  "cells_checked": 27,
  "capacity_survivors": 0,
  "CPU_seconds": 0.0018100669999999985,
  "BFS_performed": false,
  "source": {
    "title": "On nested completely regular codes and distance regular graphs",
    "authors": [
      "J.Borges",
      "J.Rifa",
      "V.A.Zinoviev"
    ],
    "year": 2014,
    "primary_url": "https://ddd.uab.cat/pub/poncom/2014/142913/intworalg_a2014p85.pdf",
    "read_scope": "pp85-89: covering-radius definitions, Section2 Lemmas1/2, explicit nested-code construction and Section4 Theorem3; not only abstract.",
    "binary_source_family": {
      "m_even_at_least": 4,
      "i_range": "1..m/2",
      "vertices": "2^(m+i)",
      "degree": "2^m-1",
      "diameter": 3,
      "smallest_degree": 15,
      "within_goal_degree_range": false
    },
    "source_scope_note": "Source distance-regularity guarantee is for completely regular binary codes. The general q-ary syndrome graph and its distance formula are derived directly here; no q-ary distance-regularity is assumed."
  },
  "relation_to_old_work": "New explicit code/covering-radius representation, but within the broad abelian Cayley class; not claimed as a new independent construction class."
}
```



**从属变体：**
```json
[
  {
    "target_Delta": 4,
    "target_D": 3,
    "savedL": 41,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 9,
    "looser_binary_volume_upper_bound": 15,
    "order_shortfall_from_savedL": 32,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 16,
    "looser_binary_volume_upper_bound": 16,
    "order_shortfall_from_savedL": 88,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 4,
    "target_D": 5,
    "savedL": 364,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 16,
    "looser_binary_volume_upper_bound": 16,
    "order_shortfall_from_savedL": 348,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 5,
    "target_D": 3,
    "savedL": 72,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 16,
    "looser_binary_volume_upper_bound": 26,
    "order_shortfall_from_savedL": 56,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 5,
    "target_D": 4,
    "savedL": 252,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 16,
    "looser_binary_volume_upper_bound": 31,
    "order_shortfall_from_savedL": 236,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 5,
    "target_D": 5,
    "savedL": 650,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 32,
    "looser_binary_volume_upper_bound": 32,
    "order_shortfall_from_savedL": 618,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 6,
    "target_D": 3,
    "savedL": 120,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 32,
    "looser_binary_volume_upper_bound": 42,
    "order_shortfall_from_savedL": 88,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 6,
    "target_D": 4,
    "savedL": 441,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 32,
    "looser_binary_volume_upper_bound": 57,
    "order_shortfall_from_savedL": 409,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 6,
    "target_D": 5,
    "savedL": 1518,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 32,
    "looser_binary_volume_upper_bound": 63,
    "order_shortfall_from_savedL": 1486,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 7,
    "target_D": 3,
    "savedL": 170,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 64,
    "looser_binary_volume_upper_bound": 64,
    "order_shortfall_from_savedL": 106,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 7,
    "target_D": 4,
    "savedL": 684,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 64,
    "looser_binary_volume_upper_bound": 99,
    "order_shortfall_from_savedL": 620,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 7,
    "target_D": 5,
    "savedL": 2810,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 64,
    "looser_binary_volume_upper_bound": 120,
    "order_shortfall_from_savedL": 2746,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 8,
    "target_D": 3,
    "savedL": 253,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 64,
    "looser_binary_volume_upper_bound": 93,
    "order_shortfall_from_savedL": 189,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 8,
    "target_D": 4,
    "savedL": 1100,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 128,
    "looser_binary_volume_upper_bound": 163,
    "order_shortfall_from_savedL": 972,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 8,
    "target_D": 5,
    "savedL": 5334,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 128,
    "looser_binary_volume_upper_bound": 219,
    "order_shortfall_from_savedL": 5206,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 9,
    "target_D": 3,
    "savedL": 585,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 128,
    "looser_binary_volume_upper_bound": 130,
    "order_shortfall_from_savedL": 457,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 9,
    "target_D": 4,
    "savedL": 1768,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 256,
    "looser_binary_volume_upper_bound": 256,
    "order_shortfall_from_savedL": 1512,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 9,
    "target_D": 5,
    "savedL": 9020,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 256,
    "looser_binary_volume_upper_bound": 382,
    "order_shortfall_from_savedL": 8764,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 10,
    "target_D": 3,
    "savedL": 650,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 128,
    "looser_binary_volume_upper_bound": 176,
    "order_shortfall_from_savedL": 522,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 10,
    "target_D": 4,
    "savedL": 2485,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 256,
    "looser_binary_volume_upper_bound": 386,
    "order_shortfall_from_savedL": 2229,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 10,
    "target_D": 5,
    "savedL": 33397,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 512,
    "looser_binary_volume_upper_bound": 638,
    "order_shortfall_from_savedL": 32885,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 11,
    "target_D": 3,
    "savedL": 715,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 128,
    "looser_binary_volume_upper_bound": 232,
    "order_shortfall_from_savedL": 587,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 11,
    "target_D": 4,
    "savedL": 3444,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 512,
    "looser_binary_volume_upper_bound": 562,
    "order_shortfall_from_savedL": 2932,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 11,
    "target_D": 5,
    "savedL": 37628,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 1024,
    "looser_binary_volume_upper_bound": 1024,
    "order_shortfall_from_savedL": 36604,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 12,
    "target_D": 3,
    "savedL": 810,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 256,
    "looser_binary_volume_upper_bound": 299,
    "order_shortfall_from_savedL": 554,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 12,
    "target_D": 4,
    "savedL": 5832,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 512,
    "looser_binary_volume_upper_bound": 794,
    "order_shortfall_from_savedL": 5320,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  },
  {
    "target_Delta": 12,
    "target_D": 5,
    "savedL": 42342,
    "baseline_as_of": "2026-10-26",
    "n": {
      "actual": null,
      "hypothetical": null
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "symbolic_order_upper_bound": 1024,
    "looser_binary_volume_upper_bound": 1586,
    "order_shortfall_from_savedL": 41318,
    "upper_bound_not_attainability": true,
    "capacity_survivors": 0,
    "graph_generated": false
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave10/new_structure_scout/REPORT.md](../../research/ddp/breadth_20261027_wave10/new_structure_scout/REPORT.md)；[research/ddp/breadth_20261027_wave10/new_structure_scout/RESULT.json](../../research/ddp/breadth_20261027_wave10/new_structure_scout/RESULT.json)；[research/ddp/breadth_20261027_wave10/new_structure_scout/terminal.json](../../research/ddp/breadth_20261027_wave10/new_structure_scout/terminal.json)；[research/ddp/breadth_20261027_wave10/new_structure_scout/screen.py](../../research/ddp/breadth_20261027_wave10/new_structure_scout/screen.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 所有标准Fq线性码coset/syndrome图：V=Fq^r，沿H各非比例列方向的全部非零倍数连边；degree=s(q-1)≤12，D∈{3,4,5}。

**正向保证：** 给定covering radius≤D的码即可严格保证全对D；不靠局部rank或采样。；实际读primary Borges–Rifa–Zinoviev2014定义/Lemma1/2/Theorem3；其明确二元distance-regular D3族最小degree15已超范围。；标准syndrome生成公式和一般qary距离公式直接证明；不把二元distance-regularity定理外推。

**仍未完成：** 该标准线性码边规则在27格均不能过现有下界；不涉及非线性分块、删选部分标量或其他非交换图。

**启发与重启依据：** 进一步增加码长度、换H或完美码名称不能绕过统一sphere容量界；新尝试必须改变实际分块/生成边规则并另给路由论证。该入口仍属于广义abelian Cayley相关类，不虚增独立方法数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

