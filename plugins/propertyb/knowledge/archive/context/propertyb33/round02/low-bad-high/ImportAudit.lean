import Aris4Math.ThirtyThree.TwentyThreeLowBadHighComplete

open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (count1 : H.sixVertices.card = 1)
    (x y : Fin 23) (dx : H.degree x = 6) (dy : H.degree y = 7)
    (bad : 2 ≤ H.codegree x y) : PropertyB H :=
  TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high H cover edges33 count1 x y dx dy bad

#check @TwentyThreeLowBadHighComplete.propertyB_of_structured_locks
#check @TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high
#print axioms TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high
#print axioms TwentyThreeLowBadHighCatalog.classify
#print axioms TwentyThreeLowBadHighNumeric.strict
#print axioms TwentyThreeLowBadHighNumeric.dual_exact
