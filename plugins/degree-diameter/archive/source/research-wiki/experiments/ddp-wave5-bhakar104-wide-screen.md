---
type: experiment
node_id: exp:ddp-wave5-bhakar104-wide-screen
title: "固定Bhakar104的宽chart必要筛与唯一短路容量"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/REPORT.md; research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/NB2_NB4_counts.json; research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/RESULT.json; research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/five_cycle_edge_counts.json; research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/raw_missing_pairs.json; research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/screen.py; research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/witness.independent_check.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# 固定Bhakar104的宽chart必要筛与唯一短路容量

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (12,4)；L=5832；条件性n=8424（未据此计纪录）

**距目标的证据：** 0→32全部≤4walk恰唯一三路，至多27<81；固定投影提升统一不行。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 104,
  "source_known_D": 4,
  "raw_missing_ordered_pairs": 3008,
  "raw_missing_unordered_pairs": 1504,
  "all_walk_counts_len0_to4": [
    0,
    0,
    0,
    1,
    0
  ],
  "fiber_capacity": 27,
  "required": 81
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/REPORT.md](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/REPORT.md)；[research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/NB2_NB4_counts.json](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/NB2_NB4_counts.json)；[research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/RESULT.json](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/RESULT.json)；[research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/five_cycle_edge_counts.json](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/five_cycle_edge_counts.json)；[research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/raw_missing_pairs.json](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/raw_missing_pairs.json)；[research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/screen.py](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/screen.py)；[research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/witness.independent_check.json](../../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/witness.independent_check.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定104投影、81fiber、每控制边每点至多3邻点且无额外fiber/非投影边

**正向保证：** 复用源104 ordinaryD4；raw必要筛先于标号搜索

**仍未完成：** raw I/NB2/NB4缺口本身只排充分证书；真正提升排除另由唯一全walk容量证明。

**启发与重启依据：** 只有改变固定投影或允许不同边机制才可能突破，改标签不够。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

