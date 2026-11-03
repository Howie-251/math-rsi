---
type: experiment
node_id: exp:ddp-rajiv441-exact-flag-recovery-20261027
title: "Rajiv441完整旗规则恢复：1323边相等，固定point panel与真实配额"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/REPORT.md; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/RESULT.json; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/COORDINATES.json; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/ROUTE_BUDGET.json; research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/Q4_PARAMETER_GATE.json"
added: 2026-10-27T16:02:06Z
tags: ["ddp", "method-ledger"]
---

# Rajiv441完整旗规则恢复：1323边相等，固定point panel与真实配额

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (6,4)；L=441；known_source_or_recovery n=441

**距目标的证据：** 实际D=4，目标D=4；Existingknown441source fact;exactcoordinateedges recovered,no repeated sourceBFS.；A63/B189/C189实际配额(0,6,0)/(2,0,4)/(0,4,2)。恢复63points/63triads及B/C flags，全部1323边与规则完全相等。初始双triangle模型及C固定line猜测被反驳，实际固定point团。自然q4迁移max15超12，未生成。







**原始证据：** [research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/REPORT.md](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/REPORT.md)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/RESULT.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/RESULT.json)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/COORDINATES.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/COORDINATES.json)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/ROUTE_BUDGET.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/ROUTE_BUDGET.json)；[research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/Q4_PARAMETER_GATE.json](../../research/ddp/more_graphs_20261027/d6_rajiv441_orbit_mechanism/Q4_PARAMETER_GATE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactpublic441source plus completeflagcoordinateedgecomparison;naturalq4point/dualparameterarithmeticonly. No sourceBFS.

**仍未完成：** 本轮没有产生新的验收通过纪录；一般图及未明示范围仍开放，Lean完整实例0。

**启发与重启依据：** 原四步路线依赖三条incident lines，不可带着错误panel或度数把q4写成degree9；原自然q4规则止损。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

