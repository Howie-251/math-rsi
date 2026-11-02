import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputs
import DegreeDiameter.Portfolio.OppositeGQ35SpreadWalks
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  OppositeGQSpread.diameter_three oldEquiv Inc spread projection spread_nonempty

#print axioms diameterAtMost_three
end DegreeDiameter.Portfolio.OppositeGQ35Spread
