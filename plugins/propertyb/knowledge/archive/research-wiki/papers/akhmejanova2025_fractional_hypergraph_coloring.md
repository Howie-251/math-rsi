---
type: paper
node_id: paper:akhmejanova2025_fractional_hypergraph_coloring
title: "Fractional hypergraph coloring"
authors: ["Margarita Akhmejanova", "Sean Longbrake"]
year: 2025
venue: "arXiv preprint; local v2 updated 2026-06-07"
external_ids:
  arxiv: "2504.12430"
  doi: null
  s2: null
tags: ["hypergraph-coloring", "fractional-coloring"]
added: 2026-10-06T08:09:30Z
---

# Fractional hypergraph coloring

## One-line thesis

将超图二染色的概率方法推广到每顶点取多色、边上无公共颜色的 (a:b)-coloring。

## Problem / Gap

研究每个顶点选择a种颜色中的b种，而每条边的所有顶点不共享同一种颜色的分数染色问题。b=1时回到普通a染色，但主要定理的参数限制不能因此忽略。

## Method

结合随机重染色与保留颜色、Hall匹配分配等方法建立充分条件。当前v2引言区分这一超图定义与通常从图的线性规划得到的 fractional coloring 观点。

## Key Results

本地为 arXiv:2504.12430v2（2026-06-07），首版日期为2025-04-16。v2 Theorem 1 要求2≤b≤a−2，Proposition 1要求a>3，Theorem 2为充分大n的渐近结果；Theorem 3在n=5,a=2,b=1时仅保证|E|≤1，未给 m(5)≥33。

## Assumptions

(a:b)-coloring 在每个顶点选b个不同颜色，且边的所有顶点的颜色集合交为空。每个结果的a、b、n范围和渐近阈值需分别满足，不能将b≥2的主定理套到普通二染色。

## Limitations / Failure Modes

已读v1 HTML引言与结果并浏览证明，随后核查当前v2 PDF pp.1–4的引言、全部结果陈述及参考文献；13页稿件的证明未全部精读或独立审计。SSRN副本与arXiv版本不可不加区分地互换。

## Reusable Ingredients

用于审查参数代入和“广义染色包含普通二染色”这类推断；随机重染色与保留颜色分配也提供相关方法入口。

## Open Questions

能否从这些方法得到小均匀度的显式改进常数？已读结果没有解决本项目32边的全部情况。

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

[arXiv版本页](https://arxiv.org/abs/2504.12430)、[v2原文](https://arxiv.org/pdf/2504.12430v2)、[本地PDF](../../ref/akhmejanova_longbrake_2025_fractional_hypergraph_coloring.pdf)及[检索记录](../../context/search_latest_bounds_20261006.md)记录一次对 Grill–Linzmayer 后续引用的核查；本轮没有在其已读结果陈述中找到目标的新界。

