import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family225
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,6},{2,3,7},{4,5,8},{6,7,8}],[{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,1,6},{2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}],{6,7,8},[],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset := by
  simp only [family,List.not_mem_nil,IsEmpty.forall_iff,implies_true]
end Family225
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
