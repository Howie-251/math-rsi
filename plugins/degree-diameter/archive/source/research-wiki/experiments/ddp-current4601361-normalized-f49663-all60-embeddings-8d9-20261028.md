---
type: experiment
node_id: exp:ddp-current4601361-normalized-f49663-all60-embeddings-8d9-20261028
title: "Current4601361 normalized F49663 transfer: all60 actual4618659 graphs failR9"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/REPORT.md; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/PREDICTION.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/RESULT.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/SOURCE_BASELINE.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/ROOTS.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/CASES.jsonl; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/checkpoint.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/native.log; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/probe.cpp; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/run.py; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/generate.py; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/terminal.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/SOURCE_NOTES.md; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/PROVENANCE.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_GAUGE.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/GAUGE_ARITHMETIC.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_EXECUTION.md; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_EXECUTION.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_construction.json; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_README.md; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_verification.txt; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/controller_capacity/REPORT.md; research/ddp/more_graphs_20261027/d8_D9_current4601361_source/controller_capacity/RESULT.json"
added: 2026-10-28T00:57:31Z
tags: ["ddp", "method-ledger"]
---

# Current4601361 normalized F49663 transfer: all60 actual4618659 graphs failR9

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,9)；L=4601361；candidate_graph_or_family n=4618659

**距目标的证据：** All60 actualsimpleconnected8regular4618659/18474636 Cayley graphs failidentityR9.0hit/incomplete/untested;exactnegativeglobalDnull,no ordinaryunorderedbadpairs. Firstcaseβ885 CPU.137325/R9missing42 wasprofiledonce thenoriginalbatchcontinued;no tunedfollowup.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 4601361,
  "source_m": 18405444,
  "source_D_inherited": 9,
  "source_action": 19070,
  "source_action_exact_order": 93,
  "source_translation": 32880,
  "source_scale": 46118,
  "source_phase_multiplier": 67,
  "normalized_source_beta": 37269,
  "target_field": 49663,
  "target_m": 18474636,
  "order_growth_fraction": 0.003759322513491117,
  "primitive_embeddings_total": 60,
  "actual_graphs_started": 60,
  "completed_R9_cases": 60,
  "started_incomplete_cases": 0,
  "untested": 0,
  "source_BFS_count": 0,
  "target_word_enumeration": 0,
  "target_field_image_gates": 0,
  "solver_calls": 0,
  "shared_raw_capacity": {
    "phase_states": 93,
    "minraw": 575896,
    "first_thin_phase": 33,
    "prefix_count": 53804809,
    "not_repeated": true
  },
  "first_actual_case": {
    "beta": 885,
    "CPU_seconds": 0.137325,
    "R9_missing": 42
  },
  "root_R9_missing_per_case": [
    42,
    42,
    52,
    62,
    42,
    40,
    32,
    56,
    60,
    40,
    58,
    54,
    58,
    58,
    22,
    50,
    38,
    50,
    42,
    36,
    50,
    26,
    52,
    46,
    48,
    52,
    54,
    34,
    56,
    54,
    44,
    66,
    66,
    36,
    48,
    50,
    60,
    48,
    34,
    60,
    48,
    52,
    38,
    30,
    56,
    42,
    44,
    40,
    38,
    34,
    52,
    42,
    32,
    52,
    40,
    74,
    34,
    56,
    48,
    56
  ],
  "first_R9_missing_vertex_per_case": [
    10036,
    9826,
    67229,
    55850,
    66360,
    2764,
    143367,
    77205,
    64702,
    19315,
    13385,
    10905,
    4226,
    98175,
    278658,
    147578,
    323917,
    24157,
    2343,
    280173,
    10421,
    310917,
    67566,
    17471,
    60849,
    58648,
    50567,
    9630,
    201978,
    61025,
    2562,
    61393,
    59503,
    142068,
    7314,
    20494,
    53515,
    66824,
    107631,
    14307,
    79164,
    55224,
    71005,
    106314,
    1372,
    164397,
    184877,
    73949,
    128148,
    9187,
    9902,
    63936,
    13453,
    256556,
    24815,
    2272,
    239428,
    62160,
    50329,
    13653
  ],
  "native_CPU_seconds": 8.56408,
  "production_native_process_plus_driver_CPU_seconds": 8.568451084000001,
  "compile_CPU_seconds_separate": 0.695524,
  "hard_native_CPU_seconds": 120,
  "memory_distance_plus_queue_bytes": 23093295,
  "modular_products_int64": true,
  "target_q_squared": 2466413569,
  "prediction": "REFUTED",
  "new_lower_bounds": 0,
  "ordinary_bad_count_units": "null;single-rootR9missingtargets are not ordinaryunorderedbadpairs",
  "large_edge_file_generated": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/REPORT.md](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/REPORT.md)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/PREDICTION.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/PREDICTION.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/RESULT.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/RESULT.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/SOURCE_BASELINE.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/SOURCE_BASELINE.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/ROOTS.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/ROOTS.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/CASES.jsonl](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/CASES.jsonl)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/checkpoint.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/checkpoint.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/native.log](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/native.log)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/probe.cpp](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/probe.cpp)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/run.py](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/run.py)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/generate.py](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/generate.py)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/terminal.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/field49663_all_embeddings/terminal.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/SOURCE_NOTES.md](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/SOURCE_NOTES.md)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/PROVENANCE.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/PROVENANCE.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_GAUGE.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_GAUGE.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/GAUGE_ARITHMETIC.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/GAUGE_ARITHMETIC.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_EXECUTION.md](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_EXECUTION.md)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_EXECUTION.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/ANALYSIS_EXECUTION.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_construction.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_construction.json)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_verification.txt](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/AUTHOR_verification.txt)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/controller_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/controller_capacity/REPORT.md)；[research/ddp/more_graphs_20261027/d8_D9_current4601361_source/controller_capacity/RESULT.json](../../research/ddp/more_graphs_20261027/d8_D9_current4601361_source/controller_capacity/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed normalized AUTHORLEFT C93/F49663,positivephase-normal(1,0),(22,1),(12,4800),(85,4208),all60 primitive93 beta actions(beta93=1,beta31!=1,beta3!=1). Unique nextfield only;no othernormal/phase/field/seed. Direct actualimplicitidentityR9,not repeatedword/imageenumerations.

**仍未完成：** Othergenerators/controllers/phases/fields or generalN(8,9) graphs remainunexcluded. No exactnegativeglobaldiameter,ordinaryallpairbadcount or formalLeaninstance was produced.

**启发与重启依据：** A0.376percent fieldgain,allcompatibleembeddings andample rawphasecapacity still do notpreserve fullD9. PrecomputedLEFTshifts make completeactualroot checks practical,soall60 were testedratherthan selectingbestmiss. This fixednormalizedfamilyisclosed;do notcontinue nextprime/coefficients/phases/seeds orchase smallmissingcounts without a substantive newrule.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

