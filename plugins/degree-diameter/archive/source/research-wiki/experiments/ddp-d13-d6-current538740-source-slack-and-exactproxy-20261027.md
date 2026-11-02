---
type: experiment
node_id: exp:ddp-d13-d6-current538740-source-slack-and-exactproxy-20261027
title: "Current538740 compound source:10787spares but minSat4, both minimumprototype exactproxy rules empty"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D6_current538740_source/REPORT.md; research/ddp/more_graphs_20261027/d13_D6_current538740_source/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE_RECEIPT.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/RESULT.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/MIN_SAT4_LOCAL.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/PARTIAL_PROXY_CHECK.json; research/ddp/more_graphs_20261027/d13_D6_current538740_source/profile.cpp; research/ddp/more_graphs_20261027/d13_D6_current538740_source/run_profile.py; research/ddp/more_graphs_20261027/d13_D6_current538740_source/prepare_source.py; research/ddp/more_graphs_20261027/d13_D6_current538740_source/profile.log; research/ddp/more_graphs_20261027/d13_D6_current538740_source/terminal.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/LATEST_AUTHOR_README.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/targeted_source_receipts.json"
added: 2026-10-27T22:37:04Z
tags: ["ddp", "method-ledger"]
---

# Current538740 compound source:10787spares but minSat4, both minimumprototype exactproxy rules empty

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,6)；L=538740；known_source_or_recovery n=538740；条件性n=538741（未据此计纪录）

**距目标的证据：** Actualsimpleundirected538740/3494842/max13,degree11:3149/12:7638/13:527953;free10787/slots13936. minSatN4 exactlyat316978,524504;zero/onefault0,soallcomplete-neighborhood false-twininsertions illegal. Bothprototypes have4fullpins anddisjointneighbor sets; full4intersectionjustprototype. Corrected N(u)-{v,w} subsetN(w) has0freeguards for all8u after complete localcandidategeneration;0newgraphs/lowerbounds.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 538740,
  "source_m": 3494842,
  "source_reported_D": 6,
  "source_degree_histogram": {
    "11": 3149,
    "12": 7638,
    "13": 527953
  },
  "free_vertices": 10787,
  "free_slots": 13936,
  "minSatN": 4,
  "minSatN_count": 2,
  "minimum_prototypes": [
    316978,
    524504
  ],
  "zeroSatN_count": 0,
  "onefault_count": 0,
  "native_profile_CPU_seconds": 0.661351,
  "compile_CPU_seconds": 0.69576,
  "profile_parent_children_CPU_seconds": 1.3688470000000001,
  "decompression_CPU_seconds": 1.1316455,
  "profile_plus_decompression_CPU_seconds": 2.5004925,
  "local_neighborhood_export_CPU_seconds": 0.20337719,
  "partial_proxy_CPU_seconds": 0.15951174499999998,
  "partial_proxy_local_adjacency_rows": 124,
  "partial_proxy_fullpins_checked": 8,
  "partial_proxy_total_guards_found": 0,
  "partial_proxy_candidate_counts": [
    [
      1,
      1,
      4,
      6
    ],
    [
      2,
      5,
      4,
      0
    ]
  ],
  "source_all_roots_BFS_repeated": 0,
  "candidate_graphs": 0,
  "solver": 0,
  "ordinary_bad_pairs": null,
  "prediction": "REFUTED",
  "UNKNOWN": 0,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D6_current538740_source/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE_RECEIPT.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE_RECEIPT.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/MIN_SAT4_LOCAL.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/MIN_SAT4_LOCAL.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/PARTIAL_PROXY_CHECK.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/PARTIAL_PROXY_CHECK.json)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/profile.cpp](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/profile.cpp)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/run_profile.py](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/run_profile.py)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/prepare_source.py](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/prepare_source.py)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/profile.log](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/profile.log)；[research/ddp/more_graphs_20261027/d13_D6_current538740_source/terminal.json](../../research/ddp/more_graphs_20261027/d13_D6_current538740_source/terminal.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/LATEST_AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/LATEST_AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/targeted_source_receipts.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/targeted_source_receipts.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actualcurrent538740literal only. Onecomplete degree/free/satNprofile ofall538740vertices, no sourceD6BFS. Then2minimumsat4prototypes literalneighbor export andlocalcorrected partialproxy test for their8fullneighbors. No guardballs/solver/candidate orold535495/534234/538440substitution.

**仍未完成：** No sourceall-rootD6measurement; actual_Dnull isdeliberate. ArbitrarymonotoneR5-neighborhoods,otherprototypes/approximateproxies,rewiringandgeneralN(13,6) remainunexcluded. T4/currentcoordinate binding notrecovered; rowcountsareactualadjacencyfacts.

**启发与重启依据：** Freevertexcount alone doesnotpredictausableclone. Currentcompoundhasmanyspares but everyprototype stillhas>=4fullneighbors. Thetwo bestsat-count prototypes lack even exactsame-length partial-neighbor substitutes. Stop thisfixedprototype rule; do not mechanically proceedtosat5/guardR5 orweakenproxybybadscore.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

