---
type: paper
node_id: paper:deutsch2006_congruences_catalan_motzkin
title: "Congruences for Catalan and Motzkin Numbers and Related Sequences"
authors: ["Emeric Deutsch", "Bruce E. Sagan"]
year: 2006
venue: "Journal of Number Theory 117:191–215"
external_ids:
  arxiv: "math/0407326"
  doi: "10.1016/j.jnt.2005.06.005"
  s2: null
tags: ["catalan-numbers", "valuations", "combinatorial-designs"]
added: 2026-10-06T06:01:30Z
---

# Congruences for Catalan and Motzkin Numbers and Related Sequences

## One-line thesis
Theorem 2.1 精确给出 ν₂(C_t)=s₂(t+1)−1；本项目采用其Catalan算术，不把它本身当成概率改进。

## Problem / Gap

研究Catalan、Motzkin及相关组合数列的同余，采用群作用、递推和Lucas同余。当前Property B项目只使用其Catalan二进赋值接口，不把其他数列问题纳入研究目标。

## Method

pp.3–6对Catalan二叉树施加二群作用。令d=s₂(t+1)−1：所有轨道大小被2^d整除，大小恰为2^d的轨道数是奇数，其他轨道大小被2^(d+1)整除，因而总数的二进赋值恰为d。Lemma 2.3的计数递推在p.6以二叉全分割给出组合解释。

## Key Results

p.3 Theorem 2.1：对t≥0，ν₂(C_t)=s₂(t+1)−1，其中C_t=binom(2t,t)/(t+1)。直接推论：C_t奇当且仅当t=2^a−1。

其余章节含Motzkin奇偶性、模3二项式与三项式系数、其他序列的结果和猜想；本页不把浏览过的内容登记为已审计的项目依赖。

## Assumptions

ν₂表示因子2的指数，s₂表示二进制数位和，t为非负整数。讨论有理数理想共度时，赋值按分子减分母延拓；欲推出有理数乘4为整数，还须排除分母的奇素因子。

## Limitations / Failure Modes

本地22页PDF显示arXiv:math/0407326v1，未与2006期刊最终版逐项比对。pp.2–6精读Theorem 2.1及证明，pp.3–5视觉核对；其余pp.1、6–22仅浏览主题、陈述及参考文献。

Catalan非整数性或二进赋值本身不推出概率界<1；还需比较整数距离与概率式的正项。Grill的两个Catalan改进族都是偶数n并限定v=2n+1，不能直接排除n=5、v=22/23。

## Reusable Ingredients

精确二进赋值公式与“奇数个最小轨道”证明方法；用于检查设计阈值的整数性和理想度数/共度数的分母。它提供算术工具，不提供标记顶点存在性或概率支配关系。

## Open Questions

项目中若出现新的理想有理共度，需先验证完整分母与到整数的距离，再判断是否能改变实际概率上界。该任务属于G3相关算术检查，不是新的领域缺口声明。

## Claims

未创建claim节点。Theorem 2.1以文献定理引用；本文不登记新的Property B结论。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

相关算术来源。[本地原文](../../ref/deutsch_sagan_2006_catalan_motzkin.pdf)，22页；[背景与方法笔记](../../context/BACKGROUND_AND_METHODS.md)第5、7节记录定理、证明要点和浏览范围。正式书目为Journal of Number Theory117(2006),191–215。

