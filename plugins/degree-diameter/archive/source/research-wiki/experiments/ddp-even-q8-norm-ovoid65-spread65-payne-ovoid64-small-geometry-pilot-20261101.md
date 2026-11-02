---
type: experiment
node_id: exp:ddp-even-q8-norm-ovoid65-spread65-payne-ovoid64-small-geometry-pilot-20261101
title: "q8小几何已完整复现：真F8/F64、O65/spread65及Payne O64/spread64全部PASS，0大图"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PARAMETERS.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/MECHANISM_NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/pilot.cpp; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/run_once.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F8_FIELD_TABLE.csv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F64_FIELD_TABLE.csv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F64_TRACE_NORM.csv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PG3_POINTS.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/ORIGINAL_INCIDENCE.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/OVOID65.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SPREAD65.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_POINTS.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_LINES.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_INCIDENCE.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/OVOID64.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_SPREAD64.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/PROOF.md"
added: 2026-11-01T11:01:34Z
tags: ["ddp", "method-ledger"]
---

# q8小几何已完整复现：真F8/F64、O65/spread65及Payne O64/spread64全部PASS，0大图

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** local_finite_geometry_reproduction

**目标与阶数：** (?,3)；L=不适用／见变体；从属目标：[[81, 3], [80, 3]]

**距目标的证据：** 新field/小GQ几何及全部非incident projection接口；不构造完整opposite/fill源，不宣D3图或Lean实例。；2.285789276CPU/20预算，全新q8有限实验终态PASS。F8=F2[x]/(x³+x+1)、F64=F8[z]/(z²+z+1)是真域（非整数mod8/64）。原585PG点/585线全9度，336960非incident投影全唯一；65点ovoid的2080pair非零、每线恰一，65spread分割。Payne保512点，576旧线+64新H线共640线，线8点/点10线，全部322560非incident投影唯一，fullO64与spread64兼容。actualP pointid2/owner64；0完整sourcegraph/BFS/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "new_full_source_graphs": 0,
  "BFS_runs": 0,
  "Lean_runs": 0,
  "solver_runs": 0,
  "CPU_seconds": 2.285789276,
  "F8_modulus": "x^3+x+1",
  "F64_modulus": "z^2+z+1",
  "original_points": 585,
  "original_lines": 585,
  "original_line_and_point_degree": 9,
  "original_nonincident_projections": 336960,
  "original_ovoid_size": 65,
  "original_spread_size": 65,
  "Payne_points": 512,
  "Payne_lines": 640,
  "Payne_points_per_line": 8,
  "Payne_lines_per_point": 10,
  "Payne_nonincident_projections": 322560,
  "Payne_ovoid_size": 64,
  "Payne_spread_size": 64,
  "actual_P_point_id": 2,
  "infinity_spread_owner": 64,
  "known_geometry_reproduction_not_record": true,
  "conditional_source_D3_instantiated": true,
  "all_processes_terminal": true,
  "subsequent_filled_source_pair_id": "ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101",
  "subsequent_accepted_filled_graphs": 2,
  "geometry_scope_graphs_counted": 0
}
```



**从属变体：**
```json
[
  {
    "label": "balanced_q8_small_geometry",
    "target": [
      81,
      3
    ],
    "actual_source_graph": null,
    "conditional_unfilled_order": 342225,
    "conditional_fill_order": 342290,
    "full_O": 65,
    "spread": 65
  },
  {
    "label": "Payne_q8_small_geometry",
    "target": [
      80,
      3
    ],
    "actual_source_graph": null,
    "conditional_unfilled_order": 327680,
    "conditional_fill_order": 327744,
    "full_O": 64,
    "spread": 64
  }
]
```

**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/MECHANISM_NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/MECHANISM_NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/pilot.cpp](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/pilot.cpp)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/run_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/run_once.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F8_FIELD_TABLE.csv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F8_FIELD_TABLE.csv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F64_FIELD_TABLE.csv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F64_FIELD_TABLE.csv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F64_TRACE_NORM.csv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/F64_TRACE_NORM.csv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PG3_POINTS.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/PG3_POINTS.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/ORIGINAL_INCIDENCE.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/ORIGINAL_INCIDENCE.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/OVOID65.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/OVOID65.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SPREAD65.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SPREAD65.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_POINTS.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_POINTS.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_LINES.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_LINES.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_INCIDENCE.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_INCIDENCE.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/OVOID64.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/OVOID64.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_SPREAD64.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/DERIVED_SPREAD64.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/PROOF.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/PROOF.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一q8特征2小几何实例，域编码与原Gram/trace/极化/实际共线逐项绑定；是已知几何与fullO大小的复现，不声称新ovoid/newrecord。balanced源342290/81和Payne327744/80都只条件未来fill数量，未生产/验收。

**正向保证：** 具体预测B(X(u),X(v))=N(u+v)成立，N非零向量各向异性，X(a,b)=(1,a,b+N(a+bz),N(a+bz))及P=(0,0,1,1)给O65；2080pair和585line交点都实际检验，非仅计数代替。；F64斜率v=lambda*u与infinity给65spread；Tr(uv′+u′v)等于实际Gram，无额外坐标变换。；派生P使保留点x0=1；新H(a,b)={(1,a,b+t,t)}与范数图唯一交t=N(a+bz)，保住旧isotropic线覆盖并兼容64新增线。旧infinity删除后64spread仍partition512；不能只核原线忽略新线。

**仍未完成：** 本小几何pilot本身0完整图/Lean；后续两filled源327744/80、342290/81现已fresh字面/129helperBFS/全点对与prefix证明并由root接受，另在两实例sourcefill节点计账。q8具体Lean仍0、仅finitepilot；knowngeometry复现不新记录，sourcefill精确优先权UNKNOWN。

**启发与重启依据：** 实际范数恒等式和新H线交点解释为何特征2的完整O可兼容，而非继续q7 partialO局部调点。下一步继承这套已核数据，不再搜O/spread或重验field；任何完整源须root另行决定及核公开竞争门。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

