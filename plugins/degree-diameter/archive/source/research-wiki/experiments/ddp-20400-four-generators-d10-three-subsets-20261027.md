---
type: experiment
node_id: exp:ddp-20400-four-generators-d10-three-subsets-20261027
title: "20400群三组四生成元图全部exactD11：固定三subsets无D10新图"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/run.py"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# 20400群三组四生成元图全部exactD11：固定三subsets无D10新图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,10)；L=19306；candidate_graph_or_family n=20400；从属目标：[[4, 10]]

**距目标的证据：** 实际D=11，目标D=10；P0P1/P0P2/P1P2的root>10分别31/392/16，全部exactD11。VT推导global无序bad分别316200/3998400/163200，分变体保存不混合。3项完成/未试0/UNKNOWN0，0D10hits/新下界；3actual候选仅内存构造、未导失败edgefile。

**其他指标（保持原计数类型）：**
```json
{
  "cases": 3,
  "completed": 3,
  "untested": 0,
  "UNKNOWN": 0,
  "candidate_graphs_constructed_in_memory": 3,
  "D10hits": 0,
  "candidate_edgefiles_exported": 0,
  "root_BFS_runs": 3,
  "source_D7_BFS_runs": 0,
  "source_downloads": 0,
  "source_group_order": 20400,
  "VTglobal_diameter_proof": true,
  "CPU_seconds": 0.111369462,
  "generator_tuning": false,
  "prediction": "REFUTED"
}
```



**从属变体：**
```json
[
  {
    "label": "pairs01",
    "target": [
      4,
      10
    ],
    "n": 20400,
    "actual_D": 11,
    "actual_graph_Delta": 4,
    "ordinary_bad_unordered_pairs": 316200,
    "ordinary_bad_target_D": 10,
    "single_root_missing_targets": 31,
    "count_scope": "Exactglobalunorderedpaircount derivedbyVTfromonefullrootBFS",
    "first_missing_target": 437,
    "connected": true,
    "graph_exported": false
  },
  {
    "label": "pairs02",
    "target": [
      4,
      10
    ],
    "n": 20400,
    "actual_D": 11,
    "actual_graph_Delta": 4,
    "ordinary_bad_unordered_pairs": 3998400,
    "ordinary_bad_target_D": 10,
    "single_root_missing_targets": 392,
    "count_scope": "Exactglobalunorderedpaircount derivedbyVTfromonefullrootBFS",
    "first_missing_target": 851,
    "connected": true,
    "graph_exported": false
  },
  {
    "label": "pairs12",
    "target": [
      4,
      10
    ],
    "n": 20400,
    "actual_D": 11,
    "actual_graph_Delta": 4,
    "ordinary_bad_unordered_pairs": 163200,
    "ordinary_bad_target_D": 10,
    "single_root_missing_targets": 16,
    "count_scope": "Exactglobalunorderedpaircount derivedbyVTfromonefullrootBFS",
    "first_missing_target": 3287,
    "connected": true,
    "graph_exported": false
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅恢复出的3inversepairs任取2的全部3subsets；actual v—pi_s(v) leftCayley图均simple/connected/4reg/20400/40800。每图完整root0BFS一次，加Gamma abstractrightregular VT证明得exactglobalD11；不是旧source原标签子图或sourceD7重验。

**仍未完成：** General(4,10)graphs above19306 and other generators remain open; this result closes only these3actualsubsets.

**启发与重启依据：** 已知六生成元D7密度不能保证删去一对后D10；这三个固定subsets完整关闭，不按16或31余缺继续调gens。其它生成元、表示或group选择不由此排除，必须另有结构依据授权。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

