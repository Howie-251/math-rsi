---
type: experiment
node_id: exp:ddp-wave2-two-orbit128-scout
title: "Q64双轨道2+4：phase容量来源筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/two_orbit128_scout/RESULT.json; research/ddp/breadth_20261027_wave2/two_orbit128_scout/SCOPE.md; research/ddp/breadth_20261027_wave2/two_orbit128_scout/TIGHT_SUM.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# Q64双轨道2+4：phase容量来源筛

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity-pass-scout

**目标与阶数：** (6,3)；L=120；条件性n=128（未据此计纪录）

**距目标的证据：** 14模式通过，未作参数搜索；交给后续独立有限profile。

**其他指标（保持原计数类型）：**
```json
{
  "phase_patterns": 32,
  "surviving_patterns": 14,
  "actual_searches": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/two_orbit128_scout/RESULT.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_scout/RESULT.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_scout/SCOPE.md](../../research/ddp/breadth_20261027_wave2/two_orbit128_scout/SCOPE.md)；[research/ddp/breadth_20261027_wave2/two_orbit128_scout/TIGHT_SUM.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_scout/TIGHT_SUM.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 32个phase模式；只是必要容量筛

**正向保证：** 32phasefiber各需32状态；短词算术校准

**仍未完成：** 容量通过不是D3存在证据。

**启发与重启依据：** 只建议一次有界实际profile，已由search执行。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

