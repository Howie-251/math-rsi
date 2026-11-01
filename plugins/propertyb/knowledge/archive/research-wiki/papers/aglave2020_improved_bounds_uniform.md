---
type: paper
node_id: paper:aglave2020_improved_bounds_uniform
title: "Improved Bounds for Uniform Hypergraphs without Property B"
authors: ["Sachin Aglave", "V. A. Amarnath", "Saswata Shannigrahi", "Shwetank Singh"]
year: 2020
venue: "Australasian Journal of Combinatorics 76(1):73–86"
external_ids:
  arxiv: "1602.00218"
  doi: null
  s2: null
tags: ["property-b", "constructions", "recoloring", "finite-vertices"]
added: 2026-10-06T06:01:30Z
---

# Improved Bounds for Uniform Hypergraphs without Property B

## One-line thesis
以多核心和块构造改善若干上界，并用覆盖约化、单交边对计数与RS重染色界证明 m(5)≥29。

## Problem / Gap

同时研究小均匀度的构造型上界，以及m(5)的有限下界。构造一个非二染色实例给出上界；排除全部较少边的实例给出下界，两种任务不能混淆。

## Method

PDF p.4／期刊p.76回顾AHT构造；pp.5–6／77–78给出multi-core构造；pp.7–10／79–82给出block及modified block构造。

下界证明在PDF pp.11–12／83–84：平衡染色排除较小v，未共边顶点合并处理较大v，剩余28边、23顶点的pair-covering情形只有度序列(8,6,…,6)或(7,7,6,…,6)。无序单点交边对数至多335；Lemma 4.4保留RS慢速重染色分析中的积分后给出严格小于1的界。

## Key Results

PDF p.5／期刊p.77 Theorem 1.3：m(5)≥29。PDF p.13／p.85 Table 2的新增上界包括m(8)≤1212、m(13)≤200889、m(14)≤528218、m(16)≤3308499、m(17)≤10375782；表中的m(5)≤51为沿用基线。

已有阅读笔记对n=5、M=28、无序单交边对上界Γ=335、p=3/10的代入作Fraction复算，得177832770103/179200000000<1。此项验证算术；Γ的适用性来自原文结构论证。

## Assumptions

超图有限简单且每边大小为n。下界部分的Γ计数无序单点交边对；转成有序γ时γ=2Γ，概率式系数必须同步改变。pair-covering由顶点合并约化取得。构造部分的副本要求按定义互不相交并满足相应余数和均匀度条件。

## Limitations / Failure Modes

本地是14页正式期刊PDF，pp.1–14全文已读；PDF pp.4、11、12视觉核对。书目年为2020，arXiv:1602.00218是2016预印本入口，不能把二者版本混写。

早期项目笔记中的广义二项式步长公式不是本次在原文核对出的公式；从k对点各取一个点也只得到k点。本文m(5)≥29不能作为32边已排除的证据。全文阅读和一次精确代入不等于独立审计所有构造。

## Reusable Ingredients

可借鉴有限v约化、顶点合并、精确度序列枚举，以及将重复共度信息转成单交边对上界的方法。AHT以Fano核心给出51边的具体基线，但改进该构造属于上界路线。对有限n，更有价值的是保留完整重染色积分而非仅引用渐近阶。

## Open Questions

本项目需要将结构约化、单交计数和严格概率式用于32边参数，但该迁移不能由28边证明自动得到。G1–G4记录的是项目内待办，不是本文已解决或全领域尚未解决问题的清单。

## Claims

本页记录Theorem 1.3等文献结果及其出处，不创建claim节点。复算的有理数值保留在阅读笔记中，不据此登记新的项目定理。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

直接相关的早期有限下界范例。[本地原文](../../ref/aglave_et_al_2020_improved_bounds.pdf)，AJC76(1)(2020),73–86，共14页。[早期阅读与原文笔记](../../context/EARLY_HISTORY_AND_SOURCES.md)包含逐段页码、真实构造和RS积分的精确复算；[背景材料](../../context/BACKGROUND_AND_METHODS.md)记录讲稿与期刊来源的区别。

