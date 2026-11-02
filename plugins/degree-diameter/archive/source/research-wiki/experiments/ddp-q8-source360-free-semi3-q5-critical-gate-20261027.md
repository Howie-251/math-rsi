---
type: experiment
node_id: exp:ddp-q8-source360-free-semi3-q5-critical-gate-20261027
title: "Q8五底点q5仅放开semi3 normal：29路线仍22形式，25个w全失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/REPORT.md; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/PREDICTION.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/FORMAL_ENDPOINTS.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/EVALUATIONS.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/RESULT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/terminal.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/run.py; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/RAW_ANALYSIS_FIELDS.json"
added: 2026-10-27T23:23:55Z
tags: ["ddp", "method-ledger"]
---

# Q8五底点q5仅放开semi3 normal：29路线仍22形式，25个w全失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** necessary-route-coverage-gate

**目标与阶数：** (3,9)；L=600；条件性n=1000（未据此计纪录）

**距目标的证据：** No graph generated or BFS; exactcritical-slot necessaryendpoint calculations only.；事前至少一w满25预测REFUTED。关键29routes只22不同8integercoeffs，形式容量已<25；固定矩阵全25w image最大17、passer0。0图/BFS/solver，无UNKNOWN/未试。

**其他指标（保持原计数类型）：**
```json
{
  "source_known_n": 360,
  "source_known_D": 8,
  "all_NB_D9_prefixes": 1534,
  "critical_raw_paths": 29,
  "distinct_free_module_coefficients": 22,
  "fixed_rep_w_evaluations": 25,
  "max_critical_image": 17,
  "passer_count": 0,
  "new_graphs": 0,
  "source_BFS": 0,
  "candidate_BFS": 0,
  "solver": 0,
  "CPU_seconds": 0.010288600000000002,
  "old_evidence_overwritten": false,
  "baseline_date": "2026-10-27",
  "source_credit": "JianxiangChen(3,8)360; NishantBhakar fivebaseF3²⋊Q8 voltage description; this worker performs only the one-free-semi-normal necessarygate."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/REPORT.md](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/REPORT.md)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/PREDICTION.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/PREDICTION.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/FORMAL_ENDPOINTS.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/FORMAL_ENDPOINTS.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/EVALUATIONS.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/EVALUATIONS.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/RESULT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/RESULT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/terminal.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/terminal.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/run.py](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/run.py)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/RAW_ANALYSIS_FIELDS.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/free_third_centre_gate/RAW_ANALYSIS_FIELDS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定source360的5base/Q8 pattern和q5 i/j；只将base3 semi-edge normal j*e1改为任意w。新R*e1⊕R*w模块完整NB≤9关键槽，随后25个w全评价；其它normal/field/matrix未改。

**仍未完成：** Independent voltage assignments, different base/group mechanisms and general largercubic graphs are not excluded.

**启发与重启依据：** 释放一个绑定仅把旧20形式增加到22，不能解除剩余通用路线重复；此规则停止，不按最大像17续改其它normal或求解器。不同完整机制需新的覆盖依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

