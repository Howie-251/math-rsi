import Aris4Math.ThirtyThree.TwentyFourFullFive
open Aris4Math
example (H : Simple5Hypergraph (Fin 24)) (edges33 : H.edges.card = 33)
    (selected : ThirtyThree.TwentyFourQuadRedirect.FullFiveLocks H) : PropertyB H :=
  ThirtyThree.TwentyFourFullFive.propertyB_of_full_five H edges33 selected
#print Aris4Math.ThirtyThree.TwentyFourFullFive.propertyB_of_full_five
#print axioms Aris4Math.ThirtyThree.TwentyFourFullFive.propertyB_of_full_five
#print axioms Aris4Math.ThirtyThree.TwentyFourFullFiveData.exact_bounds
