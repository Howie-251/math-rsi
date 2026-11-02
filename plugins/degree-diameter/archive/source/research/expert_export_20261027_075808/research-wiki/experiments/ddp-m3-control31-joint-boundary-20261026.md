---
type: experiment
node_id: exp:ddp-m3-control31-joint-boundary-20261026
title: "31点控制图共同端口瓶颈与有界联合SAT"
idea_id: "idea:ddp-m3-affine-line-cover"
verdict: no
confidence: medium
date: "2026-10-26"
hardware: "single CPU"
duration: "diagnosis about12CPU s; SAT0.02474CPU s"
provenance: "research/ddp/m3_control31_diagnosis/REPORT.md; research/ddp/m3_control31_diagnosis/joint_boundary_sat.terminal.json"
added: 2026-10-27T07:55:15Z
tags: ["ddp", "local-diagnosis", "unproved-unsat", "method-ledger"]
---

# 31点控制图共同端口瓶颈与有界联合SAT

**verdict:** `no`  ·  **confidence:** `medium`  ·  tests `idea:ddp-m3-affine-line-cover`

## Metrics
**对象层级：** controller

**目标与阶数：** (4,3)；L=不适用／见变体；controller n=31；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': 837, 'graph_generated': False}

**距目标的证据：** 原图两无序缺孔。2885单交换严格恶化；单侧90/113400端口分配均不改善。88位置16变量边、46固定边、所有961有序对A³>0的联合模型：7326变量23052子句，一次CaDiCaL exit20，result file UNSATISFIABLE。

**其他指标（保持原计数类型）：**
```json
{
  "intended_final_target": {
    "Delta": 12,
    "D": 3,
    "savedL": 810,
    "n_if_full_lift_valid": 837,
    "graph_generated": false
  }
}
```

**既有原文指标：** 原图两无序缺孔。2885单交换严格恶化；单侧90/113400端口分配均不改善。88位置16变量边、46固定边、所有961有序对A³>0的联合模型：7326变量23052子句，一次CaDiCaL exit20，result file UNSATISFIABLE。



**原始证据：** [research/ddp/m3_control31_diagnosis/REPORT.md](../../research/ddp/m3_control31_diagnosis/REPORT.md)；[research/ddp/m3_control31_diagnosis/joint_boundary_sat.terminal.json](../../research/ddp/m3_control31_diagnosis/joint_boundary_sat.terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 两个端口系统独立调整都被共同唯一路由约束；联合模型仍未找到控制图。SAT为无证明日志的发现级UNSAT，未登记认证排除，不外推一般31点图。继续需改变固定46边中的实际路由，当前不恢复同样随机或端口任务。

**启发与重启依据：** 两个端口系统独立调整都被共同唯一路由约束；联合模型仍未找到控制图。SAT为无证明日志的发现级UNSAT，未登记认证排除，不外推一般31点图。继续需改变固定46边中的实际路由，当前不恢复同样随机或端口任务。

**单独的重启条件：** Change actual routes among the fixed46 edges; do not restore the same port/random or uncertified-SAT task.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

