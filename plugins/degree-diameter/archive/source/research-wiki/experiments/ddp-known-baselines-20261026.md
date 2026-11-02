---
type: experiment
node_id: exp:ddp-known-baselines-20261026
title: "继承准备期五张已知图的有限检查；零新纪录"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-10-26"
hardware: ""
duration: ""
provenance: "context/DD_PORTFOLIO_START_20261026/validation/baseline_verification.json"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "inherited-known-baseline", "method-ledger"]
---

# 继承准备期五张已知图的有限检查；零新纪录

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** 多目标：known baseline→[6, 3]／L=120；known baseline→[8, 3]／L=253；known baseline→[8, 4]／L=1100；known baseline→[10, 4]／L=2485；known baseline→[8, 5]／L=5334（逐变体，不合成一个距离）

**距目标的证据：** Known n=120,253,1100,2485,5334; imported reports say all roots checked by C++ BFS and independent Python bitsets. This session did not rerun them.



**既有原文指标：** Known n=120,253,1100,2485,5334; imported reports say all roots checked by C++ BFS and independent Python bitsets. This session did not rerun them.

**从属变体：**
```json
[
  {
    "label": "known baseline",
    "target": [
      6,
      3
    ],
    "n": 120,
    "actualD": 3,
    "bad_pairs": 0,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 120,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 0
  },
  {
    "label": "known baseline",
    "target": [
      8,
      3
    ],
    "n": 253,
    "actualD": 3,
    "bad_pairs": 0,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 253,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 0
  },
  {
    "label": "known baseline",
    "target": [
      8,
      4
    ],
    "n": 1100,
    "actualD": 4,
    "bad_pairs": 0,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 1100,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 0
  },
  {
    "label": "known baseline",
    "target": [
      10,
      4
    ],
    "n": 2485,
    "actualD": 4,
    "bad_pairs": 0,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 2485,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 0
  },
  {
    "label": "known baseline",
    "target": [
      8,
      5
    ],
    "n": 5334,
    "actualD": 5,
    "bad_pairs": 0,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki",
    "savedL": 5334,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 0
  }
]
```

**原始证据：** [context/DD_PORTFOLIO_START_20261026/validation/baseline_verification.json](../../context/DD_PORTFOLIO_START_20261026/validation/baseline_verification.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 对象：(6,3,120)、(8,3,253)、(8,4,1100)、(10,4,2485)、(8,5,5334)。均为公开已有构造，**零项新纪录**。

120点边表从UPC完整公开数值边表转录；另四张根据公开半直积公式与生成元重新展开。随后两个实现均从展开边表读取：C++全源BFS和Python整数位集的同步可达递推。全部顶点、全部点对检查一致，点数、边数、最大度和直径符合来源参数。

确切输入、源码、逐次结果在项目内`context/DD_PORTFOLIO_START_20261026/baselines/`、`tools/`、`validation/`。未使用抽样、推测对称性或搜索器缓存，没有做新构造搜索或Lean。此处独立指两个代码路径，不是两位独立研究者。

这5图是生成与验证器回归材料，不要求每次会话重跑，不作为“本Goal解决了5道题”。另外7个优先入口尚未在本包独立验算。

**启发与重启依据：** 对象：(6,3,120)、(8,3,253)、(8,4,1100)、(10,4,2485)、(8,5,5334)。均为公开已有构造，**零项新纪录**。

120点边表从UPC完整公开数值边表转录；另四张根据公开半直积公式与生成元重新展开。随后两个实现均从展开边表读取：C++全源BFS和Python整数位集的同步可达递推。全部顶点、全部点对检查一致，点数、边数、最大度和直径符合来源参数。

确切输入、源码、逐次结果在项目内`context/DD_PORTFOLIO_START_20261026/baselines/`、`tools/`、`validation/`。未使用抽样、推测对称性或搜索器缓存，没有做新构造搜索或Lean。此处独立指两个代码路径，不是两位独立研究者。

这5图是生成与验证器回归材料，不要求每次会话重跑，不作为“本Goal解决了5道题”。另外7个优先入口尚未在本包独立验算。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

