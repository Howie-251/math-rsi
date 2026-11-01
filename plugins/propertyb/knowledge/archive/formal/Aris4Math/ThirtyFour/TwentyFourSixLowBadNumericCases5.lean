import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_50 : Numeric.validProfile (p 50) 34 ∧ (p 50).emptyPairCap=none ∧
    (∀ j, (positions 50 j).val+1∈(p 50).correctionCenters) ∧
    (∀ j z, 0≤α 50 j z) ∧ (∀ j z, j∉R 50 j z) ∧
    (∀ j z, quota 50 j z ≤
      (4*avoidedCount (p 50) ((positions 50 j).val+1) (avoidedPositions (positions 50) (R 50 j z))+2-
        (24-1-(R 50 j z).card))/3) ∧
    (∀ j, loss 50 j ≤ (∑ z, (quota 50 j z : ℚ)*α 50 j z)-
      penaltySum (p 50) ((positions 50 j).val+1) (fun z => avoidedPositions (positions 50) (R 50 j z)) (α 50 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 50) (k.val+1) true)
      (min (CachedRows.cachedA (p 50) (k.val+1) false) (CachedRows.cachedC (p 50) (k.val+1)-centerLoss (positions 50) (loss 50) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_51 : Numeric.validProfile (p 51) 34 ∧ (p 51).emptyPairCap=none ∧
    (∀ j, (positions 51 j).val+1∈(p 51).correctionCenters) ∧
    (∀ j z, 0≤α 51 j z) ∧ (∀ j z, j∉R 51 j z) ∧
    (∀ j z, quota 51 j z ≤
      (4*avoidedCount (p 51) ((positions 51 j).val+1) (avoidedPositions (positions 51) (R 51 j z))+2-
        (24-1-(R 51 j z).card))/3) ∧
    (∀ j, loss 51 j ≤ (∑ z, (quota 51 j z : ℚ)*α 51 j z)-
      penaltySum (p 51) ((positions 51 j).val+1) (fun z => avoidedPositions (positions 51) (R 51 j z)) (α 51 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 51) (k.val+1) true)
      (min (CachedRows.cachedA (p 51) (k.val+1) false) (CachedRows.cachedC (p 51) (k.val+1)-centerLoss (positions 51) (loss 51) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_52 : Numeric.validProfile (p 52) 34 ∧ (p 52).emptyPairCap=none ∧
    (∀ j, (positions 52 j).val+1∈(p 52).correctionCenters) ∧
    (∀ j z, 0≤α 52 j z) ∧ (∀ j z, j∉R 52 j z) ∧
    (∀ j z, quota 52 j z ≤
      (4*avoidedCount (p 52) ((positions 52 j).val+1) (avoidedPositions (positions 52) (R 52 j z))+2-
        (24-1-(R 52 j z).card))/3) ∧
    (∀ j, loss 52 j ≤ (∑ z, (quota 52 j z : ℚ)*α 52 j z)-
      penaltySum (p 52) ((positions 52 j).val+1) (fun z => avoidedPositions (positions 52) (R 52 j z)) (α 52 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 52) (k.val+1) true)
      (min (CachedRows.cachedA (p 52) (k.val+1) false) (CachedRows.cachedC (p 52) (k.val+1)-centerLoss (positions 52) (loss 52) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_53 : Numeric.validProfile (p 53) 34 ∧ (p 53).emptyPairCap=none ∧
    (∀ j, (positions 53 j).val+1∈(p 53).correctionCenters) ∧
    (∀ j z, 0≤α 53 j z) ∧ (∀ j z, j∉R 53 j z) ∧
    (∀ j z, quota 53 j z ≤
      (4*avoidedCount (p 53) ((positions 53 j).val+1) (avoidedPositions (positions 53) (R 53 j z))+2-
        (24-1-(R 53 j z).card))/3) ∧
    (∀ j, loss 53 j ≤ (∑ z, (quota 53 j z : ℚ)*α 53 j z)-
      penaltySum (p 53) ((positions 53 j).val+1) (fun z => avoidedPositions (positions 53) (R 53 j z)) (α 53 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 53) (k.val+1) true)
      (min (CachedRows.cachedA (p 53) (k.val+1) false) (CachedRows.cachedC (p 53) (k.val+1)-centerLoss (positions 53) (loss 53) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_54 : Numeric.validProfile (p 54) 34 ∧ (p 54).emptyPairCap=none ∧
    (∀ j, (positions 54 j).val+1∈(p 54).correctionCenters) ∧
    (∀ j z, 0≤α 54 j z) ∧ (∀ j z, j∉R 54 j z) ∧
    (∀ j z, quota 54 j z ≤
      (4*avoidedCount (p 54) ((positions 54 j).val+1) (avoidedPositions (positions 54) (R 54 j z))+2-
        (24-1-(R 54 j z).card))/3) ∧
    (∀ j, loss 54 j ≤ (∑ z, (quota 54 j z : ℚ)*α 54 j z)-
      penaltySum (p 54) ((positions 54 j).val+1) (fun z => avoidedPositions (positions 54) (R 54 j z)) (α 54 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 54) (k.val+1) true)
      (min (CachedRows.cachedA (p 54) (k.val+1) false) (CachedRows.cachedC (p 54) (k.val+1)-centerLoss (positions 54) (loss 54) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_55 : Numeric.validProfile (p 55) 34 ∧ (p 55).emptyPairCap=none ∧
    (∀ j, (positions 55 j).val+1∈(p 55).correctionCenters) ∧
    (∀ j z, 0≤α 55 j z) ∧ (∀ j z, j∉R 55 j z) ∧
    (∀ j z, quota 55 j z ≤
      (4*avoidedCount (p 55) ((positions 55 j).val+1) (avoidedPositions (positions 55) (R 55 j z))+2-
        (24-1-(R 55 j z).card))/3) ∧
    (∀ j, loss 55 j ≤ (∑ z, (quota 55 j z : ℚ)*α 55 j z)-
      penaltySum (p 55) ((positions 55 j).val+1) (fun z => avoidedPositions (positions 55) (R 55 j z)) (α 55 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 55) (k.val+1) true)
      (min (CachedRows.cachedA (p 55) (k.val+1) false) (CachedRows.cachedC (p 55) (k.val+1)-centerLoss (positions 55) (loss 55) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_56 : Numeric.validProfile (p 56) 34 ∧ (p 56).emptyPairCap=none ∧
    (∀ j, (positions 56 j).val+1∈(p 56).correctionCenters) ∧
    (∀ j z, 0≤α 56 j z) ∧ (∀ j z, j∉R 56 j z) ∧
    (∀ j z, quota 56 j z ≤
      (4*avoidedCount (p 56) ((positions 56 j).val+1) (avoidedPositions (positions 56) (R 56 j z))+2-
        (24-1-(R 56 j z).card))/3) ∧
    (∀ j, loss 56 j ≤ (∑ z, (quota 56 j z : ℚ)*α 56 j z)-
      penaltySum (p 56) ((positions 56 j).val+1) (fun z => avoidedPositions (positions 56) (R 56 j z)) (α 56 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 56) (k.val+1) true)
      (min (CachedRows.cachedA (p 56) (k.val+1) false) (CachedRows.cachedC (p 56) (k.val+1)-centerLoss (positions 56) (loss 56) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_57 : Numeric.validProfile (p 57) 34 ∧ (p 57).emptyPairCap=none ∧
    (∀ j, (positions 57 j).val+1∈(p 57).correctionCenters) ∧
    (∀ j z, 0≤α 57 j z) ∧ (∀ j z, j∉R 57 j z) ∧
    (∀ j z, quota 57 j z ≤
      (4*avoidedCount (p 57) ((positions 57 j).val+1) (avoidedPositions (positions 57) (R 57 j z))+2-
        (24-1-(R 57 j z).card))/3) ∧
    (∀ j, loss 57 j ≤ (∑ z, (quota 57 j z : ℚ)*α 57 j z)-
      penaltySum (p 57) ((positions 57 j).val+1) (fun z => avoidedPositions (positions 57) (R 57 j z)) (α 57 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 57) (k.val+1) true)
      (min (CachedRows.cachedA (p 57) (k.val+1) false) (CachedRows.cachedC (p 57) (k.val+1)-centerLoss (positions 57) (loss 57) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_58 : Numeric.validProfile (p 58) 34 ∧ (p 58).emptyPairCap=none ∧
    (∀ j, (positions 58 j).val+1∈(p 58).correctionCenters) ∧
    (∀ j z, 0≤α 58 j z) ∧ (∀ j z, j∉R 58 j z) ∧
    (∀ j z, quota 58 j z ≤
      (4*avoidedCount (p 58) ((positions 58 j).val+1) (avoidedPositions (positions 58) (R 58 j z))+2-
        (24-1-(R 58 j z).card))/3) ∧
    (∀ j, loss 58 j ≤ (∑ z, (quota 58 j z : ℚ)*α 58 j z)-
      penaltySum (p 58) ((positions 58 j).val+1) (fun z => avoidedPositions (positions 58) (R 58 j z)) (α 58 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 58) (k.val+1) true)
      (min (CachedRows.cachedA (p 58) (k.val+1) false) (CachedRows.cachedC (p 58) (k.val+1)-centerLoss (positions 58) (loss 58) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_59 : Numeric.validProfile (p 59) 34 ∧ (p 59).emptyPairCap=none ∧
    (∀ j, (positions 59 j).val+1∈(p 59).correctionCenters) ∧
    (∀ j z, 0≤α 59 j z) ∧ (∀ j z, j∉R 59 j z) ∧
    (∀ j z, quota 59 j z ≤
      (4*avoidedCount (p 59) ((positions 59 j).val+1) (avoidedPositions (positions 59) (R 59 j z))+2-
        (24-1-(R 59 j z).card))/3) ∧
    (∀ j, loss 59 j ≤ (∑ z, (quota 59 j z : ℚ)*α 59 j z)-
      penaltySum (p 59) ((positions 59 j).val+1) (fun z => avoidedPositions (positions 59) (R 59 j z)) (α 59 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 59) (k.val+1) true)
      (min (CachedRows.cachedA (p 59) (k.val+1) false) (CachedRows.cachedC (p 59) (k.val+1)-centerLoss (positions 59) (loss 59) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
