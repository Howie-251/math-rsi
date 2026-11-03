---
type: experiment
node_id: exp:ddp-loz3243-source-exact-three-orbit-recipe-20261027
title: "(4,8)Loz3243源恢复：三轨道C47:C23配方全部12972arcs吻合"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/REPORT.md; research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_FACTS.json; research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_DOWNLOAD.json; research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source3243.raw_adj.txt; research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/official_sage.txt; research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source_analysis.py; research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/PHASE_RAW_COUNTS.json"
added: 2026-10-27T21:04:56Z
tags: ["ddp", "method-ledger"]
---

# (4,8)Loz3243源恢复：三轨道C47:C23配方全部12972arcs吻合

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (4,8)；L=3243；known_source_or_recovery n=3243

**距目标的证据：** 实际D=8，目标D=8；Published official verifier result inherited; sourceD8 BFS was not rerun. All12972literal arcs were checked against recovered exact recipe.；成功恢复原真实源；公开Aut1081=C47:C23、非Cayley/非VT、D8/girth10继承。原源保旧边单点增点因全regular无slot被阻断；继承girth10可严格排除原源所有非trivial ordinary covers目标D9。不是新下界。

**其他指标（保持原计数类型）：**
```json
{
  "source_m": 6486,
  "source_arcs_matched": 12972,
  "source_BFS": 0,
  "source_girth10_inherited": true,
  "source_Aut_order_inherited": 1081,
  "source_not_Cayley_inherited": true,
  "deck_base_count": 3,
  "deck_group_order": 1081,
  "action_order": 23,
  "source_r": 6,
  "raw_phase_NB9_words_per_root": 39365,
  "raw_phase_minimum": 510,
  "source_check_CPU_seconds": 0.019697199,
  "candidate_generated_in_source_recovery": 0,
  "baseline_date": "2026-10-27",
  "source_credit": "Eyal Loz July2006, official Comellas desc_g8/raw/Sage links retained in SOURCE_FACTS."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_FACTS.json)；[research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_DOWNLOAD.json](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_DOWNLOAD.json)；[research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source3243.raw_adj.txt](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source3243.raw_adj.txt)；[research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/official_sage.txt](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/official_sage.txt)；[research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source_analysis.py](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/source_analysis.py)；[research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/PHASE_RAW_COUNTS.json](../../research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/PHASE_RAW_COUNTS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一官方3243 actual literal，86376bytes/3243rows/6486edges/all4regular。恢复G=F47 semidirect C23 multiplier6，phase-fast编号x+23y；K3三底点loops(3,8),(11,2),(6,35)，cross01/02=e，cross12=(4,45)，全部12972arcs MATCH。

**仍未完成：** Recovered exact source does not itself imply any larger graph. Only the separately recorded one p139 control was generated.

**启发与重启依据：** 不从因式分解猜群；原3243有3 deck orbits。不同场的电压迁移并非原图ordinarycover，须单独实际覆盖检查，不能套旧1344的投影结论。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

