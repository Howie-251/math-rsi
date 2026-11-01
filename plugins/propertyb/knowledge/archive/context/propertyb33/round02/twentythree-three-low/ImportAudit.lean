import Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (three : H.sixVertices.card = 3) : PropertyB H :=
  TwentyThreeThreeLowComplete.propertyB_of_three_sixes H cover edges33 three

#print axioms Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete.propertyB_of_three_sixes
#print Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete.propertyB_of_three_sixes
