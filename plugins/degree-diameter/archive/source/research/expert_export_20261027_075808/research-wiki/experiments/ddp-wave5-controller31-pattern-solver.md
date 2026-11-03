---
type: experiment
node_id: exp:ddp-wave5-controller31-pattern-solver
title: "31点edge-local十八模式稀疏证书求解工具"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/controller31_pattern_solver/README.md; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/batch.json; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/calibrate.py; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/calibration.json; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/core.py; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/run_one.py; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/terminal.json; research/ddp/breadth_20261027_wave5/controller31_pattern_solver/worker.py"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 31点edge-local十八模式稀疏证书求解工具

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** tool

**目标与阶数：** (12,3)；L=810；条件性n=837（未据此计纪录）

**距目标的证据：** 工具已校准，输入0、MILP调用0、新图0。

**其他指标（保持原计数类型）：**
```json
{
  "solver_calls": 0,
  "candidates_received": 0,
  "calibration": "original30 actual matrices plus old31 immediate raw rejection"
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/controller31_pattern_solver/README.md](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/README.md)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/batch.json](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/batch.json)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/calibrate.py](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/calibrate.py)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/calibration.json](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/calibration.json)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/core.py](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/core.py)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/run_one.py](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/run_one.py)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/terminal.json](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/terminal.json)；[research/ddp/breadth_20261027_wave5/controller31_pattern_solver/worker.py](../../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/worker.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定31输入的精确pattern模型；本批没有上游raw passer

**正向保证：** 确定性Euler交替2factor与inverseports；reverse路径配对及1116binary稀疏模型已校准

**仍未完成：** 没有对一般31控制图做UNSAT声明。

**启发与重启依据：** 仅当明确raw31 passer出现再用工具；不自行生成输入。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

