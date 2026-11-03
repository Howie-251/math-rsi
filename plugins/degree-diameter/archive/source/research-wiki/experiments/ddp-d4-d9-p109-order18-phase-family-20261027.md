---
type: experiment
node_id: exp:ddp-d4-d9-p109-order18-phase-family-20261027
title: "(4,9)p109阶十八phase族：新285144完整无解，继承旧71286闭五轨道"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/REPORT.md; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/PREDICTION.json; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/FORMS_PREDICTION.json; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/RESULT.json; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/terminal.json; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/ISOMORPHISM.json; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/PROOF_SCOPE.md; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/search.cpp; research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/run.py"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# (4,9)p109阶十八phase族：新285144完整无解，继承旧71286闭五轨道

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-family-exhaustion

**目标与阶数：** (4,9)；L=7884；条件性n=11772（未据此计纪录）

**距目标的证据：** 新预测REFUTED。新285144+继承71286=356430规范设置闭五orbit；按对称证明覆盖15raw phasepairs的1069290参数，但后者不是显式测试或图数。全324slotfieldcover是接受标准，290049槽求值均在必要筛阶段完成。

**其他指标（保持原计数类型）：**
```json
{
  "E": [
    2,
    10,
    14,
    22,
    26,
    34
  ],
  "symmetry_units": [
    1,
    13,
    25
  ],
  "raw_unordered_phase_pairs": 15,
  "phase_pair_orbits": 5,
  "new_frame_reps": [
    [
      2,
      10
    ],
    [
      2,
      14
    ],
    [
      2,
      34
    ],
    [
      10,
      22
    ]
  ],
  "new_normalized_settings_evaluated": 285144,
  "inherited_orbit_rep": [
    2,
    22
  ],
  "inherited_old_actual_pair": [
    10,
    14
  ],
  "inherited_settings_not_recomputed": 71286,
  "all_normalized_orbit_settings_closed": 356430,
  "symmetry_covered_raw_parameter_domain": 1069290,
  "new_numeric_settings": 285144,
  "capacity_pruned_settings": 0,
  "slot_evaluations": 290049,
  "per_frame": [
    {
      "phase_pair": [
        2,
        10
      ],
      "settings": 71286,
      "slot_evaluations": 75617,
      "native_CPU_seconds": 0.162086
    },
    {
      "phase_pair": [
        2,
        14
      ],
      "settings": 71286,
      "slot_evaluations": 71464,
      "native_CPU_seconds": 0.11333
    },
    {
      "phase_pair": [
        2,
        34
      ],
      "settings": 71286,
      "slot_evaluations": 71286,
      "native_CPU_seconds": 0.081498
    },
    {
      "phase_pair": [
        10,
        22
      ],
      "settings": 71286,
      "slot_evaluations": 71682,
      "native_CPU_seconds": 0.122412
    }
  ],
  "full_survivors": 0,
  "unattempted": 0,
  "UNKNOWN": 0,
  "actual_graphs_generated": 0,
  "actual_graph_BFS": 0,
  "source_BFS": 0,
  "native_CPU_seconds": 0.47932600000000003,
  "compile_CPU_seconds": 1.047358471,
  "total_batch_CPU_seconds": 1.5362021279999998,
  "forms_generation_CPU_seconds": 2.174545,
  "input_generic_triples": 2457436,
  "input_slots": 7776,
  "baseline_date": "2026-10-27",
  "independent_method_count_added": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/FORMS_PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/FORMS_PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/RESULT.json](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/RESULT.json)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/terminal.json](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/terminal.json)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/ISOMORPHISM.json](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/ISOMORPHISM.json)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/PROOF_SCOPE.md](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/PROOF_SCOPE.md)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/search.cpp](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/search.cpp)；[research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/run.py](../../research/ddp/more_graphs_20261027/d4_D9_current7884_transfer/phase_order18_family/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定p109/M36/C=(1,6)/loop(0,3)，A/B phases为E={2,10,14,22,26,34}中不同无序pair；u1/13/25等价给5orbits。新4reps(2,10),(2,14),(2,34),(10,22)×6actions×109²=285144全数值处理；旧(2,22)orbit含(10,14)继承71286不重跑。0capacity-prune/未试/UNKNOWN/全槽survivor/实际图/BFS。

**仍未完成：** Otherprimes/M/C0/phaseorders andgeneral11772degree4diameter9graphs notexcluded.

**启发与重启依据：** 改变quotientphase落点仍不能在固定p109/order18电压阶/C1机制下同时覆盖；该完整phase族停止。不扩prime/M/C0/其他phaseorder或追坏对分数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

