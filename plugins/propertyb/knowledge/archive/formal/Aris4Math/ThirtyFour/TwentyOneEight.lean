import Aris4Math.ThirtyFour.TwentyOneEightClaw
import Aris4Math.ThirtyFour.TwentyOneEightRules
namespace Aris4Math.ThirtyFour.TwentyOneEight
open TwentyOneEightGraph

/-- Complete minimum-eight branch for actual 34-edge hypergraphs on 21 vertices. -/
theorem propertyB_of_minimum_eight (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) : PropertyB H := by
  classical
  by_contra noB
  have large:=eights_at_least_nineteen H size minimum
  apply contradiction H (eights H) (Finset.card_pos.mp (by omega))
    (neighbors_at_least_six H cover size minimum)
  exact ⟨TwentyOneEightStructure.triangle_free H cover size noB,
    TwentyOneEightRules.path_isolate H cover size minimum noB,
    TwentyOneEightRules.cycle_common H cover size minimum noB,
    TwentyOneEightClaw.no_common_edge H cover size minimum noB⟩
end Aris4Math.ThirtyFour.TwentyOneEight
#print axioms Aris4Math.ThirtyFour.TwentyOneEight.propertyB_of_minimum_eight
