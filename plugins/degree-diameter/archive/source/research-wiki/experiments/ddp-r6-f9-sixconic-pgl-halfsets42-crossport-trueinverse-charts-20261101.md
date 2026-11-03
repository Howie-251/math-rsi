---
type: experiment
node_id: exp:ddp-r6-f9-sixconic-pgl-halfsets42-crossport-trueinverse-charts-20261101
title: "F9六conic端口：两互补轨道与42真逆chart完整局部接口"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PREDICTION.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PARAMETERS.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/PARAMETERS.json"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# F9六conic端口：两互补轨道与42真逆chart完整局部接口

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** local_finite_chart_conditions

**目标与阶数：** (54,3)；L=不适用／见变体

**距目标的证据：** GF9=GF3[w]/(w²+1)、六conic参数[∞,0,1,2,w,−w]、固定局部均匀port-line/nointrafiber三维机制；新增crossport复用PGL与12旧chart，不重算旧范围。；继承q=2r−3，r6给q9；720PGL2F9置换对252个5子集分72/180两轨，均补集不变；六固定conic ports的12self±chart/300turn PASS。新增30crosschart/750turn，合42实际chart/1050满秩turn，每chart10pencil rays覆盖729。self正矩阵全非involution，必须用真实inverse。局部CPU0.655405084+0.167296002；不计完整图。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "PGL_count": 720,
  "halfsets": 252,
  "orbit_sizes": [
    72,
    180
  ],
  "total_charts": 42,
  "fullrank_turns": 1050,
  "pencil_offsets": 729,
  "new_graphs": 0,
  "local_CPU": 0.822701086,
  "global_edge_coloring_required": false
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PREDICTION.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PREDICTION.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_f9_projective_halves/cross_port_extension/PARAMETERS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** GF9=GF3[w]/(w²+1)、六conic参数[∞,0,1,2,w,−w]、固定局部均匀port-line/nointrafiber三维机制；新增crossport复用PGL与12旧chart，不重算旧范围。

**正向保证：** p<q取canonical跨port、p>q取实际inverse，selfport按端点u<v选正负，支持任意port配对且不要求6边着色。；局部满秩与pencil对任意源坐标成立，不要求控制器闭路矩阵积恒等。

**仍未完成：** 局部charts本身不提供控制器A³全覆盖，也不计图或新下界；全r/q无例外族未声称。

**启发与重启依据：** 知道局部路线可同时实现后，把下一问题集中到有三角且A³positive控制器；最终只选实际8chart接Schreier78，停止盲调局部矩阵。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

