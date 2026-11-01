---
type: paper
node_id: paper:cherkashin2023_small_nonuniform_hypergraphs
title: "On small non-uniform hypergraphs without property B"
authors: ["Danila Cherkashin"]
year: 2023
venue: "arXiv:2303.03803; local version v1"
external_ids:
  arxiv: "2303.03803"
  doi: null
  s2: null
tags: ["property-b", "nonuniform", "construction", "weighted-edges"]
added: 2026-10-06T06:45:14Z
---

# On small non-uniform hypergraphs without property B

## One-line thesis
研究非均匀超图的边长加权极值，给出小阶构造及渐近上界改进；不直接排除32条五元边。

## Problem / Gap
对非均匀超图定义 \(q(H)=\sum_{e\in E}2^{-|e|}\)，研究最小边长为 n 且不可二染色时的最小权重 q(n)。此问题允许不同边长，与固定五元边数目标不同，PDF pp.1–2。

## Method
先构造一个只有少量合法二染色的均匀超图，再针对剩余染色添加较大的单色边。小阶构造基于16点仿射平面；渐近论证利用随机超图和 alteration，pp.3–4。

## Key Results
Theorem 1.1（p.2，证明 p.4）把 q(n) 的渐近上界改为 \((1+o(1))(e\ln2/8)n^2\)。p.3 给出16顶点、20条四元边与60条八元边的不可二染色构造，权重为95/64；正文报告其四元部分恰有120个合法二染色，均为8/8分割。

## Assumptions
非均匀有限超图，边长至少2；最小边长 n。正文所称 simple hypergraph 是边两两交至多一个顶点，即线性超图，不能误读成本项目仅要求无重复边的定义。

## Limitations / Failure Modes
权重 q(n) 的上界及包含八元边的构造不能直接用来证明或反驳五元目标。全文5页正文已读，但没有重新枚举 Figure 1 构造的120个染色，也未将该计数记为本项目计算结果。

## Reusable Ingredients
保留合法染色集合后逐个添加覆盖约束的思路，可帮助组织候选搜索。覆盖模型仍必须严格保留本项目所有边恰有五个顶点的条件。

## Open Questions
若把启发式搜索限定为五元边，如何有效寻找或排除覆盖全部二染色的32边集合？本文的非均匀构造没有回答这一固定边长问题。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
背景和搜索思路参考，当前证明不依赖其新定理。[本地PDF](../../ref/cherkashin_2023_small_nonuniform.pdf)，arXiv:2303.03803v1，5页正文已读；[原文](https://arxiv.org/pdf/2303.03803)。适用范围见[文献更新](../../context/LITERATURE_UPDATE_20261006.md)。

## Abstract (original)

> For a given hypergraph $H = (V,E)$ consider the sum $q(H)$ of $2^{-|e|}$ over $e \in E$. Consider the class of hypergraphs with the smallest edge of size $n$ and without a 2-colouring without monochromatic edges. Let $q(n)$ be the smallest value of $q(H)$ in this class. We provide a survey of the known bounds on $q(n)$ and make some minor refinements.
