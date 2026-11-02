---
type: claim
node_id: claim:dd82-brown58-one-ce-matching-exclusion
name: "Brown58固定EI、一CE保留加EE匹配至少14坏对"
description: ""
node_type: claim
status: verified
provenance: ".aris/traces/research-review/dd82-brown58-one-ce-matching-root.md"
tags: ["dd82", "n58", "brown", "construction-obstruction"]
date: 2026-10-18
added: 2026-10-18T13:19:54Z
---

# Brown58固定EI、一CE保留加EE匹配至少14坏对

**status:** `verified`

## Statement
固定Brown57分割并加hub仅接C。每E恰保留两个原C邻居之一，EI边及非边不变，原EE保留并只增一个原非边完美匹配，则无论II、CI如何共同修改，至少14对E点无长度至多2路径。

## Honest scope
完整固定E边界的重连模板，不限III分割或II删边数。未排除改变EI、CE保留规则、EE新增结构或hub邻集的Brown扩展，更非全部58点。

## Evidence chain
computations/dd82/construction/BROWN58_ONE_CE_MATCHING_OBSTRUCTION.md：168唯一共C点对，锦标赛至多保留56，至少112失路；匹配至多14直接加84二步，至少14仍坏。根推导、独立本地核对与 reviews/dd82/20261018_brown58_one_ce_matching_review.json 实际SCOPED ACCEPT。新证明为纯计数，原Brown分割度数与CE无三角继承已检查有限事实；未重跑，无Lean。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

