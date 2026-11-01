import Aris4Math.ThirtyThree.TwentyFourLowComplete
open Aris4Math
example (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) : PropertyB H ∨
      ThirtyThree.TwentyFourSelection.FiveMatchingLocks H ∨
      ThirtyThree.TwentyFourSelection.MixedLocks H :=
  ThirtyThree.propertyB_or_matching_or_mixed H cover edges33
#check @Aris4Math.ThirtyThree.propertyB_or_matching_or_mixed
#print axioms Aris4Math.ThirtyThree.propertyB_or_matching_or_mixed
