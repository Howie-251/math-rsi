import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
example : Numeric.validProfile (p 0) 34 ∧ (p 0).emptyPairCap=none ∧
    (∀ j, (positions 0 j).val+1∈(p 0).correctionCenters) ∧
    (∀ j z, 0≤α 0 j z) ∧ (∀ j z, j∉R 0 j z) ∧
    (∀ j z, quota 0 j z ≤
      (4*avoidedCount (p 0) ((positions 0 j).val+1) (avoidedPositions (positions 0) (R 0 j z))+2-
        (24-1-(R 0 j z).card))/3) ∧
    (∀ j, loss 0 j ≤ (∑ z, (quota 0 j z : ℚ)*α 0 j z)-
      penaltySum (p 0) ((positions 0 j).val+1) (fun z => avoidedPositions (positions 0) (R 0 j z)) (α 0 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 0) (k.val+1) true)
      (min (CachedRows.cachedA (p 0) (k.val+1) false) (CachedRows.cachedC (p 0) (k.val+1)-centerLoss (positions 0) (loss 0) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
example : Numeric.validProfile (p 37) 34 ∧ (p 37).emptyPairCap=none ∧
    (∀ j, (positions 37 j).val+1∈(p 37).correctionCenters) ∧
    (∀ j z, 0≤α 37 j z) ∧ (∀ j z, j∉R 37 j z) ∧
    (∀ j z, quota 37 j z ≤
      (4*avoidedCount (p 37) ((positions 37 j).val+1) (avoidedPositions (positions 37) (R 37 j z))+2-
        (24-1-(R 37 j z).card))/3) ∧
    (∀ j, loss 37 j ≤ (∑ z, (quota 37 j z : ℚ)*α 37 j z)-
      penaltySum (p 37) ((positions 37 j).val+1) (fun z => avoidedPositions (positions 37) (R 37 j z)) (α 37 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 37) (k.val+1) true)
      (min (CachedRows.cachedA (p 37) (k.val+1) false) (CachedRows.cachedC (p 37) (k.val+1)-centerLoss (positions 37) (loss 37) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
example : Numeric.validProfile (p 90) 34 ∧ (p 90).emptyPairCap=none ∧
    (∀ j, (positions 90 j).val+1∈(p 90).correctionCenters) ∧
    (∀ j z, 0≤α 90 j z) ∧ (∀ j z, j∉R 90 j z) ∧
    (∀ j z, quota 90 j z ≤
      (4*avoidedCount (p 90) ((positions 90 j).val+1) (avoidedPositions (positions 90) (R 90 j z))+2-
        (24-1-(R 90 j z).card))/3) ∧
    (∀ j, loss 90 j ≤ (∑ z, (quota 90 j z : ℚ)*α 90 j z)-
      penaltySum (p 90) ((positions 90 j).val+1) (fun z => avoidedPositions (positions 90) (R 90 j z)) (α 90 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 90) (k.val+1) true)
      (min (CachedRows.cachedA (p 90) (k.val+1) false) (CachedRows.cachedC (p 90) (k.val+1)-centerLoss (positions 90) (loss 90) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
example : Numeric.validProfile (p 174) 34 ∧ (p 174).emptyPairCap=none ∧
    (∀ j, (positions 174 j).val+1∈(p 174).correctionCenters) ∧
    (∀ j z, 0≤α 174 j z) ∧ (∀ j z, j∉R 174 j z) ∧
    (∀ j z, quota 174 j z ≤
      (4*avoidedCount (p 174) ((positions 174 j).val+1) (avoidedPositions (positions 174) (R 174 j z))+2-
        (24-1-(R 174 j z).card))/3) ∧
    (∀ j, loss 174 j ≤ (∑ z, (quota 174 j z : ℚ)*α 174 j z)-
      penaltySum (p 174) ((positions 174 j).val+1) (fun z => avoidedPositions (positions 174) (R 174 j z)) (α 174 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 174) (k.val+1) true)
      (min (CachedRows.cachedA (p 174) (k.val+1) false) (CachedRows.cachedC (p 174) (k.val+1)-centerLoss (positions 174) (loss 174) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
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
