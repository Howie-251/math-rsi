import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_10 : cachedFree 10 = freeValue 10 ∧
    (∀ j : Fin 5, cachedCenterA 10 j = aValue 10 j ∧ cachedCenterC 10 j = cValue 10 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_11 : cachedFree 11 = freeValue 11 ∧
    (∀ j : Fin 5, cachedCenterA 11 j = aValue 11 j ∧ cachedCenterC 11 j = cValue 11 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_12 : cachedFree 12 = freeValue 12 ∧
    (∀ j : Fin 5, cachedCenterA 12 j = aValue 12 j ∧ cachedCenterC 12 j = cValue 12 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_13 : cachedFree 13 = freeValue 13 ∧
    (∀ j : Fin 5, cachedCenterA 13 j = aValue 13 j ∧ cachedCenterC 13 j = cValue 13 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_14 : cachedFree 14 = freeValue 14 ∧
    (∀ j : Fin 5, cachedCenterA 14 j = aValue 14 j ∧ cachedCenterC 14 j = cValue 14 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.rows_14
