---
type: experiment
node_id: exp:ddp-wave11-binary72-tight-words
title: "固定72 binary lift：26必需词筛与1024个offset0图完整覆盖终态"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave11/binary72_tight_words/REPORT.md; research/ddp/breadth_20261027_wave11/binary72_tight_words/terminal.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/coverage_terminal.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/required_words.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/all_passers.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/all_passers_scores.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/first_finalist_calibration.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/best.edges; research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/best.independent_check.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/root_rank_check.json; research/ddp/breadth_20261027_wave11/binary72_tight_words/search.cpp; research/ddp/breadth_20261027_wave11/binary72_tight_words/full_coverage.cpp; reviews/ddp/wave11_scoped_review_20261027.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# 固定72 binary lift：26必需词筛与1024个offset0图完整覆盖终态

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,4)；L=1100；candidate_graph_or_family n=1152；条件性n=1152（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=12384；saved_explicit1152_graph_only;root_independent_all1152_ordinary_BFS;other1023_actual_D_not_measured；2419200输入恰1024通过26词rank4；八个companion各128。1024/1024个offset0图完整R4全部失败，best为1152/4608/8reg，root唯一全源BFS确认D5、12384个>4普通无序对；其余2418176被必要rank拒绝。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "finalgraph",
  "controller_order": 72,
  "finalgraph_order": 1152,
  "finalgraph_edges": 4608,
  "canonical_inputs": 2419200,
  "required_words": 26,
  "unique4_ordered_controller_slots": 468,
  "rank_survivors": 1024,
  "rank_rejected": 2418176,
  "survivors_by_companion": [
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128
  ],
  "bbbb_prefilter_used": false,
  "nonrequired_word_tests": 0,
  "rank_tests": 6822848,
  "full_R4_candidates_total": 1024,
  "full_R4_candidates_checked": 1024,
  "full_R4_hits": 0,
  "best_passer_id": 68,
  "best_samefiber_bad_pairs": 0,
  "best_crossfiber_bad_pairs": 12384,
  "offsets": 0,
  "global_label_parameters": true,
  "edge_local_model_excluded": false,
  "nonzero_offset_model_excluded": false,
  "canonical_enumeration_repeated_once_to_persist_all_passers": true,
  "passers_cache_persisted": true,
  "first_phase_CPU_seconds": 1.504110786,
  "second_phase_CPU_seconds": 2.1516369620000004,
  "root_final_check_CPU_seconds": 0.3909508,
  "producer_BFS_performed": false,
  "scoped_external_review": {
    "raw_path": "reviews/ddp/wave11_scoped_review_20261027.json",
    "scope": "First-three-topic mathematical/direction review;not exhaustive code proof or a rerun of2419200 inputs.",
    "model_reported": "gemini-3.8-flash-high",
    "effort_reported": "high"
  }
}
```



**从属变体：**
```json
[
  {
    "id": "required26_rank_stage",
    "status": "COMPLETE_REQUIRED26_SURVIVORS_EXIST",
    "canonical_inputs": 2419200,
    "survivors": 1024,
    "graphs_generated": 0,
    "scope": "Necessary rank only;survivors are not finalgraph coverage successes."
  },
  {
    "id": "all1024_offset0_full_R4_stage",
    "status": "COMPLETE_GLOBAL_LABEL_OFFSET0_NO_D4",
    "candidates_checked": 1024,
    "hits": 0,
    "scope": "Complete fixed72/global/offset0 model after necessary screening;not edge-local or nonzerooffset."
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave11/binary72_tight_words/REPORT.md](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/REPORT.md)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/terminal.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/terminal.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/coverage_terminal.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/coverage_terminal.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/required_words.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/required_words.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/all_passers.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/all_passers.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/all_passers_scores.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/all_passers_scores.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/first_finalist_calibration.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/first_finalist_calibration.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/best.edges](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/best.edges)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/best.independent_check.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/best.independent_check.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/root_rank_check.json](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/root_rank_check.json)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/search.cpp](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/search.cpp)；[research/ddp/breadth_20261027_wave11/binary72_tight_words/full_coverage.cpp](../../research/ddp/breadth_20261027_wave11/binary72_tight_words/full_coverage.cpp)；[reviews/ddp/wave11_scoped_review_20261027.json](../../reviews/ddp/wave11_scoped_review_20261027.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定72点有标签控制图、四个global GL4(F2) maps/branch vectors及逆关系；offset全部0。第一阶段完整2419200规范输入的26个唯一四路词必要rank；第二阶段1024通过者完整全图R4。不含edge-local自由映射或任意非零offset。

**正向保证：** 468个唯一四步有序控制slot对应26种必需词，满rank4为16点fiber覆盖必要条件。；aaaa循环基规范化完整给8×20160×15个输入；未用bbbb/cccc预筛，未测试其余82个非必需词。；共同线性换基仅重命名fiber点，所以两阶段合并关闭固定72/global/offset0模型。

**仍未完成：** 非零offset（global或逐边）可能改变多route仿射子空间的并；任意144条边独立maps/vectors的edge-local族仍开放。1024个全R4失败不表示每个图均D5；仅best有独立D5测量。

**启发与重启依据：** 先只用真实唯一route的必要词，避免把旧108通用词排除误套固定图；必要rank通过后仍须完整联合覆盖。此offset0模型已闭，不追加seed；重开须实质改变offset或edge-local覆盖结构并另有明确依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

