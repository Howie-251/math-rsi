---
type: idea
node_id: idea:dd82-joint-twofactor58
title: "58点完整二块equitable域的联合构造"
stage: archived
outcome: negative
added: 2026-10-18T08:53:28Z
based_on: []
target_gaps: ["gap:G4"]
tags: ["dd82", "58", "construction", "joint-twofactor"]
---

# 58点完整二块equitable域的联合构造

**stage:** `proposed`  ·  **outcome:** `pending`

完整58点二块equitable构造域：H0/H1各为自由29点2正则图，C自由行列度6；合法右侧重标令跨路线矩阵K=J+I，两侧圈型都不固定。内部与跨边在同一真实图中共同实现。与已认证双Hamilton子族不同，不枚举圈型。

## Thesis
4+4被短奇偶矛盾否决；二块equitable目标只剩内部2度/跨6度。放开两侧二因子避免已认证Hamilton固定结构，而非仅换跨边。

## Key risks
任意58目标未必有二块equitable划分。P=I只有两侧内部结构保持自由时无损。短UNKNOWN不表示域耗尽。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


## 实际试验
完整模型唯一profile返回UNKNOWN，57.906149CPU秒，没有构造/排除；不重跑、不加时。数学路线仍可依据新推导继续，不因每小时报告或本次有限试验而强制换hypothesis。见exp:dd82-joint-twofactor58-20261018。

## 后续数学闭合（不改求解终态）
新的分量极值证明迫使两侧为C29，连接旧独立证书，整个两块equitable构造族被排除；更强地，任意58目标的诱导二正则子图≤28点。第3/4轮实际接受。原单次实验依旧UNKNOWN；族负结果来自新纸面归约和旧证书，不是追加求解。
