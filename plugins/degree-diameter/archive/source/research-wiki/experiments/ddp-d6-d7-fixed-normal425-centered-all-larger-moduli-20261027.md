---
type: experiment
node_id: exp:ddp-d6-d7-fixed-normal425-centered-all-larger-moduli-20261027
title: "20400的425-normal cover固定centered族：K23压缩后全部m>17排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/MODEL_NOTES.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/SUPPORTS.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/RESIDUE_DECISION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/supports.cpp; research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/decide.py"
added: 2026-10-27T19:58:37Z
tags: ["ddp", "method-ledger"]
---

# 20400的425-normal cover固定centered族：K23压缩后全部m>17排除

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** fixed-voltage-family-obstruction

**目标与阶数：** (6,7)；L=20400；条件性n=27600（未据此计纪录）

**距目标的证据：** raw投影最低66足18/19但不充分。m18/19首根分别37/68 targets缺项，全48代表缺项和2004/3720非无序坏对。K23 witness=root0→base37,a4,b1；18..23无admissible，m>23由同23整数support基数排除，因此固定basis/section/centered recipe所有m>17均闭。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 20400,
  "base_vertices": 48,
  "projected_states": 1200,
  "root_representatives": 48,
  "words_per_root": 117187,
  "total_words": 5624976,
  "minimum_raw_count": 66,
  "integer_support_cap_K": 23,
  "cap_target": {
    "root": 0,
    "base": 37,
    "a": 4,
    "b": 1
  },
  "checked_moduli": [
    18,
    19,
    20,
    21,
    22,
    23
  ],
  "admissible_moduli": [],
  "source_D7_rechecked": false,
  "native_initial_CPU": 0.070223,
  "initial_compile_total_CPU": 1.299940586,
  "native_support_CPU": 0.052561,
  "closure_compile_total_CPU": 1.198228144,
  "newgraphs": 0,
  "BFS": 0
}
```



**从属变体：**
```json
[
  {
    "name": "m18",
    "target_Delta": 6,
    "target_D": 7,
    "savedL": 20400,
    "n": 21600,
    "n_is_hypothetical": true,
    "actual_D": null,
    "outcome": "ExactR7 endpoint hole; no graph generated"
  },
  {
    "name": "m19",
    "target_Delta": 6,
    "target_D": 7,
    "savedL": 20400,
    "n": 22800,
    "n_is_hypothetical": true,
    "actual_D": null,
    "outcome": "ExactR7 endpoint hole; no graph generated"
  },
  {
    "name": "m20",
    "target_Delta": 6,
    "target_D": 7,
    "savedL": 20400,
    "n": 24000,
    "n_is_hypothetical": true,
    "actual_D": null,
    "outcome": "ExactR7 endpoint hole; no graph generated"
  },
  {
    "name": "m21",
    "target_Delta": 6,
    "target_D": 7,
    "savedL": 20400,
    "n": 25200,
    "n_is_hypothetical": true,
    "actual_D": null,
    "outcome": "ExactR7 endpoint hole; no graph generated"
  },
  {
    "name": "m22",
    "target_Delta": 6,
    "target_D": 7,
    "savedL": 20400,
    "n": 26400,
    "n_is_hypothetical": true,
    "actual_D": null,
    "outcome": "ExactR7 endpoint hole; no graph generated"
  },
  {
    "name": "m23",
    "target_Delta": 6,
    "target_D": 7,
    "savedL": 20400,
    "n": 27600,
    "n_is_hypothetical": true,
    "actual_D": null,
    "outcome": "ExactR7 endpoint hole; no graph generated"
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/MODEL_NOTES.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/MODEL_NOTES.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/SUPPORTS.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/SUPPORTS.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/RESIDUE_DECISION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/RESIDUE_DECISION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/supports.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/supports.cpp)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/decide.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/centered_lift_quotient/modulus_closure/decide.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 继承已绑定48base/F5²×C17源recipe，c中心化为[-8,8]，不保旧C16/全Aut，仅保平移deck。48roots×1200targets完整NB≤7路径整数端点X，min|X|23使所有更大moduli只剩18..23；全部exactresidues失败，0图/BFS。

**仍未完成：** Only the fixedcentered-recipe largercyclicfactor family is closed; general(6,7)construction remains open.

**启发与重启依据：** 合法参数扩张不要求保留旧complement action，但必须保完整路线余数覆盖。数据导出的整数support上界使无限modulus疑问成为完整有限决定，不能因粗容量或足够integer数继续抽样。未排其它gauge/representatives/base，当前不展开。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

