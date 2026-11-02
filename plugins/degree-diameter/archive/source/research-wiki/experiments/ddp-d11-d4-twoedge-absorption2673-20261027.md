---
type: experiment
node_id: exp:ddp-d11-d4-twoedge-absorption2673-20261027
title: "(11,4)两host边吸收2673项全闭：47新根通过但旧对损坏"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/REPORT.md; research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/RESULT.json; research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/PROOF.md; research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/frozen.json; research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/first_oldpair_witness.json"
added: 2026-10-27T18:21:15Z
tags: ["ddp", "method-ledger"]
---

# (11,4)两host边吸收2673项全闭：47新根通过但旧对损坏

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (11,4)；L=3645；条件性n=3646（未据此计纪录）

**距目标的证据：** 冻结实际存在两point-copy/host边2673项，删F，新x连4端点+all7free=11。2626项source R3(S)不足，47项新根完整但旧旧D4反例，0新图、0未试/UNKNOWN。代表ordinal127点p40，3352到2244在修改后>4，不猜精确D或全图坏对数。

**其他指标（保持原计数类型）：**
```json
{
  "candidates": 2673,
  "R3_screen_failures": 2626,
  "R3_passers": 47,
  "oldpair_failures": 47,
  "modified_root_BFS": 1432,
  "max_old_roots": 44,
  "endpoint_R3_preparations": 1964,
  "CPU_total": 2.599767662,
  "native_CPU": 0.100774,
  "newgraphs": 0,
  "source_allBFS_revalidation": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/RESULT.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/PROOF.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/PROOF.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/frozen.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/frozen.json)；[research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/first_oldpair_witness.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_pair_probe/first_oldpair_witness.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 冻结实际存在两point-copy/host边2673项，删F，新x连4端点+all7free=11。2626项source R3(S)不足，47项新根完整但旧旧D4反例，0新图、0未试/UNKNOWN。代表ordinal127点p40，3352到2244在修改后>4，不猜精确D或全图坏对数。

**仍未完成：** No complete newgraph in this finite experiment; unrelatedrules and finalLean remain open.

**启发与重启依据：** 新根覆盖不是完整图验收。精确低成本验证证明：F端点⊂S给dist_G-F(v,S)=dist_G(v,S)；旧pair若两端均outsideR1_G(Fendpoints)则任何≤4路不经F，故检查至多44旧根+新根完整而非抽样。全两edge+7free固定类已闭；新paired-switch吸收是不同删除集合，须另有预测。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

