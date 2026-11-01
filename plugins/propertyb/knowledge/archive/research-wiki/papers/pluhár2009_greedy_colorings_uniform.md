---
type: paper
node_id: paper:pluhár2009_greedy_colorings_uniform
title: "Greedy Colorings of Uniform Hypergraphs"
authors: ["András Pluhár"]
year: 2009
venue: "Random Structures & Algorithms 35:216–221"
external_ids:
  arxiv: null
  doi: "10.1002/rsa.20267"
  s2: null
tags: ["property-b", "random-greedy", "ordered-chains"]
added: 2026-10-06T06:01:30Z
---

# Greedy Colorings of Uniform Hypergraphs

## One-line thesis
以随机排列和有序链分析二色及多色可染性；单点交有序边对的概率是可复用的精确组成项。

## Problem / Gap

用随机顶点顺序和贪心思想简化超图二染色下界证明，并分析有序链与多色可染性。其n^(1/4)2^n界弱于RS渐近界，重点是较直接的随机排列方法。

## Method

p.2用独立连续均匀权重生成均匀随机排列。二色算法按本地原文文字为初始全蓝，把每条边的排列首点改红。若产生红边，该边末点必同时是另一边首点，因此无有序冲突边对足以保证成功。

p.3 Lemma 2给出无有序k-链的排列与k可染性之间的刻画；pp.4–5将局部边相交条件与Lovász局部引理结合。

## Key Results

pp.2–3：指定有向单点交边对的冲突概率为q_n=((n−1)!)²/(2n−1)!，因此用有序单交边对数γ可得失败概率≤γq_n。Corollary 1给出m(n)>0.5268·n^(1/4)·2^n（n≥3）的文献界。

pp.4–5 Theorem 4：若每条边至多与D条其他边相交，且2e(2D²−D)q_n≤1，则可二染色。该表述的D不包含边本身。

## Assumptions

有限n-一致超图，n>1；均匀排列或等价独立连续权重。指定方向的单点交概率与无序边对的双方向概率不同。局部依赖通过事件涉及的顶点集合确定，不能把边度与顶点度混为一谈。

## Limitations / Failure Modes

本地6页pp.1–6全文已读，p.2算法与Claim 1视觉核对。Claim 1把红边数X与全部precedes指标和写成等号；稳妥关系是X≤冲突有序边对数Z。一个红边可有多个见证，冲突边对也未必对应红边。E[X]≤E[Z]仍足以给出所用上界。

其首点改红的文字规则与CK的末点贪心实现不同，不逐字混用。没有对全部多色常数和局部依赖计数进行独立审计。

## Reusable Ingredients

精确边对概率q_n、把失败覆盖为有序链事件、用均匀排列分析有限图。无冲突是充分条件，不是单个固定排列贪心成功的必要条件。

## Open Questions

对本项目，需在G1中从明确选定的算法重建条件概率，再在G3中处理link修正的实际方向；本文不提供32边、中心多锁点的现成证书。

## Claims

仅记录可定位的文献结果和可复用的上界关系；没有创建项目claim节点。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

随机排列方法的基础文献。[本地原文](../../ref/pluhar_2009_greedy_colorings.pdf)，6页；[背景与方法笔记](../../context/BACKGROUND_AND_METHODS.md)第4.2、7节记录原文表述与阅读范围。正式书目为Random Structures & Algorithms 35(2009),216–221。

