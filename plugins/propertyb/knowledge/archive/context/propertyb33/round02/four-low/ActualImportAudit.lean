import Aris4Math.ThirtyThree.TwentyThreeFourLowActual

open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (many : 4 ≤ H.sixVertices.card) :
    PropertyB H ∨ ∃ vertices : Fin 4 ↪ Fin 23, ∃ k : Fin 3,
      (∀ i, H.degree (vertices i) = 6) ∧
      (∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) ∧
      (∀ T, QuadProfiles.count H vertices T =
        TwentyThreeFourLowCatalog.counts ⟨k.val,by omega⟩ T) :=
  TwentyThreeFourLowActual.propertyB_or_unit_counts H cover edges many

#check TwentyThreeFourLowActual.actual_representative
#print axioms TwentyThreeFourLowActual.actual_representative
#print axioms TwentyThreeFourLowActual.propertyB_or_unit_counts
