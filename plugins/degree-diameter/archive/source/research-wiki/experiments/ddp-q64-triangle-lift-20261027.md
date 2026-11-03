---
type: experiment
node_id: exp:ddp-q64-triangle-lift-20261027
title: "指定双三角形的中心提升有限搜索"
idea_id: "idea:ddp-bicayley-d3"
verdict: no
confidence: high
date: "2026-10-27"
hardware: "local CPU, one worker"
duration: "10.386599 CPU seconds including preparation"
provenance: "research/ddp/m2_coset_tower/nonabelian4_256_triangle_lift/REPORT.md"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 指定双三角形的中心提升有限搜索

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-bicayley-d3`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** (8,3)；L=253；条件性n=256（未据此计纪录）

**距目标的证据：** 16 starts; 144 segments; 204384 legal projection evaluations; best L6; zero center assignments and no saved graph.



**既有原文指标：** 16 starts; 144 segments; 204384 legal projection evaluations; best L6; zero center assignments and no saved graph.



**原始证据：** [research/ddp/m2_coset_tower/nonabelian4_256_triangle_lift/REPORT.md](../../research/ddp/m2_coset_tower/nonabelian4_256_triangle_lift/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 256 点、8 度的指定双三角形试验已完成 16 个起点、144 段和 204384 次合法投影评分。两个三角形保证每个顶点的中心对应点可在三步内到达，修复了上一轮的具体障碍；但最好投影仍为 L=6，每个合法中心提升至少有 192 个距离大于三的无序点对。该下界未必可达到；本批没有枚举中心位，也没有保存新完整图。累计实测 10.386599 CPU 秒。

**启发与重启依据：** 256 点、8 度的指定双三角形试验已完成 16 个起点、144 段和 204384 次合法投影评分。两个三角形保证每个顶点的中心对应点可在三步内到达，修复了上一轮的具体障碍；但最好投影仍为 L=6，每个合法中心提升至少有 192 个距离大于三的无序点对。该下界未必可达到；本批没有枚举中心位，也没有保存新完整图。累计实测 10.386599 CPU 秒。

**单独的重启条件：** The added triangles repair center-antipodes, but projection L6 remains; no extra center bit batch was run.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

