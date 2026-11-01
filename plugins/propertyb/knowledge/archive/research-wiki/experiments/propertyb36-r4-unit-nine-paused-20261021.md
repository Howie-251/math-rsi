---
type: experiment
node_id: exp:propertyb36-r4-unit-nine-paused-20261021
title: "25点恰四低：完整九单位必要域、40轨pilot与暂停边界"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-21"
hardware: "local exact arithmetic and original-H paper derivation"
duration: "40 orbit pilot CPU9.851216 seconds; stopped"
provenance: "context/propertyb35-paper/round01/root/whole_class_followup_20261020/r4_nine_unit/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/r4_nine_unit/PAUSE_STATE.json; context/propertyb35-paper/PAUSE_HANDOFF_20261021.md"
added: 2026-10-20T16:56:34Z
tags: ["property-b", "m5-ge36", "pause-handoff", "actual-caller", "provisional"]
---

# 25点恰四低：完整九单位必要域、40轨pilot与暂停边界

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
374目录标记域47124→12928标签、289无色族、6618彩色轨。旧17布局至少一标签strict3614轨（3115全部标记strict、499部分strict）；新增40轨raw严格、1000独立位置行、133标签，最大23063/24024，CPU9.851216。余2964轨未新DP，完整DP未启动。四低真实低迹为6二低、12一低、17纯高，每low三条二低和三private块。

## Reasoning
用户暂停，REPORT与PAUSE_STATE确认无活程序。已得且root核的弱选点事实：选四个单位七度后，交权总<=16且至少13外七度，另选一点交权<=1；连四低得九锁全单位或仅一七七lambda2。此为已有条件工具，混合新概率域没有生成，不能关闭r4。旧强单位选择Brooks例外与40pilot边界原样保留；局部轨数量不是实际H分类或完成比例。无新路线／Goal，partial。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

