---
type: paper
node_id: paper:gao2026_peeling_hypergraphs_structural
title: "Peeling Hypergraphs: A Structural Sufficient Condition for Property B"
authors: ["Lezhe Gao"]
year: 2026
venue: "Zenodo manuscript v1"
external_ids:
  arxiv: null
  doi: "10.5281/zenodo.21475089"
  s2: null
tags: ["property-b", "structural-condition"]
added: 2026-10-06T08:09:30Z
---

# Peeling Hypergraphs: A Structural Sufficient Condition for Property B

## One-line thesis

可按边顺序持续加入新顶点的 peeling 条件保证超图具有 Property B。

## Problem / Gap

稿件寻找可直接构造合法二染色的结构充分条件，研究哪些超图允许逐边延伸染色。它没有提出 m(5) 的新数值界。

## Method

对边序列 e_i，把当前边分为新顶点 S_i 和已出现顶点 T_i，要求 |S_i|+1_{T_i≠∅}≥2。每步给新顶点着色，使当前边非单色，同时不改变已经处理的边。

## Key Results

Theorem 3.1 给出 peeling 蕴含 Property B；Theorem 4.3 给出相应无环顶点归属刻画。对普通图，满足这种顺序的图恰为森林；某个贪心顺序停滞不能说明不存在其他有效顺序。

## Assumptions

讨论有限、无孤立顶点的超图，并要求存在满足 Definition 1.1 的整个边排序。结构充分条件不等价于所有可二染超图的完整刻画。

## Limitations / Failure Modes

已读本地9页稿件的全部内容以核对主张和适用范围，未完成每个证明的独立审计。由其定义可直接推出：5-uniform、32边的 peeling 超图至少有5+31=36个非孤立顶点，因此该条件不能覆盖本项目19–25点的约化分支。

## Reusable Ingredients

逐边延伸染色的明确不变量可用于测试结构性构造；“一个顺序失败”与“不存在可行顺序”必须区分。

## Open Questions

是否存在适用于19–25点、32条五元边的其他结构充分条件？本文 peeling 条件本身不回答这一问题。

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

[Zenodo原始记录](https://zenodo.org/records/21475089)、[本地PDF](../../ref/gao_2026_peeling_hypergraphs.pdf)及[范围核对](../../context/search_latest_bounds_20261006.md)用于排除相近题名造成的误判。记录发布于2026-07-22，稿件首页标2026-07-23；不是本目标的已有证明或反例。

