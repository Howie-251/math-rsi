---
type: experiment
node_id: exp:dd82-joint-twofactor58-20261018
title: "58点自由双二因子共同模型：单次UNKNOWN"
idea_id: "idea:dd82-joint-twofactor58"
verdict: partial
confidence: high
date: "2026-10-18"
hardware: "single CPU1,4GiB AS"
duration: "solve57.906149CPU/58.206894wall seconds; prepare2.352518CPU/2.369912wall"
provenance: "computations/dd82/construction/joint_twofactor58_run/DELIVERY.md; computations/dd82/construction/joint_twofactor58_run/result.json"
added: 2026-10-18T09:13:11Z
tags: ["dd82", "58", "unknown", "twofactor"]
---

# 58点自由双二因子共同模型：单次UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-joint-twofactor58`

## Metrics
206103variables/674424clauses; one no-proof solver call, exit0 UNKNOWN; no model/certificate/independent BFS

## Reasoning
完整均匀两块构造族的共同模型已实现并作小例与源码检查。有限试验未决定；不是无解或空间耗尽。纸面奇偶与两块归约另有接受证明。继续的数学问题是自由内部圈分量与跨侧路径如何兼容，不自动加时或枚举圈型。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


## 数学结果的后续更新
该实验自身仍是UNKNOWN。随后分量刚性及既有证书排除整个两块equitable族，并推出诱导二正则子图≤28点；它们是另记claim的数学证据，不将此实验改写为UNSAT或认证。见[新全域必要条件](../claims/dd82-induced-twofactor58-size-bound.md)。
