import Aris4Math.ThirtyThree.TwentyThreeHighQuad

open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (many : 19 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (x y : Fin 23) (ne : x ≠ y) (dx : H.degree x = 7) (dy : H.degree y = 7)
    (large : 3 ≤ H.codegree x y) :
    ∃ coloring : Fin 23 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter fun x => coloring x = true).card ∧
      (e.filter fun x => coloring x = true).card ≤ 4 := by
  exact TwentyThreeHighQuad.propertyB_of_pair_at_least_three H cover edges many x y dx dy ne large

#check TwentyThreeHighQuad.propertyB_of_pair_at_least_three
#print axioms TwentyThreeHighQuadData.certificates
#print axioms TwentyThreeHighQuad.data_complete
#print axioms TwentyThreeHighQuad.actual_data
#print axioms TwentyThreeHighQuad.propertyB_of_four
#print axioms TwentyThreeHighQuad.propertyB_of_pair_at_least_three
