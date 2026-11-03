---
type: experiment
node_id: exp:ddp-more-graphs-20261027-michel684-p43-free-projective
title: "Michel684的p43五电压射影全范围：7000402项、10078薄跨层幸存、0完整命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/REPORT.md; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/RESULT.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/GAUGE.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PREDICTION.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/CAPACITY.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PROFILE1000.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PROFILE_FORECAST.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/REMAINDER.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/prepare.py; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/enumerate.cpp; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/coefficients.txt; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/COMPILE.json; research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/terminal.json"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# Michel684的p43五电压射影全范围：7000402项、10078薄跨层幸存、0完整命中

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (7,4)；L=684；条件性n=774（未据此计纪录）；从属目标：[[7, 4]]

**距目标的证据：** No graph edge table or ordinary BFS. Both identity-orbit roots and all18 endpoint layers perroot; first thin cross checked in every parameter and only survivors checked remaining slots until first failure.；规约证明后完整7000402项全部完成；10078项补齐thin cross，预测SUPPORTED，但全部其它槽失败，0完整774命中、0图。

**其他指标（保持原计数类型）：**
```json
{
  "normalized_scope": 7000402,
  "numerically_enumerated_cases": 7000402,
  "minimum_allslot_form_capacity": 61,
  "thin_cross_form_capacity": 78,
  "thin_cross_survivors": 10078,
  "first_other_failed_slot_counts": {
    "0": 50,
    "3": 4,
    "27": 10024
  },
  "full_hits": 0,
  "new_graphs": 0,
  "profile_cases": 1000,
  "profile_replayed": false,
  "native_CPU_seconds": 0.585992,
  "capacity_CPU_seconds": 0.019920528,
  "compile_user_CPU_seconds": 1.117281,
  "compile_system_CPU_seconds": 0.144751,
  "all_source_BFS": 0,
  "source_reverified": false,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "label": "r6-projective-five-voltage",
    "target": [
      7,
      4
    ],
    "savedL": 684,
    "n": {
      "actual": null,
      "hypothetical": 774
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3500201,
    "cases_enumerated": 3500201,
    "thin_cross_slot": {
      "root": 0,
      "target_side": 1,
      "phase": 7
    },
    "thin_cross_survivors": 5078,
    "first_other_failed_slot_counts": {
      "0": 19,
      "3": 2,
      "27": 5057
    },
    "full_hits": 0,
    "metric_scope": "Normalized voltage assignments and first-failure endpoint slots, not wholegraph ordinary bad pairs."
  },
  {
    "label": "r36-projective-five-voltage",
    "target": [
      7,
      4
    ],
    "savedL": 684,
    "n": {
      "actual": null,
      "hypothetical": 774
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3500201,
    "cases_enumerated": 3500201,
    "thin_cross_slot": {
      "root": 0,
      "target_side": 1,
      "phase": 7
    },
    "thin_cross_survivors": 5000,
    "first_other_failed_slot_counts": {
      "0": 31,
      "3": 2,
      "27": 4967
    },
    "full_hits": 0,
    "metric_scope": "Normalized voltage assignments and first-failure endpoint slots, not wholegraph ordinary bad pairs."
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/REPORT.md](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/REPORT.md)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/RESULT.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/RESULT.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/GAUGE.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/GAUGE.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/CAPACITY.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/CAPACITY.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PROFILE1000.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PROFILE1000.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PROFILE_FORECAST.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/PROFILE_FORECAST.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/REMAINDER.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/REMAINDER.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/prepare.py](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/prepare.py)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/enumerate.cpp](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/enumerate.cpp)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/coefficients.txt](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/coefficients.txt)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/COMPILE.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/COMPILE.json)；[research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/terminal.json](../../research/ddp/more_graphs_20261027/d4_michel684_prime43_transfer/free_projective_scope/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** p43; C9 quotient; nontrivial order3 actions r6/r36; exactly Michel684 original fixed phases A4/3,B1/6,cross2/6/3, equivalently gauged A4/3,B1/6,cross0/4/1. All5 nonzero free translations modulo scaling, first nonzero=1. Not other phasepatterns or general774graphs.

**正向保证：** 有效共同共轭及B侧重标将七个原平移归成五个自由变量，再按非零共同缩放完整P4(F43)枚举。；每个非零规范项连通simple7regular；全部36槽形式容量支持43。

**仍未完成：** Other phasepatterns, other primes or quotientgroups, and arbitrary degree7 diameter4 graphs remain open. r1 is not enumerated; the earlier same-side327<387 abelian bound is inherited separately.

**启发与重启依据：** 相比两个canonical失败，完整射影范围证明单薄跨层可补齐但固定连接不能联合覆盖。停止精确固定phase范围；只有结构性连接/相位规则改变及新授权有限任务才重启，不续seed或局部badscore。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

