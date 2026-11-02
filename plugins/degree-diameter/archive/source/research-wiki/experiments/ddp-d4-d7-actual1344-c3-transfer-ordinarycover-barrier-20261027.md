---
type: experiment
node_id: exp:ddp-d4-d7-actual1344-c3-transfer-ordinarycover-barrier-20261027
title: "Actual1344 unique ≤8 route blocks every ordinary nontrivial cover at D8"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/REPORT.md; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/SOURCE.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/RESULT.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/SOURCE_BINDING_CHECK.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/source_binding_probe.py; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/RAW_ROUTE_COUNTS.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/raw_count_diagnostic.py; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/run.py; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PROVISIONAL_WRONG_SOURCE_RESULT.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PROVISIONAL_WRONG_SOURCE_run.py; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/UNIQUE_ROUTE_CHECK.json; research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/unique_route_check.py"
added: 2026-10-27T21:01:32Z
tags: ["ddp", "method-ledger"]
---

# Actual1344 unique ≤8 route blocks every ordinary nontrivial cover at D8

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (4,8)；L=3243；条件性n=4032（未据此计纪录）

**距目标的证据：** Correct C3 root0 NB≤8 endpoint check reaches3572/4032, missing460 representative states; all1344 projected endpoints present. Exact source raw route counts have min1: target(base0,g200) has sole word W6 W4 W6^-1 in the full≤8 range. Unique lifting means no ordinary3cover can cover all3 points of its target fiber. No complete graph exported/BFS or exactD/new lower bound claimed.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 1344,
  "source_reported_D": 7,
  "source_group_order": 672,
  "source_all_roots_BFS_repeated": 0,
  "source_single_root_projection_R7_calibration_count": 1,
  "source_calibration_algorithm": "Bounded set-frontier exploration through depth7 after observed notation conflict",
  "source_calibration_reached": 1344,
  "source_calibration_shells": [
    1,
    4,
    12,
    36,
    107,
    298,
    599,
    287
  ],
  "corrected_permutation_product": "(g*W)[j]=W[g[j]]",
  "provisional_wrong_source_excluded_from_family_results": true,
  "correct_c3_representative_endpoint_checks": 1,
  "candidate_full_BFS_roots": 0,
  "correct_root_R8_missing_states": 460,
  "correct_root_projected_zero_masks": 0,
  "ordinary_bad_count_units": "Not measured;460 is a single-root lifted-state complement",
  "NB_words_root0": 13121,
  "raw_minimum": 1,
  "raw_slots_below3": 5,
  "unique_word": [
    6,
    4,
    -6
  ],
  "raw_count_recurrence_and_direct_enumeration": "All1344 endpoint counts MATCH",
  "identity_source_words": [
    [],
    [
      2,
      1,
      2,
      1,
      2,
      1,
      2,
      1
    ],
    [
      1,
      2,
      1,
      2,
      1,
      2,
      1,
      2
    ]
  ],
  "prediction": "REFUTED",
  "new_lower_bounds": 0,
  "correct_control_CPU_seconds": 0.049311833,
  "source_binding_diagnostic_CPU_seconds": 0.018933454999999995,
  "final_raw_capacity_diagnostic_CPU_seconds": 0.027703110999999996,
  "explicit_failed_graph_exports": 0,
  "unperformed_second_representative_check": 1,
  "independent_minimum_slot_check": "debruijn meet-in-middle partiallengths<=4, unique word[6,4,-6], no BFS/voltage/group enumeration"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/SOURCE.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/SOURCE.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/SOURCE_BINDING_CHECK.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/SOURCE_BINDING_CHECK.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/source_binding_probe.py](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/source_binding_probe.py)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/RAW_ROUTE_COUNTS.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/RAW_ROUTE_COUNTS.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/raw_count_diagnostic.py](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/raw_count_diagnostic.py)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/run.py](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/run.py)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PROVISIONAL_WRONG_SOURCE_RESULT.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PROVISIONAL_WRONG_SOURCE_RESULT.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PROVISIONAL_WRONG_SOURCE_run.py](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/PROVISIONAL_WRONG_SOURCE_run.py)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/UNIQUE_ROUTE_CHECK.json](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/UNIQUE_ROUTE_CHECK.json)；[research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/unique_route_check.py](../../research/ddp/more_graphs_20261027/d4_D7_current1344_C3_transfer/unique_route_check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual Dhar1344 source: G=SmallGroup(672,1047), two-base involution/cross voltage recipe. One directG×C3 control checked at root0; subsequent raw1 endpoint proves every ordinary unbranched k-sheet cover k>=2 of this source fails D<=8. Not arbitrary4032 graphs, branched covers, rewiring, changed base/group/voltages.

**仍未完成：** General N(4,8), rewired sources and branched/non-cover constructions remain open; Lean formalization not performed.

**启发与重启依据：** Short-path multiplicity must precede module or sheet tuning. The source has a unique short route, so changing C3 to a twisted action cannot repair the ordinary-cover deficit. The initial opposite-permutation multiplication was a source-binding bug, isolated as corrigendum rather than counted as another method; a bounded projection calibration fixed it. Reopening requires changing the actual projection/adjacency rule beyond ordinary covers.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

