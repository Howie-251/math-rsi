import Aris4Math.ThirtyThree.TwentyFourFourLow
import Aris4Math.ThirtyThree.TwentyFourTripleLow
import Aris4Math.ThirtyThree.TwentyFourFullFive

/-! Close all three four-low-lock branches, including the full-quad
redirection. The only remaining selected inputs use five matching locks or
two degree-six and three degree-seven locks. -/
namespace Aris4Math.ThirtyThree

/-- Actual 24-point inputs reduce to the two remaining five-lock callers. -/
theorem propertyB_or_matching_or_mixed (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) :
    PropertyB H ∨ TwentyFourSelection.FiveMatchingLocks H ∨ TwentyFourSelection.MixedLocks H := by
  rcases TwentyFourQuadRedirect.selected_of_twenty_four H cover edges33 (by simp) with
    pairs | triple | full | matching | mixed
  · obtain ⟨S,four,degrees,unit,pairs⟩ := pairs
    exact Or.inl (TwentyFourFourLow.propertyB_of_four_pairs H cover edges33 S four degrees unit pairs)
  · obtain ⟨S,four,degrees,unit,B,sub,three,traces⟩ := triple
    exact Or.inl (TwentyFourTripleLow.propertyB_of_four_triple H cover edges33 S four
      degrees unit B sub three traces)
  · exact Or.inl (TwentyFourFullFive.propertyB_of_full_five H edges33 full)
  · exact Or.inr (Or.inl matching)
  · exact Or.inr (Or.inr mixed)

end Aris4Math.ThirtyThree
#print axioms Aris4Math.ThirtyThree.propertyB_or_matching_or_mixed
