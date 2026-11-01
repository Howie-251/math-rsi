import Aris4Math.ThirtyThree.TwentyFourQuadRedirect

#check Aris4Math.ThirtyThree.TwentyFourQuadRedirect.selected_of_twenty_four
#print Aris4Math.ThirtyThree.TwentyFourQuadRedirect.TripleLocks
#print Aris4Math.ThirtyThree.TwentyFourQuadRedirect.FullFiveLocks
#print axioms Aris4Math.ThirtyThree.TwentyFourQuadRedirect.selected_of_twenty_four

open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) :
    (∃ S : Finset (Fin 24), S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧
      H.UnitCodegrees S ∧ H.multiTraces S = S.powersetCard 2) ∨
    TwentyFourQuadRedirect.TripleLocks H ∨
    TwentyFourQuadRedirect.FullFiveLocks H ∨
    TwentyFourSelection.FiveMatchingLocks H ∨ TwentyFourSelection.MixedLocks H := by
  exact TwentyFourQuadRedirect.selected_of_twenty_four H cover edges (by simp)
