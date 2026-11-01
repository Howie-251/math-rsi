import Aris4Math.ThirtyThree.TwentyThreeFourLowActual
import Aris4Math.ThirtyThree.TwentyThreeFourLowUnit

namespace Aris4Math.ThirtyThree.TwentyThreeFourLowComplete

/-- The actual four-low-point branch, including all unit and nonunit types. -/
theorem propertyB_of_four_sixes (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (many4 : 4 ≤ H.sixVertices.card) : PropertyB H := by
  rcases TwentyThreeFourLowActual.propertyB_or_unit_counts H cover edges33 many4 with
    done | ⟨vertices,k,degrees,unit,actual⟩
  · exact done
  · exact TwentyThreeFourLowUnit.propertyB_of_counts H cover vertices degrees unit k actual

end Aris4Math.ThirtyThree.TwentyThreeFourLowComplete

#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowComplete.propertyB_of_four_sixes
