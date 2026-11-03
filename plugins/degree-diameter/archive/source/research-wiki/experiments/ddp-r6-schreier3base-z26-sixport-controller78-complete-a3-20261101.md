---
type: experiment
node_id: exp:ddp-r6-schreier3base-z26-sixport-controller78-complete-a3-20261101
title: "三base×Z26六端口Schreier78：三角＋全部三步控制覆盖命中后停止"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PARAMETERS.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/controller78.edges; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/CONTROLLER_ROUTE_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/THREE_PORT_WITNESSES.tsv"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# 三base×Z26六端口Schreier78：三角＋全部三步控制覆盖命中后停止

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (54,3)；L=55350；controller n=78

**距目标的证据：** 实际D=3，目标D=3；3base×Z26。a+base0自移2、base1→2+6、base2→1+17；a−真逆；b±沿base三cycle零shift；s交换0/1并±5且base2自移13；t交换0/2并±10且base1自移13。；实际简单6regular78点／234边，m26和参数(α0,α1,α2,σ,τ)=(2,6,17,5,10)，selfmatching shift13；inverseports[1,0,3,2,4,5]。234deck类见证逐译全部6084有序对PASS，其中216同层/非邻类均NB3、18相邻类交pencil；b三角覆盖每点。α0=1已穷尽375000、α0=2试85110即成功，共460110合法候选，0.752870034CPU含编译/导出/字面核对。控制器本身不计项目完整图。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "controller_order": 78,
  "controller_degree": 6,
  "edges": 234,
  "parameters": [
    2,
    6,
    17,
    5,
    10
  ],
  "all_A3_pairs": 6084,
  "tested_simple_candidates": 460110,
  "branch1_complete": true,
  "branch2_complete": false,
  "CPU": 0.752870034,
  "fiber_graph_counted_here": false,
  "full_graph_separate_node": "ddp-schreier78-f9-six-conic-affine-fullgraph-56862-d54-d3-20261101"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/controller78.edges](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/controller78.edges)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/CONTROLLER_ROUTE_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/CONTROLLER_ROUTE_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/THREE_PORT_WITNESSES.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/THREE_PORT_WITNESSES.tsv)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 3base×Z26。a+base0自移2、base1→2+6、base2→1+17；a−真逆；b±沿base三cycle零shift；s交换0/1并±5且base2自移13；t交换0/2并±10且base1自移13。

**正向保证：** 单位deck缩放把合法α0分gcd1/2两轨，可归一1或2；simple充要α0非0/13、其余四参数非零、α1+α2非零。；b³在每个deck产生三角，先修同层必要路线；第六匹配给新跨层路线。；所有controller三步词为实际字面关系，不把形式词或两stepR2混为三步支持。

**仍未完成：** 成功后α0=2剩余未扫，不称解唯一；控制器到fullF9图的合法性另由56862节点验收，具体Lean仍在途。

**启发与重启依据：** 此前局部charts成功而controller缺路；转熟悉三base、保强制三角并加第六匹配，在达到公开54门所需最小可用3m偶m26处命中；立即停搜索并展开唯一完整56862图。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

