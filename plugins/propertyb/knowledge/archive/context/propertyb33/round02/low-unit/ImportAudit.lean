import Aris4Math.ThirtyThree.TwentyThreeLowUnitComplete

open Aris4Math Aris4Math.ThirtyThree

theorem low_unit_original_coloring (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count : H.sixVertices.card = 1) (x : Fin 23) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1) :
    ∃ coloring : Fin 23 → Bool, ∀ edge ∈ H.edges,
      1 ≤ (edge.filter fun v => coloring v = true).card ∧
      (edge.filter fun v => coloring v = true).card ≤ 4 :=
  TwentyThreeLowUnitComplete.propertyB_of_low_unit H cover edges33 count x dx unit

#check TwentyThreeLowUnitComplete.propertyB_of_low_unit
#print axioms TwentyThreeLowUnitComplete.propertyB_of_low_unit
#print axioms TwentyThreeLowUnitSixCatalog.classify
#print axioms TwentyThreeLowUnitSixActual.actual_representative
#print axioms TwentyThreeLowUnitSixRecovery.recovery_formula
#print axioms TwentyThreeLowUnitSixCounts.propertyB_of_counts
#print axioms low_unit_original_coloring
