import Aris4Math.ThirtyThree.OrdinaryLink

#check Aris4Math.ThirtyThree.OrdinaryLink.ordinary_bad_pair_budget_of_codegree_one
#check Aris4Math.ThirtyThree.OrdinaryLink.ordinaryBadPairs_eq_filter
#check Aris4Math.ThirtyThree.OrdinaryLink.weight_lower_of_twenty_degree_eight
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.ordinary_bad_pair_budget_of_codegree_one
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.weight_lower_of_twenty_degree_eight

open Aris4Math Aris4Math.LinkDeletion Aris4Math.ThirtyThree.OrdinaryLink
open scoped BigOperators

example (H : Simple5Hypergraph (Fin 20)) (x y : Fin 20)
    (hne : x ≠ y) (hone : H.codegree x y = 1) (hd : H.degree x = 8) :
    4 ≤ (ordinaryBadPairs H x y).card :=
  four_le_ordinary_bad_pairs_of_twenty H x y hne hone (by simp) hd

example (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (x y : Fin 20) (hne : x ≠ y) (hone : H.codegree x y = 1)
    (hd : H.degree x = 8) (w : Finset (Fin 20) × Finset (Fin 20) → ℚ)
    (base : ∀ p ∈ H.badLinkPairs x, (21 / 2210 : ℚ) ≤ unorderedWeight w p)
    (ordinary : ∀ p ∈ ordinaryBadPairs H x y,
      (126 / 12155 : ℚ) ≤ unorderedWeight w p) :
    (1239 / 24310 : ℚ) ≤ ∑ d ∈ directedBadPairs H x, w d := by
  rw [directed_bad_sum]
  exact weight_lower_of_twenty_degree_eight H cover x y hne hone (by simp) hd w base ordinary
