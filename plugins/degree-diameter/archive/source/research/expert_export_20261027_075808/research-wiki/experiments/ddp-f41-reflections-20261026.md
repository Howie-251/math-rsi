---
type: experiment
node_id: exp:ddp-f41-reflections-20261026
title: "F41半直积C8内部反射分支完整检查"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU per task"
duration: "195.565 cumulative CPU s"
provenance: "research/ddp/m1_f41_reflections/SEARCH_REPORT.md; research/ddp/m1_f41_reflections/DERIVATION.md"
added: 2026-10-27T07:55:14Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# F41半直积C8内部反射分支完整检查

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=656

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=984；Existing Wiki Metrics; no experiment rerun；40 mixed和4 both骨架全部完成：14059884赋值、13740658合法。mixed最优1804坏对，both984；独立全656根BFS均五正则D6。



**既有原文指标：** 40 mixed和4 both骨架全部完成：14059884赋值、13740658合法。mixed最优1804坏对，both984；独立全656根BFS均五正则D6。

**从属变体：**
```json
[
  {
    "label": "mixed",
    "n": 656,
    "actualD": 6,
    "bad_pairs": 1804,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "both-reflection",
    "n": 656,
    "actualD": 6,
    "bad_pairs": 984,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  }
]
```

**原始证据：** [research/ddp/m1_f41_reflections/SEARCH_REPORT.md](../../research/ddp/m1_f41_reflections/SEARCH_REPORT.md)；[research/ddp/m1_f41_reflections/DERIVATION.md](../../research/ddp/m1_f41_reflections/DERIVATION.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** A双反射固定后保留mixed三变量和both四变量，未误用旧projective缩放或mixed侧交换。形式容量筛选有候选保全，实际完整有限范围仅此群/分配，不排一般656图。

**启发与重启依据：** A双反射固定后保留mixed三变量和both四变量，未误用旧projective缩放或mixed侧交换。形式容量筛选有候选保全，实际完整有限范围仅此群/分配，不排一般656图。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

