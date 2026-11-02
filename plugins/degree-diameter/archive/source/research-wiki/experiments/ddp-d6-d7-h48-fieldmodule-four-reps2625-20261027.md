---
type: experiment
node_id: exp:ddp-d6-d7-h48-fieldmodule-four-reps2625-20261027
title: "(6,7)H48 normalfield四指定表示：2625projective设置完整无命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/terminal.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/MODEL_BINDINGS.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/cases.tsv; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/search.cpp; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/run.py; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/representation_tables/REPRESENTATIONS.json"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# (6,7)H48 normalfield四指定表示：2625projective设置完整无命中

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-family-exhaustion

**目标与阶数：** (6,7)；L=20400

**距目标的证据：** 预测REFUTED。q7/q8/q9条件性阶数39984/52224/66096；family多阶数多连通状态，顶层actualD/badpairsnull。q8控制仅visited3264、component ecc7，不能称52224图D7；另controls q7D8、q9±D9均非D7成果。

**其他指标（保持原计数类型）：**
```json
{
  "parameter_settings": 2625,
  "legal_six_generators": 2625,
  "connected_settings": 2212,
  "disconnected_settings": 413,
  "new_Cayley_root_BFS": 2625,
  "source_BFS_repeated": 0,
  "complete_edgefiles_exported": 0,
  "unattempted": 0,
  "UNKNOWN": 0,
  "source_controls_included_once": true,
  "q11_control_included": false,
  "normalization": "globalFq* groupautomorphism; allzero disconnected",
  "native_CPU_seconds": 3.65488,
  "input_prepare_CPU_seconds": 0.0074225039999999964,
  "compile_CPU_seconds": 0.896225309,
  "total_batch_CPU_seconds": 4.561592177,
  "intended_orders": [
    39984,
    52224,
    66096
  ],
  "baseline_date": "2026-10-27",
  "independent_method_count_added": 0
}
```



**从属变体：**
```json
[
  {
    "name": "q7",
    "q": 7,
    "n": {
      "actual": null,
      "hypothetical": 39984
    },
    "settings": 400,
    "processed": 400,
    "legal": 400,
    "connected": 400,
    "disconnected": 0,
    "full_D7_hits": 0,
    "edgefiles_exported": 0,
    "control": {
      "tuple": [
        0,
        1,
        0,
        3
      ],
      "connected": true,
      "actual_D": 8,
      "scope": "One sourcecenteredcontrol only"
    }
  },
  {
    "name": "q8",
    "q": 8,
    "n": {
      "actual": null,
      "hypothetical": 52224
    },
    "settings": 585,
    "processed": 585,
    "legal": 585,
    "connected": 192,
    "disconnected": 393,
    "full_D7_hits": 0,
    "edgefiles_exported": 0,
    "control": {
      "tuple": [
        0,
        0,
        0,
        1
      ],
      "connected": false,
      "visited": 3264,
      "component_eccentricity": 7,
      "actual_D": null
    }
  },
  {
    "name": "q9_plusg",
    "q": 9,
    "n": {
      "actual": null,
      "hypothetical": 66096
    },
    "settings": 820,
    "processed": 820,
    "legal": 820,
    "connected": 810,
    "disconnected": 10,
    "full_D7_hits": 0,
    "edgefiles_exported": 0,
    "control": {
      "tuple": [
        0,
        1,
        0,
        1
      ],
      "connected": true,
      "actual_D": 9,
      "scope": "Onecontrol only"
    }
  },
  {
    "name": "q9_minusg",
    "q": 9,
    "n": {
      "actual": null,
      "hypothetical": 66096
    },
    "settings": 820,
    "processed": 820,
    "legal": 820,
    "connected": 810,
    "disconnected": 10,
    "full_D7_hits": 0,
    "edgefiles_exported": 0,
    "control": {
      "tuple": [
        0,
        1,
        0,
        1
      ],
      "connected": true,
      "actual_D": 9,
      "scope": "Onecontrol only"
    }
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/terminal.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/terminal.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/MODEL_BINDINGS.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/MODEL_BINDINGS.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/cases.tsv](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/cases.tsv)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/search.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/search.cpp)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/run.py)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/representation_tables/REPRESENTATIONS.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/representation_tables/REPRESENTATIONS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅VALID q7/q8/q9±四rep的Gq=(Fq²×C17)⋊H48，A=αnormal0；B/C的H,c17源部分固定、四normal坐标全部projective firstnonzero1。400+585+820+820=2625完整BFS，全部sixgenerators合法；connected2212、disconnected413，0D7hit/edgefile/未试/UNKNOWN。q11/D8独立不计。

**仍未完成：** Otherrepresentations/generatorquotientparts andgeneral(6,7)graphs remainopen.

**启发与重启依据：** 合法semidirect表示和source商路线容量不保证连通或完整覆盖。GF8整数embedding用primechar，trueinverse由新field正gens重算。四rep全部projective族按约停止，不加q/rep/Hparts/c17/gauge或score修边。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

