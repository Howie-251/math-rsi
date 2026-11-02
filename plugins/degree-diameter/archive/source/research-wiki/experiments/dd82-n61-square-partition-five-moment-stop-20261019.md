---
type: experiment
node_id: exp:dd82-n61-square-partition-five-moment-stop-20261019
title: "额外四圈分割范围：新谱区间与五矩仍相容"
idea_id: "idea:dd82-n61-global-closure-spectral"
verdict: no
confidence: high
date: "2026-10-19"
hardware: "local CPU, exact standard-library fractions checker"
duration: "未单独记录CPU/进程级耗时；不为补计时重跑"
provenance: "computations/dd82/spectral/square_partition_moment_diagnostic.md; computations/dd82/spectral/square_partition_moment_diagnostic.py; proofs/dd82/n61/GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md §7.12"
added: 2026-10-19T14:01:49Z
tags: ["dd82", "n61", "moment-diagnostic", "conditional-scope"]
---

# 额外四圈分割范围：新谱区间与五矩仍相容

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:dd82-n61-global-closure-spectral`

## Metrics
一次有限可行性计算在9个有理试探原子中找到5个严格内部原子；有理数检查PASS，矩为(60,-8,424,-512,3712)。

## Reasoning
否定本次有界假设：额外T=d=0、每条边恰属一个四圈所给的新谱区间，加前五矩，不能完成排除。精确正测度给整个区间上的四次以内分离不可能；权重不是整数重数，不证明原图存在。没有重跑旧输入包。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

