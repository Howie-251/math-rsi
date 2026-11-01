import Aris4Math.ThirtyThree.TwentyThreeDefectSelection
open Aris4Math Aris4Math.ThirtyThree.TwentyThreeDefectSelection

#check energy_update_balance
#check exists_four_part_defect_one
#check exists_five_with_degree_le_one
#check exists_six_locks_low_unit_of_count
#check exists_mixed_five_of_high_three

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (count : H.sixVertices.card = 1)
    (x : Fin 23) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1) :
    ∃ f : Fin 6 → Fin 23, Function.Injective f ∧ f 5 = x ∧
      (∀ i, H.degree (f i) = if i.val < 5 then 7 else 6) ∧
      (∀ i : Fin 5, H.codegree x (f i.castSucc) = 1) ∧
      (∀ i : Fin 5, (Finset.univ.filter fun j : Fin 5 =>
        j ≠ i ∧ 2 ≤ H.codegree (f i.castSucc) (f j.castSucc)).card ≤ 1) :=
  exists_six_locks_low_unit_of_count H cover edges (by simp) count x dx unit

#print axioms energy_update_balance
#print axioms exists_four_part_defect_one
#print axioms exists_five_with_degree_le_one
#print axioms exists_six_locks_low_unit_of_count
#print axioms exists_mixed_five_of_high_three
