---
type: experiment
node_id: exp:ddp-coset-towers-20261026
title: "陪集塔固定425、1066、2257与3200三逆对范围的实际终态"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU worker per sequential batch"
duration: "d4 2.67061CPU s; q41 preparation/search about1.70CPU s; d6 103.72CPU s; F64 109.924CPU s"
provenance: "research/ddp/m2_coset_tower/d4_q25; research/ddp/m2_coset_tower/RING98_SCOPE.md; research/ddp/source650_hierarchy/ALGEBRAIC_DIAGNOSIS.md; reviews/ddp/m2_coset_tower_review_disposition_20261026.md; research/ddp/m2_coset_tower/q41_search; research/ddp/m2_coset_tower/d6_q61; research/ddp/m2_coset_tower/d7_f64_three_pairs"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "coset-tower", "finite-exclusion", "method-ledger"]
---

# 陪集塔固定425、1066、2257与3200三逆对范围的实际终态

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** graph_or_graph_family

**目标与阶数：** 多目标：F25 fixed tower→[4, 5]／L=364；F41 fixed tower→[5, 5]／L=650；F61 fixed tower→[6, 5]／L=1518；F64 three-pair tower→[7, 5]／L=2810；Z98/C42 fixedtower capacity proof; planned340200 inputs never run→[7, 5]／L=2810（逐变体，不合成一个距离）

**距目标的证据：** d4/F25 all66;d5/F41 valid22932 and HH-scored15190;d6/F61 valid1980573 and HH-scored1671690;d7/F64 three pairs valid1058400,all scored. Independent full edge-list BFS confirms best425 D7/18450bad;1066 D7/42230bad;2257 D6/127185bad;3200 D6/83328bad. F64 best11200edges,7regular,roots48/78/42; independent all3200-root checker0.20992s. Head-zero normalized counts d6=804 and F64=3016; neither family has block-zero among HH passers.；后续结果优先：research-wiki/experiments/ddp-f64-central-quotient-20261026.md；Later existing note closes the cyclic F64 two-pair/two-involution remainder and combines to close that cyclic3200 tower; not faithful semilinear or other towers.

**其他指标（保持原计数类型）：**
```json
{
  "superseding_existing_wiki": [
    {
      "path": "research-wiki/experiments/ddp-f64-central-quotient-20261026.md",
      "note": "Later existing note closes the cyclic F64 two-pair/two-involution remainder and combines to close that cyclic3200 tower; not faithful semilinear or other towers."
    }
  ]
}
```

**既有原文指标：** d4/F25 all66;d5/F41 valid22932 and HH-scored15190;d6/F61 valid1980573 and HH-scored1671690;d7/F64 three pairs valid1058400,all scored. Independent full edge-list BFS confirms best425 D7/18450bad;1066 D7/42230bad;2257 D6/127185bad;3200 D6/83328bad. F64 best11200edges,7regular,roots48/78/42; independent all3200-root checker0.20992s. Head-zero normalized counts d6=804 and F64=3016; neither family has block-zero among HH passers.

**从属变体：**
```json
[
  {
    "label": "F25 fixed tower",
    "target": [
      4,
      5
    ],
    "n": 425,
    "actualD": 7,
    "bad_pairs": 18450,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 364,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 2
  },
  {
    "label": "F41 fixed tower",
    "target": [
      5,
      5
    ],
    "n": 1066,
    "actualD": 7,
    "bad_pairs": 42230,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 2
  },
  {
    "label": "F61 fixed tower",
    "target": [
      6,
      5
    ],
    "n": 2257,
    "actualD": 6,
    "bad_pairs": 127185,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 1518,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "F64 three-pair tower",
    "target": [
      7,
      5
    ],
    "n": 3200,
    "actualD": 6,
    "bad_pairs": 83328,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 2810,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  },
  {
    "label": "Z98/C42 fixedtower capacity proof; planned340200 inputs never run",
    "target": [
      7,
      5
    ],
    "n": 4900,
    "n_role": "prospective unconstructed order",
    "actualD": null,
    "bad_pairs": null,
    "count_type": null,
    "evidence": "research/ddp/m2_coset_tower/RING98_SCOPE.md:3,18",
    "savedL": 2810,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  }
]
```

**原始证据：** [research/ddp/m2_coset_tower/d4_q25](../../research/ddp/m2_coset_tower/d4_q25)；[research/ddp/m2_coset_tower/RING98_SCOPE.md](../../research/ddp/m2_coset_tower/RING98_SCOPE.md)；[research/ddp/source650_hierarchy/ALGEBRAIC_DIAGNOSIS.md](../../research/ddp/source650_hierarchy/ALGEBRAIC_DIAGNOSIS.md)；[reviews/ddp/m2_coset_tower_review_disposition_20261026.md](../../reviews/ddp/m2_coset_tower_review_disposition_20261026.md)；[research/ddp/m2_coset_tower/q41_search](../../research/ddp/m2_coset_tower/q41_search)；[research/ddp/m2_coset_tower/d6_q61](../../research/ddp/m2_coset_tower/d6_q61)；[research/ddp/m2_coset_tower/d7_f64_three_pairs](../../research/ddp/m2_coset_tower/d7_f64_three_pairs)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** No D5 in any stated finite batch. Necessary HH failures need no full score; best scores have HH-conditioned scope. Fixed425/1066/2257 towers also have separate all-involution exclusions. F64 two-pair/two-involution branch remains open; only three-pair batch exhausted. Separate Z98/4900 tower has a complete paper capacity exclusion including all cost2 block jumps, so planned340200 input search was never executed. Exact six-type group-set route criterion now proved in FULL_ROUTE_CRITERIA.md. No new lower bound, no general-order exclusion.

**启发与重启依据：** No D5 in any stated finite batch. Necessary HH failures need no full score; best scores have HH-conditioned scope. Fixed425/1066/2257 towers also have separate all-involution exclusions. F64 two-pair/two-involution branch remains open; only three-pair batch exhausted. Separate Z98/4900 tower has a complete paper capacity exclusion including all cost2 block jumps, so planned340200 input search was never executed. Exact six-type group-set route criterion now proved in FULL_ROUTE_CRITERIA.md. No new lower bound, no general-order exclusion.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

