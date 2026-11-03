---
type: experiment
node_id: exp:ddp-delorme-duality-spread-truncated12-inducedmatching-54-55-56-direct-comparison-20261101
title: "Delorme duality/spread＋一般matching复制：54/55/56比较保证55512/56540/57568"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_SMALL_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_small_check.py; research/ddp/two_successful_methods_20261101/public_baseline_audit/delorme1985_primary_text.txt; research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md"
added: 2026-11-01T16:56:30Z
tags: ["ddp", "method-ledger"]
---

# Delorme duality/spread＋一般matching复制：54/55/56比较保证55512/56540/57568

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** 多目标：54degree→[54, 3]／L=55512；55degree→[55, 3]／L=56540；56degree_comparison_only→[56, 3]／L=57568（逐变体，不合成一个距离）

**距目标的证据：** No largegraph generated/read; primary publishedingredients combined with oneactualstandard12controller/144threewalks/4openNpartition smallcertificate.；Delorme§1/§6的q16 symplectic GQ duality product，实际标准truncatedtetrahedron12点3度控制器144有序对恰三步覆盖，4中心openN分割。§8(a) spread经duality给257点ovoid，源52428/51regular，1028中心fullN分割全源但诱导514K2（独立中心预测被推翻）。用一般§7 matching复制而非dist≥3特例，k次后degree51+k、n52428+1028k，故54:55512、55:56540、56:57568。已接受56862/56943优势改1350/403。一次小图/标量原检查.0007805CPU，0大图/BFS/solver/Lean。 最新来源澄清：这些D3比较值是本项目代入／组合已发表方法得到的构造保证；未定位对应具体数字的作者独立边表，不是全球最大值认证。公式、primary URL、原文位置及适用条件见31参数来源索引。 54..59的1028Δ保证用Delorme的duality/spread/一般matching复制，并包含本项目明确构造的12点controller替代；不是论文直接印出的逐degree数值纪录，也不是找到55512/56540等作者rawedgepackage。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "large_graphs_generated_or_read": 0,
  "BFS_solver_Lean": 0,
  "finite_original_CPU": 0.0007805,
  "controller_graphs_checked": 1,
  "controller_order": 12,
  "controller_degree": 3,
  "exact_threewalk_pairs": 144,
  "controller_center_openN_partition": true,
  "q": 16,
  "source_formula_order": 52428,
  "source_formula_degree": 51,
  "centers": 1028,
  "center_induced_matching_edges": 514,
  "center_independence_prediction": "REFUTED_CORRECTED_MATCHING",
  "bounds": [
    {
      "Delta": 54,
      "D": 3,
      "order": 55512
    },
    {
      "Delta": 55,
      "D": 3,
      "order": 56540
    },
    {
      "Delta": 56,
      "D": 3,
      "order": 57568
    }
  ],
  "published_numeric_values_or_edgefiles_located": false,
  "original_D1_drawing_identified": false,
  "priority_or_globalrecord_certified": false,
  "new_56_graph_counted": false,
  "D3_comparison_evidence_identity": {
    "evidence_kind": "PROJECT_SUBSTITUTION_OR_COMBINATION_OF_PUBLISHED_METHODS",
    "numeric_author_edgefile_located": false,
    "global_maximum_established": false,
    "source_index": "research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json",
    "source_trace": "research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md",
    "mathematical_validity_and_existing_counts_unchanged": true
  },
  "D54_59_comparison_formula_identity": {
    "cap_range": [
      54,
      59
    ],
    "formula": "52428+(Delta-51)*1028=1028*Delta",
    "source": "Delorme1985§§1_6_7_8a",
    "explicit_12_controller_substitution_by_this_project": true,
    "paper_direct_numeric_record_list": false,
    "numeric_author_edgefile_located": false,
    "primary_urls": [
      "https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf"
    ],
    "note": "12点控制器代入和数值组合由本项目给出；不是论文直接印出的逐度数纪录"
  }
}
```



**从属变体：**
```json
[
  {
    "label": "54degree",
    "target": [
      54,
      3
    ],
    "savedL": 55512
  },
  {
    "label": "55degree",
    "target": [
      55,
      3
    ],
    "savedL": 56540
  },
  {
    "label": "56degree_comparison_only",
    "target": [
      56,
      3
    ],
    "savedL": 57568
  }
]
```

**原始证据：** [research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_SMALL_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_SMALL_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_small_check.py](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_small_check.py)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/delorme1985_primary_text.txt](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/delorme1985_primary_text.txt)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅本次明确published ingredient组合、q16经典symplecticGQ、任意选边定向与有精确三步覆盖的标准truncated12替换控制器；原文D1绘图未确认。中心4×257、诱导514K2，每次复制含新新matching及跨copy连接，逐原edge成K_(k+1,k+1)，不能套独立centers特例。

**正向保证：** 控制器(i,j),i≠j∈0..3，固定i成三角＋(i,j)↔(j,i)matching；C={(0,1),(1,0),(2,3),(3,2)}的openN分割12点且诱导2K2，实际保存144三词。；坐标关系Bf^ε相乘为B³f^(ε1+ε2+ε3)，duality与incidence relation交换，奇次方使GQ三步incidence覆盖成立；无需假定f为polarity或识别原D1图。；对同一published symplecticGQ的spreadS取O=f^-1(S)，每block恰交一次；C×O的每个顶点包括center恰一个center邻居，故center诱导matching，不是independent。；一般§7条件(a)空、(b)outside唯一center邻居、(c)matching每端50outside邻居给距离和≤3；可重复，所有点degree51+k，新增matching边明确计入。

**仍未完成：** 数值是本次从公开方法直接组合推导，未在原文定位列出的55512/56540/57568或独立公开edgefiles；不是全球最高或原创认证。未识别D1绘图、其他JGT1985全文缺口保持。56仅比较保证，当前没有新增accepted56图。

**启发与重启依据：** 初始独立center预测被实际2K2/514K2推翻，改用published一般inducedmatching复制与实际度账，比较数值仍严格成立并增强。替代旧55350/56375，并纠正raw最终C中的旧优势；图/Lean定义不变，不付费重审或重跑大图。此audit只核一个标准小controller与标量，不派q/controller/degree列表。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

