import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection
open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count : H.sixVertices.card = 1) (x : Fin 23) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1)
    (upper : ∀ y z, y ≠ z → H.degree y = 7 → H.degree z = 7 → H.codegree y z ≤ 2) :
    ∃ e : Fin 3, ∃ w : Fin 6 ↪ Fin 23,
      (∀ i, H.degree (w i) = if i=5 then 6 else 7) ∧
      (∀ i j, i ≠ j → H.codegree (w i) (w j) =
        if ({i,j} : Finset (Fin 6)) = {0,1} ∧ 0 < e.val then 2 else
        if ({i,j} : Finset (Fin 6)) = {2,3} ∧ 1 < e.val then 2 else 1) :=
  TwentyThreeLowUnitSixSelection.exists_locks H cover edges33 count x dx unit upper

#print axioms TwentyThreeLowUnitSixSelection.matching_complete
#print axioms TwentyThreeLowUnitSixSelection.normalized
#print axioms TwentyThreeLowUnitSixSelection.actual_related
#print axioms TwentyThreeLowUnitSixSelection.exists_locks
#check TwentyThreeLowUnitSixSelection.exists_locks
