---
type: experiment
node_id: exp:ddp-h9-d13-51417-source-binding-20261027
title: "公开(13,5)51417图绑定：50554核心+863 extras"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/CORE_COVER_TRANSFER.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/READY_FOR_POOL.json; research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/PREDICTION.md; research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/REPORT.md; research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/RESULT.json; research/ddp/refresh_20261029/C11_CAPACITY_AUTGATE_WIKI_REPORT.md; research/ddp/refresh_20261029/d13_core_swap_extension_signature/CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json; research/ddp/refresh_20261029/d13_core_swap_extension_signature/PERIPHERAL_SIGNATURES.json; research/ddp/refresh_20261029/d13_core_swap_extension_signature/PREDICTION.md; research/ddp/refresh_20261029/d13_core_swap_extension_signature/REPORT.md; research/ddp/refresh_20261029/d13_core_swap_extension_signature/RESULT.json; research/ddp/refresh_20261029/d13_core_swap_extension_signature/TERMINAL.json; research/ddp/refresh_20261029/d13_core_swap_extension_signature/check_once.py; research/ddp/refresh_20261029/C33_REVIEW_D13_SWAP_POOL_WIKI_REPORT.md"
added: 2026-10-29T22:28:55Z
tags: ["ddp", "method-ledger"]
---

# 公开(13,5)51417图绑定：50554核心+863 extras

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,5)；L=51417；known_source_or_recovery n=51417

**距目标的证据：** 源51417/m324451/max13，核心50554的33397类商图与F逐边一致；current核心与旧core有2706边替换，不能假设旧raw orientation。每个类块complete或perfect matching，故可lift所有F短路，whole-class阻塞邻域保证核心R4。；full-Aut输入门为PERIPHERAL_BINDING_MISSING，0source边表读/edgecheck/BFS/solver；这是所需置换未提供，不是无非平凡Aut或Aut-image池无解。；外围50629的core邻域签名原重数1，施该core swap后重数0，故即使外围任意置换也不能延拓这个core swap；一次source读、0BFS/solver、0.304361371CPU。

**其他指标（保持原计数类型）：**
```json
{
  "core_n": 50554,
  "extras": 863,
  "free_vertices": 13248,
  "free_core_vertices": 12946,
  "free_extra_vertices": 302,
  "removed_core_edges": 2706,
  "added_core_edges": 2706,
  "full_source_Aut_bound": false,
  "full_Aut_gate_completed_as_read_only": true,
  "full_Aut_gate_edge_checks": 0,
  "full_Aut_nonexistence_proven": false,
  "specified_core_swap_full_extension_excluded": true,
  "specified_core_swap_extension_witness": 50629,
  "specified_core_swap_target_signature_multiplicity": 0
}
```



**从属变体：**
```json
[
  {
    "label": "originalB0_full_automorphism_transport_bounded_input_gate_20261029",
    "status": "PERIPHERAL_BINDING_MISSING_IN_BOUNDED_READ_SCOPE",
    "base_n": 51417,
    "base_m": 324451,
    "core_n": 50554,
    "peripheral_n": 863,
    "certified_operation": "simultaneous swap ofsavedcore splitpairs only; phi=tau²",
    "whole_source_peripheral_permutation_available": false,
    "source_files_read": 5,
    "source_graph_reads": 0,
    "full_edge_set_checks": 0,
    "BFS_runs": 0,
    "transported_neighborhoods": 0,
    "solver_calls": 0,
    "automorphism_nonexistence_claimed": false,
    "original40_Aut_image_pool_excluded": false,
    "restart_requires": "An explicit compatible peripheral-image permutation and full source automorphism binding, or a separately justified alternative action."
  },
  {
    "label": "specified_core_swap_full_extension_signature_multiplicity_gate_20261029",
    "status": "SPECIFIED_CORE_SWAP_HAS_NO_FULL_AUTOMORPHISM_EXTENSION",
    "base_n": 51417,
    "base_m": 324451,
    "core_n": 50554,
    "peripheral_n": 863,
    "inherited_core_swap_pairs": 17157,
    "core_automorphism_rechecked": false,
    "source_graph_reads": 1,
    "peripheral_signature_groups": 843,
    "signature_group_size_histogram": {
      "1": 826,
      "2": 14,
      "3": 3
    },
    "compared_signature_groups": 68,
    "obstruction": {
      "source_peripheral_vertices": [
        50629
      ],
      "source_core_neighbors": [
        61,
        5156,
        10143,
        15136,
        21698,
        28257,
        34765,
        38196,
        41629,
        44965
      ],
      "transformed_core_neighbors": [
        64,
        5159,
        10146,
        15130,
        21692,
        28251,
        34768,
        38199,
        41632,
        44965
      ],
      "source_multiplicity": 1,
      "target_multiplicity": 0,
      "matching_target_peripheral_vertices": []
    },
    "exclusion": "This specified core involution cannot extend to a full-source automorphism, even with an arbitrary permutation of the863 peripheral vertices.",
    "all_full_source_automorphisms_excluded": false,
    "full_edge_automorphism_checks": 0,
    "BFS_calls": 0,
    "solver_calls": 0,
    "new_graphs": 0,
    "CPU_seconds": 0.304361371
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/CORE_COVER_TRANSFER.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/CORE_COVER_TRANSFER.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/READY_FOR_POOL.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/READY_FOR_POOL.json)；[research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/PREDICTION.md](../../research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/PREDICTION.md)；[research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/REPORT.md](../../research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/REPORT.md)；[research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/RESULT.json](../../research/ddp/refresh_20261029/d13_B0_full_automorphism_gate/RESULT.json)；[research/ddp/refresh_20261029/C11_CAPACITY_AUTGATE_WIKI_REPORT.md](../../research/ddp/refresh_20261029/C11_CAPACITY_AUTGATE_WIKI_REPORT.md)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/PERIPHERAL_SIGNATURES.json](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/PERIPHERAL_SIGNATURES.json)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/PREDICTION.md](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/PREDICTION.md)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/REPORT.md](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/REPORT.md)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/RESULT.json](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/RESULT.json)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/TERMINAL.json](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/TERMINAL.json)；[research/ddp/refresh_20261029/d13_core_swap_extension_signature/check_once.py](../../research/ddp/refresh_20261029/d13_core_swap_extension_signature/check_once.py)；[research/ddp/refresh_20261029/C33_REVIEW_D13_SWAP_POOL_WIKI_REPORT.md](../../research/ddp/refresh_20261029/C33_REVIEW_D13_SWAP_POOL_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actual published51417 source binding and stable/whole-class core coverage only; sourceD5 inherited publicly, not allsource reverified.；后续原B0全图Aut搬运40邻域入口仅完成5文件读取门：已证操作只到50554core，863外围无绑定，未验任何全图置换或生成imagepool。；随后一次literal边表签名门严格否定这个指定core involution的任意外围延拓，不否定其它全图自同构。

**仍未完成：** 指定core involution的全图延拓已由外围签名重数1≠0严格排除。其它全图自同构及其混合邻域池未排；另行固定外围guard的literal候选不是全图Aut，须实际验证覆盖，不能继承Aut结论。

**启发与重启依据：** 稳定B15可不依赖pair orientation迁移；raw非稳定集合须先恢复真正映射或取whole-class closure。实际13248点有degree余量，但不推出邻域合法。；不能把core phi=tau²外推到外围或任意固定863外围。旧wholeclass几何pool、max40 multiplicity和P40clique不包含新Aut-image邻域池；须有显式全图绑定才可搬运原B0完整覆盖。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

