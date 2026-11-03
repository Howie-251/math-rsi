---
type: experiment
node_id: exp:ddp-affine930-d11-fivepair-20261026
title: "930点十一度五逆对分支完整失败"
idea_id: "idea:ddp-affine-cayley-d3"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "local CPU, one worker per bounded batch"
duration: "128.733068 production/prep +0.026326115 independent CPU s"
provenance: "research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_PRODUCTION_REPORT.md"
added: 2026-10-27T07:55:14Z
tags: ["ddp", "diameter3", "method-ledger"]
---

# 930点十一度五逆对分支完整失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-affine-cayley-d3`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (11,3)；L=715；candidate_graph_or_family n=930

**距目标的证据：** 实际D=4，目标D=3；原报告bad（类型见详情）=55800；Existing Wiki Metrics; no experiment rerun；8260050raw,254536illegal,8005514legal fullrootBFS;noD3. BestD4,bad55800,rootspectrum1/11/110/688/120.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family.

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

**既有原文指标：** 8260050raw,254536illegal,8005514legal fullrootBFS;noD3. BestD4,bad55800,rootspectrum1/11/110/688/120.



**原始证据：** [research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_PRODUCTION_REPORT.md](../../research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_PRODUCTION_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Onlyfivepair+1reflectionfixedgroupbranchclosed;other37fourpairmodesopen. Independentall930rootfinaldoneonce.

**启发与重启依据：** Onlyfivepair+1reflectionfixedgroupbranchclosed;other37fourpairmodesopen. Independentall930rootfinaldoneonce.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

