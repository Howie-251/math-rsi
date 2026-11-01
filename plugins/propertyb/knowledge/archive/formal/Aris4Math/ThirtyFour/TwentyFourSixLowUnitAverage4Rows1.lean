import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_5 : TwentyFourSlotAverageCache.cachedFree (positions 5) (p 5)=freeValue 5 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 5) (p 5) j=aValue 5 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 5) (p 5) j=cValue 5 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_6 : TwentyFourSlotAverageCache.cachedFree (positions 6) (p 6)=freeValue 6 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 6) (p 6) j=aValue 6 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 6) (p 6) j=cValue 6 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_7 : TwentyFourSlotAverageCache.cachedFree (positions 7) (p 7)=freeValue 7 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 7) (p 7) j=aValue 7 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 7) (p 7) j=cValue 7 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_8 : TwentyFourSlotAverageCache.cachedFree (positions 8) (p 8)=freeValue 8 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 8) (p 8) j=aValue 8 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 8) (p 8) j=cValue 8 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_9 : TwentyFourSlotAverageCache.cachedFree (positions 9) (p 9)=freeValue 9 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 9) (p 9) j=aValue 9 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 9) (p 9) j=cValue 9 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4
