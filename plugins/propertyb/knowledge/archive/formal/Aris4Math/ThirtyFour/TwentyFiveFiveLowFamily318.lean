import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family318
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{2,3,7},{4,5,8},{6,7,8}],[],∅,[],some ⟨[{2,3,7},{4,5,8},{6,7,8}],[{0,1},{0,2},{0,3},{0,4},{0,5},{0,6},{0,7},{0,8}],0⟩⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset := by
  simp only [family,List.not_mem_nil,IsEmpty.forall_iff,implies_true]
end Family318
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
