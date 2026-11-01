import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_5 : cachedFree 5 = freeValue 5 ∧
    (∀ j : Fin 5, cachedCenterA 5 j = aValue 5 j ∧ cachedCenterC 5 j = cValue 5 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_6 : cachedFree 6 = freeValue 6 ∧
    (∀ j : Fin 5, cachedCenterA 6 j = aValue 6 j ∧ cachedCenterC 6 j = cValue 6 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_7 : cachedFree 7 = freeValue 7 ∧
    (∀ j : Fin 5, cachedCenterA 7 j = aValue 7 j ∧ cachedCenterC 7 j = cValue 7 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_8 : cachedFree 8 = freeValue 8 ∧
    (∀ j : Fin 5, cachedCenterA 8 j = aValue 8 j ∧ cachedCenterC 8 j = cValue 8 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_9 : cachedFree 9 = freeValue 9 ∧
    (∀ j : Fin 5, cachedCenterA 9 j = aValue 9 j ∧ cachedCenterC 9 j = cValue 9 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.rows_9
