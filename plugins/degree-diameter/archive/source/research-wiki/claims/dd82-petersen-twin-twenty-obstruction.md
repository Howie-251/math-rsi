---
type: claim
node_id: claim:dd82-petersen-twin-twenty-obstruction
name: "Twin Petersen attachments force at least twenty bad pairs"
description: "New20-bad-pair candidate contains two HS graphs sharing40 vertices."
node_type: claim
status: verified
provenance: "proofs/dd82/construction/PETERSEN_DOUBLE_HS_REPAIR.md"
tags: ["dd82", "construction", "n60"]
date: 2026-10-11
added: 2026-10-11T15:39:17Z
---

# Twin Petersen attachments force at least twenty bad pairs

**status:** `verified`

## Statement
If two Petersen fibers have identical core neighborhoods under a bijection, all four core routes coincide; at most eight of ten cross targets are reachable per vertex, so at least twenty unordered pairs fail. The saved graph attains twenty.

## Honest scope
Twin attachment family, not full six-fiber family or arbitrary n60. No Lean.

## Evidence chain
Explicit complete graph, independent BFS, all four route maps and two induced50-point Moore graphs checked, elementary eight-slot bound.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

