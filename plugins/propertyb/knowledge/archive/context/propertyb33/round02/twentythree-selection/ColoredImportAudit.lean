import Aris4Math.ThirtyThree.TwentyThreeColoredSelection
open Aris4Math Aris4Math.ThirtyThree.TwentyThreeColoredSelection

#check colored_ten_selection
#check exists_ten_common_unit
#check actual_colored_selection
#check exists_locks_low_bad_high_of_count

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (count : H.sixVertices.card = 1)
    (x y : Fin 23) (dx : H.degree x = 6) (dy : H.degree y = 7)
    (bad : 2 ≤ H.codegree x y) :
    ∃ f : Fin 5 → Fin 23, Function.Injective f ∧ f 0 = x ∧ f 1 = y ∧
      (∀ i, H.degree (f i) = if i = 0 then 6 else 7) ∧
      (2 ≤ H.codegree (f 0) (f 1) ∧ H.codegree (f 0) (f 1) ≤ 3) ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → ¬ (i = 2 ∧ j = 3) →
        H.codegree (f i) (f j) = 1) ∧
      (H.codegree (f 2) (f 3) ≠ 1 → ∀ e ∈ H.edges,
        ¬ (f 1 ∈ e ∧ f 2 ∈ e ∧ f 3 ∈ e)) :=
  exists_locks_low_bad_high_of_count H cover edges (by simp) count x y dx dy bad

#print axioms colored_ten_selection
#print axioms exists_ten_common_unit
#print axioms actual_colored_selection
#print axioms exists_locks_low_bad_high_of_count
