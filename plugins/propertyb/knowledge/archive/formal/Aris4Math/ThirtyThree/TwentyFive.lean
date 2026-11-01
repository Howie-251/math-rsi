import Aris4Math.ThirtyThree.TwentyFiveStructure
import Aris4Math.ThirtyThree.EightTraceClassification
import Aris4Math.ThirtyThree.EightProfiles
import Aris4Math.ThirtyThree.SixLargeProfiles

/-! The entire 25-vertex, 33-edge pair-covering branch.  Actual lock selection,
complete trace classification, input multiplicities and exact strict probability
bounds are all discharged by the imported results. -/

namespace Aris4Math.ThirtyThree

theorem twenty_five_propertyB (H : Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H := by
  obtain large | triples := TwentyFiveStructure.exists_six_large_or_eight_triples H
    cover edges33 (by simp)
  · obtain ⟨S,six,degrees,unit,large⟩ := large
    exact SixLargeProfiles.propertyB_of_large_trace H S six unit degrees edges33 large
  · obtain ⟨S,eight,degrees,unit,small,many,covers⟩ := triples
    obtain ⟨k,label,family⟩ := EightTraceClassification.exists_full_labeled_eight H S
      eight unit small many covers
    exact EightProfiles.propertyB_of_eight_family H S label unit degrees edges33 k family

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.twenty_five_propertyB
