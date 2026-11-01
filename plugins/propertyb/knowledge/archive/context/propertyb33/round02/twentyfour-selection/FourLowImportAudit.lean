import Aris4Math.ThirtyThree.TwentyFourFourLow

#check Aris4Math.ThirtyThree.TwentyFourFourLow.propertyB_of_four_pairs
#print axioms Aris4Math.ThirtyThree.TwentyFourFourLow.propertyB_of_four_pairs
#print axioms Aris4Math.ThirtyThree.TwentyFourFourLowData.order_covers
#print axioms Aris4Math.ThirtyThree.TwentyFourFourLow.slots_complete

open Aris4Math
example (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (S : Finset (Fin 24)) (four : S.card = 4)
    (degrees : ∀ x ∈ S, H.degree x = 6) (unit : H.UnitCodegrees S)
    (pairs : H.multiTraces S = S.powersetCard 2) : PropertyB H := by
  exact ThirtyThree.TwentyFourFourLow.propertyB_of_four_pairs H cover edges S four degrees unit pairs
