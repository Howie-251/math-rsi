import Aris4Math.ThirtyFour.TwentyFourSixLowBadActual
import Aris4Math.ThirtyFour.TwentyFourSixLowSelection

namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadComplete
/-- Complete actual branch for at least six degree-six vertices containing a
nonunit pair. All local counts, matching labels and certificates are internal. -/
theorem propertyB_of_nonunit_low_pair (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (size : H.edges.card=34) (many : 6≤H.sixVertices.card)
    (bad : ∃x∈H.sixVertices,∃y∈H.sixVertices,x≠y ∧ H.codegree x y≠1) : PropertyB H := by
  classical
  obtain ⟨f,b,degrees,pairs⟩ := TwentyFourSixLowSelection.exists_labeled H cover many bad
  apply TwentyFourSixLowBadActual.propertyB_of_six_labeled H size f b degrees
  intro i j ij
  rw [pairs i j ij]
  simp [TwentyFourSixLowBadCoverage.low,ij]

/-- Under a counterexample assumption, six or more low vertices must have
all pair codegrees one. This is the input to the remaining unit-low branch. -/
theorem unit_of_not_propertyB (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (size : H.edges.card=34) (many : 6≤H.sixVertices.card)
    (noB : ¬PropertyB H) : H.UnitCodegrees H.sixVertices := by
  intro x hx y hy xy
  by_contra bad
  exact noB (propertyB_of_nonunit_low_pair H cover size many ⟨x,hx,y,hy,xy,bad⟩)
end Aris4Math.ThirtyFour.TwentyFourSixLowBadComplete
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadComplete.propertyB_of_nonunit_low_pair
