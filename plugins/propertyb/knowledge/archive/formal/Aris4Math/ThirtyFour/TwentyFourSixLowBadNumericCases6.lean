import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_60 : Numeric.validProfile (p 60) 34 ∧ (p 60).emptyPairCap=none ∧
    (∀ j, (positions 60 j).val+1∈(p 60).correctionCenters) ∧
    (∀ j z, 0≤α 60 j z) ∧ (∀ j z, j∉R 60 j z) ∧
    (∀ j z, quota 60 j z ≤
      (4*avoidedCount (p 60) ((positions 60 j).val+1) (avoidedPositions (positions 60) (R 60 j z))+2-
        (24-1-(R 60 j z).card))/3) ∧
    (∀ j, loss 60 j ≤ (∑ z, (quota 60 j z : ℚ)*α 60 j z)-
      penaltySum (p 60) ((positions 60 j).val+1) (fun z => avoidedPositions (positions 60) (R 60 j z)) (α 60 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 60) (k.val+1) true)
      (min (CachedRows.cachedA (p 60) (k.val+1) false) (CachedRows.cachedC (p 60) (k.val+1)-centerLoss (positions 60) (loss 60) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_61 : Numeric.validProfile (p 61) 34 ∧ (p 61).emptyPairCap=none ∧
    (∀ j, (positions 61 j).val+1∈(p 61).correctionCenters) ∧
    (∀ j z, 0≤α 61 j z) ∧ (∀ j z, j∉R 61 j z) ∧
    (∀ j z, quota 61 j z ≤
      (4*avoidedCount (p 61) ((positions 61 j).val+1) (avoidedPositions (positions 61) (R 61 j z))+2-
        (24-1-(R 61 j z).card))/3) ∧
    (∀ j, loss 61 j ≤ (∑ z, (quota 61 j z : ℚ)*α 61 j z)-
      penaltySum (p 61) ((positions 61 j).val+1) (fun z => avoidedPositions (positions 61) (R 61 j z)) (α 61 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 61) (k.val+1) true)
      (min (CachedRows.cachedA (p 61) (k.val+1) false) (CachedRows.cachedC (p 61) (k.val+1)-centerLoss (positions 61) (loss 61) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_62 : Numeric.validProfile (p 62) 34 ∧ (p 62).emptyPairCap=none ∧
    (∀ j, (positions 62 j).val+1∈(p 62).correctionCenters) ∧
    (∀ j z, 0≤α 62 j z) ∧ (∀ j z, j∉R 62 j z) ∧
    (∀ j z, quota 62 j z ≤
      (4*avoidedCount (p 62) ((positions 62 j).val+1) (avoidedPositions (positions 62) (R 62 j z))+2-
        (24-1-(R 62 j z).card))/3) ∧
    (∀ j, loss 62 j ≤ (∑ z, (quota 62 j z : ℚ)*α 62 j z)-
      penaltySum (p 62) ((positions 62 j).val+1) (fun z => avoidedPositions (positions 62) (R 62 j z)) (α 62 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 62) (k.val+1) true)
      (min (CachedRows.cachedA (p 62) (k.val+1) false) (CachedRows.cachedC (p 62) (k.val+1)-centerLoss (positions 62) (loss 62) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_63 : Numeric.validProfile (p 63) 34 ∧ (p 63).emptyPairCap=none ∧
    (∀ j, (positions 63 j).val+1∈(p 63).correctionCenters) ∧
    (∀ j z, 0≤α 63 j z) ∧ (∀ j z, j∉R 63 j z) ∧
    (∀ j z, quota 63 j z ≤
      (4*avoidedCount (p 63) ((positions 63 j).val+1) (avoidedPositions (positions 63) (R 63 j z))+2-
        (24-1-(R 63 j z).card))/3) ∧
    (∀ j, loss 63 j ≤ (∑ z, (quota 63 j z : ℚ)*α 63 j z)-
      penaltySum (p 63) ((positions 63 j).val+1) (fun z => avoidedPositions (positions 63) (R 63 j z)) (α 63 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 63) (k.val+1) true)
      (min (CachedRows.cachedA (p 63) (k.val+1) false) (CachedRows.cachedC (p 63) (k.val+1)-centerLoss (positions 63) (loss 63) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_64 : Numeric.validProfile (p 64) 34 ∧ (p 64).emptyPairCap=none ∧
    (∀ j, (positions 64 j).val+1∈(p 64).correctionCenters) ∧
    (∀ j z, 0≤α 64 j z) ∧ (∀ j z, j∉R 64 j z) ∧
    (∀ j z, quota 64 j z ≤
      (4*avoidedCount (p 64) ((positions 64 j).val+1) (avoidedPositions (positions 64) (R 64 j z))+2-
        (24-1-(R 64 j z).card))/3) ∧
    (∀ j, loss 64 j ≤ (∑ z, (quota 64 j z : ℚ)*α 64 j z)-
      penaltySum (p 64) ((positions 64 j).val+1) (fun z => avoidedPositions (positions 64) (R 64 j z)) (α 64 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 64) (k.val+1) true)
      (min (CachedRows.cachedA (p 64) (k.val+1) false) (CachedRows.cachedC (p 64) (k.val+1)-centerLoss (positions 64) (loss 64) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_65 : Numeric.validProfile (p 65) 34 ∧ (p 65).emptyPairCap=none ∧
    (∀ j, (positions 65 j).val+1∈(p 65).correctionCenters) ∧
    (∀ j z, 0≤α 65 j z) ∧ (∀ j z, j∉R 65 j z) ∧
    (∀ j z, quota 65 j z ≤
      (4*avoidedCount (p 65) ((positions 65 j).val+1) (avoidedPositions (positions 65) (R 65 j z))+2-
        (24-1-(R 65 j z).card))/3) ∧
    (∀ j, loss 65 j ≤ (∑ z, (quota 65 j z : ℚ)*α 65 j z)-
      penaltySum (p 65) ((positions 65 j).val+1) (fun z => avoidedPositions (positions 65) (R 65 j z)) (α 65 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 65) (k.val+1) true)
      (min (CachedRows.cachedA (p 65) (k.val+1) false) (CachedRows.cachedC (p 65) (k.val+1)-centerLoss (positions 65) (loss 65) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_66 : Numeric.validProfile (p 66) 34 ∧ (p 66).emptyPairCap=none ∧
    (∀ j, (positions 66 j).val+1∈(p 66).correctionCenters) ∧
    (∀ j z, 0≤α 66 j z) ∧ (∀ j z, j∉R 66 j z) ∧
    (∀ j z, quota 66 j z ≤
      (4*avoidedCount (p 66) ((positions 66 j).val+1) (avoidedPositions (positions 66) (R 66 j z))+2-
        (24-1-(R 66 j z).card))/3) ∧
    (∀ j, loss 66 j ≤ (∑ z, (quota 66 j z : ℚ)*α 66 j z)-
      penaltySum (p 66) ((positions 66 j).val+1) (fun z => avoidedPositions (positions 66) (R 66 j z)) (α 66 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 66) (k.val+1) true)
      (min (CachedRows.cachedA (p 66) (k.val+1) false) (CachedRows.cachedC (p 66) (k.val+1)-centerLoss (positions 66) (loss 66) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_67 : Numeric.validProfile (p 67) 34 ∧ (p 67).emptyPairCap=none ∧
    (∀ j, (positions 67 j).val+1∈(p 67).correctionCenters) ∧
    (∀ j z, 0≤α 67 j z) ∧ (∀ j z, j∉R 67 j z) ∧
    (∀ j z, quota 67 j z ≤
      (4*avoidedCount (p 67) ((positions 67 j).val+1) (avoidedPositions (positions 67) (R 67 j z))+2-
        (24-1-(R 67 j z).card))/3) ∧
    (∀ j, loss 67 j ≤ (∑ z, (quota 67 j z : ℚ)*α 67 j z)-
      penaltySum (p 67) ((positions 67 j).val+1) (fun z => avoidedPositions (positions 67) (R 67 j z)) (α 67 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 67) (k.val+1) true)
      (min (CachedRows.cachedA (p 67) (k.val+1) false) (CachedRows.cachedC (p 67) (k.val+1)-centerLoss (positions 67) (loss 67) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_68 : Numeric.validProfile (p 68) 34 ∧ (p 68).emptyPairCap=none ∧
    (∀ j, (positions 68 j).val+1∈(p 68).correctionCenters) ∧
    (∀ j z, 0≤α 68 j z) ∧ (∀ j z, j∉R 68 j z) ∧
    (∀ j z, quota 68 j z ≤
      (4*avoidedCount (p 68) ((positions 68 j).val+1) (avoidedPositions (positions 68) (R 68 j z))+2-
        (24-1-(R 68 j z).card))/3) ∧
    (∀ j, loss 68 j ≤ (∑ z, (quota 68 j z : ℚ)*α 68 j z)-
      penaltySum (p 68) ((positions 68 j).val+1) (fun z => avoidedPositions (positions 68) (R 68 j z)) (α 68 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 68) (k.val+1) true)
      (min (CachedRows.cachedA (p 68) (k.val+1) false) (CachedRows.cachedC (p 68) (k.val+1)-centerLoss (positions 68) (loss 68) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_69 : Numeric.validProfile (p 69) 34 ∧ (p 69).emptyPairCap=none ∧
    (∀ j, (positions 69 j).val+1∈(p 69).correctionCenters) ∧
    (∀ j z, 0≤α 69 j z) ∧ (∀ j z, j∉R 69 j z) ∧
    (∀ j z, quota 69 j z ≤
      (4*avoidedCount (p 69) ((positions 69 j).val+1) (avoidedPositions (positions 69) (R 69 j z))+2-
        (24-1-(R 69 j z).card))/3) ∧
    (∀ j, loss 69 j ≤ (∑ z, (quota 69 j z : ℚ)*α 69 j z)-
      penaltySum (p 69) ((positions 69 j).val+1) (fun z => avoidedPositions (positions 69) (R 69 j z)) (α 69 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 69) (k.val+1) true)
      (min (CachedRows.cachedA (p 69) (k.val+1) false) (CachedRows.cachedC (p 69) (k.val+1)-centerLoss (positions 69) (loss 69) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
