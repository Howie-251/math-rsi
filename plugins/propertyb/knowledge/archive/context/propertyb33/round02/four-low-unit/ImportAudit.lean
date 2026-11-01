import Aris4Math.ThirtyThree.TwentyThreeFourLowComplete
open Aris4Math Aris4Math.ThirtyThree
example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ j, H.degree (vertices j) = 6)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (k : Fin 3) (actual : ∀ T, QuadProfiles.count H vertices T =
      TwentyThreeFourLowCatalog.counts (k.castLE (by omega)) T) : PropertyB H :=
  TwentyThreeFourLowUnit.propertyB_of_counts H cover vertices degrees unit k actual
#check @TwentyThreeFourLowUnit.propertyB_of_counts
#print axioms TwentyThreeFourLowUnit.propertyB_of_counts
#print axioms TwentyThreeFourLowUnitFacts.slot_complete
#print axioms TwentyThreeFourLowUnitChoice.choice_exact
#print axioms TwentyThreeFourLowUnitNumeric.weights_exact
example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (many4 : 4 ≤ H.sixVertices.card) : PropertyB H :=
  TwentyThreeFourLowComplete.propertyB_of_four_sixes H cover edges33 many4
#check @TwentyThreeFourLowComplete.propertyB_of_four_sixes
#print axioms TwentyThreeFourLowComplete.propertyB_of_four_sixes
