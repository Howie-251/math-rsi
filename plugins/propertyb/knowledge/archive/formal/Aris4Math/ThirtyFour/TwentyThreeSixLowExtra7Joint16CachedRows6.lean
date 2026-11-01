import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_24 : cachedFree 24=freeValue 24 ∧
      (∀ j : Fin 7, cachedCenterA 24 j=aValue 24 j ∧ cachedCenterC 24 j=cValue 24 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_25 : cachedFree 25=freeValue 25 ∧
      (∀ j : Fin 7, cachedCenterA 25 j=aValue 25 j ∧ cachedCenterC 25 j=cValue 25 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_26 : cachedFree 26=freeValue 26 ∧
      (∀ j : Fin 7, cachedCenterA 26 j=aValue 26 j ∧ cachedCenterC 26 j=cValue 26 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_27 : cachedFree 27=freeValue 27 ∧
      (∀ j : Fin 7, cachedCenterA 27 j=aValue 27 j ∧ cachedCenterC 27 j=cValue 27 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
