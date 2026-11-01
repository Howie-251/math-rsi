import Aris4Math.ProfileApplication
import Aris4Math.TraceProfiles
import Aris4Math.K4Profiles

/-! Complete finite-goal branches using the analytic lock classification. -/

namespace Aris4Math.LargeVertices

/-- Complete 24-vertex branch, including actual four-lock classification,
all exact trace multiplicities, and the conditional probability argument. -/
theorem twenty_four_propertyB (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) : PropertyB H := by
  obtain ⟨p, vertices, real, noCap, noCorrection, strict⟩ :=
    K4Profiles.exists_realized_bounded_profile24 H cover edges32
  exact ProfileApplication.propertyB_of_uncorrected_profile H vertices
    K4Profiles.positions24 p real noCap noCorrection strict

/-- Complete 25-vertex branch. Pair covering and 32 edges are exactly the
normalization delivered by the original-goal reduction. No profile or
probability assumption occurs in this statement. -/
theorem twenty_five_propertyB (H : Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) : PropertyB H := by
  obtain ⟨p, vertices, real, noCap, noCorrection, strict⟩ :=
    TraceProfiles.exists_realized_bounded_profile25 H cover edges32
  exact ProfileApplication.propertyB_of_uncorrected_profile H vertices
    TraceProfiles.positions25 p real noCap noCorrection strict

end Aris4Math.LargeVertices

#print axioms Aris4Math.LargeVertices.twenty_five_propertyB
#print axioms Aris4Math.LargeVertices.twenty_four_propertyB
