import Aris4Math.ThirtyFour.TwentyFiveFiveLowComplete
import Aris4Math.ThirtyFour.TwentyFiveEightLowComplete
import Aris4Math.ThirtyFour.TwentyFiveNineLowComplete

/-! Full 25-vertex theorem. All three actual lock-selection alternatives are
closed internally. Building this module checks the entire local source chain. -/
namespace Aris4Math.ThirtyFour

theorem twenty_five_propertyB (H : Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (edges : H.edges.card=34) : PropertyB H := by
  rcases TwentyFiveSelection.exists_nine_or_ten_unit_locks H cover edges with five | eight | nine
  · exact TwentyFiveFiveLow.propertyB H edges five
  · exact TwentyFiveEightLowComplete.propertyB H edges eight
  · exact TwentyFiveNineLowComplete.propertyB H edges nine

end Aris4Math.ThirtyFour
#print axioms Aris4Math.ThirtyFour.twenty_five_propertyB
