---
type: experiment
node_id: exp:ddp-q64-central-matching-20261027
title: "固定投影的中心匹配替换检查"
idea_id: "idea:ddp-bicayley-d3"
verdict: no
confidence: high
date: "2026-10-27"
hardware: "local CPU, one worker"
duration: "0.042962933 CPU seconds"
provenance: "research/ddp/m2_coset_tower/nonabelian4_256_central_matching/SCOPE.md"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 固定投影的中心匹配替换检查

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-bicayley-d3`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** (8,3)；L=253；条件性n=256（未据此计纪录）

**距目标的证据：** All 22 fixed projection modifications fail necessary quotient radius-three coverage; zero center assignments and no graph BFS.



**既有原文指标：** All 22 fixed projection modifications fail necessary quotient radius-three coverage; zero center assignments and no graph BFS.



**原始证据：** [research/ddp/m2_coset_tower/nonabelian4_256_central_matching/SCOPE.md](../../research/ddp/m2_coset_tower/nonabelian4_256_central_matching/SCOPE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定上一轮 L4 投影，删两条跨轨道匹配并加入内部中心匹配的 22 个选择全部检查完毕，均在商图三步覆盖条件处失败。此结论覆盖这 22 个固定改动及其合法中心提升，不排除采用其他投影的一般构造。

**启发与重启依据：** 固定上一轮 L4 投影，删两条跨轨道匹配并加入内部中心匹配的 22 个选择全部检查完毕，均在商图三步覆盖条件处失败。此结论覆盖这 22 个固定改动及其合法中心提升，不排除采用其他投影的一般构造。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

