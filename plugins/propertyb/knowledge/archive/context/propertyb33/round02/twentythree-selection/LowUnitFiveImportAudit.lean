import Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete
open Aris4Math Aris4Math.ThirtyThree

theorem low_unit_high_pair_original_coloring
    (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33)
    (many : 17 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (x y z : Fin 23) (dx : H.degree x = 6) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (unit : ∀ a, H.degree a = 7 → H.codegree x a = 1)
    (yz : y ≠ z) (cyz : 3 ≤ H.codegree y z) :
    ∃ coloring : Fin 23 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter fun w => coloring w = true).card ∧
      (e.filter fun w => coloring w = true).card ≤ 4 :=
  TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair H cover edges33 many x y z
    dx dy dz unit yz cyz

#print axioms TwentyThreeLowUnitFiveCatalog.classify
#print axioms TwentyThreeLowUnitFiveComplete.propertyB_of_locks
#print axioms TwentyThreeLowUnitFiveComplete.propertyB_of_high_three
#print axioms TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair
#print axioms low_unit_high_pair_original_coloring
#print TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair
