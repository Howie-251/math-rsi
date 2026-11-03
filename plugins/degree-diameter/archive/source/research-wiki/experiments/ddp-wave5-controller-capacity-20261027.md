---
type: experiment
node_id: exp:ddp-wave5-controller-capacity-20261027
title: "第五轮控制图、非均匀分支与短路容量：未获新下界"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: "CPU, at most one worker per finite profile"
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/REPORT.md; RESULTS.json"
added: 2026-10-27T05:30:18Z
tags: ["ddp", "breadth", "controller", "capacity"]
---

# 第五轮控制图、非均匀分支与短路容量：未获新下界

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
第五轮已验证新下界0。31点双bowtie三起点600000合法交换无raw passer；Fano分裂42点全部13122候选失败；C10最好80点控制图独立D5/20个>4无序对；HS850一次26参数四起点100000提案后独立D4/26180个>3无序对；仿射旗80前8规范方案宽覆盖均失败，最好独立D5/208个>4无序对。F3四维商chart全部108个四字词满秩是正向复用规则，原72宽chart的自纤维/二步修补独立恢复，二者不混用。

## Reasoning
各有限范围已停止，不追加seed或预算。近端自动覆盖尚不能解决全局远端覆盖；fixed104投影的唯一三步walk给27<81容量障碍，独立短枚举确认。UT3(F9)五逆对全部D3机制由投影关系weight短证明排除；F2三维通用三步chart全部197568规范输入无解，Fano方向障碍给纸面解释，单个最佳候选36词已独立校准。这些包含机制变体、工具和局部规则，不按行数算独立方法，也不外推任意同阶图。专家03:15快照保留，持续HTML已更新05:30；后续须改变真实全局覆盖瓶颈。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

