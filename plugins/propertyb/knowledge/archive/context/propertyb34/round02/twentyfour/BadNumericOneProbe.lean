import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
example : Numeric.validProfile (p 179) 34 ∧ (p 179).emptyPairCap=none ∧
    (∀ j, (positions 179 j).val+1∈(p 179).correctionCenters) ∧
    (∀ j z, 0≤α 179 j z) ∧ (∀ j z, j∉R 179 j z) ∧
    (∀ j z, quota 179 j z ≤
      (4*avoidedCount (p 179) ((positions 179 j).val+1) (avoidedPositions (positions 179) (R 179 j z))+2-
        (24-1-(R 179 j z).card))/3) ∧
    (∀ j, loss 179 j ≤ (∑ z, (quota 179 j z : ℚ)*α 179 j z)-
      penaltySum (p 179) ((positions 179 j).val+1) (fun z => avoidedPositions (positions 179) (R 179 j z)) (α 179 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 179) (k.val+1) true)
      (min (CachedRows.cachedA (p 179) (k.val+1) false) (CachedRows.cachedC (p 179) (k.val+1)-centerLoss (positions 179) (loss 179) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
