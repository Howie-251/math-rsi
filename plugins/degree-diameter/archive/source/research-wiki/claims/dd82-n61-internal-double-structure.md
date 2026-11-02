---
type: claim
node_id: claim:dd82-n61-internal-double-structure
name: "Order61 internal double-path structure and three-case representation"
description: "Initial three-type representation for actual order61 internal double paths, with reviewed pure reductions and lossless same-A model. Subsequent checked r0_h1_b0 exclusion proves universal h0; only r1_h0_b0 and r2_h0_b1 remain, both UNKNOWN in original and refined runs. This historical representation is superseded in current scope by the common-attachment exclusion claim; no full internal-D or order61 exclusion."
node_type: claim
status: sound-modulo-imports
provenance: "reviews/dd82/proof-checker-n61-internal-path-20261013/PROOF_AUDIT.json; DELTA_ADJACENCY_AUDIT.json; DELTA_PORT_MODEL_AUDIT.json; reviews/dd82/20261013_V3_n61_internal_proof_model_review.json"
tags: ["dd82", "n61", "defect"]
date: 2026-10-13
added: 2026-10-13T15:49:16Z
---

# Order61 internal double-path structure and three-case representation

**status:** `sound-modulo-imports`

## Statement
For any actual61 target and any consecutive D-path triple, Auw=0, rh=0 and h<=1. The initial necessary types were (0,1,0),(1,0,0),(2,0,1); the subsequent common-attachment exclusion removes (0,1,0). The local parent partition, Toeplitz A block and path length<=52 hold. In the third type the endpoint unit ports have exactly the three necessary locations of INTERNAL_DOUBLE_SHARED_TWO_PORTS.md. Complete same-A representation in INTERNAL_DOUBLE_FULL_GRAPH_DESIGN.md preserves every target with such a triple.

## Honest scope
Conditional on inherited actual B-connected,row4,entry<=2 and D-path-forest results, including their reviewed finite and checked-CNF imports. This claim records necessary structure and mathematical representation, not a full internal-D exclusion, graph construction or Lean theorem. The implementation and five actual runs were completed subsequently; their exact scope is recorded separately. Original fresh check and explicitly reused deltas remain distinct; Gemini accepted exact scopes.

## Evidence chain
Proof manuscripts under proofs/dd82/n61/INTERNAL_DOUBLE_*.md; actual local receipts and Gemini rounds1–2. Reviewer domain miscount corrected: 11 possible positions per endpoint, combined union12. The original free-edge counts were predictions at the time of this representation; later measured CNF sizes and results are in the linked experiment.

## Current status after the completed loop
Updated 2026-10-18 from the completed 2026-10-13 run: [universal common-neighbor inclusion](dd82-n61-internal-common-attachment-exclusion.md) excludes h=1 by a checked contradiction. Both h=0 types remain open after original and refined runs. See [five actual profiles](../experiments/dd82-internal-double61-five-profiles-20261013.md) and [the full remaining-space / user-comments note](../DD82_PROGRESS_AND_COMMENTS_20261018.md). The bounded review loop closed at 4/4; the current overall Goal is ACTIVE under the human-in-loop plan. Proof status remains `sound-modulo-imports`.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


## 2026-10-18 有界历史对齐后的使用范围
旧[3,3]四完整轨道恰好覆盖本条内部双路径域，并均有实际RAW UNSAT记录。因此研究工作继承RAW避免重复长路径/r1/r2探索；严格证明等级不升级，原两类新输入UNKNOWN保持。详见[对齐报告](../DD82_OLD_NEW61_ALIGNMENT_20261018.md)。本条数学结构及h0的独立认证价值保留，不把重叠域当成新开放构造域。
