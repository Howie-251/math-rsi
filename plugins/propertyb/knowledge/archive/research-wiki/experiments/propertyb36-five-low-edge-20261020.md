---
type: experiment
node_id: exp:propertyb36-five-low-edge-20261020
title: "全五低原边与至少18六度子类：两划分共同交叠染色"
idea_id: ""
verdict: yes
confidence: high
date: "2026-10-20"
hardware: "local Mac; exact C++ plus independent literal bitmasks"
duration: "independent full run 0.059339 CPU seconds; root replay retained separately"
provenance: "proofs/propertyb35/TWENTYFIVE_FIVE_LOW_EDGE.md §§1–6; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/PROOF.md; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/RESULT.json; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/independent/COMPARISON.json; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/root_replay/ROOT_REPLAY.json; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/ROOT_ACCEPTANCE.md; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/TRANSFER_TRIAGE.md; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_RECONCILIATION.md; proofs/propertyb35/TWENTYFIVE_MANY_SIX.md (separate r17 extension)"
added: 2026-10-20T13:18:42Z
tags: ["property-b", "m5-ge36", "five-low-edge", "two-partition-overlap", "complete-local-domain", "r18-r19-analytic-selection"]
---

# 全五低原边与至少18六度子类：两划分共同交叠染色

**verdict:** `yes`  ·  **confidence:** `high`

## Metrics
Scope: 25 vertices, 35 distinct 5-edges, pair-cover. A real original edge G whose five vertices all have degree six guarantees Property B; this also closes every r>=18 degree-six subclass.
Two-partition local domain: 70 row compositions, 19,834 complete row-sorted matrices, 264 row/column orbits; exact minimum joint conflict count 400 of C(20,10)=184,756, uniquely J-I. Single-partition conflict count 16,980. Production integer inclusion-exclusion, independent literal bitmask replay of all 48,775,584 representative/coloring pairs, and root recompilation/replay all PASS; every representative key/count matches.
Actual H coloring: three degree-six centers on G share the same 20 outside points; failure bound 184,674/184,756<1, slack 82; the centers then receive independent compatible colors. Independent full verification CPU 0.059339 seconds, with complete domain and counts retained.

## Reasoning
verdict=yes is restricted to the all-five-low-edge / r>=18 subclasses, not to the full m(5)>=36 goal. The canonical proof connects the actual 35 original edges to a Bool coloring; it does not assume that separately feasible local views can be joined.
Selecting G is analytic. Assuming no five-low edge, low-point pair uniqueness gives sum l=6r and sum C(l,2)=C(r,2), hence r<=19. For r19, every low point lies in six l4 edges, so 4n4=114 is impossible. For r18, each low point lies in one l3 and five l4 edges, giving n3=6 and 4n4=90, also impossible. These r18/r19 short counts were checked by root and q4; they need no degree-spectrum or whole-H enumeration.
Reusable gain: one positive two-partition intersection, subtracted once from three conflict events, makes the common balanced-coloring argument strict. This replaces further subdivision of the nine r21 design parameters; no 19/18/17-point local matrix classification was added. The general three-low same-edge gate is D-5alpha<=12; other three-low inputs still require that hypothesis.
Review correction: GEMINI_RECONCILIATION.md records two valid SUCCESS responses from the same Gemini 4 Argon (High) / high thread (initial and continuation), not two independent reviewers. The first statically read the actual three-low caller, five-low theorem, original r>=20 selection, and local-lemma derivation; it hand-checked 16980, 8008/6006, the legal single intersection subtraction, 160650+2002(D-5alpha), and the strict five-low numerator 184674 with slack 82. The continuation independently hand-checked the r18/r19 per-low-point divisibility arguments and accepted r>=18. Together they support the three-low D-5alpha<=12 gate, five-low theorem, and r>=18 subclass under the declared finite-arithmetic import. Gemini did not compile or execute the local programs or independently recompute all 19834 terminals / 264 orbits; those deterministic execution records are separately retained. Grok has no completed positive result recorded for this scope, so this is not dual-model approval.
The eight major open classes have not decreased. A subsequent, separately scoped r17 analytic extension is now documented in proofs/propertyb35/TWENTYFIVE_MANY_SIX.md and exp:propertyb36-r17-macro-selection-20261020; it combines with this unchanged r>=18 evidence to close r>=17. General 25-point many-low inputs now remain at r=3..16 with no all-five-low original edge. This record's yes verdict and completed Gemini reviews remain restricted to the earlier three-low/five-low/r>=18 scope; they are not r17 approval. The separate conditional W gates are not unconditional coverage. Full m(5)>=36 remains unproved; no new claim or Lean theorem is created.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

