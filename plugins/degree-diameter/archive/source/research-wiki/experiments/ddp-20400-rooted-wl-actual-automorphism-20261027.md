---
type: experiment
node_id: exp:ddp-20400-rooted-wl-actual-automorphism-20261027
title: "20400源单根1WL第8轮全离散，恢复并验一个实际自同构0→850"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/AUTOMORPHISM_CHECK.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root0.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root850.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/run.py"
added: 2026-10-27T19:58:36Z
tags: ["ddp", "method-ledger"]
---

# 20400源单根1WL第8轮全离散，恢复并验一个实际自同构0→850

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (6,7)；L=20400；known_source_or_recovery n=20400

**距目标的证据：** 事前single-root WL全离散预测支持，两个根classcounts均3/4/5/6/10/58/2991/20400。pi双射且pi0=850，61200edges保持、0edgefail。root0稳定子平凡由rootedWL离散直接证；reportedAutregular本身不曾被当成WL离散的逻辑保证。

**其他指标（保持原计数类型）：**
```json
{
  "actual_source_n": 20400,
  "actual_source_m": 61200,
  "degree6_vertices": 20400,
  "source_parse_count": 1,
  "sparse6_literal_characters": 163211,
  "author_script_executed": false,
  "WL_roots": [
    0,
    850
  ],
  "WL_rounds_per_root": [
    8,
    8
  ],
  "WL_final_classcounts": [
    20400,
    20400
  ],
  "max_cell": 1,
  "class_count_sequence": [
    3,
    4,
    5,
    6,
    10,
    58,
    2991,
    20400
  ],
  "actual_automorphisms_recovered": 1,
  "bijection": true,
  "root_image": 850,
  "undirected_edges_checked": 61200,
  "automorphism_edge_failures": 0,
  "root0_stabilizer_trivial": true,
  "CPU_seconds": 0.886444407,
  "decode_import_CPU_seconds": 0.503508661,
  "graph_BFS": 0,
  "group_search": false,
  "extraanchors_or2WL": false,
  "candidate_graphs": 0,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/AUTOMORPHISM_CHECK.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/AUTOMORPHISM_CHECK.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root0.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root0.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root850.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root850.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 从已存Sage仅提取最长sparse6，用现有networkx唯一解析actual20400/61200/simple6reg；不执行作者脚本。root0 canonical1WL与条件授权的minN0=850各8round离散，按同色恢复pi，并完整检bijective/rootimage/61200edges。只1个actualAut，不搜大群/其余5邻映射，不BFS/复验D7。

**仍未完成：** Other5neighborautomorphisms, fullgroupcoordinate/generatorrecipe and a relation-preserving larger-parameterconstruction remain unperformed; sourceD7inherited, notnewlyBFSverified.

**启发与重启依据：** 从实际图用canonical rootedWL恢复regular作用接口可替代空等gens；成功只是1个实际Aut，不是完整Cayley配方或新图。若进一步恢复其它邻映射/normalform须另有明确授权，本批已停不自动升2WL/加anchors。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

