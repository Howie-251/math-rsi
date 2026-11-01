import Aris4Math.ThirtyThree.TwentyThreeHighReduction
import Aris4Math.ThirtyThree.TwentyThreeHighFive
import Aris4Math.ThirtyThree.TwentyThreeHighSix

/-! The actual 23-point, 33-edge branch with no degree-six vertices. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighComplete

theorem propertyB_of_no_sixes (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (noSix : H.sixVertices.card = 0) : PropertyB H := by
  rcases TwentyThreeHighReduction.propertyB_or_cluster_cases H cover edges33 noSix with
    done | five | six
  · exact done
  · exact TwentyThreeHighFive.propertyB_of_five_case H cover edges33 five
  · exact TwentyThreeHighSix.propertyB_of_six_case H edges33 six

end Aris4Math.ThirtyThree.TwentyThreeHighComplete
#print axioms Aris4Math.ThirtyThree.TwentyThreeHighComplete.propertyB_of_no_sixes
