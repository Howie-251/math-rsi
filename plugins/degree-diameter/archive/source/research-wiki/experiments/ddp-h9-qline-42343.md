---
type: experiment
node_id: exp:ddp-h9-qline-42343
title: "完整新图：(12,5)42343，超过实时公开42342门槛"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/global_coverage_20261027/candidate42343/README.md; research/ddp/global_coverage_20261027/candidate42343/parameters.json; research/ddp/global_coverage_20261027/candidate42343/generate.py; research/ddp/global_coverage_20261027/candidate42343/FINAL_MATH_PROOF.md; research/ddp/global_coverage_20261027/candidate42343/graph_d12_D5_n42343.edges; research/ddp/global_coverage_20261027/candidate42343/independent_all_source_BFS.json; research/ddp/global_coverage_20261027/candidate42343/verify_all.cpp; research/ddp/global_coverage_20261027/candidate42343/BASELINE_REFRESH.json; research/ddp/global_coverage_20261027/candidate42343/dry_run_structure_check.json; reviews/ddp/h9_quadric_42343_final.raw.json; reviews/ddp/h9_quadric_42343.DISPOSITION.md; research/ddp/global_coverage_20261027/candidate42343/new_vertex_R4_parent_depth.json; research/ddp/global_coverage_20261027/candidate42343/new_vertex_R4_certificate_summary.json; research/ddp/global_coverage_20261027/candidate42343/lean_stage/HANDOFF.md; research/ddp/global_coverage_20261027/candidate42343/lean_stage/STATUS.json; formal/DegreeDiameter/Portfolio/SingleExtension.lean"
added: 2026-10-27T10:50:19Z
tags: ["ddp", "method-ledger"]
---

# 完整新图：(12,5)42343，超过实时公开42342门槛

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,5)；L=42342；candidate_graph_or_family n=42343

**距目标的证据：** 实际D=5，目标D=5；普通无序坏对=0；Root independent full42343-source BFS from expanded edge list; all eccentricities5. Mathematical verification complete; Lean incomplete.；n42343,m245229,maxdegree12,connected,simple,Dexact5,badunordered0；全部42343根独立BFS通过。2026-10-27实时官方主表与描述仍42342，数学新下界提高1。尚未Lean、尚未对外发布，Goal ACTIVE。

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bound_mathematically_verified": true,
  "new_graphs_generated": 1,
  "independent_full_BFS_graphs": 1,
  "roots_checked": 42343,
  "checked_n": 42343,
  "checked_m": 245229,
  "degree_cap": 12,
  "exact_D": 5,
  "all_source_check_CPU_seconds": 60.3519,
  "all_source_check_wall_seconds": 15.1209,
  "mandatory_pins": [
    452,
    6195,
    10312,
    12353,
    13822,
    21068,
    24695,
    29805,
    36474,
    38101
  ],
  "anchors": [
    4633,
    20168
  ],
  "new_vertex": 42342,
  "saved_baseline_date": "2026-10-26",
  "baseline_refreshed_UTC": "2026-10-27 10:39:09 UTC",
  "current_public_baseline": 42342,
  "improvement": 1,
  "Lean_complete": false,
  "public_submission": false,
  "Goal_complete": false,
  "source_author": "Dharunish Yugeswardeenoo; underlying partial fold and duality Rishabh Rajiv",
  "mechanism_evidence_node": "exp:ddp-h9-global-coverage-20261027",
  "final_review_status": "SUCCESS",
  "actual_review_model": "gemini-3.8-flash-high",
  "actual_review_effort": "high",
  "review_thread": "0b674e3b-b23a-4189-9225-867fe954664a",
  "abstract_Lean_extension_compiled": true,
  "actual_newpoint_parent_depth_certificate": "new_vertex_R4_parent_depth.json",
  "actual_graph_Lean_binding_complete": false,
  "abstract_Lean_extension_type_and_axioms_checked": true,
  "abstract_Lean_standard_axioms": [
    "propext",
    "Classical.choice",
    "Quot.sound"
  ],
  "new_axioms_added": false,
  "native_decide_used": false
}
```





**原始证据：** [research/ddp/global_coverage_20261027/candidate42343/README.md](../../research/ddp/global_coverage_20261027/candidate42343/README.md)；[research/ddp/global_coverage_20261027/candidate42343/parameters.json](../../research/ddp/global_coverage_20261027/candidate42343/parameters.json)；[research/ddp/global_coverage_20261027/candidate42343/generate.py](../../research/ddp/global_coverage_20261027/candidate42343/generate.py)；[research/ddp/global_coverage_20261027/candidate42343/FINAL_MATH_PROOF.md](../../research/ddp/global_coverage_20261027/candidate42343/FINAL_MATH_PROOF.md)；[research/ddp/global_coverage_20261027/candidate42343/graph_d12_D5_n42343.edges](../../research/ddp/global_coverage_20261027/candidate42343/graph_d12_D5_n42343.edges)；[research/ddp/global_coverage_20261027/candidate42343/independent_all_source_BFS.json](../../research/ddp/global_coverage_20261027/candidate42343/independent_all_source_BFS.json)；[research/ddp/global_coverage_20261027/candidate42343/verify_all.cpp](../../research/ddp/global_coverage_20261027/candidate42343/verify_all.cpp)；[research/ddp/global_coverage_20261027/candidate42343/BASELINE_REFRESH.json](../../research/ddp/global_coverage_20261027/candidate42343/BASELINE_REFRESH.json)；[research/ddp/global_coverage_20261027/candidate42343/dry_run_structure_check.json](../../research/ddp/global_coverage_20261027/candidate42343/dry_run_structure_check.json)；[reviews/ddp/h9_quadric_42343_final.raw.json](../../reviews/ddp/h9_quadric_42343_final.raw.json)；[reviews/ddp/h9_quadric_42343.DISPOSITION.md](../../reviews/ddp/h9_quadric_42343.DISPOSITION.md)；[research/ddp/global_coverage_20261027/candidate42343/new_vertex_R4_parent_depth.json](../../research/ddp/global_coverage_20261027/candidate42343/new_vertex_R4_parent_depth.json)；[research/ddp/global_coverage_20261027/candidate42343/new_vertex_R4_certificate_summary.json](../../research/ddp/global_coverage_20261027/candidate42343/new_vertex_R4_certificate_summary.json)；[research/ddp/global_coverage_20261027/candidate42343/lean_stage/HANDOFF.md](../../research/ddp/global_coverage_20261027/candidate42343/lean_stage/HANDOFF.md)；[research/ddp/global_coverage_20261027/candidate42343/lean_stage/STATUS.json](../../research/ddp/global_coverage_20261027/candidate42343/lean_stage/STATUS.json)；[formal/DegreeDiameter/Portfolio/SingleExtension.lean](../../formal/DegreeDiameter/Portfolio/SingleExtension.lean)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Preserve every edge of public42342 graph; append one vertex42342 with a fixed12-neighbor set:10 mandatory pins of an ambientQ-line and2 exact-completion anchors. One generated graph and one independent all-source verification.

**正向保证：** All245217 oldedges preserved plus12newedges; oldneighbors each had degree<=11.；Root independently rebuilt the rawsource graph and checked all42342 oldvertices lie within radius4 of the12pins.；Root rebuilt expanded edge list and ran all42343 ordinary BFS sources: maximum degree12, exactD5,0badpairs,0unreachable.；Deterministic generator dry-run reproduces the exact validated edge set without modifying it.；Official live table and linked description both still report42342; improvement1 and no exact-optimum claim.

**仍未完成：** 完整实际图的Lean验收仍未完成。通用SingleExtension与parentDepth soundness已build/类型公理核对，实际R4父深度证书已导出；旧图D5与具体图输入/edgefile/degree绑定仍需完成。Gemini最终SUCCESS，公开未提交，Goal ACTIVE。

**启发与重启依据：** 停止固定7线的剩余搜索：首完整解已满足存在性目标。由675个成功对象恢复Q-line的统一旧覆盖，再做有限degree筛及至多2anchors精确完整补全；不以坏对下降驱动续算。当前优先该新成果的交付、审阅与形式化。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

