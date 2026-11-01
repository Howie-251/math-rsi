import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_8 : cachedFree 8=freeValue 8 ∧
      (∀ j : Fin 7, cachedCenterA 8 j=aValue 8 j ∧ cachedCenterC 8 j=cValue 8 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_9 : cachedFree 9=freeValue 9 ∧
      (∀ j : Fin 7, cachedCenterA 9 j=aValue 9 j ∧ cachedCenterC 9 j=cValue 9 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_10 : cachedFree 10=freeValue 10 ∧
      (∀ j : Fin 7, cachedCenterA 10 j=aValue 10 j ∧ cachedCenterC 10 j=cValue 10 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_11 : cachedFree 11=freeValue 11 ∧
      (∀ j : Fin 7, cachedCenterA 11 j=aValue 11 j ∧ cachedCenterC 11 j=cValue 11 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
