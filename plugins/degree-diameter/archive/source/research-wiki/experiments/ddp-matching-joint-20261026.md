---
type: experiment
node_id: exp:ddp-matching-joint-20261026
title: "六匹配扩张的共同路径修复profile"
idea_id: "idea:ddp-matching-augmentation"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU per task"
duration: "120.078 search CPU s +0.828 independent check"
provenance: "research/ddp/m1_matching_joint/REPORT.md; research/ddp/m1_matching_joint/PROFILE_INDEPENDENT_REPORT.md"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# 六匹配扩张的共同路径修复profile

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-matching-augmentation`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,5)；L=2810；candidate_graph_or_family n=2812

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=331；Existing Wiki Metrics; no experiment rerun；完整单删边损伤表996145项；旧十例强下界只漏0–2坏对。120CPU profile4542736提案，best强下界330、真实331=295旧旧+36新旧，last339。两图均2812点七正则D6。



**既有原文指标：** 完整单删边损伤表996145项；旧十例强下界只漏0–2坏对。120CPU profile4542736提案，best强下界330、真实331=295旧旧+36新旧，last339。两图均2812点七正则D6。



**原始证据：** [research/ddp/m1_matching_joint/REPORT.md](../../research/ddp/m1_matching_joint/REPORT.md)；[research/ddp/m1_matching_joint/PROFILE_INDEPENDENT_REPORT.md](../../research/ddp/m1_matching_joint/PROFILE_INDEPENDENT_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原G到配对端点的距离给出精确新hub捷径；强下界唯一遗漏是多删边共同损伤。只一次启发式profile，无新下界、无额外seed。

**启发与重启依据：** 原G到配对端点的距离给出精确新hub捷径；强下界唯一遗漏是多删边共同损伤。只一次启发式profile，无新下界、无额外seed。

**单独的重启条件：** Address common damage from multiple deletions; the strong bound alone misses that damage.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

