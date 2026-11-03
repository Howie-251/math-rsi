---
type: experiment
node_id: exp:ddp-stale-d6d9-331387-source-single-edge-subdivision-all-types-20261101
title: "6D9旧331387源：无余度append关闭；三generator-type的R8缺口排全部单边细分，非全参数关闭"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/run_once.py; research/ddp/more_graphs_20261027/d6_D9_current331387_source/AUTHOR_deg6_D9_CHK.c; research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_D6_D10_primary_cache/desc_g9.html; research/ddp/more_graphs_20261027/d6_D9_current331387_source/field6959_all_embeddings/REPORT.md; research/ddp/more_graphs_20261027/d6_D9_current331387_source/ramified6860_quotient_gate/REPORT.md"
added: 2026-11-01T18:31:39Z
tags: ["ddp", "method-ledger"]
---

# 6D9旧331387源：无余度append关闭；三generator-type的R8缺口排全部单边细分，非全参数关闭

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_route_or_input_transfer_gate

**目标与阶数：** (6,9)；L=331387；条件性n=331388（未据此计纪录）

**距目标的证据：** Inherited sourceD9; three exact modified-old endpoint-R8 queries only, no full candidate or old-oldD9 BFS；实际小Crecipe与cached primary给331387/994161全6regular，非新全degree扫描；cap6纯保边append无连接余度。RIGHT Cayley C49⋊41F6763的三inverse-pair代表(25,1254)/(18,541)/(47,4642)在各自删边host中端点B8 union仅覆盖317299/317512/317359，漏14088/13875/14028个旧点；首漏labels20/6/20，新细分点距各至少10。三query覆盖全oldedges的理由是lefttranslation，不是三随机样本。未生成331388完整图、未测oldold或原sourceD9。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 2929687,
  "located_baseline": 331387,
  "Moore_space": 2598300,
  "Moore_space_is_only_upper_bound_slack": true,
  "source_order": 331387,
  "source_edges": 994161,
  "source_degree_evidence": {
    "minimum": 6,
    "maximum": 6,
    "all_regular": true,
    "basis": "Cached primary explicit min/max plus existing Cayley six-generator recipe; no new full degree-profile measurement"
  },
  "free_vertices_at_cap6": 0,
  "total_degree_spare_at_cap6": 0,
  "source_D9": "INHERITED_NOT_REVERIFIED",
  "source_primary_authors": "Alexis Rodriguez and Eduardo Canale",
  "source_communication_date": "2012-08-20",
  "source_C_recipe": "research/ddp/more_graphs_20261027/d6_D9_current331387_source/AUTHOR_deg6_D9_CHK.c",
  "actual_source_raw_adjacency_not_downloaded": true,
  "group": {
    "phase_order": 49,
    "normal_field_order": 6763,
    "action": 41,
    "RIGHT_law": "(j,n)(k,t)=(j+k,n*41^k+t)",
    "inverse_closed_generators": [
      [
        25,
        1254
      ],
      [
        24,
        2125
      ],
      [
        18,
        541
      ],
      [
        31,
        3289
      ],
      [
        47,
        4642
      ],
      [
        2,
        1300
      ]
    ],
    "source_C_uses_left_multiplication": true,
    "right_Cayley_isomorphism": "inversion"
  },
  "three_endpoint_radius8_queries": [
    {
      "type": 0,
      "positive_generator": [
        25,
        1254
      ],
      "inverse_generator": [
        24,
        2125
      ],
      "deleted_edge": [
        0,
        170329
      ],
      "covered_old_count": 317299,
      "missing_old_count": 14088,
      "first_missing_label": 20,
      "first_missing_coordinates": [
        0,
        20
      ],
      "minimum_new_point_distance_to_missing": 10,
      "multi_source_depth8_histogram": [
        2,
        10,
        50,
        250,
        1250,
        6231,
        29687,
        114373,
        165446
      ],
      "expanded_vertices": 151853,
      "neighbor_darts_examined": 911118,
      "query_CPU_seconds": 0.008073
    },
    {
      "type": 1,
      "positive_generator": [
        18,
        541
      ],
      "inverse_generator": [
        31,
        3289
      ],
      "deleted_edge": [
        0,
        122275
      ],
      "covered_old_count": 317512,
      "missing_old_count": 13875,
      "first_missing_label": 6,
      "first_missing_coordinates": [
        0,
        6
      ],
      "minimum_new_point_distance_to_missing": 10,
      "multi_source_depth8_histogram": [
        2,
        10,
        50,
        250,
        1250,
        6233,
        29676,
        114342,
        165699
      ],
      "expanded_vertices": 151813,
      "neighbor_darts_examined": 910878,
      "query_CPU_seconds": 0.008
    },
    {
      "type": 2,
      "positive_generator": [
        47,
        4642
      ],
      "inverse_generator": [
        2,
        1300
      ],
      "deleted_edge": [
        0,
        322503
      ],
      "covered_old_count": 317359,
      "missing_old_count": 14028,
      "first_missing_label": 20,
      "first_missing_coordinates": [
        0,
        20
      ],
      "minimum_new_point_distance_to_missing": 10,
      "multi_source_depth8_histogram": [
        2,
        10,
        50,
        250,
        1250,
        6231,
        29686,
        114481,
        165399
      ],
      "expanded_vertices": 151960,
      "neighbor_darts_examined": 911760,
      "query_CPU_seconds": 0.008
    }
  ],
  "all_single_edges_covered_by_lefttranslations": true,
  "three_queries_are_not_random_samples": true,
  "newroot_distance_claim": "at least10, no unsupported exactdistance or route",
  "oldold_candidate_BFS": 0,
  "original_source_allroot_D9_BFS": 0,
  "field_source_validation": 0,
  "raw_graph_download_generation": 0,
  "prior_closed_scopes_inherited": [
    {
      "receipt": "research/ddp/more_graphs_20261027/d6_D9_current331387_source/field6959_all_embeddings/REPORT.md",
      "scope": "Only normalized phases1,36,45 and normals0,1,1512 over F6959, all42 order49 actions",
      "outcome": "34 thin-image rejects;8 target-radius9 failures;0hit"
    },
    {
      "receipt": "research/ddp/more_graphs_20261027/d6_D9_current331387_source/ramified6860_quotient_gate/REPORT.md",
      "scope": "Specified Z6860 semidirect-C49, all compatible actions and three inverse pairs",
      "outcome": "Forced abelian quotient obstruction; no graph generation needed"
    }
  ],
  "cumulative_charged_CPU_seconds": 0.827553591,
  "CPU_budget_seconds": 10,
  "prior_source_interface_charge": 0.22202574400000002,
  "preparation_and_failure_history_preserved": true,
  "no_timer_reset": true,
  "terminal": true
}
```

**既有原文指标：** Subdivision distance proof: writeH=G−{u,v}. Every simple newz-to-oldt path first takeszu orzv and thereafter stays inH, so d(z,t)=1+min(d_H(u,t),d_H(v,t)). Thus the two-sourceR8 miss gives d(z,t)>=10. Translation proof: for a right Cayley edge{g,gs}, lefttranslation by g^(-1) maps it to{1,s}. Ifs is an inverse generator, lefttranslation by the positive generator maps{1,s^(-1)} to{s,1}. Lefttranslation extends by mapping insertedz to the representative insertedz, so three positive types exhaustalloldedge subdivisions. Noedge-transitivity across the three pairs is assumed. Author left-Cayley and this right-Cayley model are related by the already-bound inversion isomorphism.



**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/run_once.py)；[research/ddp/more_graphs_20261027/d6_D9_current331387_source/AUTHOR_deg6_D9_CHK.c](../../research/ddp/more_graphs_20261027/d6_D9_current331387_source/AUTHOR_deg6_D9_CHK.c)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_D6_D10_primary_cache/desc_g9.html](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_D6_D10_primary_cache/desc_g9.html)；[research/ddp/more_graphs_20261027/d6_D9_current331387_source/field6959_all_embeddings/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D9_current331387_source/field6959_all_embeddings/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D9_current331387_source/ramified6860_quotient_gate/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D9_current331387_source/ramified6860_quotient_gate/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All single old-edge subdivisions of this fixed inverse-closed six-generator Cayley source; three types exhaust edges by left translations. Full-oldedge-preserving connected append also has no spare at cap6. No multi-edge subdivisions, old rewiring or all(6,9) exclusion.

**仍未完成：** General(6,9) and other edge-edit mechanisms remain open; no new graph or parameter.

**启发与重启依据：** STOP every single-edge subdivision of this fixed source. NewrootR9 pass would still not certify old-oldD9, but allthree types already fail. Do not repeat the sameedge at other labels or reopen priorF6959/ramified6860 closed families. Other grafts, multiple edited edges or a different source require genuinely changed premises; Moore余量不保证可实现。

**单独的重启条件：** Only an explicitly changed source/connection operation; no new timer, generator/field ladder or otheredge label for this closed single-subdivision rule.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- D6D9_THREECUT_STAR_TERMINAL_20261101 -->
## 2026-11-01 21:22:23 UTC 后续固定源纯星范围（原历史不改）

后续独立scope已关闭：固定actual331387源至多三distinct旧边删除（可共享端点）＋一点连接任意获释端点的纯star完整NO；不得据此扩大旧F6959或single范围。旧singleNo/F6959normalNo均未重跑，保留历史；详见新机制节点与FINAL_PROOF。

[新scope实验](./ddp-stale-d6d9-fixed331387-at-most-threecuts-pure-star-complete-no-20261101.md)；[完整纸面证明](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/threecut_star331388_gate/FINAL_PROOF.md)；[ROOT处置](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/threecut_star331388_gate/ROOT_DISPOSITION.json)。这一链接不重计旧结论为新成果。
