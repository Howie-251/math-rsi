import Aris4Math.ThirtyThree.TwentyFourMixed
open Aris4Math
example (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33)
    (many : 18 ≤ (ThirtyThree.TwentyFourSelection.sevenVertices H).card) :
    ∃ c : Fin 24 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 := by
  exact ThirtyThree.TwentyFourMixed.propertyB_of_many_sevens H cover edges33 many
#check ThirtyThree.TwentyFourMixed.propertyB_of_mixed_locks
#check ThirtyThree.TwentyFourMixed.propertyB_of_many_sevens
#print axioms ThirtyThree.TwentyFourMixed.propertyB_of_mixed_locks
#print axioms ThirtyThree.TwentyFourMixed.propertyB_of_many_sevens
