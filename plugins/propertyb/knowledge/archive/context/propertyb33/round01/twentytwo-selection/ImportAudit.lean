import Aris4Math.ThirtyThree.TwentyTwoComplete

example (H : Aris4Math.Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges : H.edges.card = 33) :
    Aris4Math.ThirtyThree.TwentyTwoSelection.Selected H :=
  Aris4Math.ThirtyThree.TwentyTwoSelection.exists_locks_of_twenty_two H cover edges (by simp)

#print Aris4Math.ThirtyThree.TwentyTwoSelection.exists_locks_of_twenty_two
#print axioms Aris4Math.ThirtyThree.TwentyTwoSelection.exists_locks_of_twenty_two
#print Aris4Math.ThirtyThree.TwentyTwoSelection.PairCase
#print Aris4Math.ThirtyThree.TwentyTwoSelection.TripleCase
#print Aris4Math.ThirtyThree.TwentyTwoSelection.QuadCase
#print Aris4Math.ThirtyThree.TwentyTwoSelection.Selected

example (H : Aris4Math.Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges : H.edges.card = 33) : Aris4Math.PropertyB H :=
  Aris4Math.ThirtyThree.twenty_two_propertyB H cover edges

#print Aris4Math.ThirtyThree.twenty_two_propertyB
#print axioms Aris4Math.ThirtyThree.twenty_two_propertyB
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.data_complete
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.propertyB_of_quadCase
