import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDual

open Aris4Math Aris4Math.ThirtyThree

/-- Conditional audit: the actual multiplicities are still a caller obligation. -/
theorem six_dual_original_coloring (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (c : Fin 9)
    (actual : ∀ T, MultiLockRecovery.count H vertices T =
      TwentyThreeLowUnitSixDualData.counts c T) :
    ∃ coloring : Fin 23 → Bool, ∀ edge ∈ H.edges,
      1 ≤ (edge.filter fun x => coloring x = true).card ∧
      (edge.filter fun x => coloring x = true).card ≤ 4 :=
  TwentyThreeLowUnitSixDual.propertyB_of_counts H vertices c actual

#check TwentyThreeLowUnitSixDual.propertyB_of_counts
#print axioms TwentyThreeLowUnitSixDual.propertyB_of_counts
#print axioms six_dual_original_coloring
