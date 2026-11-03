import DegreeDiameter.Portfolio.OppositeGQ35SpreadDegree
import DegreeDiameter.Portfolio.OppositeGQ35SpreadLowerGeneric
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 := by
  intro h
  have hn := OppositeGQSpread.diameter_two_card_le graph 24 forward forward_covers h
  rw [card_vertex] at hn
  omega

#print axioms not_diameterAtMost_two
end DegreeDiameter.Portfolio.OppositeGQ35Spread
