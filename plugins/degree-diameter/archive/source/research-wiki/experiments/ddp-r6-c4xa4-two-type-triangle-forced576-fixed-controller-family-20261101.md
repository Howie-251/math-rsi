---
type: experiment
node_id: exp:ddp-r6-c4xa4-two-type-triangle-forced576-fixed-controller-family-20261101
title: "C4×A4双类型三角强制控制器：固定576参数全失败"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/RESULT.json"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# C4×A4双类型三角强制控制器：固定576参数全失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (54,3)；L=55350；controller n=96

**距目标的证据：** 固定S3+1+1cosets，a=(0,doubletransposition)、b=(2,V4)与指定crossS形式的576参数；不是全部96controller或全部groupvoltage。；2types×C4×A4的96点6度固定coset模型，所有576参数全检，所有点有三角但两代表root三步目标最多170/192、最少仍缺22。实际literalports/432walks与groupformula逐项交叉一致。0.21893895CPU，0fiber/BFS/solver/Lean；不能把有三角当成全A³覆盖。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "tested": 576,
  "untested": 0,
  "controller_candidate_order": 96,
  "min_two_root_missing_threewalk_targets": 22,
  "fiber_graphs": 0,
  "CPU": 0.21893895
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_triangle_c4a4_controller/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定S3+1+1cosets，a=(0,doubletransposition)、b=(2,V4)与指定crossS形式的576参数；不是全部96controller或全部groupvoltage。

**仍未完成：** 其他coset形状／96点控制器仍开放，未测完整fiber图直径。

**启发与重启依据：** 同层三角必要障碍修好仍不足，具体缺的是跨层三步路线；停止本固定576参数，不靠总缺项更少继续调。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

