import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows6
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedRows7
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedPenalty6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_exact (l : Layout) : cachedFree l=freeValue l ∧
    (∀ j : Fin 7, cachedCenterA l j=aValue l j ∧ cachedCenterC l j=cValue l j) := by
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
  · exact rows_20
  · exact rows_21
  · exact rows_22
  · exact rows_23
  · exact rows_24
  · exact rows_25
  · exact rows_26
  · exact rows_27
  · exact rows_28
  · exact rows_29
  · exact rows_30
theorem free_exact (l : Layout) : cachedFree l=freeValue l := (rows_exact l).1
theorem a_exact (l : Layout) (j : Fin 7) : cachedCenterA l j=aValue l j := ((rows_exact l).2 j).1
theorem c_exact (l : Layout) (j : Fin 7) : cachedCenterC l j=cValue l j := ((rows_exact l).2 j).2
theorem penalty_exact (j : Fin 7) : penalty support μ beta (weights positions p) j (R j) (delta j)=penaltyValue j := by
  fin_cases j
  · exact penalty_0
  · exact penalty_1
  · exact penalty_2
  · exact penalty_3
  · exact penalty_4
  · exact penalty_5
  · exact penalty_6
theorem strict :
    (∑ l, gamma l*free (positions l) (p l)) +
    (∑ l, ∑ j, ((gamma l-beta l j)*a positions p l j+beta l j*c positions p l j)) -
    (∑ j, ((∑ q, (quota j q : ℚ)*delta j q)-
      penalty support μ beta (weights positions p) j (R j) (delta j))) < 1 := by
  simp_rw [free_eq,a_eq,c_eq,free_exact,a_exact,c_exact,penalty_exact]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric.strict
