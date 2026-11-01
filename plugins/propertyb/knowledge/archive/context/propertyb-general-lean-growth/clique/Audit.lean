import Aris4Math.General.Structure.Clique

open Aris4Math.General.RS

#print singleIntersecting_common_point_bound
#print singleIntersecting_card_le_of_no_common
#print singleIntersecting_card_le_cliqueBudget
#print singleGraph_isClique_card_le_cliqueBudget
#print axioms singleIntersecting_common_point_bound
#print axioms singleIntersecting_card_le_of_no_common
#print axioms singleIntersecting_card_le_cliqueBudget
#print axioms singleGraph_isClique_card_le_cliqueBudget

/-- A separate import using the raw finite family and actual edge graph. -/
example {V : Type*} [Fintype V] [DecidableEq V] (E : Finset (Finset V))
    (k : ℕ) (hk : 2 ≤ k) (hU : Uniform E k)
    (s : Finset {e : Finset V // e ∈ E})
    (hs : (singleGraph E).IsClique (s : Set _)) :
    s.card ≤ max (k * k - k + 1) ((Fintype.card V - 1) / (k - 1)) := by
  exact singleGraph_isClique_card_le_cliqueBudget hU hk s hs
