---
type: experiment
node_id: exp:ddp-stale-d4d3-messieres-n1-all3075-two-cut-fourstar42-no-20261101
title: "4D3 cached MessieresN1→42：全3075两不交删边四星严格NO；3案修新根却均伤oldold，非其他源排除"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/INPUT_BINDING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ALL3075_PAIR_PARAMETERS.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ALL3075_PAIR_STAGES.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/PAPER_SCOPE_REVIEW.md"
added: 2026-11-01T19:59:47Z
tags: ["ddp", "method-ledger"]
---

# 4D3 cached MessieresN1→42：全3075两不交删边四星严格NO；3案修新根却均伤oldold，非其他源排除

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (4,3)；L=41；条件性n=42（未据此计纪录）

**距目标的证据：** All3075 actual edited42/84 candidates rejected by finalcandidate ordinaryBFS;no accepted finalgraph/globalD per failed candidate claimed；预测存在newrootR3通过案得到支持3次，但没有完整D3图。3075unordereddisjointedgepairs全完成：3072案newrootR3失败，3案过门却全oldold失败，仅4个candidate旧labelBFS。首oldpair(1,33)两端均非pin：旧源一次针对pair诊断给3路1–17–22–33，删边17–22后实际新最短4路1–17–41–22–33；没有枚举所有旧最短路或声称旧路线unique。缓存JSON输入parse1，0sourceD3allroot/field/solver/Lean。累计.350856972/20CPU含接口.121139383；无未访问配置，只排该fixedsource/rule。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "related_cached_source_node": "ddp-stale-d4d5-messieres-three41-any-ninecover-capacity-20261101",
  "same_as_old_ninecover_scope": false,
  "new_source_gate_node": false,
  "source_id": "MessieresN1",
  "source_n": 41,
  "source_m": 82,
  "source_degree": 4,
  "target_n": 42,
  "target_m": 84,
  "target_degree": 4,
  "Moore_bound": 53,
  "Moore_space_from_baseline": 12,
  "Moore_space_is_not_constructibility": true,
  "unordered_disjoint_edgepair_domain": 3075,
  "configurations_finished": 3075,
  "newroot_R3_fail": 3072,
  "newroot_R3_pass": 3,
  "oldold_fail_after_pass": 3,
  "prediction_newroot_supported": true,
  "prediction_complete_graph_success": false,
  "candidate_newroot_ordinary_BFS": 3075,
  "candidate_old_label_BFS": 4,
  "source_single_pair_diagnostic": 1,
  "source_D3_allroot_BFS": 0,
  "first_oldold_failure": {
    "configuration": {
      "index": 1374,
      "old_edge_indices": [
        20,
        57
      ],
      "old_cut_edges": [
        [
          5,
          15
        ],
        [
          17,
          22
        ]
      ],
      "new_label": 41,
      "four_pins": [
        5,
        15,
        17,
        22
      ]
    },
    "BFS": {
      "root": 1,
      "target": 33,
      "distance": 4,
      "reached": 42,
      "eccentricity": 4,
      "actual_path": [
        1,
        17,
        41,
        22,
        33
      ],
      "distance_histogram": {
        "0": 1,
        "1": 4,
        "2": 12,
        "3": 24,
        "4": 1
      }
    },
    "both_endpoints_nonpin": true
  },
  "one_oldpair_route_diagnostic": {
    "original_source_pair": {
      "root": 1,
      "target": 33,
      "distance": 3,
      "actual_path": [
        1,
        17,
        22,
        33
      ],
      "visited_when_target_first_found": 24,
      "partial_discovered_max_distance": 3,
      "partial_discovery_histogram": {
        "-1": 17,
        "0": 1,
        "1": 4,
        "2": 12,
        "3": 7
      },
      "traversal_stopped_after_target_discovery": true,
      "minus1_is_unvisited_not_unreachable": true,
      "global_source_eccentricity_or_D3_verified": false
    },
    "new_candidate_distance": 4,
    "cut_edges_on_this_one_original_route": [
      [
        17,
        22
      ]
    ],
    "all_original_geodesics_enumerated": false,
    "uniqueness_claimed": false,
    "single_pair_only": true
  },
  "old_route_uniqueness_claimed": false,
  "source_cached_JSON_parses": 1,
  "remaining_unvisited_pairs": 0,
  "complete_fixed_rule_exclusion": true,
  "cumulative_charged_CPU_seconds": 0.350856972,
  "CPU_budget_seconds": 20,
  "inherited_interface_CPU_seconds": 0.121139383,
  "no_timer_reset": true,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/INPUT_BINDING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/INPUT_BINDING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ALL3075_PAIR_PARAMETERS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ALL3075_PAIR_PARAMETERS.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ALL3075_PAIR_STAGES.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ALL3075_PAIR_STAGES.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/PAPER_SCOPE_REVIEW.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/source_interface/PAPER_SCOPE_REVIEW.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only cached literal MessieresN1,41vertices/82edges/4regular. For each unordered pair of vertex-disjoint oldedges,delete exactly2 oldedges and add newvertex41 joined to their4 endpoints. Exactly3075 configurations,each42/84 and4regular. NewrootR3 gate first,oldlabel ordinaryBFS only for passers. This is not the older ordinaryninecover/D5 model,notN2/N3,otherN1rewirings or general4D3.

**仍未完成：** N2/N3 sources,otherN1rewirings and generalN(4,3) remain open;0new acceptedgraph/parameter/Lean.

**启发与重启依据：** STOP this exact N1 two-disjoint-cut plusone4star family. Newroot coverage can be repaired while nonpin oldpairs lose their distance3 routes;do not infer complete success from newrootR3 or focus only on pins. Do not continue source/cut/seed/model budget automatically. The canonical alternative41_ninecover node supplies the same cachedN1 input,not a reused exclusion for this different edit scope.

**单独的重启条件：** A separately justified different rewiring or source;N2/N3 and otherN1edits remain outside this strictNO.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- PETERSEN_AND_N2N3_TERMINALS_20261101 -->
## 后续N2/N3同架构对照终态

本页N1旧3075案NO仍有效且不重跑。N2/N3各3075案后来也完整NO：N2六次newrootpass却全oldoldfail，N3无pass；首N2旧pair0→1为ONE_PIN、3→4，区别于N1首BOTH_NONPIN。见[同机制sourcecomparison](ddp-stale-d4d3-messieres-n2n3-two-cut4star-source-comparison-20261101.md)。现root另批N2第三cut＋oldoldrepair改变生成规则、尚待终态；不可拿上述two-cutNO外推，不新增独立方法。
