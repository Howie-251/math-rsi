---
type: experiment
node_id: exp:ddp-20400-chi6-complete-quartic-cayley216-20261027
title: "(4,10)另一χ6耦合四生成元规范族：fresh216全连通、均D≥11"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/terminal.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/cases.tsv; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/probe.cpp; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/run.py; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/PROOF.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/FAITHFUL_C17_COUPLINGS.md"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# (4,10)另一χ6耦合四生成元规范族：fresh216全连通、均D≥11

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-family-exhaustion

**目标与阶数：** (4,10)；L=19306；条件性n=20400（未据此计纪录）

**距目标的证据：** 新预测REFUTED。Cayleylefttranslation使每项identityecc=全D；D分布11:122,12:92,13:2。不是216个不同新图，未算普通无序坏对或挑best失败图。

**其他指标（保持原计数类型）：**
```json
{
  "chi17_alpha": 6,
  "new_settings": 216,
  "legal_inverseclosed4_cases": 216,
  "connected_settings": 216,
  "new_Cayley_root_BFS": 216,
  "chi5_controls_inherited": 0,
  "skip_count": 0,
  "exact_D_histogram": {
    "12": 92,
    "13": 2,
    "11": 122
  },
  "complete_edgefiles_exported": 0,
  "source_BFS_repeated": 0,
  "Aut_preparation_repeated": 0,
  "unattempted": 0,
  "UNKNOWN": 0,
  "cursor": {
    "a": 7,
    "b": 8,
    "line_index": 5
  },
  "native_CPU_seconds": 0.092164,
  "compile_CPU_seconds": 0.8076179929999999,
  "total_batch_CPU_seconds": 0.9019097399999999,
  "baseline_date": "2026-10-27",
  "independent_method_count_added": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/terminal.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/terminal.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/cases.tsv](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/cases.tsv)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/probe.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/probe.cpp)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/alternate_chi6_family/run.py)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/PROOF.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/PROOF.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/FAITHFUL_C17_COUPLINGS.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/FAITHFUL_C17_COUPLINGS.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一χ17alpha6新群(F5²×C17)⋊H48，rho保实际sourceA/B。g=α^a(a1,3,5,7)，h=(v,c1,βα^b)(b0..8,v6projectivelines)，全部216新设置，skip空，χ5控制继承0；216真4gens合法、216connected、216actualidentityfullBFS。0D<=10hit/edgefile/未试/UNKNOWN。

**仍未完成：** No generaldegree4D10 upperbound or arbitrary20400graph exclusion.

**启发与重启依据：** 保持sourceF5nearfield模作用但换non-equivalentfaithfulC17coupling仍无quarticD10；在独立chi6group重算真逆元，不继承chi5D11控制。固定完整规范族停止，不改χ/field/Hphase/score。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

