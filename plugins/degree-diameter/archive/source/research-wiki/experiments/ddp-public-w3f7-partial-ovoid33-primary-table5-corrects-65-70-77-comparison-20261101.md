---
type: experiment
node_id: exp:ddp-public-w3f7-partial-ovoid33-primary-table5-corrects-65-70-77-comparison-20261101
title: "公开W(3,7)33点计算例纠正65／70／77比较：161650／169900／181450"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png; research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/ACTUAL_POINTS.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/INTERFACE_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/INTERFACE_NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/PROOF.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md"
added: 2026-11-01T16:56:30Z
tags: ["ddp", "method-ledger"]
---

# 公开W(3,7)33点计算例纠正65／70／77比较：161650／169900／181450

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (?,3)；L=不适用／见变体

**距目标的证据：** 文献存在性与旧已核复制接口的有限标量推论，0controller/完整图/BFS/Lean。；实际原PDF p131定义W(q)=symplectic W(3,q)，p140 §4.3 Table5 W(7)行33点/1等价类，作者报告穷尽计算，非upper43/Q4partialovoid。公开160000/64源×50spread，一般§7复制推161650/65、169900/70、181450/77；本地161150/166650差−500/−3250，条件175692差−5758。 最新来源澄清：这些D3比较值是本项目代入／组合已发表方法得到的构造保证；未定位对应具体数字的作者独立边表，不是全球最大值认证。公式、primary URL、原文位置及适用条件见31参数来源索引。 65/70比较161650/169900来自160000+1650(Δ−64)：2007扫描p140实际partialovoid33×spread50，公开opposite源与Delorme一般§7复制组合；不是2007论文直接列D3点数或找到对应数字edgefile。旧161150/166650确低于此保证；当前最好161700/169950各多50。opposite公式依现代primary对缺失JGT原文的明确复述，不能说本项目已读JGT全文；filled160050归属仍UNKNOWN。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "primary_partial_ovoid_lower_bound": 33,
  "published_computational_maximum_claim": 33,
  "inequivalent_maximum_objects": 1,
  "current_public_guarantees": {
    "65,3": 161650,
    "70,3": 169900,
    "77,3": 181450
  },
  "local_differences": {
    "65,3": -500,
    "70,3": -3250,
    "77,3_conditional": -5758
  },
  "known_publicly_dominated_total": 43,
  "known_publicly_dominated_saved_table_overlap": 40,
  "pending_outside_saved_table_graphs": 27,
  "pending_outside_saved_table_pairs": 22,
  "named_legal_total": 133,
  "legal_pairs": 26,
  "phase_graphs": 29,
  "phase_pairs": 23,
  "complete_Lean_total": 19,
  "certified_global_records": 0,
  "primary_query_batches": 1,
  "queries": 3,
  "scalar_CPU_seconds": 7.233999999998325e-06,
  "coordinate_reproduction_status": "ACTUAL_REPRODUCED33_AND_FRESH_FILLED_SOURCE_FULLN_INTERFACE_PASS",
  "new_full_graphs": 0,
  "large_BFS_Lean_solver_runs": 0,
  "coordinate_reproduction_CPU_seconds": 1.185446749,
  "interface_CPU_seconds": 0.071535943,
  "reproduction_counted_as_new_record": false,
  "subsequent_accepted_family_id": "ddp-gq77-published-p33-immutable-fulln64-clone-eight-degree65-72-family-20261101",
  "subsequent_accepted_graphs": 8,
  "D3_comparison_evidence_identity": {
    "evidence_kind": "PROJECT_SUBSTITUTION_OR_COMBINATION_OF_PUBLISHED_METHODS",
    "numeric_author_edgefile_located": false,
    "global_maximum_established": false,
    "source_index": "research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json",
    "source_trace": "research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md",
    "mathematical_validity_and_existing_counts_unchanged": true
  },
  "P33_public_guarantee_source_identity": {
    "formula": "160000+1650*(Delta-64)",
    "range": [
      65,
      79
    ],
    "ingredients": [
      "CimrakovaFack2007p140Table5_W3F7partialO33",
      "publishedW3F7spread50",
      "publishedoppositeGQsource160000max64",
      "DelormeEJC1985general§7inducedsubgraphreplication"
    ],
    "primary_urls": [
      "https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf#page=12",
      "https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf",
      "https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2"
    ],
    "numbers_are_project_combinations_not_paper_printed_D3_orders": true,
    "numeric_author_edgefile_located": false,
    "global_maximum_established": false,
    "old_local65_70": [
      161150,
      166650
    ],
    "guarantee65_70": [
      161650,
      169900
    ],
    "current_best_local65_70": [
      161700,
      169950
    ],
    "current_margin": [
      50,
      50
    ],
    "filled160050_priority": "UNKNOWN_ifsamepublicsourceandinterfaceexists_gain0"
  }
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/ACTUAL_POINTS.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/ACTUAL_POINTS.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/INTERFACE_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/INTERFACE_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/INTERFACE_NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/INTERFACE_NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/PROOF.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/PROOF.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 当前primary可核W(3,7)33计算下界，未复跑作者最大团计算或取到坐标；直接组合已发表机制而非独立公开数值图或全球维护表。旧图合法、Lean及A/B/C全部保持，全球纪录认证0。

**正向保证：** 一次3query后沿明确primary引用打开出版社原始扫描PDF并实际视觉读表；不是从Ceria通用15/upper43推测。；Q(4,7)48点ovoid对偶成W(3,7)partialspread，不能错代；Wpartialovoid才对应Qpartialspread。；一般复制保留matching连接；不把本项目160050/O22当公开。

**仍未完成：** 公开33大小现已实际复现：原400点标签下33坐标、528新pair非零，fresh1650N64接口PASS。此复现本身不记图/新纪录；其filled160050上的k1..8八完整图已fresh独验并由root接受，单独family记8实例，具体Lean/新外审未结。公开推论及旧O22两图支配状态保留，全球/优先权未认证。

**启发与重启依据：** 25阈值检验发现33，使旧65/70竞争状态立即改为已被公开推论超过，并停止m33纪录目的续批。下一步从明确公开33原对象出发做坐标/接口复现；复现与新完整构造分账，不为文档同步计成果。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

