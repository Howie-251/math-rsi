---
type: idea
node_id: idea:dd82-global-matchings58
title: "从空图用八轮全局匹配生成完整58点八正则图"
stage: archived
outcome: unknown
added: 2026-10-18T07:50:09Z
based_on: []
target_gaps: ["gap:G4"]
tags: ["dd82", "construction", "full-graph"]
---

# 从空图用八轮全局匹配生成完整58点八正则图

**stage:** `archived`  ·  **outcome:** `unknown`

从单调几何的强迫饱和障碍转向共同分配全部度数；每轮优化真实单边覆盖收益，旧几何只作同分偏好。没有旧边或核受保护。

## Thesis
八轮边不重复完美匹配直接返回完整58点232边图，再用独立BFS判断真实坏对；收益和可重复计数，逐轮记录实际改善。一次8seed试验已完成，实际5.450637CPU秒含独立BFS；全部直径3、坏对177–201。三个容量界已排除全部8份实际F6（Gemini2接受）；一份F5完整共同补全实际UNKNOWN27.827669CPU秒。最终Gemini3已接受交付，有限机制3/4关闭；不自动续跑旧交换、退到F4或换seed。

## Key risks
匹配并的初始限制可能错过目标；分轮贪心可能积累覆盖冲突。不同有标签边表不等于非同构。失败不能排除58阶。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

