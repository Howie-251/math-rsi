---
type: experiment
node_id: exp:ddp-r6-k4-double-voltage-z20-full-fixed-family-f9-lift-obstruction-20261101
title: "K4×Z20六shift固定全族：完整归一覆盖失败，F9 lift严格停止"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/PREDICTION.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/COMBINED_SCOPE.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/COMBINED_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/ACTUAL_LIFT_OBSTRUCTION.md"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# K4×Z20六shift固定全族：完整归一覆盖失败，F9 lift严格停止

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (54,3)；L=55350；controller n=80

**距目标的证据：** 4base×Z20，每个K4 baseedge恰zero和nonzeroshift两条匹配，六shift非零；包括unit及connectedunit-free参数。只闭该固定生成族与指定full-line/nointrafiberlift。；anchor1的19^5=2476099全失败；unit-free补域161051中243由不连通证明排、160808实际失败。合2636907归一赋值实测，并非逐枚全原始19^6=47045881；全族由base置换/单位归一及gcd连通性覆盖。1.652804399CPU，0fiber/BFS/solver/Lean。缺非邻NB3时至多6×81=486<729目标坐标，所以此固定控制器全族的full9line/nointrafiberF9³D3 lift不可能。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "controller_candidate_order": 80,
  "normalized_assignments_tested": 2636907,
  "disconnected_excluded_by_proof": 243,
  "raw_domain": 47045881,
  "all_raw_individually_enumerated": false,
  "fiber_graphs": 0,
  "total_CPU": 1.652804399
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/PREDICTION.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/PREDICTION.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/COMBINED_SCOPE.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/COMBINED_SCOPE.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/COMBINED_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/COMBINED_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/ACTUAL_LIFT_OBSTRUCTION.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_k4_c20_controller/ACTUAL_LIFT_OBSTRUCTION.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 4base×Z20，每个K4 baseedge恰zero和nonzeroshift两条匹配，六shift非零；包括unit及connectedunit-free参数。只闭该固定生成族与指定full-line/nointrafiberlift。

**正向保证：** connected iff gcd(六shift,20)=1；connectedunit-free必有5或15，归一anchor5/U覆盖补域。；缺非邻三步walk无法由两次crossing或chartoffset补齐729点，阻断是实际lift必要条件。

**仍未完成：** 一般80点6度控制器、改局部图、加intrafiber边、其他deckgroup未排。

**启发与重启依据：** 原anchor1负结果不足以排全族，先补精确unit-free归一范围；闭合后不换模数/seed续同类，转带三角的不同Schreier规则。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

