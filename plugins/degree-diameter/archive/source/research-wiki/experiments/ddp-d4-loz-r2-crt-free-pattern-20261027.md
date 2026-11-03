---
type: experiment
node_id: exp:ddp-d4-loz-r2-crt-free-pattern-20261027
title: "Loz固定r2四逆对相位：四个可改善CRT模数全自由平移范围无图"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_crt75_free_translation/REPORT.md; research/ddp/more_graphs_20261027/d4_crt75_free_translation/PREDICTION.json; research/ddp/more_graphs_20261027/d4_crt75_free_translation/CAPACITY.json; research/ddp/more_graphs_20261027/d4_crt75_free_translation/RESULT.json; research/ddp/more_graphs_20261027/d4_crt75_free_translation/OTHER_DIVISORS_RESULT.json; research/ddp/more_graphs_20261027/d4_crt75_free_translation/check.py; research/ddp/more_graphs_20261027/d4_crt75_free_translation/other_divisors.py"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# Loz固定r2四逆对相位：四个可改善CRT模数全自由平移范围无图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (8,4)；L=1100；条件性n=1500（未据此计纪录）

**距目标的证据：** Exactidentity-root phase10 wordcoverage, no edgegraph/BFS generated.；75/93/123全部规范平移类无薄层幸存；155的phase10形式144<155统一排除。0新图，不能外推其它phase/action。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "normalized_scope": 76166,
  "full_cover_hits": 0,
  "CPU_seconds": 0.881899082,
  "prediction_supported": false,
  "allsource_BFS": 0,
  "global_family_excluded": false,
  "closed_moduli": [
    75,
    93,
    123,
    155
  ]
}
```



**从属变体：**
```json
[
  {
    "modulus": 75,
    "hypothetical_order": 1500,
    "normalized_classes": 10075,
    "actual_n": null
  },
  {
    "modulus": 93,
    "hypothetical_order": 1860,
    "normalized_classes": 12909,
    "actual_n": null
  },
  {
    "modulus": 123,
    "hypothetical_order": 2460,
    "normalized_classes": 22399,
    "actual_n": null
  },
  {
    "modulus": 155,
    "hypothetical_order": 3100,
    "normalized_classes": 30783,
    "actual_n": null
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d4_crt75_free_translation/REPORT.md](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/REPORT.md)；[research/ddp/more_graphs_20261027/d4_crt75_free_translation/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_crt75_free_translation/CAPACITY.json](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/CAPACITY.json)；[research/ddp/more_graphs_20261027/d4_crt75_free_translation/RESULT.json](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/RESULT.json)；[research/ddp/more_graphs_20261027/d4_crt75_free_translation/OTHER_DIVISORS_RESULT.json](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/OTHER_DIVISORS_RESULT.json)；[research/ddp/more_graphs_20261027/d4_crt75_free_translation/check.py](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/check.py)；[research/ddp/more_graphs_20261027/d4_crt75_free_translation/other_divisors.py](../../research/ddp/more_graphs_20261027/d4_crt75_free_translation/other_divisors.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixedr2,phases1/12/11/16,all legal targetmoduli75/93/123/155 in55<m<=160; all connectedtranslations modulo unit scaling or a uniformphasecapacity bound.

**正向保证：** Primitive ringtriples are normalized locally, so cases with no globalunitcoordinate are included.；Canonical knownrejections reused for93/123; m75 includes one previously testedcanonical class.；No oldsourceBFS or failedgraph allsourcecheck.

**仍未完成：** Differentactions/phases and othergraphmechanisms remain open.

**启发与重启依据：** CRT/nilpotent structure alone did not repair the thinphase in thisfixedsource profile. Stop the completefinite scope, change routephase structure rather than tune the bestfailed parameters.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

