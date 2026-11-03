# Complete C5 paired-matching superset join: paper review

This review reads the actual `c5_once.py`, `C5_ACTION_AND_BINDING.json`, `C5_COMPRESSED_EXACT_MODEL.json`, `joint_once.py`, `JOINT_DOMAIN.json`, `JOINT_RESULT.json` and `JOINT_TERMINAL.json`. It repeats no action binding, side enumeration, bitset query, source/field construction, graph, BFS, solver or Lean computation. The raw capacity prediction and complete joint conclusion are separate.

## Actual action and exact compressed family

The saved order-five symplectic matrix is

```text
2 2 0 1
1 2 1 0
1 0 1 2
1 2 2 0
```

The numeric owner bound its two literal40-label permutations, eight5-orbits on each side, and all160 source incidences. The actual compressed model retains280 matching blocks,16 orbit-degree equations and216 far-orbit cover clauses. Collinear/concurrent blocks remain allowed, no girth-five restriction or additional cut was imposed, and all five original far rows in each orbit were checked to fold to the same positive OR.

The paper model in `PAPER_INTERFACE.md` proves these are exactly the paired matchings invariant under this common C5 action. An invariant matching cannot stay inside an odd5-orbit. Each of the105 orbit-pairings has5^4 shift choices, giving65625 matchings on each side. Reading `c5_once.py` confirms that the code enumerates these pairings and Cartesian products, builds each mask by OR of its four blocks, and asserts the full65625 count. The block masks cover both point and line far clauses; they are not restricted to the matching's own side.

## The capacity-only prediction was refuted

The complete single-side maxima are114 for P and113 for Q. Their sum227≥216 does not exclude a joint completion. The first two argmax masks have union158 and overlap69; that one pair is not the joint optimum and supplies no general negative conclusion. This was a legitimate negative answer to the proposed capacity-only obstruction, not a graph and not a failure of the exact coverage representation. The later join addresses the missing complementarity question.

## Strict capacity pruning

For any full union of216 bits, popcount(P)+popcount(Q)≥216 is necessary. Since every Q mask has at most113 bits, a P mask with fewer than103 cannot participate. Since every P mask has at most114 bits, a Q mask with fewer than102 cannot participate. The inequalities are strict: coverage103 or102 must be retained.

The actual domain receipt reports54856 P masks below103 and50427 Q masks below102. This leaves10769 P and15198 Q masks. The pruning concerns only possible full unions; it does not select particular shifts, matching shapes, triangle counts or symmetries beyond the already fixed C5 family.

## Exact inverted-index join

Index the retained Q masks by positions0..15197. For each far-clause bit r, define B_r as the bitset of Q positions whose masks contain r. `joint_once.py` constructs these membership bitsets by setting the actual eligible-Q position for each present mask bit. The byte-to-integer convention is little-endian, so its position map agrees with `JOINT_Q_MEMBERSHIP.json`.

For a retained P mask define M(P)=FULL216 minus P. Start with every eligible Q position and intersect B_r for each r in M(P). After any processed set T⊆M(P), the remaining positions are exactly

{Q eligible : T⊆mask(Q)}.

This is proved by induction on the AND operations. If the set becomes empty early, no later intersection can restore a Q, so that P has no partner even if unprocessed missing bits remain. If every missing bit is processed and a position survives, its Q covers all of M(P), equivalently P OR Q=FULL216. The code verifies that OR before any first-hit export.

The masks are actual216-bit masks from the exact compressed model; hence the code's `FULL ^ Pmask` is precisely the complement within that universe. Padding bits of the membership bytearrays start zero and the initial all-Q mask is restricted to the exact number of eligible positions. The loop stops only on an empty set, all missing bits processed, first positive, or an explicitly UNKNOWN process failure. It does not replace coverage by counts or by the argmax pair.

## Actual terminal conclusion

`JOINT_RESULT.json` records every one of10769 retained P masks queried, all10769 intersections empty, no partner, no remaining P, and78098 AND operations. `JOINT_ALL_P_STAGES.tsv` stores the pruned/query status, missing bits processed and survivor counts for every original P index. All low-coverage pairs are excluded by the strict bounds, and every remaining possible Q is represented in each applicable intersection. Thus the complete implicit65625²=4306640625 paired domain is covered without explicitly iterating that many pairs.

The actual result is **no diameter-at-most-three incidence-plus-two-matchings graph in this fixed common-C5-invariant family**. The process returned normally, did not time out, and generated no graph. It used no solver, BFS, repeated side enumeration or old model regeneration. Actual cumulative case cost at that terminal was3.272020095/10CPU seconds. This complete join is logically stronger than the earlier refuted capacity-only prediction; both historical results remain true descriptions of their respective questions.

## Symplectic conjugacy transport

Sp4(F3) has order51840 with a single factor5. Every order-five subgroup inside it is a Sylow5 subgroup, and Sylow conjugacy carries any such subgroup to the actual chosen one. A symplectic collineation permutes points and isotropic lines while preserving the160 incidence edges. Applying it to both matching sides preserves degrees and all graph distances.

Therefore, if a paired matching completion had any common order-five subgroup inside Sp4(F3), conjugation would produce a completion in the fixed family just excluded. The NO consequently covers **all paired completions with some common symplectic C5 symmetry**, not just this matrix's label presentation.

This does not make symmetry WLOG for arbitrary matchings. One matching may be invariant while the other breaks the chosen action; both may lack common C5 symmetry entirely. Neither case is excluded by this joint gate. Broader automorphism classifications and general(5,3) graphs are also outside its scope. No new action enumeration is needed for the conjugacy corollary.

## Review boundary

The code's source/label/action and masks are inherited from the actual saved binding and complete enumeration, not independently rerun by this paper. Reading the source revealed no logical gap in the block/row folding, exact side-factor OR, strict thresholds, membership index or complete termination condition. The result is a finite model-specific exclusion, not a new graph, parameter, Lean instance, global record or originality assertion. The unrestricted old paired-matching model remains UNKNOWN.
