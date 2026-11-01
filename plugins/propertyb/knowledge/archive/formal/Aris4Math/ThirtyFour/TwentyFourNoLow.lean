import Aris4Math.ThirtyFour.TwentyFourNoLowActual
import Aris4Math.ThirtyFour.TwentyFourNoLowSelection

namespace Aris4Math.ThirtyFour.TwentyFourNoLow

/-- Complete no-six-degree branch at 24 vertices and 34 edges. All lock
selection, complete local classification, exact certificates and the original
coloring are connected internally. -/
theorem propertyB_of_no_six (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (none : H.sixVertices.card=0) : PropertyB H := by
  classical
  by_contra noB
  obtain ⟨f,b,degrees,pairs⟩ :=
    TwentyFourNoLowSelection.exists_labeled_six H cover size none noB
  apply noB
  apply TwentyFourNoLowActual.propertyB_of_six_labeled H size f b degrees
  intro i j ij
  rw [pairs i j ij]
  simp [TwentyFourNoLowCoverage.low,ij]

end Aris4Math.ThirtyFour.TwentyFourNoLow
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLow.propertyB_of_no_six
