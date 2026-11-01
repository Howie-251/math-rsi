import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_180 : Numeric.validProfile (p 180) 34 ∧ (p 180).emptyPairCap=none ∧
    (∀ j, (positions 180 j).val+1∈(p 180).correctionCenters) ∧
    (∀ j z, 0≤α 180 j z) ∧ (∀ j z, j∉R 180 j z) ∧
    (∀ j z, quota 180 j z ≤
      (4*avoidedCount (p 180) ((positions 180 j).val+1) (avoidedPositions (positions 180) (R 180 j z))+2-
        (24-1-(R 180 j z).card))/3) ∧
    (∀ j, loss 180 j ≤ (∑ z, (quota 180 j z : ℚ)*α 180 j z)-
      penaltySum (p 180) ((positions 180 j).val+1) (fun z => avoidedPositions (positions 180) (R 180 j z)) (α 180 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 180) (k.val+1) true)
      (min (CachedRows.cachedA (p 180) (k.val+1) false) (CachedRows.cachedC (p 180) (k.val+1)-centerLoss (positions 180) (loss 180) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
