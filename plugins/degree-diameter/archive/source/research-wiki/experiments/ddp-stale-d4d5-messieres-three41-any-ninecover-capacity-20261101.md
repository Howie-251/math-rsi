---
type: experiment
node_id: exp:ddp-stale-d4d5-messieres-three41-any-ninecover-capacity-20261101
title: "4D5目标369的新源对照：N1/N2/N3返回容量仅1/3/1，排各自任意普通九cover"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/INITIAL_PARSE_FAILURE_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/INITIAL_PARSE_FAILURE_TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N1.ROUTE_CAPACITY.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.ROUTE_CAPACITY.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N3.ROUTE_CAPACITY.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/run_once.py"
added: 2026-11-01T17:57:59Z
tags: ["ddp", "method-ledger"]
---

# 4D5目标369的新源对照：N1/N2/N3返回容量仅1/3/1，排各自任意普通九cover

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_route_or_input_transfer_gate

**目标与阶数：** (4,5)；L=364；条件性n=369（未据此计纪录）

**距目标的证据：** No full target graph was generated; source legality inherited only；三个新source各枚长度0..5非回退walk19885条／1681orderedpair。最紧N1(11,11)=1与N3(1,1)=1均仅空路；N2(0,0)=3为空路及0–37–4–16–40–0两方向。每个槽不足9，任何普通9sheetcover从固定lift根只能到不足9个同fiber端点，故缺返回路线而非电压取值不佳；“至少一源过门”预测被推翻。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "source_variants": [
    {
      "source_id": "N1",
      "actual_fetch_URL": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/41_Messieres_N1.adjlist",
      "input_vertices": 41,
      "input_edges": 82,
      "input_degree_histogram": {
        "4": 41
      },
      "literal_edge_set_equals_old_Allwright1a": false,
      "minimum_count": 1,
      "tight_pair": [
        11,
        11
      ],
      "tight_pair_walks": [
        [
          11
        ]
      ],
      "tight_pair_walk_length_histogram": {
        "0": 1
      },
      "ordered_pairs_counted": 1681,
      "nonbacktracking_walks_including_length0_total": 19885
    },
    {
      "source_id": "N2",
      "actual_fetch_URL": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/41_Messieres_N2.adjlist",
      "input_vertices": 41,
      "input_edges": 82,
      "input_degree_histogram": {
        "4": 41
      },
      "literal_edge_set_equals_old_Allwright1a": false,
      "minimum_count": 3,
      "tight_pair": [
        0,
        0
      ],
      "tight_pair_walks": [
        [
          0
        ],
        [
          0,
          37,
          4,
          16,
          40,
          0
        ],
        [
          0,
          40,
          16,
          4,
          37,
          0
        ]
      ],
      "tight_pair_walk_length_histogram": {
        "0": 1,
        "5": 2
      },
      "ordered_pairs_counted": 1681,
      "nonbacktracking_walks_including_length0_total": 19885
    },
    {
      "source_id": "N3",
      "actual_fetch_URL": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/41_Messieres_N3.adjlist",
      "input_vertices": 41,
      "input_edges": 82,
      "input_degree_histogram": {
        "4": 41
      },
      "literal_edge_set_equals_old_Allwright1a": false,
      "minimum_count": 1,
      "tight_pair": [
        1,
        1
      ],
      "tight_pair_walks": [
        [
          1
        ]
      ],
      "tight_pair_walk_length_histogram": {
        "0": 1
      },
      "ordered_pairs_counted": 1681,
      "nonbacktracking_walks_including_length0_total": 19885
    }
  ],
  "prediction": "REFUTED_ALL_THREE_NEW_SOURCES_HAVE_ROUTE_DEFICIT",
  "required_sheet_endpoints": 9,
  "count_lengths": [
    0,
    5
  ],
  "shortest_lift_projects_nonbacktracking_proof": true,
  "source_D3_and_nonisomorphism": "primary claim inherited; not source BFS/isomorphism checked",
  "new_source_BFS": 0,
  "official_adjlistt_typo_404": true,
  "corrected_adjlist_actual_downloads": 3,
  "first_parse_failure_preserved": true,
  "charged_CPU": 0.32443119,
  "CPU_budget": 10,
  "first_failure_charged_CPU": 0.14797470699999998,
  "no_timer_reset": true,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/INITIAL_PARSE_FAILURE_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/INITIAL_PARSE_FAILURE_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/INITIAL_PARSE_FAILURE_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/INITIAL_PARSE_FAILURE_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N1.ROUTE_CAPACITY.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N1.ROUTE_CAPACITY.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.ROUTE_CAPACITY.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.ROUTE_CAPACITY.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N3.ROUTE_CAPACITY.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N3.ROUTE_CAPACITY.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/run_once.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only the actual October2026 Michel de Messieres N1,N2,N3 source graphs listed by Comellas, each41vertices/82edges. Any ordinary9sheet local-bijection cover of each fixed source, including arbitrary permutation voltages; not source editing, added fiber edges or all369vertex graphs. Old Allwright1(a) C9/affine exclusions are inherited without rerun.

**仍未完成：** No accepted target graph; broader rules beyond the exact recorded scope remain open.

**启发与重启依据：** STOP these three fixed-source ordinary9covers; no C9/S9 voltage solver or source-label variant. A new authorized rule must change actual source/routing structure, not merely the deck group.

**单独的重启条件：** STOP these three fixed-source ordinary9covers; no C9/S9 voltage solver or source-label variant. A new authorized rule must change actual source/routing structure, not merely the deck group.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- FINAL16416_TECHNICAL_REVIEWS_N1_TWO_CUT_20261101 -->
## cachedN1在另一改边问题中的新终态（旧ninecover范围不变）

N1同一41/82源被用于4D3/42目标的两不交oldedgecut＋新4star；完整3075配置全排，3newrootpass均oldoldfail。不是复跑本页9cover/D5，也不把本页N2/N3的coverNO搬给新rewire。见[固定N1新实验](ddp-stale-d4d3-messieres-n1-all3075-two-cut-fourstar42-no-20261101.md)。0新source验收或独立方法；其他source/改边仍未排，不自动续算。
