import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_0 : TwentyFourSlotAverageCache.cachedFree (positions 0) (p 0)=freeValue 0 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 0) (p 0) j=aValue 0 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 0) (p 0) j=cValue 0 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_1 : TwentyFourSlotAverageCache.cachedFree (positions 1) (p 1)=freeValue 1 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 1) (p 1) j=aValue 1 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 1) (p 1) j=cValue 1 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_2 : TwentyFourSlotAverageCache.cachedFree (positions 2) (p 2)=freeValue 2 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 2) (p 2) j=aValue 2 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 2) (p 2) j=cValue 2 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_3 : TwentyFourSlotAverageCache.cachedFree (positions 3) (p 3)=freeValue 3 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 3) (p 3) j=aValue 3 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 3) (p 3) j=cValue 3 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_4 : TwentyFourSlotAverageCache.cachedFree (positions 4) (p 4)=freeValue 4 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 4) (p 4) j=aValue 4 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 4) (p 4) j=cValue 4 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
