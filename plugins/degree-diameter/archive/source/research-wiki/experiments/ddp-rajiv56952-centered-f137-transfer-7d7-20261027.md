---
type: experiment
node_id: exp:ddp-rajiv56952-centered-f137-transfer-7d7-20261027
title: "Rajiv56952 CRT-centeredF137 control69048:rawcapacity663 passes but exactglobalD8"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/REPORT.md; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/SOURCE_RECEIPT.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/RECIPE.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/CAPACITY.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/RESULT.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/R7_MISSING.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/identity_distances.u8.bin; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/INITIALIZATION_ERROR.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/INITIALIZATION_ERROR.log; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/probe.cpp; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/run.py; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/native.log; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/terminal.json; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_RESULT.json"
added: 2026-10-27T22:54:42Z
tags: ["ddp", "method-ledger"]
---

# Rajiv56952 CRT-centeredF137 control69048:rawcapacity663 passes but exactglobalD8

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,7)；L=56952；candidate_graph_or_family n=69048

**距目标的证据：** 实际D=8，目标D=7；Sourcepublishedrow0exactlymatches7SIDs;sourceinverse/actionarithmeticvalid. 504quotient NB0..7 raw391910words/min663>=137 permitsgraph. Actualsimpleconnected7regular69048/241668 hasglobalexactD8 byCayleyVT/fullidentityBFS;187rootR7misses,first26. Noordinarybadpairmeasurement/newLB. Initialcodeassertabortedbeforecapacity/graphandwasroutinefixedwithsamemathparameters,notasecondcandidate.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 56952,
  "source_M": 2373,
  "source_action": 44,
  "source_firstrow_binding": "EXACT_MATCH",
  "source_full_module_conjugating_shift": 714,
  "source_field113_shift": 36,
  "source_centered_translations": [
    -3,
    -21,
    -37
  ],
  "target_q": 137,
  "target_M": 2877,
  "target_action": 695,
  "quotient_n": 504,
  "NB_words_length0to7": 391910,
  "quotient_min_raw_count": 663,
  "quotient_first_min_slot": 135,
  "actual_graphs": 1,
  "actual_graph_n": 69048,
  "actual_graph_m": 241668,
  "actual_full_identity_BFS": 1,
  "global_D": 8,
  "distance_histogram": [
    1,
    7,
    42,
    252,
    1512,
    8443,
    32678,
    25926,
    187
  ],
  "root_R7_missing": 187,
  "first_R7_missing": 26,
  "ordinary_bad_pair_scope": "Unmeasured;187isone-rootR7statecomplement",
  "source_q113_BFS": 0,
  "initialization_error_before_capacity_graph": true,
  "native_CPU_seconds": 0.011695,
  "native_process_CPU_seconds": 0.013701999999999992,
  "compile_CPU_seconds": 0.898825,
  "successful_run_parent_children_CPU_seconds": 0.912817,
  "initial_error_run_CPU_seconds": 0.881991,
  "total_including_initialization_fix_CPU_seconds": 1.794808,
  "cumulative_native_process_CPU_seconds": 0.016127000000000002,
  "prediction": "REFUTED",
  "UNKNOWN": 0,
  "new_lower_bounds": 0,
  "independent_paper_arithmetic_proof": "research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_RESULT.json"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/SOURCE_RECEIPT.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/SOURCE_RECEIPT.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/RECIPE.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/RECIPE.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/CAPACITY.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/CAPACITY.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/R7_MISSING.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/R7_MISSING.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/identity_distances.u8.bin](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/identity_distances.u8.bin)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/INITIALIZATION_ERROR.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/INITIALIZATION_ERROR.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/INITIALIZATION_ERROR.log](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/INITIALIZATION_ERROR.log)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/probe.cpp](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/probe.cpp)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/run.py](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/run.py)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/native.log](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/native.log)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/terminal.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/terminal.json)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d7_D7_rajiv56952_centered_F137_transfer/ANALYSIS_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactlyonefixedq137 transferofactualRajiv56952 source:keepC24-by-Z21quotient/sourcephases1,2,7and12;field-onlysourceconjugation36representedbyfullmoduleh714;keepcenteredcoeff-3,-21,-37/involution0;targetactionCRT695. First504NBcapacity thenoneactualimplicit69048Cayleygraph/onefullidentityBFS. Nootherprime/action/translation/seed.

**仍未完成：** GeneralCRTfieldtransfers,otheractions/primes/coefficientsandgeneralN(7,7) are notexcluded. Sourceq113D7 inheritedandnotreverified. Capacitypassdoesnotassertfieldcoverage.

**启发与重启依据：** TrueCRTdecomposition andsourcecenteringpreservegroup/quotientrelationsanddegree,butrawroutemultiplicityisnecessaryonly:fieldendpointcoincidencesstillpreventD7. Stopthissingleq137controlwithoutchasing187missesoraddingroots/primes/vectors. ThegeneralCRTfamilyremainsopen.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

