---
type: paper
node_id: paper:ferber2019_quantitative_lovász_criterion
title: "A quantitative Lovász criterion for Property B"
authors: ["Asaf Ferber", "Asaf Shapira"]
year: 2019
venue: "arXiv:1903.04968; local version v1"
external_ids:
  arxiv: "1903.04968"
  doi: null
  s2: null
tags: ["property-b", "random-greedy", "single-intersection", "extremal-equality"]
added: 2026-10-06T06:45:12Z
---

# A quantitative Lovász criterion for Property B

## One-line thesis
确定不可二染色均匀超图所需的有序单交边对最少数，并刻画等号时的完整子超图。

## Problem / Gap
Lovász 判据说明不可二染色超图必有单点交边对。本文问有序单交边对至少有多少，以及等号时有哪些结构，PDF pp.1–2。

## Method
随机排列配合 Pluhár 贪心染色；失败必须出现一个先左边、再唯一交点、再右边的分离事件。一个有序单交边对被分离的概率为 \((n-1)!^2/(2n-1)!\)，p.2 Claims 2.1–2.2。等号时所有分离事件不能重叠，再以 Bollobás 集对定理推出完整子超图，pp.3–4。

## Key Results
Proposition 1.1（p.1，证明 p.2）：不可二染色 n-一致超图的有序单交边对数至少为 \(n\binom{2n-1}{n}\)。Theorem 1（p.2，证明 pp.3–4）：等号时必须包含 \(K_{2n-1}^n\)。

代入 n=5 得阈值630；32边超图不能包含有126边的 \(K_9^5\)，而有序边对数为偶数，因此本项目任何反例必须满足 \(\gamma\ge632\)。这是对文献定理的直接代入，仍不足以排除32边。

## Assumptions
有限 n-一致超图；simple pair 指两条边交集恰有一个顶点；\(m_2(H)\) 计数有序边对。不要将 simple pair 与本项目“无重复边”的 simple hypergraph 定义混淆。

## Limitations / Failure Modes
等号刚性不是稳定性定理，不能直接用于接近630的参数。该数值下界没有使用本项目19–25个顶点的条件；相对于当前锁定方法，它单独提供的排除能力较弱。

## Reusable Ingredients
分离事件的精确概率；同一右边及同一交点的多个左见证会产生事件交叠；由排列事件的等号条件导出局部刚性，再连接集对不等式。具体条件锁定下的交叠扣除仍需另行证明。

## Open Questions
在本项目的低度、共度及锁定轮廓下，是否能强迫足够的分离事件交叠，从而改进逐位置概率上界？本文未给出这样的有限参数估计。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
为临界有序边对提供独立的概率核对和附加必要条件。[本地PDF](../../ref/ferber_shapira_2019_quantitative_lovasz.pdf)，arXiv:1903.04968v1，4页全文已读；[原文](https://arxiv.org/pdf/1903.04968)。本轮交叠探索见[文献更新](../../context/LITERATURE_UPDATE_20261006.md)，未成为已验证项目claim。

## Abstract (original)

> A well known observation of Lovász is that if a hypergraph is not $2$-colorable, then at least one pair of its edges intersect at a single vertex. %This very simple criterion turned out to be extremly useful . In this short paper we consider the quantitative version of Lovász's criterion. That is, we ask how many pairs of edges intersecting at a single vertex, should belong to a non $2$-colorable $n$-uniform hypergraph? Our main result is an {\em exact} answer to this question, which further characterizes all the extremal hypergraphs. The proof combines Bollobás's two families theorem with Pluhar's randomized coloring algorithm.
