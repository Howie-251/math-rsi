import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_4 : cachedFree 4=freeValue 4 ∧
      (∀ j : Fin 7, cachedCenterA 4 j=aValue 4 j ∧ cachedCenterC 4 j=cValue 4 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_5 : cachedFree 5=freeValue 5 ∧
      (∀ j : Fin 7, cachedCenterA 5 j=aValue 5 j ∧ cachedCenterC 5 j=cValue 5 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_6 : cachedFree 6=freeValue 6 ∧
      (∀ j : Fin 7, cachedCenterA 6 j=aValue 6 j ∧ cachedCenterC 6 j=cValue 6 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
theorem rows_7 : cachedFree 7=freeValue 7 ∧
      (∀ j : Fin 7, cachedCenterA 7 j=aValue 7 j ∧ cachedCenterC 7 j=cValue 7 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
