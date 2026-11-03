---
type: experiment
node_id: exp:ddp-current-d5d7-6000-source-cyclic-capacity-20261027
title: "Current 6000 two-base recipe: ten-route quotient obstruction closes literal order4 cyclic enlargement"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/REPORT.md; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/SOURCE_FACTS.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/CAPACITY_RESULT.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/FORMAL_Z_POLYNOMIAL_SETS.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/capacity.py; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/README.md; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/construction.json; research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/terminal.json"
added: 2026-10-27T20:53:05Z
tags: ["ddp", "method-ledger"]
---

# Current 6000 two-base recipe: ten-route quotient obstruction closes literal order4 cyclic enlargement

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (5,7)；L=6000

**距目标的证据：** 54612 complete named word paths,27306 per root. Raw minimum10 at rootbase1 to targetbase1,w=(2,4),c1,y0; nine formal z polynomials in that slot. Fixed projected graph admits no ordinary cover with >10 sheets. Literal polynomial bound excludes m10; m6..9 admit no order4 unit; m>=11 violates raw bound. No candidate modulus or graph evaluated. Published source6000/D7 inherited only.

**其他指标（保持原计数类型）：**
```json
{
  "source_reported_D": 7,
  "source_D_verified_here": false,
  "source_recipe_degree": 5,
  "source_group_order": 3000,
  "base_vertices": 2,
  "projected_graph_order": 1200,
  "NB_word_paths": 54612,
  "root_representatives": 2,
  "NB_words_per_root": 27306,
  "minimum_raw_routes": 10,
  "minimum_formal_z_polynomials": 9,
  "root_minimum_raw_routes": [
    12,
    10
  ],
  "formal_ring": "Z[r]/(r^8-1)",
  "larger_moduli_closed": "All m>5 retaining source z-action exactorder4 and literal z-exponents; any ordinary cover of fixed quotient with >10 sheets also excluded.",
  "candidate_modulus_evaluations": 0,
  "actual_new_graphs": 0,
  "source_graph_BFS": 0,
  "candidate_graph_BFS": 0,
  "CPU_seconds": 0.113592038,
  "prediction": "SUPPORTED",
  "ordinary_bad_count_units": "null: local route/form capacity is not a graph bad-pair count"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/SOURCE_FACTS.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/CAPACITY_RESULT.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/CAPACITY_RESULT.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/FORMAL_Z_POLYNOMIAL_SETS.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/FORMAL_Z_POLYNOMIAL_SETS.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/capacity.py](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/capacity.py)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/README.md](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/README.md)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/construction.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/construction.json)；[research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/terminal.json](../../research/ddp/more_graphs_20261027/d5_D7_current6000_transfer/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actual author two-base recipe over ((F5^2 semidirect C3) x C5) semidirect C8 recovered. No old source graph generated/BFS. Delete z to obtain a fixed1200-vertex projected recipe, enumerate all NB words through length7 from its two identity roots. For unchanged literal z-exponents, close all larger cyclic moduli m>5 retaining z-action exactorder4.

**仍未完成：** No claim about other projected recipes, altered z-action order, alternative field modules, or arbitrary N(5,7) constructions. Later GF9/D8 experiment is a separate scope.

**启发与重启依据：** Recover the actual two-orbit voltage recipe before changing factors. A source-specific thin quotient slot blocks every direct z enlargement preserving its action order, independent of aggregate Moore budget. Only a substantive change of action order, quotient voltages or another group would reopen a different scope; none started by this source/capacity record.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

