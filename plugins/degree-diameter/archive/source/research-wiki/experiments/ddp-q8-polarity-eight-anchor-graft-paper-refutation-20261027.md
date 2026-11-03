---
type: experiment
node_id: exp:ddp-q8-polarity-eight-anchor-graft-paper-refutation-20261027
title: "(9,3)585→586八anchor重接：纸面统一漏8ports，未跑56候选"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/REPORT.md; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/PREDICTION.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/RESULT.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/parallel_classes.py; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/RESULT.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/SOURCE.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/FALSE_TWIN_CONSTRAINT.md"
added: 2026-10-27T19:14:14Z
tags: ["ddp", "method-ledger"]
---

# (9,3)585→586八anchor重接：纸面统一漏8ports，未跑56候选

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** paper-obstruction

**目标与阶数：** (9,3)；L=585；条件性n=586（未据此计纪录）

**距目标的证据：** 对每个wi取其唯一旧port qi；8个qi互异且不在{p,pi}。被删ui-wi是x到qi唯一3步入口；pi-wi需4步，unusedportmatching也无两步可达端。因此newx至少漏8ports，原D3构造主张纸面REFUTED。不是实际失败图的直径或普通坏对总数。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 585,
  "source_m": 2600,
  "source_ports": 65,
  "source_core": 520,
  "inherited_design": "Steiner3-(65,9,1)",
  "derived_plane_lines": 72,
  "derived_parallel_classes": 9,
  "circles_per_parallel_class": 8,
  "eligible_nonN_p_classes_max": 8,
  "synchronized_choices_per_class": 7,
  "maximum_planned_candidates": 56,
  "candidate_graphs_generated": 0,
  "candidate_cases_evaluated": 0,
  "newroot_missing_ports_lower_bound": 8,
  "hypothetical_edges": 2637,
  "hypothetical_degree_histogram": {
    "9": 586
  },
  "source_adjacency_parses": 0,
  "source_BFS": 0,
  "candidate_BFS": 0,
  "sigma_searches_by_this_task": 0,
  "independent_method_count_added": 0,
  "baseline_date": "2026-10-27",
  "source_credit": "Delorme polarity source; existingactual585literal inherited",
  "parent_theory_review": "Thecomplete newedge-type pathclassification was checked beforeanycandidateexecution.",
  "full_false_twin_D3_order_upper_bound": 578
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/REPORT.md](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/REPORT.md)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/PREDICTION.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/PREDICTION.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/RESULT.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/RESULT.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/parallel_classes.py](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/gadget_preparation/parallel_classes.py)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/RESULT.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/RESULT.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/SOURCE.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/SOURCE.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/FALSE_TWIN_CONSTRAINT.md](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/FALSE_TWIN_CONSTRAINT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 继承实际585源perfect1code及520个S(core)的Steiner3-(65,9,1)。选p和非N(p)derived parallelclass的8anchors，删8条ui-wi、加pi-wi，新x连anchors+p，余56ports仅加matching。此规则degree/simple可证为586/2637全9reg，但不依赖σ就有newroot必要条件障碍。最大预定8classes×7同步choices=56，实际候选生成/枚举/BFS均0。

**仍未完成：** This fixedgraft refutation doesnot exclude arbitrary586degree9diameter3graphs or otherQ8geometric augmentations.

**启发与重启依据：** σ等变与全9regular不能代替覆盖；该规则同时切断8类唯一port入口。停止本graft，不拿q换p微修、不开56候选。重启需一次保留全部8类qi三步路线的不同连接机制。 Further literal class identification shows x would be a degree9 false twin, independently forcing order<=578. This rejects the stated586 gadget before graph generation.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

