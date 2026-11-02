---
type: experiment
node_id: exp:ddp-f4-uniform-k4-regular-deck-single-f-controller-order60-bound-20261101
title: "Uniform K4×regular deck单F控制器：同index短群词迫使deck≤15、controller≤60"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/PRED.json; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/RESULT.json; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/PROOF.md; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/SYMBOLIC_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/REPORT.md; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/TERMINAL.json; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/symbolic_gate.py; research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/gate.cpp"
added: 2026-11-01T06:18:21Z
tags: ["ddp", "method-ledger"]
---

# Uniform K4×regular deck单F控制器：同index短群词迫使deck≤15、controller≤60

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (20,3)；L=不适用／见变体；条件性n=4096（未据此计纪录）

**距目标的证据：** No numeric controller or4096 fiber graph.3120 formal words counted only; actual327680 voltage assignments evaluated0, compiled binary never executed.；同index≤3步压缩群词在五P cycletypes各有root上界13/11/11/13/15，所以任regular deck group H若此uniformK4/singleF组织D3则|H|≤15、controller≤60；不需commutative。实际3120symbolicwords CPU0.002083549，原拟5×16^4=327680数值赋值实际0；binary仅compile未run，0fiber/solver/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_Lean_instances": 0,
  "new_independent_frameworks": 0,
  "controller_vertices_hypothetical": 64,
  "deck_order_hypothetical": 16,
  "uniform_permutation_types": 5,
  "formal_walks_enumerated": 3120,
  "chosen_type_root_upper_bounds": [
    13,
    11,
    11,
    13,
    15
  ],
  "regular_deck_order_upper": 15,
  "controller_order_upper": 60,
  "potential_numeric_assignments_covered_by_proof": 327680,
  "actual_numeric_assignments_enumerated": 0,
  "numeric_gate_compiled": true,
  "numeric_gate_executed": false,
  "fiber_graphs": 0,
  "solver_calls": 0,
  "Lean_calls": 0,
  "CPU_seconds": 0.002083549,
  "new_lower_bound_mathematically_verified": false
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/PRED.json](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/PRED.json)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/SYMBOLIC_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/SYMBOLIC_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/REPORT.md](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/REPORT.md)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/symbolic_gate.py](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/symbolic_gate.py)；[research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/gate.cpp](../../research/ddp/two_successful_methods_20261101/f4_controller64_K4_voltage/gate.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Controller(i,h) with each h a completeK4, external F(i,h)=(P(i),h*g_i) and actual inverse, P uniformS4 and four fixed regular deck group elements. All groups/assignments within this exact organization, not arbitrary64controllers or fiber mechanisms. For D3 deck order≤15; strict closure for order≥16.

**正向保证：** 三步内相邻internal步可压缩，F/F^-1反向连续步消去；自由群word计数不假设deck交换。；五P共轭类型覆盖任S4，cycle3类的固定indexroot仍仅13，不能借其另三个index的17覆盖逃掉。；从3120formal words到任何具体群同态评价只会碰撞、不会增加sameindex可达点，故无需数值327680枚举。

**仍未完成：** 非uniform external2factors、其他控制器组织、改fiber路线机制和一般4096图未排。没有新controller/fiber图或新Lean；并非枚尽所有16阶群/所有5正则图。

**启发与重启依据：** 原whole-ball64slot/voltage筛选在numeric运行前，被sameindex deck位移计数取代；K4内部三角词都不改变deck，不能弥补同index缺额。停止Z16/D8/其他群或modulus梯子及保留binary，不续unused枚举。下一若扩大控制器须改变uniform singleF组织，而非换群名字。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

