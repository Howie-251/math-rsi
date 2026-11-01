import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_28 : cachedFree 28=freeValue 28 ∧
      (∀ j : Fin 7, cachedCenterA 28 j=aValue 28 j ∧ cachedCenterC 28 j=cValue 28 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_29 : cachedFree 29=freeValue 29 ∧
      (∀ j : Fin 7, cachedCenterA 29 j=aValue 29 j ∧ cachedCenterC 29 j=cValue 29 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_30 : cachedFree 30=freeValue 30 ∧
      (∀ j : Fin 7, cachedCenterA 30 j=aValue 30 j ∧ cachedCenterC 30 j=cValue 30 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
