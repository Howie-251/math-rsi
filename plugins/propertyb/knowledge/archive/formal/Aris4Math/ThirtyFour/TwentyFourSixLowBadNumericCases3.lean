import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_30 : Numeric.validProfile (p 30) 34 ∧ (p 30).emptyPairCap=none ∧
    (∀ j, (positions 30 j).val+1∈(p 30).correctionCenters) ∧
    (∀ j z, 0≤α 30 j z) ∧ (∀ j z, j∉R 30 j z) ∧
    (∀ j z, quota 30 j z ≤
      (4*avoidedCount (p 30) ((positions 30 j).val+1) (avoidedPositions (positions 30) (R 30 j z))+2-
        (24-1-(R 30 j z).card))/3) ∧
    (∀ j, loss 30 j ≤ (∑ z, (quota 30 j z : ℚ)*α 30 j z)-
      penaltySum (p 30) ((positions 30 j).val+1) (fun z => avoidedPositions (positions 30) (R 30 j z)) (α 30 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 30) (k.val+1) true)
      (min (CachedRows.cachedA (p 30) (k.val+1) false) (CachedRows.cachedC (p 30) (k.val+1)-centerLoss (positions 30) (loss 30) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_31 : Numeric.validProfile (p 31) 34 ∧ (p 31).emptyPairCap=none ∧
    (∀ j, (positions 31 j).val+1∈(p 31).correctionCenters) ∧
    (∀ j z, 0≤α 31 j z) ∧ (∀ j z, j∉R 31 j z) ∧
    (∀ j z, quota 31 j z ≤
      (4*avoidedCount (p 31) ((positions 31 j).val+1) (avoidedPositions (positions 31) (R 31 j z))+2-
        (24-1-(R 31 j z).card))/3) ∧
    (∀ j, loss 31 j ≤ (∑ z, (quota 31 j z : ℚ)*α 31 j z)-
      penaltySum (p 31) ((positions 31 j).val+1) (fun z => avoidedPositions (positions 31) (R 31 j z)) (α 31 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 31) (k.val+1) true)
      (min (CachedRows.cachedA (p 31) (k.val+1) false) (CachedRows.cachedC (p 31) (k.val+1)-centerLoss (positions 31) (loss 31) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_32 : Numeric.validProfile (p 32) 34 ∧ (p 32).emptyPairCap=none ∧
    (∀ j, (positions 32 j).val+1∈(p 32).correctionCenters) ∧
    (∀ j z, 0≤α 32 j z) ∧ (∀ j z, j∉R 32 j z) ∧
    (∀ j z, quota 32 j z ≤
      (4*avoidedCount (p 32) ((positions 32 j).val+1) (avoidedPositions (positions 32) (R 32 j z))+2-
        (24-1-(R 32 j z).card))/3) ∧
    (∀ j, loss 32 j ≤ (∑ z, (quota 32 j z : ℚ)*α 32 j z)-
      penaltySum (p 32) ((positions 32 j).val+1) (fun z => avoidedPositions (positions 32) (R 32 j z)) (α 32 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 32) (k.val+1) true)
      (min (CachedRows.cachedA (p 32) (k.val+1) false) (CachedRows.cachedC (p 32) (k.val+1)-centerLoss (positions 32) (loss 32) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_33 : Numeric.validProfile (p 33) 34 ∧ (p 33).emptyPairCap=none ∧
    (∀ j, (positions 33 j).val+1∈(p 33).correctionCenters) ∧
    (∀ j z, 0≤α 33 j z) ∧ (∀ j z, j∉R 33 j z) ∧
    (∀ j z, quota 33 j z ≤
      (4*avoidedCount (p 33) ((positions 33 j).val+1) (avoidedPositions (positions 33) (R 33 j z))+2-
        (24-1-(R 33 j z).card))/3) ∧
    (∀ j, loss 33 j ≤ (∑ z, (quota 33 j z : ℚ)*α 33 j z)-
      penaltySum (p 33) ((positions 33 j).val+1) (fun z => avoidedPositions (positions 33) (R 33 j z)) (α 33 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 33) (k.val+1) true)
      (min (CachedRows.cachedA (p 33) (k.val+1) false) (CachedRows.cachedC (p 33) (k.val+1)-centerLoss (positions 33) (loss 33) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_34 : Numeric.validProfile (p 34) 34 ∧ (p 34).emptyPairCap=none ∧
    (∀ j, (positions 34 j).val+1∈(p 34).correctionCenters) ∧
    (∀ j z, 0≤α 34 j z) ∧ (∀ j z, j∉R 34 j z) ∧
    (∀ j z, quota 34 j z ≤
      (4*avoidedCount (p 34) ((positions 34 j).val+1) (avoidedPositions (positions 34) (R 34 j z))+2-
        (24-1-(R 34 j z).card))/3) ∧
    (∀ j, loss 34 j ≤ (∑ z, (quota 34 j z : ℚ)*α 34 j z)-
      penaltySum (p 34) ((positions 34 j).val+1) (fun z => avoidedPositions (positions 34) (R 34 j z)) (α 34 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 34) (k.val+1) true)
      (min (CachedRows.cachedA (p 34) (k.val+1) false) (CachedRows.cachedC (p 34) (k.val+1)-centerLoss (positions 34) (loss 34) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_35 : Numeric.validProfile (p 35) 34 ∧ (p 35).emptyPairCap=none ∧
    (∀ j, (positions 35 j).val+1∈(p 35).correctionCenters) ∧
    (∀ j z, 0≤α 35 j z) ∧ (∀ j z, j∉R 35 j z) ∧
    (∀ j z, quota 35 j z ≤
      (4*avoidedCount (p 35) ((positions 35 j).val+1) (avoidedPositions (positions 35) (R 35 j z))+2-
        (24-1-(R 35 j z).card))/3) ∧
    (∀ j, loss 35 j ≤ (∑ z, (quota 35 j z : ℚ)*α 35 j z)-
      penaltySum (p 35) ((positions 35 j).val+1) (fun z => avoidedPositions (positions 35) (R 35 j z)) (α 35 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 35) (k.val+1) true)
      (min (CachedRows.cachedA (p 35) (k.val+1) false) (CachedRows.cachedC (p 35) (k.val+1)-centerLoss (positions 35) (loss 35) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_36 : Numeric.validProfile (p 36) 34 ∧ (p 36).emptyPairCap=none ∧
    (∀ j, (positions 36 j).val+1∈(p 36).correctionCenters) ∧
    (∀ j z, 0≤α 36 j z) ∧ (∀ j z, j∉R 36 j z) ∧
    (∀ j z, quota 36 j z ≤
      (4*avoidedCount (p 36) ((positions 36 j).val+1) (avoidedPositions (positions 36) (R 36 j z))+2-
        (24-1-(R 36 j z).card))/3) ∧
    (∀ j, loss 36 j ≤ (∑ z, (quota 36 j z : ℚ)*α 36 j z)-
      penaltySum (p 36) ((positions 36 j).val+1) (fun z => avoidedPositions (positions 36) (R 36 j z)) (α 36 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 36) (k.val+1) true)
      (min (CachedRows.cachedA (p 36) (k.val+1) false) (CachedRows.cachedC (p 36) (k.val+1)-centerLoss (positions 36) (loss 36) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_37 : Numeric.validProfile (p 37) 34 ∧ (p 37).emptyPairCap=none ∧
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
theorem cached_case_38 : Numeric.validProfile (p 38) 34 ∧ (p 38).emptyPairCap=none ∧
    (∀ j, (positions 38 j).val+1∈(p 38).correctionCenters) ∧
    (∀ j z, 0≤α 38 j z) ∧ (∀ j z, j∉R 38 j z) ∧
    (∀ j z, quota 38 j z ≤
      (4*avoidedCount (p 38) ((positions 38 j).val+1) (avoidedPositions (positions 38) (R 38 j z))+2-
        (24-1-(R 38 j z).card))/3) ∧
    (∀ j, loss 38 j ≤ (∑ z, (quota 38 j z : ℚ)*α 38 j z)-
      penaltySum (p 38) ((positions 38 j).val+1) (fun z => avoidedPositions (positions 38) (R 38 j z)) (α 38 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 38) (k.val+1) true)
      (min (CachedRows.cachedA (p 38) (k.val+1) false) (CachedRows.cachedC (p 38) (k.val+1)-centerLoss (positions 38) (loss 38) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_39 : Numeric.validProfile (p 39) 34 ∧ (p 39).emptyPairCap=none ∧
    (∀ j, (positions 39 j).val+1∈(p 39).correctionCenters) ∧
    (∀ j z, 0≤α 39 j z) ∧ (∀ j z, j∉R 39 j z) ∧
    (∀ j z, quota 39 j z ≤
      (4*avoidedCount (p 39) ((positions 39 j).val+1) (avoidedPositions (positions 39) (R 39 j z))+2-
        (24-1-(R 39 j z).card))/3) ∧
    (∀ j, loss 39 j ≤ (∑ z, (quota 39 j z : ℚ)*α 39 j z)-
      penaltySum (p 39) ((positions 39 j).val+1) (fun z => avoidedPositions (positions 39) (R 39 j z)) (α 39 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 39) (k.val+1) true)
      (min (CachedRows.cachedA (p 39) (k.val+1) false) (CachedRows.cachedC (p 39) (k.val+1)-centerLoss (positions 39) (loss 39) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
