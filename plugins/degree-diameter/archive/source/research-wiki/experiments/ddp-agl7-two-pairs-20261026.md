---
type: experiment
node_id: exp:ddp-agl7-two-pairs-20261026
title: "非正规AGL7两逆对完整范围：仅LL仍失败"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "OneCPUworker; independent all3200-root BFS"
duration: "106.774204 CPU seconds including final independent check"
provenance: "research/ddp/m2_coset_tower/d7_binary_agl7/STRUCTURE_CHECK.md; research/ddp/m2_coset_tower/d7_binary_agl7/REPORT.md; research/ddp/m2_coset_tower/d7_binary_agl7/terminal.json; research/ddp/m2_coset_tower/d7_binary_agl7/production.best.edges; research/ddp/m2_coset_tower/d7_binary_agl7/best.independent_verify.json; research/ddp/m2_coset_tower/d7_binary_agl7/REMAINING_SCOPE.md"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "coset-tower", "nonnormal-H", "method-ledger"]
---

# 非正规AGL7两逆对完整范围：仅LL仍失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,5)；L=2810；candidate_graph_or_family n=3200

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=28224；Existing Wiki Metrics; no experiment rerun；76384728 normalized legalHH inputs;299928 BB passes scored;2 jointhead/blockzero;best roots21/0/0,bad28224allLL,D6,7regular11200edges.



**既有原文指标：** 76384728 normalized legalHH inputs;299928 BB passes scored;2 jointhead/blockzero;best roots21/0/0,bad28224allLL,D6,7regular11200edges.



**原始证据：** [research/ddp/m2_coset_tower/d7_binary_agl7/STRUCTURE_CHECK.md](../../research/ddp/m2_coset_tower/d7_binary_agl7/STRUCTURE_CHECK.md)；[research/ddp/m2_coset_tower/d7_binary_agl7/REPORT.md](../../research/ddp/m2_coset_tower/d7_binary_agl7/REPORT.md)；[research/ddp/m2_coset_tower/d7_binary_agl7/terminal.json](../../research/ddp/m2_coset_tower/d7_binary_agl7/terminal.json)；[research/ddp/m2_coset_tower/d7_binary_agl7/production.best.edges](../../research/ddp/m2_coset_tower/d7_binary_agl7/production.best.edges)；[research/ddp/m2_coset_tower/d7_binary_agl7/best.independent_verify.json](../../research/ddp/m2_coset_tower/d7_binary_agl7/best.independent_verify.json)；[research/ddp/m2_coset_tower/d7_binary_agl7/REMAINING_SCOPE.md](../../research/ddp/m2_coset_tower/d7_binary_agl7/REMAINING_SCOPE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All nonLL pairs can be covered, but every declared two-pair input fails D5. Three-pair HH impossible;zero/onepair remainopen. These conclusions do not exclude the full AGL7 tower or arbitrary3200 graphs.

**启发与重启依据：** All nonLL pairs can be covered, but every declared two-pair input fails D5. Three-pair HH impossible;zero/onepair remainopen. These conclusions do not exclude the full AGL7 tower or arbitrary3200 graphs.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

