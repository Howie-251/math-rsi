import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_10 : Numeric.validProfile (p 10) 34 ∧ (p 10).emptyPairCap=none ∧
    (∀ j, (positions 10 j).val+1∈(p 10).correctionCenters) ∧
    (∀ j z, 0≤α 10 j z) ∧ (∀ j z, j∉R 10 j z) ∧
    (∀ j z, quota 10 j z ≤
      (4*avoidedCount (p 10) ((positions 10 j).val+1) (avoidedPositions (positions 10) (R 10 j z))+2-
        (24-1-(R 10 j z).card))/3) ∧
    (∀ j, loss 10 j ≤ (∑ z, (quota 10 j z : ℚ)*α 10 j z)-
      penaltySum (p 10) ((positions 10 j).val+1) (fun z => avoidedPositions (positions 10) (R 10 j z)) (α 10 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 10) (k.val+1) true)
      (min (CachedRows.cachedA (p 10) (k.val+1) false) (CachedRows.cachedC (p 10) (k.val+1)-centerLoss (positions 10) (loss 10) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_11 : Numeric.validProfile (p 11) 34 ∧ (p 11).emptyPairCap=none ∧
    (∀ j, (positions 11 j).val+1∈(p 11).correctionCenters) ∧
    (∀ j z, 0≤α 11 j z) ∧ (∀ j z, j∉R 11 j z) ∧
    (∀ j z, quota 11 j z ≤
      (4*avoidedCount (p 11) ((positions 11 j).val+1) (avoidedPositions (positions 11) (R 11 j z))+2-
        (24-1-(R 11 j z).card))/3) ∧
    (∀ j, loss 11 j ≤ (∑ z, (quota 11 j z : ℚ)*α 11 j z)-
      penaltySum (p 11) ((positions 11 j).val+1) (fun z => avoidedPositions (positions 11) (R 11 j z)) (α 11 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 11) (k.val+1) true)
      (min (CachedRows.cachedA (p 11) (k.val+1) false) (CachedRows.cachedC (p 11) (k.val+1)-centerLoss (positions 11) (loss 11) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_12 : Numeric.validProfile (p 12) 34 ∧ (p 12).emptyPairCap=none ∧
    (∀ j, (positions 12 j).val+1∈(p 12).correctionCenters) ∧
    (∀ j z, 0≤α 12 j z) ∧ (∀ j z, j∉R 12 j z) ∧
    (∀ j z, quota 12 j z ≤
      (4*avoidedCount (p 12) ((positions 12 j).val+1) (avoidedPositions (positions 12) (R 12 j z))+2-
        (24-1-(R 12 j z).card))/3) ∧
    (∀ j, loss 12 j ≤ (∑ z, (quota 12 j z : ℚ)*α 12 j z)-
      penaltySum (p 12) ((positions 12 j).val+1) (fun z => avoidedPositions (positions 12) (R 12 j z)) (α 12 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 12) (k.val+1) true)
      (min (CachedRows.cachedA (p 12) (k.val+1) false) (CachedRows.cachedC (p 12) (k.val+1)-centerLoss (positions 12) (loss 12) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_13 : Numeric.validProfile (p 13) 34 ∧ (p 13).emptyPairCap=none ∧
    (∀ j, (positions 13 j).val+1∈(p 13).correctionCenters) ∧
    (∀ j z, 0≤α 13 j z) ∧ (∀ j z, j∉R 13 j z) ∧
    (∀ j z, quota 13 j z ≤
      (4*avoidedCount (p 13) ((positions 13 j).val+1) (avoidedPositions (positions 13) (R 13 j z))+2-
        (24-1-(R 13 j z).card))/3) ∧
    (∀ j, loss 13 j ≤ (∑ z, (quota 13 j z : ℚ)*α 13 j z)-
      penaltySum (p 13) ((positions 13 j).val+1) (fun z => avoidedPositions (positions 13) (R 13 j z)) (α 13 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 13) (k.val+1) true)
      (min (CachedRows.cachedA (p 13) (k.val+1) false) (CachedRows.cachedC (p 13) (k.val+1)-centerLoss (positions 13) (loss 13) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_14 : Numeric.validProfile (p 14) 34 ∧ (p 14).emptyPairCap=none ∧
    (∀ j, (positions 14 j).val+1∈(p 14).correctionCenters) ∧
    (∀ j z, 0≤α 14 j z) ∧ (∀ j z, j∉R 14 j z) ∧
    (∀ j z, quota 14 j z ≤
      (4*avoidedCount (p 14) ((positions 14 j).val+1) (avoidedPositions (positions 14) (R 14 j z))+2-
        (24-1-(R 14 j z).card))/3) ∧
    (∀ j, loss 14 j ≤ (∑ z, (quota 14 j z : ℚ)*α 14 j z)-
      penaltySum (p 14) ((positions 14 j).val+1) (fun z => avoidedPositions (positions 14) (R 14 j z)) (α 14 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 14) (k.val+1) true)
      (min (CachedRows.cachedA (p 14) (k.val+1) false) (CachedRows.cachedC (p 14) (k.val+1)-centerLoss (positions 14) (loss 14) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_15 : Numeric.validProfile (p 15) 34 ∧ (p 15).emptyPairCap=none ∧
    (∀ j, (positions 15 j).val+1∈(p 15).correctionCenters) ∧
    (∀ j z, 0≤α 15 j z) ∧ (∀ j z, j∉R 15 j z) ∧
    (∀ j z, quota 15 j z ≤
      (4*avoidedCount (p 15) ((positions 15 j).val+1) (avoidedPositions (positions 15) (R 15 j z))+2-
        (24-1-(R 15 j z).card))/3) ∧
    (∀ j, loss 15 j ≤ (∑ z, (quota 15 j z : ℚ)*α 15 j z)-
      penaltySum (p 15) ((positions 15 j).val+1) (fun z => avoidedPositions (positions 15) (R 15 j z)) (α 15 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 15) (k.val+1) true)
      (min (CachedRows.cachedA (p 15) (k.val+1) false) (CachedRows.cachedC (p 15) (k.val+1)-centerLoss (positions 15) (loss 15) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_16 : Numeric.validProfile (p 16) 34 ∧ (p 16).emptyPairCap=none ∧
    (∀ j, (positions 16 j).val+1∈(p 16).correctionCenters) ∧
    (∀ j z, 0≤α 16 j z) ∧ (∀ j z, j∉R 16 j z) ∧
    (∀ j z, quota 16 j z ≤
      (4*avoidedCount (p 16) ((positions 16 j).val+1) (avoidedPositions (positions 16) (R 16 j z))+2-
        (24-1-(R 16 j z).card))/3) ∧
    (∀ j, loss 16 j ≤ (∑ z, (quota 16 j z : ℚ)*α 16 j z)-
      penaltySum (p 16) ((positions 16 j).val+1) (fun z => avoidedPositions (positions 16) (R 16 j z)) (α 16 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 16) (k.val+1) true)
      (min (CachedRows.cachedA (p 16) (k.val+1) false) (CachedRows.cachedC (p 16) (k.val+1)-centerLoss (positions 16) (loss 16) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_17 : Numeric.validProfile (p 17) 34 ∧ (p 17).emptyPairCap=none ∧
    (∀ j, (positions 17 j).val+1∈(p 17).correctionCenters) ∧
    (∀ j z, 0≤α 17 j z) ∧ (∀ j z, j∉R 17 j z) ∧
    (∀ j z, quota 17 j z ≤
      (4*avoidedCount (p 17) ((positions 17 j).val+1) (avoidedPositions (positions 17) (R 17 j z))+2-
        (24-1-(R 17 j z).card))/3) ∧
    (∀ j, loss 17 j ≤ (∑ z, (quota 17 j z : ℚ)*α 17 j z)-
      penaltySum (p 17) ((positions 17 j).val+1) (fun z => avoidedPositions (positions 17) (R 17 j z)) (α 17 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 17) (k.val+1) true)
      (min (CachedRows.cachedA (p 17) (k.val+1) false) (CachedRows.cachedC (p 17) (k.val+1)-centerLoss (positions 17) (loss 17) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_18 : Numeric.validProfile (p 18) 34 ∧ (p 18).emptyPairCap=none ∧
    (∀ j, (positions 18 j).val+1∈(p 18).correctionCenters) ∧
    (∀ j z, 0≤α 18 j z) ∧ (∀ j z, j∉R 18 j z) ∧
    (∀ j z, quota 18 j z ≤
      (4*avoidedCount (p 18) ((positions 18 j).val+1) (avoidedPositions (positions 18) (R 18 j z))+2-
        (24-1-(R 18 j z).card))/3) ∧
    (∀ j, loss 18 j ≤ (∑ z, (quota 18 j z : ℚ)*α 18 j z)-
      penaltySum (p 18) ((positions 18 j).val+1) (fun z => avoidedPositions (positions 18) (R 18 j z)) (α 18 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 18) (k.val+1) true)
      (min (CachedRows.cachedA (p 18) (k.val+1) false) (CachedRows.cachedC (p 18) (k.val+1)-centerLoss (positions 18) (loss 18) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_19 : Numeric.validProfile (p 19) 34 ∧ (p 19).emptyPairCap=none ∧
    (∀ j, (positions 19 j).val+1∈(p 19).correctionCenters) ∧
    (∀ j z, 0≤α 19 j z) ∧ (∀ j z, j∉R 19 j z) ∧
    (∀ j z, quota 19 j z ≤
      (4*avoidedCount (p 19) ((positions 19 j).val+1) (avoidedPositions (positions 19) (R 19 j z))+2-
        (24-1-(R 19 j z).card))/3) ∧
    (∀ j, loss 19 j ≤ (∑ z, (quota 19 j z : ℚ)*α 19 j z)-
      penaltySum (p 19) ((positions 19 j).val+1) (fun z => avoidedPositions (positions 19) (R 19 j z)) (α 19 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 19) (k.val+1) true)
      (min (CachedRows.cachedA (p 19) (k.val+1) false) (CachedRows.cachedC (p 19) (k.val+1)-centerLoss (positions 19) (loss 19) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
