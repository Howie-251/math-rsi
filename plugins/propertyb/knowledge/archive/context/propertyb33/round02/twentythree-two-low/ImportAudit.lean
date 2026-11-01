import Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete
open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (two : H.sixVertices.card = 2) : PropertyB H :=
  TwentyThreeTwoLowComplete.propertyB_of_two_sixes H cover edges33 two

#print axioms Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete.propertyB_of_two_sixes
#print Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete.propertyB_of_two_sixes
