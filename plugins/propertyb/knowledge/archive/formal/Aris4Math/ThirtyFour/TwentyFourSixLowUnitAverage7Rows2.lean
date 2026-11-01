import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_10 : TwentyFourSlotAverageCache.cachedFree (positions 10) (p 10)=freeValue 10 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 10) (p 10) j=aValue 10 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 10) (p 10) j=cValue 10 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_11 : TwentyFourSlotAverageCache.cachedFree (positions 11) (p 11)=freeValue 11 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 11) (p 11) j=aValue 11 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 11) (p 11) j=cValue 11 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
