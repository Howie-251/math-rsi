---
type: idea
node_id: idea:dd82-free-cross58
title: "58点双Hamilton圈与完全自由跨边"
stage: archived
outcome: negative
added: 2026-10-18T08:26:43Z
based_on: []
target_gaps: ["gap:G4"]
tags: ["dd82", "construction", "free-cross", "58"]
---

# 58点双Hamilton圈与完全自由跨边

**stage:** `archived`  ·  **outcome:** `negative`

固定两侧29圈、完全自由841跨边、行列度6，同时编码全部跨侧和同侧真实覆盖。P不固定；不要求循环C。与已关闭的共同循环作用族及贪心匹配轨迹不同，仅覆盖双Hamilton子族。唯一无proof发现运行真实UNSAT；随后独立取证和LRAT检查成功，完整受限族已获计算辅助排除。最终同线程Gemini第2轮已接受，有限机制CLOSED2/4。

## Thesis
共同选择所有跨边，避免逐轮固定前缀的不可逆容量损失；精确跨侧矩阵HC+CH+C=J+P与同侧覆盖同时实现。

## Key risks
内部两圈是额外限制。现已认证排除该精确子族，其他圈型与整个58阶仍开放。P=I不能与两侧标准圈同时无损固定。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


## 实际处置

见[实验](../experiments/dd82-free-cross58-20261018.md)与[范围命题](../claims/dd82-free-cross58-hamilton-exclusion.md)。不对该已排除族追加P枚举、奇偶表示搜索或换编码；原Goal仍ACTIVE，整体57–61不变。
