---
type: experiment
node_id: exp:ddp-r7-f11-four-orbit-twofive-typed-true-inverse-tenchart-local-interface-20261101
title: "F11七port：两轨预测被推翻，132类2+5与10张真逆chart实际成立"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PARAMETERS.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/CHART_CHECKS.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/CONTROLLER_INTERFACE.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_MECHANISM_NOTE.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.py"
added: 2026-11-01T09:45:01Z
tags: ["ddp", "method-ledger"]
---

# F11七port：两轨预测被推翻，132类2+5与10张真逆chart实际成立

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (77,3)；L=不适用／见变体

**距目标的证据：** 有限PGL轨道、选定端口及10真逆chart；未造controller或完整图。；预测264+660两轨被实际110/220/264/330四轨推翻；792七子集132为(0,0,2,5)、660为(1,2,2,2)。只前132类给264×2+330×5；finalports=[1,4,inf,0,2,3,5]、pi=[1,0,3,2,4,5,6]。10真实逆chart的360个NBturn全rank3，各12plane相邻覆盖1331，含重标.131403188CPU。独立单chart反例.000518141CPU：归一PGL逆的quotient多6倍，(0,1,1)错误往返(0,6,6)，reverse noise不能修；producer真实逆无缺陷。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "full_graphs_generated": 0,
  "BFS_runs": 0,
  "Lean_compilations": 0,
  "six_orbit_sizes": [
    110,
    220,
    264,
    330
  ],
  "seven_profiles": [
    {
      "counts": [
        0,
        0,
        2,
        5
      ],
      "objects": 132
    },
    {
      "counts": [
        1,
        2,
        2,
        2
      ],
      "objects": 660
    }
  ],
  "final_ports": [
    1,
    4,
    "inf",
    0,
    2,
    3,
    5
  ],
  "reverse_ports": [
    1,
    0,
    3,
    2,
    4,
    5,
    6
  ],
  "charts_checked": 10,
  "NBturn_rank3_checks": 360,
  "planes_per_pencil": 12,
  "producer_CPU_seconds": 0.131403188,
  "independent_counterexample_CPU_seconds": 0.0005181409999999997,
  "two_orbits_prediction_refuted": true,
  "producer_inverse_defect_found": false,
  "all_processes_terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/CHART_CHECKS.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/CHART_CHECKS.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/CONTROLLER_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/CONTROLLER_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_MECHANISM_NOTE.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_MECHANISM_NOTE.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定F11/132-profile对象/finalpi；非任意七子集、sorted邻标、任意same-type配对或所有29chart验证。端口接口是两directed2factor加三perfectmatching。

**正向保证：** 实际1320个PGL置换、924六子集、792七子集；六子集四轨各自补集不变。；真实反向必须T^-1和noise=-t；PGL尺度等价不能替代字面线性逆。；已继承机制：中间chart的36秩条件覆盖NB三步，相邻12plane互补，同纤维靠controller三角；本次只实际检验F11接口，不当一般常识的新定理。

**仍未完成：** 局部PASS仍缺符合固定port的完整controller；0图/BFS/Lean，不计新构造。

**启发与重启依据：** 预测被推翻后实际改变生成规则：只选132类和固定真逆角色，弃任意sorted标号/PGL归一逆；随后先核公开竞争门再派有界controller实验。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

