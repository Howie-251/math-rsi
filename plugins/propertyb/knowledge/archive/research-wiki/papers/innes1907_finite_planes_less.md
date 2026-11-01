---
type: paper
node_id: paper:innes1907_finite_planes_less
title: "Finite Planes With Less Than Eight Points On A Line"
authors: ["C. R. Mac Innes"]
year: 1907
venue: "The American Mathematical Monthly 14(10), 171–174"
external_ids:
  arxiv: null
  doi: "10.2307/2971152"
  s2: null
tags: ["property-b", "finite-geometry", "affine-plane", "explicit-import"]
added: 2026-10-19T15:10:23Z
---

# Finite Planes With Less Than Eight Points On A Line

## One-line thesis
五阶仿射平面唯一性：25点、每线5点的仿射平面同构到AG(2,5)；本项目作为明确文献定理导入，未独立重做历史六补全分类。

## Problem / Gap
分类小阶有限平面，确定哪些参数存在以及同阶结构是否唯一。本项目使用其中五阶仿射平面的唯一性。

## Method
将仿射平面两方向正规化为行列，固定对角线，再对过对角点的候选线作相容选择；最后用坐标变换识别模5直线模型。原文p172–173的有限相容性检查较紧凑，不能写成本项目已重新穷尽。

## Key Results
原文p172–173证明25点、每线5点的仿射平面同构到AG(2,5)。本轮实际读印刷p171–174，证明调用只导入五阶唯一性，不扩大为任意设计唯一性。

## Assumptions
点对恰一线、平行线唯一及非退化性；每条仿射直线5点。仅有相同点数、边数或局部共度矩阵不足以套用。

## Limitations / Failure Modes
本项目未独立重做历史六种补全检查，唯一性是明确外部依赖。a5至少一组不是边时，目前没有到仿射平面的已证归约。

## Reusable Ingredients
先从真实2-(25,5,1)设计直接证明仿射公理，再使用唯一性给实际坐标；坐标化后可用仿射群传送合法染色控制附加边。

## Open Questions
a5缺少整组边时，是否仍能找到足够大的仿射直线子族？当前未证明。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
在25点a5五组全为原H边时，删去五组边后实际得到2-(25,5,1)，本定理与21/100严格界共同闭合该条件分支。原始PDF为ref/literature-20261019/mac_innes_1907.pdf，阅读回执和导入接口见context/propertyb35-paper/round01/twentyfive/FULL_GROUP_EDGE_CASE.md；[原文](https://archive.org/details/jstor-2971152)。

