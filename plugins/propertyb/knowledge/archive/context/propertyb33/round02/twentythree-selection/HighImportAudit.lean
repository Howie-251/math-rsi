import Aris4Math.ThirtyThree.TwentyThreeHighSelection
open Aris4Math Aris4Math.ThirtyThree.TwentyThreeSelection
open Aris4Math.ThirtyThree.TwentyThreeHighSelection

#check seven_outside_bad_budget
#check exists_four_high_of_three
#check exists_five_high_of_path

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (many : 19 ≤ (sevenVertices H).card)
    (x y z : Fin 23) (dx : H.degree x = 7) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (cxy : H.codegree x y = 2) (cxz : H.codegree x z = 1)
    (cyz : H.codegree y z = 2) :
    ∃ f : Fin 5 → Fin 23, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
      H.codegree (f 0) (f 1) = 2 ∧ H.codegree (f 1) (f 2) = 2 ∧
      H.codegree (f 0) (f 2) = 1 ∧
      (∀ i j, i.val < 3 → 3 ≤ j.val → H.codegree (f i) (f j) = 1) :=
  exists_five_high_of_path H cover (by simp) many x y z dx dy dz xy xz yz cxy cxz cyz

#print axioms seven_outside_bad_budget
#print axioms exists_four_high_of_three
#print axioms exists_five_high_of_path
