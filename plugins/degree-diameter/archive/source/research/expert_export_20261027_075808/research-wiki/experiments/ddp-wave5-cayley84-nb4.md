---
type: experiment
node_id: exp:ddp-wave5-cayley84-nb4
title: "固定F7⋊₃C12 quartic Cayley控制器完整筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/cayley84_nb4/REPORT.md; research/ddp/breadth_20261027_wave5/cayley84_nb4/all_sets.json; research/ddp/breadth_20261027_wave5/cayley84_nb4/best_word_coverage.json; research/ddp/breadth_20261027_wave5/cayley84_nb4/first_probe.json; research/ddp/breadth_20261027_wave5/cayley84_nb4/group.json; research/ddp/breadth_20261027_wave5/cayley84_nb4/run.py; research/ddp/breadth_20261027_wave5/cayley84_nb4/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 固定F7⋊₃C12 quartic Cayley控制器完整筛

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** word-endpoint-exhaustion

**目标与阶数：** (12,4)；L=5832；条件性n=6804（未据此计纪录）

**距目标的证据：** 722组phase容量不足，98组真群词仅到12或44点，无exact-NB4。

**其他指标（保持原计数类型）：**
```json
{
  "hypothetical_controller_n": 84,
  "sets_examined": 820,
  "phase_rejected": 722,
  "true_word_passers": 98,
  "max_exact_NB4_endpoint_count_among_passers": 44,
  "words_per_set": 108
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/cayley84_nb4/REPORT.md](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/REPORT.md)；[research/ddp/breadth_20261027_wave5/cayley84_nb4/all_sets.json](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/all_sets.json)；[research/ddp/breadth_20261027_wave5/cayley84_nb4/best_word_coverage.json](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/best_word_coverage.json)；[research/ddp/breadth_20261027_wave5/cayley84_nb4/first_probe.json](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/first_probe.json)；[research/ddp/breadth_20261027_wave5/cayley84_nb4/group.json](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/group.json)；[research/ddp/breadth_20261027_wave5/cayley84_nb4/run.py](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/run.py)；[research/ddp/breadth_20261027_wave5/cayley84_nb4/terminal.json](../../research/ddp/breadth_20261027_wave5/cayley84_nb4/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 该固定84阶群全部820个simple inverse-closed四元生成集

**正向保证：** 完整inverse-closed组成已覆盖；Cayley左作用使单位根端点代表全部根

**仍未完成：** 未排其他群或非Cayley84控制器；无普通D测量。

**启发与重启依据：** 固定群范围关闭，不能仅追加seed/另种S组成。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

