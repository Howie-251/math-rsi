---
type: experiment
node_id: exp:propertyb36-pure-pair-structure-and-unit8-boundary-20261020
title: "纯一低二低核心：r6匹配结构与4684键旧八锁边界"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "analytic same-H inequalities; exact existing ABC implementation"
duration: "unit8 full 11.340919 CPU seconds plus profile 0.888407; r6 analytic only"
provenance: "context/propertyb35-paper/round01/root/whole_class_followup_20261020/r6_pure_pair/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/pure_pair_unit8/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/pure_pair_unit8/RESULT.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/pure_pair_unit8/SUMMARY.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/pure_pair_unit8/RESIDUAL_ORBITS.json; proofs/propertyb35/TWENTYFIVE_SMALL_LOW_TRACES.md"
added: 2026-10-20T14:44:10Z
tags: ["property-b", "m5-ge36", "pure-pair", "r6", "unit8", "failed-boundary", "provisional"]
---

# 纯一低二低核心：r6匹配结构与4684键旧八锁边界

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
25点35简单五边pair-cover，r3..6非B只余低迹0/1/2。r6的实际库存n1/n2/n0=6/15/14；19高点的私有次数s=0/2/4/6，h0=7+h4+2h6。零私有高点形成K6完美匹配。相同完美匹配的三高点满类至多两个；若有两个，其六高点内部总t>=2，且额外内部超额delta>=T_C+1。另h6<=2，h6=2时h4<=1。真实共同宏星量为sumW=150+D，D=3U6+U4-U2-2U1-3U0；D<=5或326D+308M<=11939足以染色，但尚未证明全域保证。
完整旧八单位锁诊断覆盖13650标记，经低交<=2及非负重数筛得4684键：r3/4/5/6可行2544/1764/356/20，余39/1228/351/20。r3余39分为旧已完成DP非严格33与旧未处理6；r4..6只表示冻结旧菜单不足，不是所有布局最优失败。最大已有raw界依次641/616、74875/68068、6971/6188、27153/24310。新ABC只算r4..6完整716轨道；r3绑定旧SCREEN/PILOT证书，不重跑旧DP。完整CPU11.340919秒，profile0.888407秒。

## Reasoning
partial记录原H条件结构及一条已明确失败边界，不代表r6或任何r3..6整类闭合。满匹配类上界由纯高边的同一Y点/点对双计数与逐行超额矛盾得出，不是匹配类型枚举；真实involution编码没有5同块情形。尚缺q6其他私有分解、q4交换类与同一纯高边六星占用的联合控制。
八锁域只保证锁度、单位锁对和低交<=2，不保证全部外点degree/paircover可实现为H。新低交条件排掉旧core15三低同迹反障碍，却没有排掉其他非严格键。停止原样追加旧ABC菜单或重跑无变化DP；只有加入实际全局degree/共同迹约束或改变数学计数时再评估。代码复用旧ABC而非独立重写；r3旧DP最优性是原报告进口，本轮不重证。八主要类仍开，25纯迹核心仍r3..6。same-family/provisional，无新Lean或verified claim。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

