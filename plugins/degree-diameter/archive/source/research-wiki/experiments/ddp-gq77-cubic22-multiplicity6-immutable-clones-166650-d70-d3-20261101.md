---
type: experiment
node_id: exp:ddp-gq77-cubic22-multiplicity6-immutable-clones-166650-d70-d3-20261101
title: "166650/70/D3完整合法／Lean与A/B/C保留；公开33点推论169900已超过3250"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PRED.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PARAMETERS.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PROOF.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/graph_d70_D3_n166650.edges; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/independent_acceptance/SUMMARY.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/independent_acceptance/PLAIN_PROOF.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/formalization/FINAL_COMPILE_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/formalization/CHECKPOINT_C.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md; research/ddp/two_successful_methods_20261101/reviews/GQ166650_A_DISPOSITION.md; research/ddp/two_successful_methods_20261101/reviews/GQ166650_B_DISPOSITION.md; research/ddp/two_successful_methods_20261101/reviews/GQ166650_FINAL_C_DISPOSITION.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png"
added: 2026-11-01T09:53:51Z
tags: ["ddp", "method-ledger"]
---

# 166650/70/D3完整合法／Lean与A/B/C保留；公开33点推论169900已超过3250

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (70,3)；L=169900；candidate_graph_or_family n=166650

**距目标的证据：** 实际D=3，目标D=3；固定已接受原160050/64regular源，不是161150当前源；center k用k=1100*copy+50*i+j，copy∈Fin6，i∈Fin22,j∈Fin50。每个新点仅连原source N(center)，源诱导边完全保留。；【当前公开比较更正】Cimráková–Fack2007 §4.3/Table5实际W(7)33点，经既有一般Delorme复制给169900，本图低3250；旧15点比较只历史。本图全部合法性、独验、具体Lean/Audit与A/B/freshC仍实际完成，未重验。166650点／5544000边；保全部原5121600边，6600克隆各接不可变原N64，422400新边、0新新边。oldload0:89650/6:70400；degree64:96250/70:70400。全部6600新根literalBFS覆盖终图、0旧根；预测132根(1,64,3191,163394)、6468根(1,64,3254,163331)逐根符合。fresh独验总26.343279409CPU；4新Lean模块及独立Audit共9.113210473CPU，闭card166650/maxdegree≤70/真实WalkD3/非D2、无证书前提/std3。新scope A/B/distinct fresh C均实际SUCCESS/PASS。

**其他指标（保持原计数类型）：**
```json
{
  "validated_graph_instances": [
    {
      "Delta": 70,
      "D": 3,
      "n": 166650,
      "m": 5544000,
      "actual_diameter": 3,
      "mathematically_validated_complete_graph": true,
      "complete_Lean_graph_instance": true,
      "known_nonrecord": true,
      "latest_global_record_confirmed": false,
      "confirmed_publictable_improvement": false,
      "best_located_public_lower_bound": 169900,
      "formal_scope": "Unconditional concrete deterministic formula on original160050 source⊕Fin6600; maxdegree≤70/actualWalkD3/nonD2,std3; exactdegree and ASCII binding external.",
      "known_publicly_dominated": true,
      "public_comparison_status": "KNOWN_PUBLIC_METHOD_DERIVATION_DOMINATED",
      "bounded_gain": -3250
    }
  ],
  "mathematically_validated_complete_graph": true,
  "new_lower_bound_mathematically_verified": false,
  "new_named_complete_graphs": 1,
  "new_Lean_instances": 1,
  "source_order": 160050,
  "source_degree": 64,
  "copies": 6,
  "base_centers": 1100,
  "source_neighborhoods_immutable": true,
  "new_new_edges": 0,
  "new_root_BFS": 6600,
  "old_root_BFS": 0,
  "independent_CPU": 26.343279409,
  "concrete_Lean_CPU": 9.113210472999999,
  "reviews_A_B_distinct_C": "ALL_ACTUAL_SUCCESS_PASS",
  "review_prose_corrections": "A tightMoore4901 vs loose4971; C source160000 is400points×400lines, notline-spreadpairs; actualgraph/proofunchanged",
  "historical_public_comparison_before_primary33": {
    "public_guarantee": 164500,
    "baseline_date": "2026-11-01 bounded best-located primary-source comparison; not latest-global certification",
    "candidate_gain": 2150,
    "status": "superseded by actually read 2007 Table5 W(7)33, not a graph failure"
  },
  "known_publicly_dominated": true,
  "known_publicly_dominated_example_orders": [
    166650
  ],
  "current_public_guarantee": 169900,
  "current_candidate_minus_public": -3250,
  "public_comparison_status": "KNOWN_DOMINATED_BY_DIRECT_PUBLISHED_METHOD_COMPOSITION_NOT_GLOBAL_NUMERIC_TABLE",
  "public33_source_report": "research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md",
  "source_credit": "Current comparator uses published Cimrakova-Fack2007 W(7)33, not only Tallini15; no local unpublished source used as public."
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PRED.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PRED.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PROOF.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/PROOF.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/graph_d70_D3_n166650.edges](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/graph_d70_D3_n166650.edges)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/independent_acceptance/SUMMARY.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/independent_acceptance/SUMMARY.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/independent_acceptance/PLAIN_PROOF.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/independent_acceptance/PLAIN_PROOF.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/formalization/FINAL_COMPILE_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/formalization/FINAL_COMPILE_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/formalization/CHECKPOINT_C.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/cubic22_multiplicity70/formalization/CHECKPOINT_C.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md)；[research/ddp/two_successful_methods_20261101/reviews/GQ166650_A_DISPOSITION.md](../../research/ddp/two_successful_methods_20261101/reviews/GQ166650_A_DISPOSITION.md)；[research/ddp/two_successful_methods_20261101/reviews/GQ166650_B_DISPOSITION.md](../../research/ddp/two_successful_methods_20261101/reviews/GQ166650_B_DISPOSITION.md)；[research/ddp/two_successful_methods_20261101/reviews/GQ166650_FINAL_C_DISPOSITION.md](../../research/ddp/two_successful_methods_20261101/reviews/GQ166650_FINAL_C_DISPOSITION.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定已接受原160050/64regular源，不是161150当前源；center k用k=1100*copy+50*i+j，copy∈Fin6，i∈Fin22,j∈Fin50。每个新点仅连原source N(center)，源诱导边完全保留。

**正向保证：** base完整邻域两两不交给load≤1；新索引投影到copy∈Fin6的注入给load≤6，不要求centers独立或重复center注入。；同center两新点经任一旧邻居两步，adjacentcenters经两旧center三步，其他点对继承源短walk；路线不使用未来clones，所有prefix均D3。；完整字面旧体／全部6600N绑定和实际BFS独立验收；具体Lean与外部ASCII绑定分账。

**仍未完成：** 数学图／具体Lean／A/B/freshC完成；当前已知被公开已发表前提推论169900超过3250，旧+2150仅历史。O22规则来源／优先权及全球图最优未认证，不影响合法性。

**启发与重启依据：** 此前samecap65 currentfullN无可行center，不据此否定提高cap。改为原源的immutable N每组重复6，预测load6与两类BFS均支持；完成唯一degree70参数后停止，不自动开degree梯子。 当前primary33检验使竞争判断改变；不再以旧15点基线维持优越性。root另派公开33对象复现与filled160050邻域接口研究；未生产/计新图，不续m33竞争批次。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

