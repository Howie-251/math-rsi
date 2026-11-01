---
type: paper
node_id: paper:szeider2025_sat_modulo_symmetries
title: "SAT Modulo Symmetries: A Survey"
authors: ["Stefan Szeider"]
year: 2025
venue: "SC-Square 2025; CEUR Workshop Proceedings Vol.4116, published 2025-12-02"
external_ids:
  arxiv: null
  doi: null
  s2: null
tags: ["sat", "isomorph-free", "co-certificate-learning", "proof-certificates"]
added: 2026-10-06T06:45:14Z
---

# SAT Modulo Symmetries: A Survey

## One-line thesis
综述动态同构剪枝、合法染色驱动的约束学习及可核查SAT证书，支持组合对象的完整排除。

## Problem / Gap
组合对象的完整搜索容易被大量同构副本淹没；不可染色等 coNP 性质又不适合直接作为普通SAT的短约束。本文整理动态同构剪枝及与性质验证器配合的框架，PDF pp.1–2。

## Method
MinCheck 在部分定义的图上寻找非规范标号的置换见证，学习可提前剪枝的约束，§2 pp.2–4。Co-Certificate Learning 用第二个求解器寻找合法染色，再生成阻止同一染色的覆盖约束，§3.2 pp.4–5。超图可表示成保留两侧类型的二分关联图，§4.4 p.7。

## Key Results
§3.3 p.5 区分两种证明材料：同构剪枝的置换证书，以及逻辑推导的 DRAT 证明；完整枚举可以通过排除已发现解后验证 UNSAT 来认证。§4.4 p.7 给出超图、拟阵及有界出现次数不可满足CNF的应用；这些应用的规模不是本项目规模的运行保证。

## Assumptions
必须给出正确的对象编码和保持问题不变的同构群；额外性质验证器应输出可检查的见证。用于本项目时须区分原顶点与超边，保留五元、简单、32边及已证明结构条件。

## Limitations / Failure Modes
该综述没有直接处理 m(5)≥33。算法仍可能需要指数时间；超时、未找到候选或只有求解器状态均不是完整排除证据。本文所述证书功能尚未在本项目安装或运行。

## Reusable Ingredients
在已证明结构分支中生成候选超图；合法二染色作为 co-certificate 产生新的 COVER 约束；使用动态同构剪枝和可独立检查的搜索证明。[官方仓库](https://github.com/markirch/sat-modulo-symmetries)及[文档](https://sat-modulo-symmetries.readthedocs.io/en/latest/)已核对入口。

## Open Questions
经过局部结构约化后，本项目的困难分支能否被 CCL/SAT 完整排除？有效同构编码、剪枝规模和最终证书大小尚未实测。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
概率路线遇到困难局部型时的计算替代方法。[本地PDF](../../ref/szeider_2025_sat_modulo_symmetries_survey.pdf)，11页全文已读；[CEUR原文](https://ceur-ws.org/Vol-4116/invited1.pdf)，SC-Square 2025，页面注明2025-12-02出版。项目适配方案见[文献更新](../../context/LITERATURE_UPDATE_20261006.md)，尚无本项目运行结果。
