---
type: experiment
node_id: exp:ddp-m1-d5-four-one-20261026
title: "(5,5)内部4跨侧1：四个完整有限构造族"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU per profile"
duration: "5.640123 CPU s"
provenance: "research/ddp/m1_d5_four_one_results.md; computations/ddp/m1/d5_four_one"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# (5,5)内部4跨侧1：四个完整有限构造族

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** graph_or_graph_family

**目标与阶数：** (5,5)；L=650

**距目标的证据：** 实际D=6，目标D=5；Existing Wiki Metrics; no experiment rerun；823骨架、501645射影代表、399329合法候选完成；四族最佳坏对5616/20274/6724/666，完整图均五正则、直径6。



**既有原文指标：** 823骨架、501645射影代表、399329合法候选完成；四族最佳坏对5616/20274/6724/666，完整图均五正则、直径6。

**从属变体：**
```json
[
  {
    "label": "reported family1",
    "n": null,
    "actualD": 6,
    "bad_pairs": 5616,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "reported family2",
    "n": null,
    "actualD": 6,
    "bad_pairs": 20274,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "reported family3",
    "n": null,
    "actualD": 6,
    "bad_pairs": 6724,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "reported family4",
    "n": null,
    "actualD": 6,
    "bad_pairs": 666,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  }
]
```

**原始证据：** [research/ddp/m1_d5_four_one_results.md](../../research/ddp/m1_d5_four_one_results.md)；[computations/ddp/m1/d5_four_one](../../computations/ddp/m1/d5_four_one)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅排指定四个群及每侧两个非对合逆对的4+1范围；不排对合分支、其他群或一般图。共同共轭/缩放规约已实际进入完整生成。

**启发与重启依据：** 仅排指定四个群及每侧两个非对合逆对的4+1范围；不排对合分支、其他群或一般图。共同共轭/缩放规约已实际进入完整生成。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

