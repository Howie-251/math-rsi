---
type: experiment
node_id: exp:ddp-f9-c78-all-controller-open-neighborhood-packing-exact10-20261101
title: "固定C78全部controller openN packing精确max10：单次完整BB／646nodes"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SUMMARY.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SEARCH_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/search.cpp; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/controller_input.h; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/run_once.py; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SELECTED_OPEN_NEIGHBORHOODS.tsv; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PAIR_INTERSECTION_CERTIFICATE.tsv"
added: 2026-11-01T09:14:02Z
tags: ["ddp", "method-ledger"]
---

# 固定C78全部controller openN packing精确max10：单次完整BB／646nodes

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (?,3)；L=不适用／见变体

**距目标的证据：** 仅当前固定78×6controller的完整open-neighborhood packing；通过逐468tableentry核实际逐base配方。对应每selectedfiber放完整81点Wplane的矩形模型；不是点级/nonrectangular pinpacking、其他controller/field或全degree-diameter上界。；纸面容量先≤12（13个6-neighbor分割会使13中心诱导1regular，奇偶矛盾）；实际对唯一C78的N交空compatibilitygraph做一次完整maxclique B&B，646nodes、644boundprunes、全树终态，lower=upper=10、非timeout。U=[31,32,44,45,59,60,61,72,73,74]、60target vertices、45pair intersections0，诱导5K2，允许相邻selectedcenters。总.757685026CPU含compile/prep/wholeBB，search.001823CPU，0fiber/大图读/BFS/solver/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "controller_order": 78,
  "exact_optimum": 10,
  "lower_bound": 10,
  "upper_bound": 10,
  "initial_paper_upper": 12,
  "selected_U": [
    31,
    32,
    44,
    45,
    59,
    60,
    61,
    72,
    73,
    74
  ],
  "distinct_target_count": 60,
  "selected_induced_graph": "5K2",
  "nodes": 646,
  "bound_prunes": 644,
  "whole_exact_BB_calls": 1,
  "whole_tree_exhausted": true,
  "timeout": false,
  "total_CPU": 0.757685026,
  "search_CPU": 0.001823,
  "other_controllers_searched": 0,
  "full_graphs_BFS_Lean": 0
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SUMMARY.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SUMMARY.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SEARCH_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SEARCH_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/search.cpp](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/search.cpp)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/controller_input.h](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/controller_input.h)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/run_once.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/run_once.py)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SELECTED_OPEN_NEIGHBORHOODS.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/SELECTED_OPEN_NEIGHBORHOODS.tsv)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PAIR_INTERSECTION_CERTIFICATE.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/controller_open_n_packing/PAIR_INTERSECTION_CERTIFICATE.tsv)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅当前固定78×6controller的完整open-neighborhood packing；通过逐468tableentry核实际逐base配方。对应每selectedfiber放完整81点Wplane的矩形模型；不是点级/nonrectangular pinpacking、其他controller/field或全degree-diameter上界。

**正向保证：** compatibility clique精确等价原controller openN两两不交，不是independentset；selectedgraph实为5K2。；greedy propercolor按prefix给合法clique upperbound，整棵改进树耗尽，不把heuristic估值或纸面12当精确10。；810plane中心对60targetfibers的满N可以承接既有plane/clone接口；仍需后续完整字面图与fresh验收才能计成果。

**仍未完成：** 此节点未生成完整fiber/clone图或Lean；不排点级nonrectangular/partialplanes。m34旧域未重跑。

**启发与重启依据：** base0max7只是受限域，保留既有源并放宽到所有78controller vertices后，一次whole exactBB得真正max10；根据确定U10而非坏对下降，下一只算明确publicpositive窗口，不任意扩degree清单。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

