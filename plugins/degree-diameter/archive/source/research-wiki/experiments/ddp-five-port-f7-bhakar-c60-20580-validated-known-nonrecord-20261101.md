---
type: experiment
node_id: exp:ddp-five-port-f7-bhakar-c60-20580-validated-known-nonrecord-20261101
title: "Bhakar C60与F7五端口：20580点35正则D3完整独验，但已知35度35875更大"
idea_id: "idea:ddp-q3-three-step-plane-pencil31"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/f7_c60_d35/PREDICTION.md; research/ddp/two_successful_methods_20261101/f7_c60_d35/PROOF.md; research/ddp/two_successful_methods_20261101/f7_c60_d35/REPORT.md; research/ddp/two_successful_methods_20261101/f7_c60_d35/PUBLIC_COMPARISON.md; research/ddp/two_successful_methods_20261101/f7_c60_d35/PARAMETERS.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/GATE_RESULT.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/GENERATION_RESULT.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/CONTROLLER_ROUTE_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/LOCAL_CHART_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/graph_d35_D3_n20580.edges; research/ddp/two_successful_methods_20261101/f7_c60_d35/generate.py; research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/PRED.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/SUMMARY.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/INDEPENDENT_ACCEPTANCE.json; research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/check_literal_graph.py; research/ddp/two_successful_methods_20261101/reviews/F7_GEMINI_RAW.json; research/ddp/two_successful_methods_20261101/reviews/F7_DISPOSITION.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json; research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md"
added: 2026-11-01T16:56:30Z
tags: ["ddp", "method-ledger"]
---

# Bhakar C60与F7五端口：20580点35正则D3完整独验，但已知35度35875更大

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-q3-three-step-plane-pencil31`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (35,3)；L=35875；candidate_graph_or_family n=20580

**距目标的证据：** 实际D=3，目标D=3；普通无序坏对=0；Independent literal graph BFS from all20580 vertices; simple35regular/connected, every R3 full, exactD3；实际20580/360150、simple无向35regular、exactD3；独立全部20580根PASS，CPU1.707838828。完整3600控制pair与六chart96turn/full8-plane证书先通过，随后仅生成一图。Primary Delorme及replication给35度D3已知35875>20580，差15295，故明确非纪录，不是novelty pending。 最新来源澄清：这些D3比较值是本项目代入／组合已发表方法得到的构造保证；未定位对应具体数字的作者独立边表，不是全球最大值认证。公式、primary URL、原文位置及适用条件见31参数来源索引。 35度35875精确为Delorme q32=2^5极性商33825/max33/D3，加2×1025个absolute副本；原EJC §2 p292、§7 pp297–298、§8(c)p299，现代arxiv亦重述。不是Mizuno35 package，也未找到35875独立作者边表；甚至公开max33/33825已在cap35超过本地20580，保原非竞争判断而不称35875全球最大。

**其他指标（保持原计数类型）：**
```json
{
  "validated_graph_instances": [
    {
      "Delta": 35,
      "D": 3,
      "n": 20580,
      "m": 360150,
      "mathematically_validated_complete_graph": true,
      "complete_Lean_graph_instance": false,
      "known_nonrecord": true,
      "public_comparison_status": "KNOWN_NONRECORD_PRIMARY_BOUND",
      "compared_known_lower_bound": 35875,
      "comparison_is_latest_global_optimum": false,
      "latest_global_record_confirmed": false
    }
  ],
  "mathematically_validated_complete_graph": true,
  "new_lower_bound_mathematically_verified": false,
  "actual_order": 20580,
  "actual_edges": 360150,
  "min_degree": 35,
  "max_degree": 35,
  "diameter_exact": 3,
  "roots_checked": 20580,
  "graph_generation_CPU_seconds": 0.348461891,
  "local_gate_CPU_seconds": 0.04097255599999999,
  "independent_all_root_CPU_seconds": 1.707838828,
  "actual_charts": 6,
  "central_turns_rank3": 96,
  "adjacent_planes": 8,
  "plane_union": 343,
  "controller_order": 60,
  "controller_degree": 5,
  "controller_author": "Bhakar (f4t4nt)",
  "framework_credit": "General affine route-chart method inherited; C60 is Bhakar/f4t4nt, not Mizuno C30.",
  "controller_pairs": 3600,
  "adjacent_pairs": 300,
  "required_NB3_pairs": 3300,
  "complete_Lean_graph_instance": false,
  "new_Lean_instances": 0,
  "known_nonrecord": true,
  "compared_known_lower_bound": 35875,
  "improvement_vs_compared_known_bound": -15295,
  "public_comparison": "Delorme1985 q32:33degree33825; two absolute-vertex replicas give35degree35875. Sufficient to show nonrecord, not latest global optimum.",
  "obsolete_comparison_not_used": "13272 is only one PolarStar-family instance",
  "static_review_status": "SUCCESS",
  "first_A_B_review_does_not_cover_this": true,
  "static_review_thread": "7548e5af-769d-4736-a7d2-0ae080f78318",
  "independent_construction_framework_claimed": false,
  "static_review_model": "gemini-3.8-flash-high",
  "static_review_effort": "high",
  "static_review_selectedModelLabel": "Gemini 3.8 Flash (High)",
  "static_review_scope": "F7 six true-inverse charts, oriented matching,96turn/eight-plane/3600pair coverage and known-nonrecord public comparison only; excludesF4 and completeLean.",
  "static_review_code_execution": false,
  "static_review_is_graph_validation": false,
  "D3_comparison_evidence_identity": {
    "evidence_kind": "PROJECT_SUBSTITUTION_OR_COMBINATION_OF_PUBLISHED_METHODS",
    "numeric_author_edgefile_located": false,
    "global_maximum_established": false,
    "source_index": "research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json",
    "source_trace": "research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md",
    "mathematical_validity_and_existing_counts_unchanged": true
  },
  "D35_35875_evidence_identity": {
    "formula": "33825 + 2×1025 = 35875",
    "q": 32,
    "q_legality": "2^5",
    "source_order33825": 33825,
    "source_maxdegree": 33,
    "absolute_points": 1025,
    "copies": 2,
    "primary_urls": [
      "https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf",
      "https://arxiv.org/html/2608.27253v2#S7.SS7"
    ],
    "primary_locations": "Delorme §2 p292、§7 pp297–298、§8(c)p299；q=32=2^5合法",
    "not_Mizuno35_package": true,
    "numeric_author_edgefile_located": false,
    "not_global_maximum": true,
    "even_degree33_order33825_alone_blocks_local20580": true
  }
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/f7_c60_d35/PREDICTION.md](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/PREDICTION.md)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/PROOF.md](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/PROOF.md)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/REPORT.md](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/REPORT.md)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/PUBLIC_COMPARISON.md](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/PUBLIC_COMPARISON.md)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/GATE_RESULT.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/GATE_RESULT.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/GENERATION_RESULT.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/GENERATION_RESULT.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/CONTROLLER_ROUTE_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/CONTROLLER_ROUTE_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/LOCAL_CHART_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/LOCAL_CHART_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/graph_d35_D3_n20580.edges](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/graph_d35_D3_n20580.edges)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/generate.py](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/generate.py)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/PRED.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/PRED.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/SUMMARY.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/SUMMARY.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/INDEPENDENT_ACCEPTANCE.json](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/INDEPENDENT_ACCEPTANCE.json)；[research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/check_literal_graph.py](../../research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/check_literal_graph.py)；[research/ddp/two_successful_methods_20261101/reviews/F7_GEMINI_RAW.json](../../research/ddp/two_successful_methods_20261101/reviews/F7_GEMINI_RAW.json)；[research/ddp/two_successful_methods_20261101/reviews/F7_DISPOSITION.md](../../research/ddp/two_successful_methods_20261101/reviews/F7_DISPOSITION.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly literal60-point5regular Bhakar(f4t4nt) controller from saved1620 source darts; fibresF7^3; fixed five conic directions; six invertible charts, paired inverse ports0/1 and2/3, matching port4 uses T4 orT4^-1 by dart orientation. No field/chart/controller search or source1620/3750 revalidation. General route-chart framework is inherited, while this concrete five-port chart is new local instance.

**正向保证：** 全部300实际dart真逆绑定、六chart96个中央turn满秩、每chart八个共线平面并覆盖343。；所有3600控制层ordered pairs：300adjacent用pencil，其余3300含对角均有NB3，覆盖所有源/目标坐标。；独验实际读取边表全部20580根，所有closedR3等全顶点集，degree35且simple、connected。

**仍未完成：** 本具体图完整Lean未完成。F7补充Gemini审阅已真实SUCCESS，范围仅六chart真逆、matching定向、96turn及八平面覆盖/3600层对与Delorme已知非纪录比较；未执行BFS/编译/solver，也不覆盖F4新3840图或其Lean。20580仍明确小于已知35875，非纪录状态不因审阅改变。

**启发与重启依据：** 四端口/F5的两组三射影点扩为五端口/F7互补四点，odd port匹配须定向使用真inverse charts，确实产生完整D3推广。下一选题优先真实公开比较与可迁移条件，不因本非纪录图自动续controller66、更多q或形式化梯子。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

