# Actual double-root coverage, 2026-10-11

`DegreeDiameter/N62DoubleRoot.lean` closes the local caller gap from one actual double entry to the previously proved parent-template branches. Final theorem:

    n62_double_root_d1_or_closed_component
      (G : SimpleGraph V)
      (hdeg : degreeAtMostEight G)
      (hdiam : diameterAtMostTwo G)
      (hcard : Fintype.card V = 62)
      (hb : defectMatrix G r w = 2) :
      (∃ a, D1MatchParentTemplate G r w a) ∨
      (∃ a b, ClosedDoubleFour G r w b a)

There is no global B≤2 premise, no supplied root/template/capacity/counting certificate, and no triple-elimination assumption in this local theorem. Its actual double entry is precisely the local input being classified.

The chain constructs, in order:

1. Both double endpoints lie in no original triangle, using the already proved actual triangle row theorem.
2. An actual residual unit endpoint a gives root row 2e_w+e_a. Root r is nonadjacent to w,a; its neighborhood is independent.
3. `rootParents G r w` has cardinality 3 and `rootParents G r a` cardinality 2. Every other external vertex has exactly one actual parent.
4. Their actual finite-set intersection has size 0, 1, or 2. Adjacency w~a forces intersection empty.
5. Intersection size two constructs all fields of the existing D2MatchTemplate, which the actual D2 theorem excludes.
6. Intersection size zero constructs all labeled fields of D0ParentTemplate; size one gives the graph-only D1MatchParentTemplate.
7. Nonadjacent D0 closes by the existing MATCH result. In adjacent D0, the actual residual row at w is 2e_r+e_b. Commutation forces b adjacent to r. Its positive repeat and zero-triangle w put b outside the three w parents. Each of the two a-parent choices constructs an actual BIN template and is excluded. The remaining b constructs the BOUT template through the actual common-neighbor bridge, and its four rows close.

`DoubleRootParentData` stores only actual vertex distinctness, adjacency, cardinalities of defined parent sets, and unique-parent facts. It does not store B rows. `D1MatchParentTemplate` adds actual nonadjacency of w,a and actual parent intersection cardinality one. Both structures are constructed from the original graph by the exported chain.

The final closed component contains the original chosen double pair r,w; its exact four rows are the existing `ClosedDoubleFour G r w b a`. This is local coverage, not the global parity argument. Partitioning all double edges into pairs under absence of D1, and combining with odd double count, remains a separate step. Arbitrary order62 exclusion is not claimed.

Verification (Lean/mathlib 4.24, at most three threads):

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62DoubleRoot
lake env lean ReviewN62DoubleRoot.lean
```

Successful final build: `logs/n62-double-root-closure-first.log` (exit 0). Dedicated definitions/types/transitive-axioms/raw-callers audit: `logs/n62-double-root-type-axiom-audit.log` (exit 0). Twelve substantive exported theorems use only propext, Classical.choice and Quot.sound. The audit prints the actual parent-set and template definitions and checks two raw original-graph callers, including the final disjunction. No sorry, new axiom, native_decide or hashes introduced. Shared entry point, STATUS and final cross-family source review remain parent-owned.
