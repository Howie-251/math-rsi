---
type: experiment
node_id: exp:ddp-f9-c78-base0-complete-plane-open-neighborhood-packing-max7-20261101
title: "给定U7达base0完整plane上界7：局部证明／有限接口，未生成U7大图"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PARAMETERS.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/precheck.py"
added: 2026-11-01T09:14:02Z
tags: ["ddp", "method-ledger"]
---

# 给定U7达base0完整plane上界7：局部证明／有限接口，未生成U7大图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (56,3)；L=不适用／见变体

**距目标的证据：** 固定C78controller的base0(26个标签)、每selectedfiber完整81点既有Wplane、要求controller openN不交；仅此restricted model，不是全78controller packing或点级nonrectangular上界。；给定U7=[0,1,7,9,15,18,24]，42controller targets、567plane中心、30618不同pins有限PASS；其他U搜索0。base0碰撞当且仅当差±4/±5/±10；乘5逆变±1/±2/±6，8点cyclic gaps必有相邻3+3，纸面排8、给定7达界。325pair谓词与36gapexcess小核对，.145009067CPU。cap57此局部规则至多58563<公开58596，差33，停止base0规则；0完整graph/BFS/solver/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "base0_exact_maximum": 7,
  "U7": [
    0,
    1,
    7,
    9,
    15,
    18,
    24
  ],
  "controller_targets": 42,
  "plane_centers": 567,
  "distinct_pins": 30618,
  "conditional_U7_double56_order": 57996,
  "conditional_U7_graph_generated": false,
  "cap57_same_rule_upper": 58563,
  "cap57_public_guarantee": 58596,
  "CPU": 0.145009067,
  "large_graph_BFS_solver_Lean": 0
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/precheck.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/packing7_interface/precheck.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定C78controller的base0(26个标签)、每selectedfiber完整81点既有Wplane、要求controller openN不交；仅此restricted model，不是全78controller packing或点级nonrectangular上界。

**正向保证：** U7的samechart profile与旧controller0一致，已有55plane逆映射可继承；不重跑旧field/大图。；base0exactmax7是几何cyclicgap证明加给定witness，不将325pair或36patterns说成其他U的全域搜索。

**仍未完成：** U7条件57996/56图未生成／不计图；全controller上界由后续exact10另节点处理，非矩形pin集未排。

**启发与重启依据：** base0max7到57度仅差33仍不足，不凭小坏对数续同规则；转同一已成功C78的全部78fiber packing问题，检验能否突破受限base0瓶颈。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

