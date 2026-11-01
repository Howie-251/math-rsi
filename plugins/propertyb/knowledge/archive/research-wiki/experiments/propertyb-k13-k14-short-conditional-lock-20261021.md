---
type: experiment
node_id: exp:propertyb-k13-k14-short-conditional-lock-20261021
title: "k13/k14有界短试及实际已选锁集的条件增锁工具"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-21"
hardware: "本机"
duration: "双锁布局20.560 CPU秒；四锁单点6.536 CPU秒；k14两筛查8.735 CPU秒"
provenance: "context/propertyb-general/locks-vs-uniform-20261021/"
added: 2026-10-21T09:52:07Z
tags: ["property-b", "k13", "k14", "conditional-lock-extension", "local-certificate", "bounded-trial"]
---

# k13/k14有界短试及实际已选锁集的条件增锁工具

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
k13双/单锁共542布局未突破；条件增锁修复M9544/v972/d=e81的三锁局部域。M9564/v972已选三个度81单位共度锁点时，第四度81…128的288标记型、1134不同计数向量全部通过，最大分子4495688063231664 < S=4503599627370496。k14 M19647/19605仅端点筛查，分别止于v876/1013；无新完整m13/m14下界。

## Reasoning
可复用纸面引理：同一实际点对覆盖H中，全图最小度d、已选s个两两共度1锁点，Ei=(k-1)di-(v-1)、t=v-s-sum Ei>0，则存在共同单位邻点y，度数不超过d+floor((kM-vd-sum(di-d))/t)。每步仍须覆盖全部新增度数和迹。引理及完整局部作用见context/propertyb-general/locks-vs-uniform-20261021/conditional-extension/DERIVATION.md；不登记verified claim。Grok续接已有效grok-4.7-build/xhigh/end_turn，确认条件增锁、四锁六迹及整条布局min三项数学义务；d必须是全图最低度，各点单点迹使用实际d_i。未审随后288型数值或完整k13/14；原始与处置见conditional-extension/GROK_REVIEW.json及REVIEW_DISPOSITION.md。四锁成功不能删掉三个81度锁的真实存在条件，M9564/v813/最小度152等仍缺。有限布局和端点筛查失败不是路线极限。按用户短试范围停止，不继续研究；共同基线13为9539、统一9542(+3)、C2 9564(+25)，14为19602、19606(+4)、19647(+45)。图只红到12，一般k≥12 Lean verified状态不变。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

