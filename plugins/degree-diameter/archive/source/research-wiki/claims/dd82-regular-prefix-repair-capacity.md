---
type: claim
node_id: claim:dd82-regular-prefix-repair-capacity
name: "正则前缀的补边容量与局部重复量必要界"
description: "纯条件性不等式及实际8份F6整数见证；Gemini2接受，非Lean、非58阶全域排除。"
node_type: claim
status: verified
provenance: "computations/dd82/construction/global_matchings58_run/prefix_capacity/PREFIX_CAPACITY.md; prefix_capacity.json; degree_capacity.json; reviews/dd82/20261018_global_matchings58_results_review.json"
tags: ["dd82", "construction", "capacity", "conditional-proof"]
date: 2026-10-18
added: 2026-10-18T08:09:45Z
---

# 正则前缀的补边容量与局部重复量必要界

**status:** `verified`

## Statement
设F为58点r正则图，d=8-r，g(e)为加单边e修复的原坏对数，T_v是点v可加边中最大d个g之和。若F能单调补成8正则直径2图，则 |Bad(F)|≤floor(sum T_v/2)+58*C(d,2)。对任意整数t_v，还有 |Bad(F)|≤floor((d*sum t_v+sum_nonedge max(0,2g_uv-t_u-t_v))/2)+58*C(d,2)。每点已有非回退长度0..2路径重复量1+r²-(58-b_F(v))≤7。

## Honest scope
r正则前缀到8正则58点目标的必要条件；所写常数d和1+r²不直接覆盖任意不规则前缀。实际排除仅首批8份F6及其单调补全，非所有F6/匹配生成族/任意58图。verified指完整纸面论证、实际整数重算和跨模型审阅，不表示Lean形式化。

## Evidence chain
一新边修复并集由sum g界定，两新边路径最多58*C(d,2)；d正则新增图使端点收益/势恰按度数相加。旧路径重复在加边下不减。top-d排除6份F6；整数势再给seed0:645>644、seed3:639>638。主代理用集合邻接独立重算R1172/1160；实际Gemini2接受原规则和精确范围。完整推导及向量见[容量证明](../../computations/dd82/construction/global_matchings58_run/prefix_capacity/PREFIX_CAPACITY.md)。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

