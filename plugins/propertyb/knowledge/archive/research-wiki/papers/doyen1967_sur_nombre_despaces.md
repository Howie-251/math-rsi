---
type: paper
node_id: paper:doyen1967_sur_nombre_despaces
title: "Sur le nombre d’espaces linéaires non isomorphes de n points"
authors: ["Jean Doyen"]
year: 1967
venue: "Bulletin de la Société Mathématique de Belgique 19:421–437"
external_ids:
  arxiv: null
  doi: null
  s2: null
tags: ["finite-linear-spaces", "classification", "historical-source"]
added: 2026-10-06T08:09:30Z
---

# Sur le nombre d’espaces linéaires non isomorphes de n points

## One-line thesis

有限线性空间的小规模同构分类包含本项目四点三型与六点九型所需的历史枚举。

## Problem / Gap

研究n点有限线性空间的非同构个数，其中每一对不同点恰属于一条线。该问题与本项目把完全图边划分为团的局部分类相对应。

## Method

原文§1.1给出点、线及唯一共线条件，随后对小点数线性空间分类计数。本轮仅阅读前5页的定义与初始计数，没有将后续12页枚举推导标为已核验。

## Key Results

§2.4（期刊p.424 / PDF p.4）列出N(4)=3和N(6)=10。允许六点全部位于同一条线时有10型；删去唯一六点整块后剩9型，是与本项目六锁结构相对应的直接推论。

## Assumptions

每条线至少含2点，每对不同点恰属于一条线；全体点组成一条线的退化情形计入原文N(n)。项目排除整块时必须单独说明，不能把原文N(6)误报为9。

## Limitations / Failure Modes

本地扫描PDF共17页，已视觉阅读物理pp.1–5，pp.6–17未读；pdftotext只有分页符。该文不讨论本项目的锁定概率权重，也不证明 m(5)≥33。

## Reusable Ingredients

有限线性空间提供四点三型、六点九型的经典定义和计数来源，可与本项目独立的同构枚举交叉核对。其非同构计数不能直接替代有标号类型的权重统计。

## Open Questions

将局部同构代表转成项目条件概率表时，是否完整计入所有标号与边类型？这一义务属于项目自己的概率和枚举论证，不能由历史分类数单独承担。

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

[原文扫描](https://oeis.org/A001200/a001200.pdf)、[本地PDF](../../ref/doyen_1967_linear_spaces_provenance.pdf)及[来源核对](../../context/search_method_provenance_20261006.md)确认小线性空间分类是已有工具；研究重点是其在当前证明中的正确使用，而非要求分类原创。

