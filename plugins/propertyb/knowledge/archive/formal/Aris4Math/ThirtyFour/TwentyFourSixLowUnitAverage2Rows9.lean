import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_45 : TwentyFourSlotAverageCache.cachedFree (positions 45) (p 45)=freeValue 45 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 45) (p 45) j=aValue 45 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 45) (p 45) j=cValue 45 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_46 : TwentyFourSlotAverageCache.cachedFree (positions 46) (p 46)=freeValue 46 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 46) (p 46) j=aValue 46 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 46) (p 46) j=cValue 46 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_47 : TwentyFourSlotAverageCache.cachedFree (positions 47) (p 47)=freeValue 47 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 47) (p 47) j=aValue 47 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 47) (p 47) j=cValue 47 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
