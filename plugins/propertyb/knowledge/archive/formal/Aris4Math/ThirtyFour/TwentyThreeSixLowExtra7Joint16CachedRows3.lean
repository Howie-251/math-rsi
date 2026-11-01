import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_12 : cachedFree 12=freeValue 12 ∧
      (∀ j : Fin 7, cachedCenterA 12 j=aValue 12 j ∧ cachedCenterC 12 j=cValue 12 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_13 : cachedFree 13=freeValue 13 ∧
      (∀ j : Fin 7, cachedCenterA 13 j=aValue 13 j ∧ cachedCenterC 13 j=cValue 13 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_14 : cachedFree 14=freeValue 14 ∧
      (∀ j : Fin 7, cachedCenterA 14 j=aValue 14 j ∧ cachedCenterC 14 j=cValue 14 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_15 : cachedFree 15=freeValue 15 ∧
      (∀ j : Fin 7, cachedCenterA 15 j=aValue 15 j ∧ cachedCenterC 15 j=cValue 15 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
