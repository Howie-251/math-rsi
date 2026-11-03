---
type: experiment
node_id: exp:ddp-conder1250-edge-subdivision-two-cut-helper-family-20261027
title: "Conder1250 edgeinsertions:singlefamilyD11;all5614two-cut/helperedgeobjects failnewrootR10"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/REPORT.md; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/PREDICTION.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/SOURCE_BINDING.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/FROZEN_OBJECTS.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/A_RESULT.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/B_CASES.jsonl; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/RESULT.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/probe.cpp; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/run.py; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/native.log; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/cursor.json; research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/terminal.json; research/ddp/more_graphs_20261027/d3_D10_current1250_source/source1250.edges; research/ddp/more_graphs_20261027/d3_D10_current1250_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d3_D10_current1250_source/SOURCE_REPORT.md"
added: 2026-10-27T23:23:55Z
tags: ["ddp", "method-ledger"]
---

# Conder1250 edgeinsertions:singlefamilyD11;all5614two-cut/helperedgeobjects failnewrootR10

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (3,10)；L=1250；candidate_graph_or_family n=1252

**距目标的证据：** Aactual1251/1876/max3newdegree2 haswitness(1250,1178)>10;universalupper11givesexactD11. Bactual5614simplecubic1252/1878graphs allhavefirstnewx>10counterexample,0UNKNOWN/unattempted;theirglobalDnull,ordinarybadpairsnull. EdgeVTandfrozencompleteobjectscloseonlytheliteralinsertionfamily. 0newLB/0positiveexports.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 1250,
  "source_m": 1875,
  "source_reported_D": 10,
  "source_published_girth": 16,
  "source_published_Aut_order": 15000,
  "source_edge_VT_inherited": true,
  "source_old_BFS": 0,
  "anchor": [
    0,
    1
  ],
  "A": {
    "name": "A_single_edge_subdivision",
    "actual_n": 1251,
    "actual_m": 1876,
    "actual_D": 11,
    "max_degree": 3,
    "new_vertex_degree": 2,
    "modified_graphs": 1,
    "modified_BFS_roots": 1,
    "first_bad_pair": [
      1250,
      1178
    ],
    "scope": "AllsourceedgesbyedgeVT",
    "global_D_evidence": "OneR10witnessplusinheritedglobalupper11"
  },
  "B": {
    "name": "B_two_cut_two_helper_edge",
    "actual_n": 1252,
    "actual_m": 1878,
    "actual_D": null,
    "distance_lower_bound": 11,
    "max_degree": 3,
    "regular": true,
    "modified_graphs": 5614,
    "modified_BFS_roots": 5614,
    "first_bad_pair": [
      1250,
      1178
    ],
    "objects_unknown": 0,
    "objects_unattempted": 0,
    "scope": "Allanchoredsecondedgesandvalidunordered2+2multisetpartitions;edgeVTextendsallliteral2cutchoices,notgeneralgraphs"
  },
  "B_objects_total": 5614,
  "B_disjoint_objects": 5610,
  "B_shared_endpoint_objects": 4,
  "B_objects_nonisomorphic_claim": false,
  "B_objects_failed": 5614,
  "B_objects_unknown": 0,
  "B_objects_unattempted": 0,
  "B_new_x_failures": 5614,
  "B_new_y_checks": 0,
  "B_oldroot_checks": 0,
  "total_modified_graphs": 5615,
  "total_modified_R10_BFS": 5615,
  "ordinary_bad_pair_count_scope": "Null;witnesspairsarenotallbadpaircounts",
  "native_CPU_seconds": 0.377177,
  "native_process_CPU_seconds": 0.37922000000000033,
  "compile_CPU_seconds": 1.1627959999999997,
  "total_parent_children_CPU_seconds": 1.542226,
  "prediction": "REFUTED_COMPLETE_FIXED_FAMILY",
  "UNKNOWN": 0,
  "new_lower_bounds": 0
}
```



**从属变体：**
```json
[
  {
    "name": "A_single_edge_subdivision",
    "actual_n": 1251,
    "actual_m": 1876,
    "actual_D": 11,
    "max_degree": 3,
    "new_vertex_degree": 2,
    "modified_graphs": 1,
    "modified_BFS_roots": 1,
    "first_bad_pair": [
      1250,
      1178
    ],
    "scope": "AllsourceedgesbyedgeVT",
    "global_D_evidence": "OneR10witnessplusinheritedglobalupper11"
  },
  {
    "name": "B_two_cut_two_helper_edge",
    "actual_n": 1252,
    "actual_m": 1878,
    "actual_D": null,
    "distance_lower_bound": 11,
    "max_degree": 3,
    "regular": true,
    "modified_graphs": 5614,
    "modified_BFS_roots": 5614,
    "first_bad_pair": [
      1250,
      1178
    ],
    "objects_unknown": 0,
    "objects_unattempted": 0,
    "scope": "Allanchoredsecondedgesandvalidunordered2+2multisetpartitions;edgeVTextendsallliteral2cutchoices,notgeneralgraphs"
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/REPORT.md](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/REPORT.md)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/PREDICTION.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/PREDICTION.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/SOURCE_BINDING.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/SOURCE_BINDING.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/FROZEN_OBJECTS.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/FROZEN_OBJECTS.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/A_RESULT.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/A_RESULT.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/B_CASES.jsonl](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/B_CASES.jsonl)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/RESULT.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/RESULT.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/probe.cpp](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/probe.cpp)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/run.py](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/run.py)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/native.log](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/native.log)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/cursor.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/cursor.json)；[research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/terminal.json](../../research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/terminal.json)；[research/ddp/more_graphs_20261027/d3_D10_current1250_source/source1250.edges](../../research/ddp/more_graphs_20261027/d3_D10_current1250_source/source1250.edges)；[research/ddp/more_graphs_20261027/d3_D10_current1250_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d3_D10_current1250_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d3_D10_current1250_source/SOURCE_REPORT.md](../../research/ddp/more_graphs_20261027/d3_D10_current1250_source/SOURCE_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** FixedactualConderC1250.2raw1250/1875sourceonly. AonelexanchorsubdivisionrepresentsallsourceedgesbyedgeVT. AfterAfailure,Ball1874otheredges/validunordered2+2endpointmultisetpartitionsgive5614frozenobjects,newx/ywith2oldpinsandxyedge. EveryactualmodifiedgraphnewxR10fails,so0newy/oldrootchecks. No sourceD10BFS/noSAT/thirdcut/helper/otherarchitecture.

**仍未完成：** General1251/1252graphs,other1250hosts,moregeneralrewiring/helperattachmentsarenotexcluded. Bexactdiametersandordinaryunorderedbadpairswerenotmeasured. Frozenobjectsarenotnonisomorphismclasses.

**启发与重启依据：** Highsourcearc-symmetrymakesafullliteralinsertionfamilycheaptoexhaust,butdoesnotguaranteenewrootcoverage. Hereallnegativegraphsarealreadyrejectedbythenewroot;nooldoldverificationwasneeded. Stopthisarchitecture;donotmechanicallyaddthirdcut/helperormicrorepairwitnesses.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- D16_16416_715_PACKING1250_DELTA_20261101 -->
## 2026-11-01 19:36:04 UTC 同机制最新增量，原验收历史保留

本轮仅回看既有ConderC1250.2来源/旧scope：实际nonbipartite，不能套bipartite自动细分覆盖。单细分anchor新根到1178距11、edgeVT覆盖全部1875旧边，以及5614两cut/相邻helper对象全首新根R10失败，均严格继承、0重跑。0新HTTP/rawparse/degree/2color/BFS/候选，.122109397/5CPU；不是新source验收或新方法。STOP以上exactscope；真正threegenuinecuts/repair仍UNKNOWN且未运行，不自动派发。原完整结论与证据保留。
