---
type: experiment
node_id: exp:ddp-h4-coupled-flag-linker-subdivision-control-20261027
title: "H(4) double flag/linker subdivision: one 2838-vertex 5regular control fails from newroot2836 to target408"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/REPORT.md; research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/RESULT.json; research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/recipe.json; research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/SEVEN_STEP_WITNESS.json; research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/run.py; research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/terminal.json"
added: 2026-10-27T20:56:23Z
tags: ["ddp", "method-ledger"]
---

# H(4) double flag/linker subdivision: one 2838-vertex 5regular control fails from newroot2836 to target408

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,6)；L=2836；candidate_graph_or_family n=2838

**距目标的证据：** Actual simple connected5regular2838/7095. First newroot2836 eccentricity7,13 oldtargets outsideR6; target408 has exactdistance7, with cut-source distances6 toA and5 toB. Stop before root2837 or old-old tests. GlobalD and unorderedbadpairs unknown.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 2836,
  "source_D_reported": 6,
  "new_root": 2836,
  "new_root_eccentricity": 7,
  "new_root_old_targets_outside_R6": 13,
  "missing_count_type": "single-new-root targets, not unordered graph pairs",
  "new_root_missing_by_type": {
    "point": 10,
    "line": 2,
    "old_flag": 1
  },
  "new_roots_checked": 1,
  "new_roots_unchecked": 1,
  "old_old_checked": false,
  "source_D6_BFS_repeated": 0,
  "diagnostic_G0_target_BFS": 1,
  "controls": 1,
  "CPU_seconds": 0.022448017,
  "prediction": "REFUTED",
  "full_graph_edge_exported": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/RESULT.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/RESULT.json)；[research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/recipe.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/recipe.json)；[research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/SEVEN_STEP_WITNESS.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/SEVEN_STEP_WITNESS.json)；[research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/run.py](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/run.py)；[research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/terminal.json](../../research/ddp/more_graphs_20261027/d5_D6_current2836/coupled_flag_linker_control/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly one frozen choice of two core incidences and two vertex-disjoint cubic-linker edges on actual source2836. Each same new vertex subdivides one incidence and one linker edge, and the two new vertices are adjacent. No flag/linker grid.

**仍未完成：** Other H4 flag/linker constructions remain open. New-root coverage would not by itself imply old-old diameter<=6.

**启发与重启依据：** The four old-neighbor roles and buddy can be legal yet fail to cover a target at both route budgets. This exact structural control is refuted; do not continue to reduce13 missedtargets or expand the flag/linker choices without a genuinely new geometric prediction.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

