---
type: experiment
node_id: exp:ddp-hierarchical676-factorization-20261026
title: "K26一因子3/4块连接：对角与循环配对两张完整图"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU"
duration: "0.5882 + 0.5113 CPU s"
provenance: "research/ddp/m2_factorization676/REPORT.md; research/ddp/m2_factorization676/cyclic_pairing/REPORT.md; research/ddp/m2_hierarchical676/DISTANCE_RULES.md"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# K26一因子3/4块连接：对角与循环配对两张完整图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=676；从属目标：[[5, 5]]

**距目标的证据：** Both676vertex1690edge graphs simple connected5regular. Diagonal D8/103041badpairs,LL73110 incl73060 cross-index. Cyclic pairing D7/27142badpairs:HH0,HB588,HL1018,BB268,BL8172,LL17096; leafgraph520 and blockquotient130 each connected.



**既有原文指标：** Both676vertex1690edge graphs simple connected5regular. Diagonal D8/103041badpairs,LL73110 incl73060 cross-index. Cyclic pairing D7/27142badpairs:HH0,HB588,HL1018,BB268,BL8172,LL17096; leafgraph520 and blockquotient130 each connected.

**从属变体：**
```json
[
  {
    "label": "diagonal block pairing",
    "n": 676,
    "actualD": 8,
    "bad_pairs": 103041,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "target": [
      5,
      5
    ],
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 3
  },
  {
    "label": "cyclic block pairing",
    "n": 676,
    "actualD": 7,
    "bad_pairs": 27142,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "target": [
      5,
      5
    ],
    "savedL": 650,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 2
  }
]
```

**原始证据：** [research/ddp/m2_factorization676/REPORT.md](../../research/ddp/m2_factorization676/REPORT.md)；[research/ddp/m2_factorization676/cyclic_pairing/REPORT.md](../../research/ddp/m2_factorization676/cyclic_pairing/REPORT.md)；[research/ddp/m2_hierarchical676/DISTANCE_RULES.md](../../research/ddp/m2_hierarchical676/DISTANCE_RULES.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** The second candidate changes the actual block-pair matching to break global index preservation while keeping3/4 group multiplicities and16 incidences per block. It is one diagnostic follow-up, not a seed search. Exact head-head coverage survives but other five-step routes fail. Neither candidate improves the public bound or the earlier insertion candidate.

**启发与重启依据：** The second candidate changes the actual block-pair matching to break global index preservation while keeping3/4 group multiplicities and16 incidences per block. It is one diagnostic follow-up, not a seed search. Exact head-head coverage survives but other five-step routes fail. Neither candidate improves the public bound or the earlier insertion candidate.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

