---
type: experiment
node_id: exp:ddp-d15-d6-current1428361-source-slack-profile-20261027
title: "(15,6)当前1428361真实余量：minSatN2，无零/单满邻原型"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d15_D6_current1428361_source/REPORT.md; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/PREDICTION.json; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_FACTS.json; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/RESULT.json; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/terminal.json; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_RECEIPT.json; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/prepare_source.py; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/profile.cpp; research/ddp/more_graphs_20261027/d15_D6_current1428361_source/run_profile.py"
added: 2026-10-27T23:07:09Z
tags: ["ddp", "method-ledger"]
---

# (15,6)当前1428361真实余量：minSatN2，无零/单满邻原型

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (15,6)；L=1428361；known_source_or_recovery n=1428361；条件性n=1428362（未据此计纪录）

**距目标的证据：** Published sourceD6 inherited; complete actualsource adjacency degree/saturated-neighbor profile only, no BFS.；1428361/10692016/max15；degree13:9312/14:22759/15:1396290，free32071/slots41383；minSatN2仅2原型323107/1323865，zero/onefault0。事前≤1预测REFUTED，按约停止，无新图/距离缓存/solver。

**其他指标（保持原计数类型）：**
```json
{
  "source_n_actual": 1428361,
  "source_m_actual": 10692016,
  "source_degree_histogram_actual": {
    "13": 9312,
    "14": 22759,
    "15": 1396290
  },
  "free_vertex_count": 32071,
  "free_slots": 41383,
  "minSatN": 2,
  "minSatN_count": 2,
  "minSatN_prototypes": [
    323107,
    1323865
  ],
  "zero_fault_count": 0,
  "onefault_count": 0,
  "saturated_neighbor_histogram": {
    "2": 2,
    "3": 2,
    "4": 35,
    "5": 111,
    "6": 294,
    "7": 547,
    "8": 600,
    "9": 594,
    "10": 534,
    "11": 628,
    "12": 4335,
    "13": 34084,
    "14": 378379,
    "15": 1008216
  },
  "source_BFS": 0,
  "R5_balls": 0,
  "solver_runs": 0,
  "candidate_graphs": 0,
  "native_CPU_hard_limit": 10,
  "native_CPU_seconds": 2.06118,
  "compile_CPU_seconds": 0.7024239999999999,
  "decompression_CPU_seconds": 3.638449234,
  "profile_setup_plus_decompression_CPU_seconds": 6.4295422339999995,
  "download_wall_seconds": 103.91441109031439,
  "baseline_date": "2026-10-27",
  "source_credit": "R. Rajiv compound of four copies of H(11) incidence graph with cut matchings and11113 added vertices; published current literal by Nishant Bhakar in Zenodo23691325."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d15_D6_current1428361_source/REPORT.md](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/REPORT.md)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_FACTS.json)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/RESULT.json)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/terminal.json](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/terminal.json)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_RECEIPT.json](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/SOURCE_RECEIPT.json)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/prepare_source.py](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/prepare_source.py)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/profile.cpp](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/profile.cpp)；[research/ddp/more_graphs_20261027/d15_D6_current1428361_source/run_profile.py](../../research/ddp/more_graphs_20261027/d15_D6_current1428361_source/run_profile.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一当前Zenodo23691325/deg15_diam6_n1428361.txt.xz完整literal；一次actualdegree/free/minSatN/zero-onefault profile。未用任何旧1426903/1424896/1424474/1424472源。

**仍未完成：** Arbitrary15pin R5covers, multifault rules, and general larger(15,6)graphs are not excluded.

**启发与重启依据：** 奇阶奇degreecap确保余量，但不确保近完整free邻集；只关闭当前source零/单满邻原型入口。重开须有不同完整连接规则及明确覆盖依据，不因minSat2自动续proxy/guards。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

