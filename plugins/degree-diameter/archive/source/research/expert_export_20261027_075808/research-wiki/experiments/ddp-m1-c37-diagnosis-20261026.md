---
type: experiment
node_id: exp:ddp-m1-c37-diagnosis-20261026
title: "666点图C37商的精确缺陷与单电压邻域"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU per profile"
duration: "0.284 CPU s"
provenance: "research/ddp/m1_c37_diagnosis/DIAGNOSIS.md"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# 666点图C37商的精确缺陷与单电压邻域

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=666

**距目标的证据：** 18基点45条含环/平行边的商精确还原；每纤维71至105个形式表达式。1620电压修改中1593合法，0改善、9同图中性、1584变差；最小变差把666坏对增为1480。



**既有原文指标：** 18基点45条含环/平行边的商精确还原；每纤维71至105个形式表达式。1620电压修改中1593合法，0改善、9同图中性、1584变差；最小变差把666坏对增为1480。



**原始证据：** [research/ddp/m1_c37_diagnosis/DIAGNOSIS.md](../../research/ddp/m1_c37_diagnosis/DIAGNOSIS.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 九个37圈各附37片叶构成全部坏对图。失败来自实际表达式碰撞而非形式容量不足；单坐标严格局部最小不等于同时赋值不可行，没有追加退火。

**启发与重启依据：** 九个37圈各附37片叶构成全部坏对图。失败来自实际表达式碰撞而非形式容量不足；单坐标严格局部最小不等于同时赋值不可行，没有追加退火。

**单独的重启条件：** Single-voltage neighborhood is exhausted; simultaneous voltage changes are not excluded, but unchanged coordinate repair is not a new range.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

