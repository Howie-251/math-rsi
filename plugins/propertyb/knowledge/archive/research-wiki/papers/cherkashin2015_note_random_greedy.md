---
type: paper
node_id: paper:cherkashin2015_note_random_greedy
title: "A Note on Random Greedy Coloring of Uniform Hypergraphs"
authors: ["Danila D. Cherkashin", "Jakub Kozik"]
year: 2015
venue: "Random Structures & Algorithms 47(3):407–413; local arXiv v1 (2013)"
external_ids:
  arxiv: "1310.1368"
  doi: null
  s2: null
tags: ["property-b", "random-greedy", "asymptotic-bounds"]
added: 2026-10-06T06:01:30Z
---

# A Note on Random Greedy Coloring of Uniform Hypergraphs

## One-line thesis
用随机贪心的冲突有序边对重证渐近下界，并给出可直接核验的有限参数充分条件。

## Problem / Gap

用随机贪心简化RS的非二染色超图边数渐近下界证明，并推广至固定r色及局部边相交条件。有限小n目标需要保留概率式，不能只引用大n阶数。

## Method

pp.2–3给每点独立U[0,1]出生时间，按升序扫描，优先用蓝色，只有将形成全蓝边时才改红。若最终有红边f，其首点必是某边e的末点。因此失败被“存在冲突有序边对”覆盖；冲突要求e、f恰交一个顶点。

p.3将共同顶点出生时间分成两侧与中央三段，分别估计单边事件和边对事件。pp.3–5扩展为冲突r-链与短边事件，并使用局部引理。

## Key Results

p.3设m=κ2^(n−1)，中央长度p∈[0,1]，得到有限充分条件κ(1−p)^n+κ²p<1。指定方向单点交边对的概率为∫₀¹x^(n−1)(1−x)^(n−1)dx。

Theorem 1重证m(n)=Ω(2^n√(n/ln n))；Theorems 2–3对固定r≥2给出(n/ln n)^((r−1)/r)r^n量级的全局与局部界。这些渐近结论要求n充分大。

## Assumptions

有限n-一致超图；顶点出生时间独立连续，几乎必然无平局。p.5 Remark 3指出算法只依赖诱导的均匀排列。冲突边对有方向，“算法失败⇒存在冲突对”不能倒转。固定r渐近定理不是允许r任意随n增长的统一结论。

## Limitations / Failure Modes

本地6页全文已读，p.4视觉核对；PDF显示arXiv:1310.1368v1(2013-10-04)，并非已逐项比对的2015期刊最终版。

p.4局部证明所引用的链概率来自“冲突且链中没有短边”；复用时应将此事件与短边事件一起覆盖失败，不能把该估计套给未限定的冲突链。本文不提供锁定顶点后的统一条件概率式，也不直接给出m(5)≥33。

2026-10-21按用户给定链接复读[arXiv v1全文](https://arxiv.org/pdf/1310.1368)，覆盖六页，重点核对§1式(1.1)–(1.3)及§4 Remarks 3–5。此次只作论文阅读与以下有限参数核算，未恢复暂停的36研究。

对五元、35边，将论文参数记为 \(\kappa=35/16\)，其简化充分条件左端为
\[
F(p)=\kappa(1-p)^5+\kappa^2p,\qquad 0\le p\le1.
\]
因 \(F'(p)=-5\kappa(1-p)^4+\kappa^2\)、\(F''(p)=20\kappa(1-p)^3\ge0\)，全局最小点为
\[
p_*=1-(7/16)^{1/4},\qquad
F(p_*)=\frac{1225}{256}\left(1-\frac45(7/16)^{1/4}\right)
\approx1.671787049875332>1.
\]
严格方向不依赖浮点：\((7/16)^{1/4}<5/6\)，故最小值 \(>1225/768>1\)。这只表明式(1.3)直接用于本参数不够强，不表明实际贪心失败概率大于1，也不排除精细分析该算法取得更强结论。

## Reusable Ingredients

失败事件包含、独立出生时间与均匀排列的等价、有向单交边对的积分、有限参数三段界。可用于核对项目概率式的方向和归一化，锁点条件分布另须推导。

## Open Questions

本项目G1要求保留上述事件语义再推导有限多锁定公式；G3要求确认被扣除的link对原本确有非零方向权重。该论文的渐近优化不能替代这些小参数任务。

## Claims

未创建claim节点；文献定理与项目候选分开记录。这里的完整阅读未升级为全部渐近常数的独立审计。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

随机贪心基础来源。[本地原文](../../ref/cherkashin_kozik_2015_random_greedy.pdf)，pp.1–6；[背景与方法笔记](../../context/BACKGROUND_AND_METHODS.md)第4、7节记录精确事件、阅读深度和版本。[Grill论文页](grill2024_improved_lower_bounds.md)继续保留有限顶点数并引入锁点。

此次复读核对：Remark 4明确指出，小顶点数下精细分析随机排列可强于上述渐近估计；Remark 5解释预染色加随机修改的关系。项目已有的[Grill–Linzmayer源码](../../ref/source_packages/grill_linzmayer_2403_05674/PropB.tex)在 Greedy Coloring 节明确承接 Pluhár→Cherkashin–Kozik，并保留实际有向单交对数及积分。我们的条件排列、锁点与坏对扣除沿用这一基础机制，但不能把全部P1–P8归给本文。本文的“一般n渐近定理”和项目“小n精确下界”应分别陈述。

