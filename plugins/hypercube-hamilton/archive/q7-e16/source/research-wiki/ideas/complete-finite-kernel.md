---
type: idea
node_id: idea:complete-finite-kernel
title: "结构剥离后的完备有限核"
stage: archived
outcome: positive
added: 2026-11-16T08:18:18Z
based_on: []
target_gaps: []
tags: ["Q7", "E16", "RUP", "workflow"]
---

# 结构剥离后的完备有限核

**stage:** `archived`  ·  **outcome:** `positive`

先证明必要域完备，再验证冻结 CNF 的证书

## Thesis
先证明每个余下的实际反例经共同坐标运输给出有限核赋值，允许表覆盖必要的大面代表，小面保留符号变量。源约束和编码分别审计，再对冻结 CNF 验真。

## Key risks
核对全称来源、同一实际输入的联合运输和逆向保边。限时 SAT/CP 仅供诊断，UNKNOWN 时回到结构推导。例见 [μ=0 完整证明](../../research/seven_directions/mu0_global_2026_11_15/MU0_FULL_CLOSURE.md)。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

