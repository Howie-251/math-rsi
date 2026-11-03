---
type: claim
node_id: claim:dd82-twofactor60-cycle-rigidity
name: "60点任意两侧二因子排除与诱导最大度2子图界"
description: "Binary exact-cover blocks between any cycles of lengths divisible by five have exactly ten stripe forms. This removes every long internal cycle and imports the accepted arbitrary-orientation twelve-pentagon exclusion."
node_type: claim
status: verified
provenance: "reviews/dd82/20261018_twofactor60_extension_review.json"
tags: ["DD82", "n60", "paper-proof", "cross-model-reviewed"]
date: 2026-10-18
added: 2026-10-18T09:40:02Z
---

# 60点任意两侧二因子排除与诱导最大度2子图界

**status:** `verified`

## Statement
No order60 target admits a30+30 induced-two-factor partition. Every induced subgraph of maximum degree at most2 in any order60 target has at most29 vertices.

## Honest scope
Complete paper proof with one actual direct Gemini ACCEPT. Does not prove that arbitrary60 targets contain the partition or a30-point low-degree induced set. No whole-order exclusion, solver or Lean.

## Evidence chain
proofs/dd82/construction/TWO_BLOCK60_CYCLE_RIGIDITY.md; actual review reviews/dd82/20261018_twofactor60_extension_review.json. Binary local propagation is essential: the manuscript provides a real-valued nonperiodic counterexample. Final pentagon contradiction is inherited, not new.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

