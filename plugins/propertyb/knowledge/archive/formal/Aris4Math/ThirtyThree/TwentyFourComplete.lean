import Aris4Math.ThirtyThree.TwentyFourLowComplete
import Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete
import Aris4Math.ThirtyThree.TwentyFourMixed

/-! Complete 24-vertex branch for T33. All lock selections, local catalogs,
actual multiplicities and deleted pair weights are supplied internally. -/
namespace Aris4Math.ThirtyThree

theorem twenty_four_propertyB (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H := by
  rcases propertyB_or_matching_or_mixed H cover edges33 with colored | matching | mixed
  · exact colored
  · exact TwentyFourFiveMatchingComplete.propertyB_of_five_matching H edges33 matching
  · exact TwentyFourMixed.propertyB_of_mixed_locks H cover edges33 mixed

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.twenty_four_propertyB
