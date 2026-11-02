# Actual D1 outlet under B≤2, 2026-10-11

`DegreeDiameter/N62D1Outlet.lean` proves the actual global outlet:

    n62_exists_d1_match_parent
      (G : SimpleGraph V)
      (hdeg : degreeAtMostEight G)
      (hdiam : diameterAtMostTwo G)
      (hcard : Fintype.card V = 62)
      (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
      ∃ r w a, D1MatchParentTemplate G r w a

The actual bound B≤2 is explicit and remains unproved here. This is not an unconditional legal-order62 caller and does not formalize the separate triple-repeat elimination. Nor does it exclude D1 or settle order62 nonexistence.

The pairing is defined without choosing an orientation or a representative component:

    doublePairMate G P = { z | ∃ x∈P, B[x,z]=1 }.

For actual closed rows at r,w,b,a, the mate of {r,w} is exactly {a,b}, and the mate of {a,b} is exactly {r,w}. The sets are unequal because the four vertices are distinct. Thus the same actual definition works regardless of which orientation or closed-row witness the local root theorem returns.

`n62_double_pair_mate_properties` uses the original graph and absence of any D1 parent representative to construct these properties for every actual member of `doubleRepeatPairs G`. No abstract involution, component partition, evenness or counting certificate is supplied by the caller. `n62_double_repeat_pairs_even_of_no_d1` proves evenness from that actual involution and needs no global defect bound. `n62_exists_d1_match_parent` then contradicts the already proved oddness under B≤2.

Verification (Lean/mathlib 4.24, at most three threads):

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62D1Outlet
lake env lean ReviewN62D1Outlet.lean
```

Build: `logs/n62-d1-outlet-first.log`, exit 0 on the first attempt. Dedicated audit: `logs/n62-d1-outlet-type-axiom-audit.log`, exit 0. The audit prints the actual mate and parent-template definitions, all four exported theorem types and their transitive axioms, and checks a raw original-graph caller with explicit actual B≤2. All four theorems use only propext, Classical.choice and Quot.sound. No sorry, new axiom, native_decide or hashes were introduced. Shared imports, STATUS and source review remain parent-owned.
