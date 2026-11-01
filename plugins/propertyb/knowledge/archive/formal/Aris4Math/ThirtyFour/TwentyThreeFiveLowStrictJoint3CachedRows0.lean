import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_0 : cachedFree 0 = freeValue 0 ∧
    (∀ j : Fin 5, cachedCenterA 0 j = aValue 0 j ∧ cachedCenterC 0 j = cValue 0 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_1 : cachedFree 1 = freeValue 1 ∧
    (∀ j : Fin 5, cachedCenterA 1 j = aValue 1 j ∧ cachedCenterC 1 j = cValue 1 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_2 : cachedFree 2 = freeValue 2 ∧
    (∀ j : Fin 5, cachedCenterA 2 j = aValue 2 j ∧ cachedCenterC 2 j = cValue 2 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_3 : cachedFree 3 = freeValue 3 ∧
    (∀ j : Fin 5, cachedCenterA 3 j = aValue 3 j ∧ cachedCenterC 3 j = cValue 3 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_4 : cachedFree 4 = freeValue 4 ∧
    (∀ j : Fin 5, cachedCenterA 4 j = aValue 4 j ∧ cachedCenterC 4 j = cValue 4 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.rows_4
