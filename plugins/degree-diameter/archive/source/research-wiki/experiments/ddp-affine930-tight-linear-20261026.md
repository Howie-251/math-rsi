---
type: experiment
node_id: exp:ddp-affine930-tight-linear-20261026
title: "紧31形式纤维的排列求和必要约束"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, one worker per bounded batch"
duration: "0.284762963 linear +0.061504938 quadratic-diagnostic CPU s"
provenance: "research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_TIGHT_LINEAR.md"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 紧31形式纤维的排列求和必要约束

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** (11,3)；L=715

**距目标的证据：** d11 modes78→75;fivepair38modes markedscope8260050;fourpair37modes1094587872. No actualgraphs inthisstep.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family.

**其他指标（保持原计数类型）：**
```json
{
  "superseding_existing_wiki": [
    {
      "path": "research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md",
      "note": "Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family."
    }
  ]
}
```

**既有原文指标：** d11 modes78→75;fivepair38modes markedscope8260050;fourpair37modes1094587872. No actualgraphs inthisstep.



**原始证据：** [research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_TIGHT_LINEAR.md](../../research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_TIGHT_LINEAR.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly31 forms coveringF31 havezero sum. Onlyz normalized innullspace. Later quadratic ranks4/5 give no additional exclusion or linearization.

**启发与重启依据：** Exactly31 forms coveringF31 havezero sum. Onlyz normalized innullspace. Later quadratic ranks4/5 give no additional exclusion or linearization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

