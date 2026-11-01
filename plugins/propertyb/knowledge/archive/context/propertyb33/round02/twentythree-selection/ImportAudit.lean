import Aris4Math.ThirtyThree.TwentyThreeSelection

open Aris4Math Aris4Math.ThirtyThree.TwentyThreeSelection

#check degree_count_cases
#check indexed_six_excess_le_two
#check exists_four_sixes
#check exists_three_sixes_two_sevens_of_count
#check exists_two_sixes_three_sevens_of_count

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (count : H.sixVertices.card = 2) :
    ∃ f : Fin 5 → Fin 23, Function.Injective f ∧
      (∀ i, H.degree (f i) = if i.val < 2 then 6 else 7) ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → ¬ (i = 2 ∧ j = 3) →
        H.codegree (f i) (f j) = 1) :=
  exists_two_sixes_three_sevens_of_count H cover edges (by simp) count

#print axioms degree_count_cases
#print axioms indexed_six_excess_le_two
#print axioms exists_four_sixes
#print axioms exists_three_sixes_two_sevens_of_count
#print axioms exists_two_sixes_three_sevens_of_count
