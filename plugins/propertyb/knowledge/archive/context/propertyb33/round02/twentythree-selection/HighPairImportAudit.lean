import Aris4Math.ThirtyThree.TwentyThreeHighPair

open Aris4Math Aris4Math.ThirtyThree.TwentyThreeHighPair

example (H : Simple5Hypergraph (Fin 23)) (edges : H.edges.card = 33)
    (x y : Fin 23) (ne : x ≠ y) (dx : H.degree x = 7) (dy : H.degree y = 7)
    (large : 4 ≤ H.codegree x y) :
    ∃ coloring : Fin 23 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter fun x => coloring x = true).card ∧
      (e.filter fun x => coloring x = true).card ≤ 4 := by
  exact propertyB_of_high_pair H edges x y ne dx dy large

#check propertyB_of_high_pair
#print axioms certificates
#print axioms propertyB_of_high_pair
