---
type: experiment
node_id: exp:ddp-m1-d5-projective-20261026
title: "(5,5)共同共轭/射影规约与四个完整构造族"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "single CPU sequential"
duration: "13/27/3 4.07s; faithful batch9.452CPU s"
provenance: "research/ddp/m1_d5_projective_reduction.md; research/ddp/m1_d5_faithful_results.md; computations/ddp/m1/d5_quotient"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "finite-complete", "no-new-bound", "method-ledger"]
---

# (5,5)共同共轭/射影规约与四个完整构造族

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** graph_or_graph_family

**目标与阶数：** (5,5)；L=650

**距目标的证据：** 实际D=6，目标D=5；Existing Wiki Metrics; no experiment rerun；原702族1464骨架/267912项目代表/260922合法，最小坏对2106。忠实作用三族654/656/666点，共422骨架/743678代表/631705合法，最小坏对6540/4100/999。全部最佳图独立BFS为五正则、直径6。



**既有原文指标：** 原702族1464骨架/267912项目代表/260922合法，最小坏对2106。忠实作用三族654/656/666点，共422骨架/743678代表/631705合法，最小坏对6540/4100/999。全部最佳图独立BFS为五正则、直径6。

**从属变体：**
```json
[
  {
    "label": "original702",
    "n": 702,
    "actualD": 6,
    "bad_pairs": 2106,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "faithful family1",
    "n": 654,
    "actualD": 6,
    "bad_pairs": 6540,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "faithful family2",
    "n": 656,
    "actualD": 6,
    "bad_pairs": 4100,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "faithful family3",
    "n": 666,
    "actualD": 6,
    "bad_pairs": 999,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  }
]
```

**原始证据：** [research/ddp/m1_d5_projective_reduction.md](../../research/ddp/m1_d5_projective_reduction.md)；[research/ddp/m1_d5_faithful_results.md](../../research/ddp/m1_d5_faithful_results.md)；[computations/ddp/m1/d5_quotient](../../computations/ddp/m1/d5_quotient)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 共轭消一维、缩放取项目点，商同构规约及逐骨架完整记录使指定单逆对2+3族获得完整有限检查；均无D5图。不是一般阶数或整个M1机制排除。新构造必须改变该完整范围内的实际结构，不能增加相同seed。

**启发与重启依据：** 共轭消一维、缩放取项目点，商同构规约及逐骨架完整记录使指定单逆对2+3族获得完整有限检查；均无D5图。不是一般阶数或整个M1机制排除。新构造必须改变该完整范围内的实际结构，不能增加相同seed。

**单独的重启条件：** Change actual structure outside the completed finite group/allocation scopes; additional identical seeds cannot reopen them.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

