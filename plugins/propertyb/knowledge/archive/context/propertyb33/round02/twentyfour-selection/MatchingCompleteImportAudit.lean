import Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete

open Aris4Math Aris4Math.ThirtyThree

/-- Independent actual caller: the configuration predicate is the structural
selection output, with no catalog, profile, or multiplicity premise. -/
example (H : Simple5Hypergraph (Fin 24)) (edges33 : H.edges.card = 33)
    (selected : TwentyFourSelection.FiveMatchingLocks H) : PropertyB H :=
  TwentyFourFiveMatchingComplete.propertyB_of_five_matching H edges33 selected

#print Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete.propertyB_of_five_matching
#print axioms Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete.propertyB_of_five_matching
#print axioms Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog.classify
