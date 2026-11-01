---
type: experiment
node_id: exp:propertyb34-feasibility-20261013
title: "T34有界先导：19点完整候选与24/25新选点"
idea_id: "idea:propertyb-five-34-edge-threshold"
verdict: partial
confidence: medium
date: "2026-10-13"
hardware: ""
duration: ""
provenance: "context/propertyb34-feasibility-20261013/DERIVATION_PACKAGE.md；同目录low-vertices/、high-vertices/、independent/及REVIEW_RECONCILIATION.md；命令和原始JSON均保留。"
added: 2026-10-13T09:07:49Z
tags: ["property-b", "34-edges", "feasibility", "exact-arithmetic"]
---

# T34有界先导：19点完整候选与24/25新选点

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb-five-34-edge-threshold`

## Metrics
19点：δ5/6/7单锁，δ8的单位/高共度双锁或9三锁型全部严格；9三锁最大707/715。20点：14保证双锁8过6未过，后6覆盖全部190递增位置。21点：7条强共度双锁严格，(5,8,8)18中央布局最佳44215/43758>1。24无六度：四条强共度双锁严格；5基本型中2在本窗口严格。25五低：5基本型中完整五元迹4172/4199严格，其他4型未过；9单位混合锁纸面选择已得。

## Reasoning
具体结构与秒级精确公式诊断支持继续研究；不是整图枚举或Lean验收。低点数与五低保留行有独立标号注入核对；高点数首轮未做第二实现。Grok核25恰五低选择与预算，Gemini核21分流及19覆盖，未执行代码。19逻辑核对接受已有算术，概率与实际输入形式连接尚待完成。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

