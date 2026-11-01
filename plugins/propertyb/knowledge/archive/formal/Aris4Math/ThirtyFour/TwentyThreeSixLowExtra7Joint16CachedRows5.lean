import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_20 : cachedFree 20=freeValue 20 ∧
      (∀ j : Fin 7, cachedCenterA 20 j=aValue 20 j ∧ cachedCenterC 20 j=cValue 20 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_21 : cachedFree 21=freeValue 21 ∧
      (∀ j : Fin 7, cachedCenterA 21 j=aValue 21 j ∧ cachedCenterC 21 j=cValue 21 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_22 : cachedFree 22=freeValue 22 ∧
      (∀ j : Fin 7, cachedCenterA 22 j=aValue 22 j ∧ cachedCenterC 22 j=cValue 22 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_23 : cachedFree 23=freeValue 23 ∧
      (∀ j : Fin 7, cachedCenterA 23 j=aValue 23 j ∧ cachedCenterC 23 j=cValue 23 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
