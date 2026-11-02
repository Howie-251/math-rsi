---
type: experiment
node_id: exp:ddp-wave4-mizuno-d3-source
title: "Mizuno新版D3边局部矩阵与18个F3模式"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave4/mizuno_d3_source/README.md; research/ddp/breadth_20261027_wave4/mizuno_d3_source/REPORT.md; research/ddp/breadth_20261027_wave4/mizuno_d3_source/PROOF_ja.md; research/ddp/breadth_20261027_wave4/mizuno_d3_source/README_ja.md; research/ddp/breadth_20261027_wave4/mizuno_d3_source/SCOUT.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/bfs_certificate.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_certificate.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_structure.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/cross_checks.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/local_check.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/original_independent_certificate.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/q3_linear_problem.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/q3_local_patterns.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_degree16-diameter3.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_degree16-diameter3_certificate.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_directories.json; research/ddp/breadth_20261027_wave4/mizuno_d3_source/verification_run.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# Mizuno新版D3边局部矩阵与18个F3模式

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,3)；L=810；条件性n=837（未据此计纪录）

**距目标的证据：** 18局部模式/pencil已恢复；原框架good计数给controller n≤31，q3越810只剩31。

**其他指标（保持原计数类型）：**
```json
{
  "source_controller_n": 30,
  "source_q": 4,
  "source_n": 1920,
  "source_Delta": 16,
  "source_reported_D": 3,
  "q3_naive_n": 810,
  "q3_graph_generated": false,
  "local_patterns": 18,
  "controller_order_bound": 31
}
```





**原始证据：** [research/ddp/breadth_20261027_wave4/mizuno_d3_source/README.md](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/README.md)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/REPORT.md](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/REPORT.md)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/PROOF_ja.md](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/PROOF_ja.md)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/README_ja.md](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/README_ja.md)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/SCOUT.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/SCOUT.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/bfs_certificate.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/bfs_certificate.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_certificate.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_certificate.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_structure.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_structure.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/cross_checks.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/cross_checks.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/local_check.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/local_check.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/original_independent_certificate.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/original_independent_certificate.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/q3_linear_problem.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/q3_linear_problem.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/q3_local_patterns.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/q3_local_patterns.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_degree16-diameter3.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_degree16-diameter3.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_degree16-diameter3_certificate.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_degree16-diameter3_certificate.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_directories.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/results_directories.json)；[research/ddp/breadth_20261027_wave4/mizuno_d3_source/verification_run.json](../../research/ddp/breadth_20261027_wave4/mizuno_d3_source/verification_run.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原30控制器=10K3及6C5，2-(6,3,2)交汇；q4原图1920，q3是另问题

**正向保证：** 无内部translation；每相邻fiber平面pencil覆盖27；边矩阵可随edge变，不强加通用chart

**仍未完成：** 30×27=810仅公式，不宣称q3全局证书/图已复现；尚缺31控制器。

**启发与重启依据：** 应构造真正global31证书，不恢复旧32/33profile。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

