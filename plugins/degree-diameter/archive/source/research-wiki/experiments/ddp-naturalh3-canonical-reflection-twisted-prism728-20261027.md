---
type: experiment
node_id: exp:ddp-naturalh3-canonical-reflection-twisted-prism728-20261027
title: "NaturalH3 two-copy orthogonal-reflection prism728: solecanonicalcandidate has exactD6"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/REPORT.md; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/RECIPE.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/RESULT.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/ANALYSIS_RESULT.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/pi.txt; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/probe.cpp; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/run.py; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/native.log; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/terminal.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/RESULT.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/REFLECTION.json; research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/B2_PLANES.json; research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/source364.edges; research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/PORT_BINDING.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json; research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin"
added: 2026-10-27T22:32:03Z
tags: ["ddp", "method-ledger"]
---

# NaturalH3 two-copy orthogonal-reflection prism728: solecanonicalcandidate has exactD6

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=728

**距目标的证据：** 实际D=6，目标D=5；Actual728/1792/simple/undirected/max5,degree4:56/5:672. Solecandidate normal(0,0,1,0,0,0,1),Q1,has7portimages stillports/21full. Root0R5 misses78cross-sheetstates,first448=(1,84). Inheritedsame-sheetD5 andcross<=6 implyexactglobalD6. Noordinarybadpairmeasurement/newlowerbound.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 364,
  "source_m": 714,
  "source_degree_histogram": {
    "3": 28,
    "4": 336
  },
  "source_reported_D": 5,
  "actual_graph_n": 728,
  "actual_graph_m": 1792,
  "actual_graph_degree_histogram": {
    "4": 56,
    "5": 672
  },
  "source_coordinate_points": 364,
  "anisotropic_normals_structurally_screened": 729,
  "fixed_two_cell_normals_excluded": 378,
  "eligible_normals_after_filter": 351,
  "source_port_image_intersection": 7,
  "graph_candidates_tested": 1,
  "other_eligible_reflections_graph_untested": 350,
  "modified_graph_root_R5_BFS": 1,
  "failed_root": 0,
  "firstmissing_target": 448,
  "failed_root_cross_R5_missing": 78,
  "failed_root_layers": [
    1,
    5,
    19,
    71,
    204,
    350
  ],
  "actual_D6_scope": "OnecompleteactualrootR5lowerwitnessplusinheritedglobalupper6",
  "source_all_roots_BFS_repeated": 0,
  "ordinary_bad_pair_count_scope": "Notmeasured;78isone-rootcross-sheetstatecomplement",
  "native_CPU_seconds": 0.000362,
  "producer_total_parent_children_CPU_seconds": 0.6545230000000001,
  "geometry_selector_CPU_seconds": 0.117300399,
  "prediction": "REFUTED_FOR_ONE_SELECTED_REFLECTION",
  "UNKNOWN": 0,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/RECIPE.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/RECIPE.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/ANALYSIS_RESULT.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/pi.txt](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/pi.txt)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/probe.cpp](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/probe.cpp)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/run.py](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/run.py)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/native.log](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/native.log)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/terminal.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/terminal.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/REFLECTION.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/REFLECTION.json)；[research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/B2_PLANES.json](../../research/ddp/more_graphs_20261027/d5_D5_h3_twisted_prism728/geometry_selector/B2_PLANES.json)；[research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/source364.edges](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/source364.edges)；[research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/PORT_BINDING.json](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/PORT_BINDING.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json)；[research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin](../../research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Two complete copies of actualnaturalH3 source364/714 plus one inter-sheetmatching from a single canonicalQ6F3 orthogonalreflection. Selector structurally inspects729normals, rejectsfixed-two-port-cellobstructions, then minimizesspareoverlap andlexnormal beforegraphwork. Exactlyone728graph constructed andoneactualrootR5 traversed; nootherreflectiongraph/seed/matching.

**仍未完成：** OtheradmissibleQ1reflections andgeneral5D5graphs are notexcluded. Geometryfilter excludes378Q2reflection candidates bythefixed-celllemma;351remainstructurallyeligible,onlyonegraphwastried. No arbitrarypermutations/extra matchinglayer examined.

**启发与重启依据：** An actualorthogonalreflection outside sourceAut and moving21of28ports is insufficient torepairallcross-sheetD5 routes. Completegraphtraversal mustallow3/5matchingcrossings. Stop thiscanonicalcandidate; anyrestartrequiresanewstructuralruleandexplicitfiniteauthorization, not selectingmorepi bybadpairscore.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

