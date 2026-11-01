import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_16 : cachedFree 16=freeValue 16 ∧
      (∀ j : Fin 7, cachedCenterA 16 j=aValue 16 j ∧ cachedCenterC 16 j=cValue 16 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_17 : cachedFree 17=freeValue 17 ∧
      (∀ j : Fin 7, cachedCenterA 17 j=aValue 17 j ∧ cachedCenterC 17 j=cValue 17 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_18 : cachedFree 18=freeValue 18 ∧
      (∀ j : Fin 7, cachedCenterA 18 j=aValue 18 j ∧ cachedCenterC 18 j=cValue 18 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_19 : cachedFree 19=freeValue 19 ∧
      (∀ j : Fin 7, cachedCenterA 19 j=aValue 19 j ∧ cachedCenterC 19 j=cValue 19 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
