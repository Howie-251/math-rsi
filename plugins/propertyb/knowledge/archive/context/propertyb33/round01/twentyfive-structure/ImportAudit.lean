import Aris4Math.ThirtyThree.TwentyFiveStructure

open Aris4Math Aris4Math.ThirtyThree.TwentyFiveStructure

#check exists_six_large_or_eight_triples
#check eight_subsets_containing_triple
#check exists_eight_subset_preserving_five_triples
#print axioms exists_six_large_or_eight_triples
#print axioms ten_le_triple_count
#print axioms exists_eight_subset_preserving_five_triples

example (H : Simple5Hypergraph (Fin 25)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) :
    (∃ S : Finset (Fin 25), S.card = 6 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S ∧
      ∃ B ∈ H.multiTraces S, 4 ≤ B.card) ∨
    (∃ S : Finset (Fin 25), S.card = 8 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S ∧
      (∀ B ∈ H.multiTraces S, B.card ≤ 3) ∧
      5 ≤ ((H.multiTraces S).filter fun B => B.card = 3).card ∧
      ∀ x ∈ S, ∃ B ∈ H.multiTraces S, B.card = 3 ∧ x ∈ B) :=
  exists_six_large_or_eight_triples H cover edges (by simp)
