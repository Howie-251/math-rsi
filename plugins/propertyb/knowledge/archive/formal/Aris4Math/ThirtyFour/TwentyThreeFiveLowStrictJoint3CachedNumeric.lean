import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedRows0
import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedRows1
import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedRows2
import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedRows3
import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedPenalty
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_exact (l : Layout) : cachedFree l = freeValue l ∧
    (∀ j : Fin 5, cachedCenterA l j = aValue l j ∧ cachedCenterC l j = cValue l j) := by
  fin_cases l
  · exact rows_0
  · exact rows_1
  · exact rows_2
  · exact rows_3
  · exact rows_4
  · exact rows_5
  · exact rows_6
  · exact rows_7
  · exact rows_8
  · exact rows_9
  · exact rows_10
  · exact rows_11
  · exact rows_12
  · exact rows_13
  · exact rows_14
  · exact rows_15
  · exact rows_16
  · exact rows_17
  · exact rows_18
  · exact rows_19

theorem free_exact (l : Layout) : cachedFree l = freeValue l := (rows_exact l).1
theorem a_exact (l : Layout) (j : Fin 5) : cachedCenterA l j = aValue l j := ((rows_exact l).2 j).1
theorem c_exact (l : Layout) (j : Fin 5) : cachedCenterC l j = cValue l j := ((rows_exact l).2 j).2
theorem strict :
    (∑ l, gamma l*free (positions l) (p l)) +
    (∑ l, ∑ j, ((gamma l-beta l j)*a positions p l j+beta l j*c positions p l j)) -
    (∑ j, ((∑ q, (quota j q : ℚ)*delta j q)-
      penalty support μ beta (weights positions p) j (R j) (delta j))) < 1 := by
  simp_rw [free_eq,a_eq,c_eq,free_exact,a_exact,c_exact,penalty_zero]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.strict
