---
type: experiment
node_id: exp:ddp-f64-semilinear-20261026
title: "忠实半线性F64固定塔：全部生成元组成失败"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "One CPU worker; final graph independently checked from all3200 roots"
duration: "Three-pair12.503756 CPU s; two-pair89.786032 CPU s including preflight/profile, final check0.269335 s"
provenance: "research/ddp/m2_coset_tower/d7_f64_semilinear/STRUCTURE.md; research/ddp/m2_coset_tower/d7_f64_semilinear/NORMALIZATION.md; research/ddp/m2_coset_tower/d7_f64_semilinear/REPORT.md; research/ddp/m2_coset_tower/d7_f64_semilinear/best.independent_verify.json"
added: 2026-10-27T07:55:14Z
tags: ["ddp", "coset-tower", "semilinear", "finite-family", "method-ledger"]
---

# 忠实半线性F64固定塔：全部生成元组成失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,5)；L=2810；candidate_graph_or_family n=3200

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=38976；Existing Wiki Metrics; no experiment rerun；忠实半线性F64固定塔已完整失败：三逆对5058306规范输入、4484088 HH通过、1240 BB通过均评分，最好D6/51072坏对；两逆对两对合41490060合法输入、38982510 HH通过、18524 BB通过均评分，累计89.786032CPU秒。后者最好评分图3200点11200边，独立全部3200根确认简单连通七正则、D6、38976坏对，根缺失24/30/0。至多一逆对由H正规且K/H=C7的280<384容量排除。因此整个指定半线性塔无D5；一般3200点图与其他塔仍开放。零新下界，无新外审或Lean，无当前搜索队列。



**既有原文指标：** 忠实半线性F64固定塔已完整失败：三逆对5058306规范输入、4484088 HH通过、1240 BB通过均评分，最好D6/51072坏对；两逆对两对合41490060合法输入、38982510 HH通过、18524 BB通过均评分，累计89.786032CPU秒。后者最好评分图3200点11200边，独立全部3200根确认简单连通七正则、D6、38976坏对，根缺失24/30/0。至多一逆对由H正规且K/H=C7的280<384容量排除。因此整个指定半线性塔无D5；一般3200点图与其他塔仍开放。零新下界，无新外审或Lean，无当前搜索队列。

**从属变体：**
```json
[
  {
    "label": "three inverse pairs",
    "n": 3200,
    "actualD": 6,
    "bad_pairs": 51072,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  },
  {
    "label": "two inverse pairs two involutions",
    "n": 3200,
    "actualD": 6,
    "bad_pairs": 38976,
    "count_type": "reported_bad_pairs_type_not_explicit_in_wiki"
  }
]
```

**原始证据：** [research/ddp/m2_coset_tower/d7_f64_semilinear/STRUCTURE.md](../../research/ddp/m2_coset_tower/d7_f64_semilinear/STRUCTURE.md)；[research/ddp/m2_coset_tower/d7_f64_semilinear/NORMALIZATION.md](../../research/ddp/m2_coset_tower/d7_f64_semilinear/NORMALIZATION.md)；[research/ddp/m2_coset_tower/d7_f64_semilinear/REPORT.md](../../research/ddp/m2_coset_tower/d7_f64_semilinear/REPORT.md)；[research/ddp/m2_coset_tower/d7_f64_semilinear/best.independent_verify.json](../../research/ddp/m2_coset_tower/d7_f64_semilinear/best.independent_verify.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Faithful action removes the cyclic kernel and permits BB and complete head coverage in some graphs, but no tested generator composition completes all routes. Three-pair and two-pair scopes exhaust ≥2 pairs; normal-H/C7 capacity excludes ≤1 pair. Scope is this fixed G,H,K only.

**启发与重启依据：** Faithful action removes the cyclic kernel and permits BB and complete head coverage in some graphs, but no tested generator composition completes all routes. Three-pair and two-pair scopes exhaust ≥2 pairs; normal-H/C7 capacity excludes ≤1 pair. Scope is this fixed G,H,K only.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

