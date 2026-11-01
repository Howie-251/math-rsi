import Aris4Math.ThirtyThree.TwentyFive

example (H : Aris4Math.Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (edges : H.edges.card = 33) : Aris4Math.PropertyB H :=
  Aris4Math.ThirtyThree.twenty_five_propertyB H cover edges

#print Aris4Math.ThirtyThree.twenty_five_propertyB
#print axioms Aris4Math.ThirtyThree.twenty_five_propertyB
#print axioms Aris4Math.ThirtyThree.EightProfiles.numeric_counts
#print axioms Aris4Math.ThirtyThree.EightProfiles.strict
#print axioms Aris4Math.ThirtyThree.SixLargeProfiles.numeric_counts
#print axioms Aris4Math.ThirtyThree.SixLargeProfiles.strict
