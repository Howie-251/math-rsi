---
type: experiment
node_id: exp:ddp-wave6-covers-linker-20261027
title: "普通循环覆盖与仿射平面504点分层图：局部保证成立、全局未闭"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/REPORT.md; RESULTS.json"
added: 2026-10-27T06:04:52Z
tags: ["ddp", "breadth", "voltage", "layered-graph"]
---

# 普通循环覆盖与仿射平面504点分层图：局部保证成立、全局未闭

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
第六轮新下界0。普通循环覆盖：固定41点C9因self五形式少于九停止，root独立短枚举吻合；120点C13全部14400槽容量19至49，通过后实际两起点4000提案，1560点最佳图独立全源D6、31655个>5无序对。新的AG(2,3)三层504点六正则构造保证全部A-A四步覆盖，原定两起点4000全局H交换后最好图独立D6、17073个>4无序对；主要缺项B-C6485、C-C3186。

## Reasoning
504点数由63个A、189个C、252个B及六度预算导出，不是任意邻接矩阵。局部正向覆盖成立，远端尚未覆盖；最好状态相关H短端点仅698，低于粗必要840，坏对下降不代表接近D4。跨cell不交标签C-C需H，且同cell已有四步路，必须保留此例外。普通张量积的七项数值越线均被同步walk阻断，shift/toggle384整个指定参数族返回phase只有30形式少于64；无参数盲搜。旧纯CayleyD3度4至7最优性文献报告30/60/108/168低于一般图门槛，因此取消78点入口，不重证Conder分类，不限制一般多轨道图。各有限profile停止，不追加种子、底图或预算；一般图与整体研究Goal仍开放。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

