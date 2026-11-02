---
type: experiment
node_id: exp:ddp-polarity13-ecycle9-chords4-42-uniformt-obstruction-20261028
title: "C9 plus offset4 secant chords: three positive routeclasses but uniform T-root misses E,0compile/SAT"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/REPORT.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREDICTION_DISPOSITION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/RESULT.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_UNIFORM_T_E.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_UNIFORM_T_E.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREPARATION_STATE.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREPARATION_STATE_BEFORE_REVIEW.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/terminal.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_CONSTRUCTION.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_CONSTRUCTION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_COUNTEREXAMPLE_ATTACK.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_COUNTEREXAMPLE_ATTACK.json"
added: 2026-10-28T02:49:07Z
tags: ["ddp", "method-ledger"]
---

# C9 plus offset4 secant chords: three positive routeclasses but uniform T-root misses E,0compile/SAT

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** targeted-external-core-reassignment-paper-obstruction

**目标与阶数：** (4,3)；L=41；条件性n=42（未据此计纪录）

**距目标的证据：** Uniform t in fullT adjacent tofreeds0: branches0+0+4+4 imply R3Ecapacity<=8<9,soeverydeclaredcompletion failsD3. E-E/c-allR3/a-E positivepredictions remainSUPPORTED; joint existenceREFUTED. OnlyPRED+paper+labelcoordination;0INPUT/CNF/decoder/SAT/graph/BFS.

**其他指标（保持原计数类型）：**
```json
{
  "declared_A_vertices": 12,
  "declared_S_vertices": 18,
  "declared_E_vertices": 9,
  "helper_vertices": 3,
  "hypothetical_n": 42,
  "hypothetical_m": 84,
  "supported_subpredictions": [
    "E_E",
    "c_all_R3",
    "a_E"
  ],
  "refuted_subprediction": "joint_existence",
  "uniform_external_targets": 9,
  "uniform_R3_capacity_upper": 8,
  "uniform_missing_lowerbound": 1,
  "count_type": "symbolic routeclass bound,notordinarybadpairs",
  "new_INPUT_generated": false,
  "new_CNF_generated": false,
  "new_decoder_generated": false,
  "CNF_variables": null,
  "CNF_clauses": null,
  "compiler_calls": 0,
  "SAT_calls": 0,
  "chosen_graphs": 0,
  "graph_BFS": 0,
  "voltage_assignments_enumerated": 0,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/REPORT.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/REPORT.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREDICTION_DISPOSITION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREDICTION_DISPOSITION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_UNIFORM_T_E.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_UNIFORM_T_E.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_UNIFORM_T_E.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_UNIFORM_T_E.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREPARATION_STATE.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREPARATION_STATE.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREPARATION_STATE_BEFORE_REVIEW.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/PREPARATION_STATE_BEFORE_REVIEW.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/terminal.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/terminal.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_CONSTRUCTION.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_CONSTRUCTION.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_CONSTRUCTION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_CONSTRUCTION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_COUNTEREXAMPLE_ATTACK.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_COUNTEREXAMPLE_ATTACK.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_COUNTEREXAMPLE_ATTACK.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ecycle9_chords4/ANALYSIS_COUNTEREXAMPLE_ATTACK.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly the parentdeclared C9/offset4 secantpair ES reassignment with pair0 bothES removed, P3 helpers, a-E0/E4, fullT-c and remaining A/freeS ports asdeclared. Not all42graphs or all Ecorereassignments.

**仍未完成：** General42graphs and materiallydifferentEcore/attachment/source rules remainunexcluded. This closes onlythedeclared targetedfamily.

**启发与重启依据：** Repairing the externalcore and onehelper root can still destroy a specificoldroot class. The retained fullTneighbor of the doublycut S-pair loses two entire potentialexternal branches. This rule stops; this batch stops without automatic spoke or pair retuning.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

