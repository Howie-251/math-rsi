---
type: experiment
node_id: exp:ddp-d5-d8-gf9-fullnormal132698-plus162-20261027
title: "(5,8)6000源两GF9表示的完整normal射影族：新132698全无解、继承162"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/REPORT.md; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/terminal.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/parameters.u8.bin; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/normal6_matrix_forms.meta.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/FORMS_INPUT_META.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/FIRST_FAIL_SLOT_COUNTS.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/search.cpp; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/actual_builder.hpp; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/run.py; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_free_B/RESULT.json"
added: 2026-10-27T20:56:23Z
tags: ["ddp", "method-ledger"]
---

# (5,8)6000源两GF9表示的完整normal射影族：新132698全无解、继承162

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-family-exhaustion

**目标与阶数：** (5,8)；L=18810；条件性n=19440（未据此计纪录）

**距目标的证据：** 完整132698新setting、133557槽求值、0容量预排/完整通过/实际图/BFS/UNKNOWN/未试。新预测REFUTED；合继承162关闭132860规范族。首失败槽420计数是求值次序分布，不是图普通坏对。

**其他指标（保持原计数类型）：**
```json
{
  "all_projective_settings": 132860,
  "new_settings_evaluated": 132698,
  "inherited_closed_settings": 162,
  "inherited_recomputed": false,
  "new_per_model": 66349,
  "capacity_pruned_settings": 0,
  "numeric_settings": 132698,
  "slot_evaluations": 133557,
  "minimum_forms_per_slot": 216,
  "normal_targets_per_slot": 81,
  "required_slots": 480,
  "matrix_forms_per_model": 203476,
  "NB_words_per_root": 109226,
  "actual_graphs_generated": 0,
  "new_graph_BFS": 0,
  "source_BFS": 0,
  "unattempted": 0,
  "UNKNOWN": 0,
  "native_CPU_seconds": 0.357179,
  "compile_CPU_seconds": 1.251274139,
  "total_batch_CPU_seconds": 1.611240062,
  "model_first_failure_summary": [
    {
      "scalar": 4,
      "slot420_first_fail_count": 65972,
      "first_fail_counts_sum": 66349
    },
    {
      "scalar": 8,
      "slot420_first_fail_count": 65988,
      "first_fail_counts_sum": 66349
    }
  ],
  "baseline_date": "2026-10-27",
  "baseline_provenance": "Parent current table source and saved 5D8=18810; no independent table refresh in this finite worker."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/terminal.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/terminal.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/parameters.u8.bin](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/parameters.u8.bin)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/normal6_matrix_forms.meta.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/normal6_matrix_forms.meta.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/FORMS_INPUT_META.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/FORMS_INPUT_META.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/FIRST_FAIL_SLOT_COUNTS.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/FIRST_FAIL_SLOT_COUNTS.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/search.cpp](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/search.cpp)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/actual_builder.hpp](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/actual_builder.hpp)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/run.py](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/full_normal_voltage_family/run.py)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_free_B/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/q9_D8_free_B/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保留原6000两底点/H24/z5/全部phase；F9=t²+1两表示alpha=±(1+t)K，VA/VB/VD六坐标任意，globalscalar首非零1。各66430类中81个既闭free-B直接继承，新66349/model共132698逐参数完整必要路由检验；仅480槽全81像才展开图。

**仍未完成：** Other representations, phase profiles, fields and general degree5 diameter8 graphs remain outside this exact finite scope.

**启发与重启依据：** 解除全部normal关系仍无法满足此两表示的固定H24/z5/base phase覆盖；停止这一frame，不按坏点数续调。重启须改变已冻结表示/路由机制或取得新的结构理由，不能把一般19440点(5,8)不存在作为结论。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

