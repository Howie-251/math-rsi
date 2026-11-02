---
type: experiment
node_id: exp:ddp-c60-plus18-clique-helpers-sixregular-controller-exact-cnf-unknown-20261101
title: "保C60加18 clique helpers：完整精确CNF两批UNKNOWN，模型保持开放"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/MODEL_REVIEW.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/MODEL_REVIEW.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/TERMINAL.json"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# 保C60加18 clique helpers：完整精确CNF两批UNKNOWN，模型保持开放

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (54,3)；L=55350

**距目标的证据：** 固定既有Bhakar C60旧诱导图、指定H=2K3+3K4、给定pin分组大小及exactA³覆盖CNF；保持原CNF/UNKNOWN与独立新refinement路径，不第三timer。；保5regularC60，18helper H=2K3+3K4；6组4pins+12组3pins分割全部60old，目标6regular78controller。44460vars/145047clauses首批UNKNOWN，scope59.218355CPU。新必要密度规则：3pin独立且N并≥14，34220triples中19260合格；新增1800binary+82080triple条款，228927clauses第二批UNKNOWN，scope26.079808CPU。合85.298162706<90，所有进程终态；无controller/fiber，非UNSAT。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "controller_target_order": 78,
  "conditional_full_graph_order": 56862,
  "solver_calls": 2,
  "solver_results": [
    "UNKNOWN",
    "UNKNOWN"
  ],
  "total_CPU": 85.298162706,
  "third_timer": false,
  "controller_generated": false,
  "fiber_graph_generated": false
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/MODEL_REVIEW.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/MODEL_REVIEW.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/MODEL_REVIEW.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/MODEL_REVIEW.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/c60_helper78_controller/density_refinement/TERMINAL.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定既有Bhakar C60旧诱导图、指定H=2K3+3K4、给定pin分组大小及exactA³覆盖CNF；保持原CNF/UNKNOWN与独立新refinement路径，不第三timer。

**正向保证：** 3pin的15oldedge incidences需覆盖14外clique颜色，至多1次重复，故独立/N并≥14为必要密度cut；MODEL_REVIEW确认精确需求。

**仍未完成：** 两UNKNOWN没有排除固定模型或一般78controller；0目标图／0新lowerbound。

**启发与重启依据：** 反馈给出具体重复预算才能授权一次不同条款refinement；再次UNKNOWN后停止同模型计算。改有三角Schreier生成规则得到78成功，不能反称此CNF无解。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

