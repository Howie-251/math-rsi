---
type: experiment
node_id: exp:ddp-rajiv252-fullneighborhood-clone253-criticaledges-20261028
title: "Rajiv252 clone-and-cut253: all630 edges critical, unchanged-star full-clone family excluded"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/REPORT.md; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/MODEL_SCOPE.md; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/PREDICTION.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/RESULT.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/INPUT.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/CRITICAL_WITNESSES.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ROOT_COUNTS.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/NONZERO_ROUTE_INTERSECTIONS.jsonl; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/NEIGHBORHOOD_NONCRITICAL_GATE.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/criticality.py; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/run.py; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/checkpoint.json; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/terminal.json; research/ddp/second_mechanism/rajiv252.edges; research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md; research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ANALYSIS_CLONE_FOLD.md; research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ANALYSIS_CLONE_FOLD.json"
added: 2026-10-28T02:09:14Z
tags: ["ddp", "method-ledger"]
---

# Rajiv252 clone-and-cut253: all630 edges critical, unchanged-star full-clone family excluded

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (5,4)；L=252；条件性n=253（未据此计纪录）

**距目标的证据：** All630edges critical;0noncritical/0eligible prototypes. Exact252x426=107352 NB<=4 route prefixes,40110 ordered endpoint intersections nonempty, firstpair witness for everyedge. No candidate graph, BFS or cutset enumeration.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 252,
  "source_m": 630,
  "source_regular_degree": 5,
  "source_D_inherited": 4,
  "hypothetical_target_n": 253,
  "actual_target_n": null,
  "actual_target_D": null,
  "roots_route_enumerated": 252,
  "NB_prefixes_per_root": 426,
  "NB_prefixes_total": 107352,
  "ordered_nonzero_endpoint_intersections": 40110,
  "critical_edges": 630,
  "noncritical_edges": 0,
  "eligible_prototypes_under_necessary_gate": 0,
  "BFS": 0,
  "new_graphs": 0,
  "cut_set_searches": 0,
  "allroot_source_distance_reaudit": 0,
  "new_lower_bounds": 0,
  "worker_CPU_seconds": 0.289197,
  "driver_CPU_seconds": 0.0005100769999999977,
  "compile_CPU_seconds": 0,
  "workers": 1,
  "independent_construction_scope_paper_review": "VALID;no numerical rerun"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/REPORT.md](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/REPORT.md)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/MODEL_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/MODEL_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/RESULT.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/RESULT.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/INPUT.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/INPUT.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/CRITICAL_WITNESSES.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/CRITICAL_WITNESSES.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ROOT_COUNTS.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ROOT_COUNTS.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/NONZERO_ROUTE_INTERSECTIONS.jsonl](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/NONZERO_ROUTE_INTERSECTIONS.jsonl)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/NEIGHBORHOOD_NONCRITICAL_GATE.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/NEIGHBORHOOD_NONCRITICAL_GATE.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/criticality.py](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/criticality.py)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/run.py](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/run.py)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/checkpoint.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/checkpoint.json)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/terminal.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/terminal.json)；[research/ddp/second_mechanism/rajiv252.edges](../../research/ddp/second_mechanism/rajiv252.edges)；[research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md](../../research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md)；[research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md](../../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ANALYSIS_CLONE_FOLD.md](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ANALYSIS_CLONE_FOLD.md)；[research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ANALYSIS_CLONE_FOLD.json](../../research/ddp/more_graphs_20261027/small_d5_D4_rajiv252_free_neighborhood_clone253/ANALYSIS_CLONE_FOLD.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed original252/630/5regular/D4 source. Delete any F avoiding the complete star of prototype x and meeting every neighbor of x, then add one clone adjacent to the entire unchanged five-element neighborhood. All prototypes and all such F are excluded by the all-edge criticality and clone-fold proof. Not arbitrary253graphs or other source modifications.

**仍未完成：** General253-point graphs, changes to the prototype star, non-full-neighborhood new vertices, other old-edge surgery and the general(5,4) problem are unexcluded.

**启发与重启依据：** Full-neighborhood cloning preserves old-pair distances exactly under its fold to the retained prototype. Therefore it cannot repair deletion of any critical oldedge. This complete fixed-source rule stops; later work needs a genuinely different route-changing surgery or a source with usable slack, rather than more clone/cut combinations.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

