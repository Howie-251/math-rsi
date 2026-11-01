import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_20 : Numeric.validProfile (p 20) 34 ∧ (p 20).emptyPairCap=none ∧
    (∀ j, (positions 20 j).val+1∈(p 20).correctionCenters) ∧
    (∀ j z, 0≤α 20 j z) ∧ (∀ j z, j∉R 20 j z) ∧
    (∀ j z, quota 20 j z ≤
      (4*avoidedCount (p 20) ((positions 20 j).val+1) (avoidedPositions (positions 20) (R 20 j z))+2-
        (24-1-(R 20 j z).card))/3) ∧
    (∀ j, loss 20 j ≤ (∑ z, (quota 20 j z : ℚ)*α 20 j z)-
      penaltySum (p 20) ((positions 20 j).val+1) (fun z => avoidedPositions (positions 20) (R 20 j z)) (α 20 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 20) (k.val+1) true)
      (min (CachedRows.cachedA (p 20) (k.val+1) false) (CachedRows.cachedC (p 20) (k.val+1)-centerLoss (positions 20) (loss 20) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_21 : Numeric.validProfile (p 21) 34 ∧ (p 21).emptyPairCap=none ∧
    (∀ j, (positions 21 j).val+1∈(p 21).correctionCenters) ∧
    (∀ j z, 0≤α 21 j z) ∧ (∀ j z, j∉R 21 j z) ∧
    (∀ j z, quota 21 j z ≤
      (4*avoidedCount (p 21) ((positions 21 j).val+1) (avoidedPositions (positions 21) (R 21 j z))+2-
        (24-1-(R 21 j z).card))/3) ∧
    (∀ j, loss 21 j ≤ (∑ z, (quota 21 j z : ℚ)*α 21 j z)-
      penaltySum (p 21) ((positions 21 j).val+1) (fun z => avoidedPositions (positions 21) (R 21 j z)) (α 21 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 21) (k.val+1) true)
      (min (CachedRows.cachedA (p 21) (k.val+1) false) (CachedRows.cachedC (p 21) (k.val+1)-centerLoss (positions 21) (loss 21) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_22 : Numeric.validProfile (p 22) 34 ∧ (p 22).emptyPairCap=none ∧
    (∀ j, (positions 22 j).val+1∈(p 22).correctionCenters) ∧
    (∀ j z, 0≤α 22 j z) ∧ (∀ j z, j∉R 22 j z) ∧
    (∀ j z, quota 22 j z ≤
      (4*avoidedCount (p 22) ((positions 22 j).val+1) (avoidedPositions (positions 22) (R 22 j z))+2-
        (24-1-(R 22 j z).card))/3) ∧
    (∀ j, loss 22 j ≤ (∑ z, (quota 22 j z : ℚ)*α 22 j z)-
      penaltySum (p 22) ((positions 22 j).val+1) (fun z => avoidedPositions (positions 22) (R 22 j z)) (α 22 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 22) (k.val+1) true)
      (min (CachedRows.cachedA (p 22) (k.val+1) false) (CachedRows.cachedC (p 22) (k.val+1)-centerLoss (positions 22) (loss 22) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_23 : Numeric.validProfile (p 23) 34 ∧ (p 23).emptyPairCap=none ∧
    (∀ j, (positions 23 j).val+1∈(p 23).correctionCenters) ∧
    (∀ j z, 0≤α 23 j z) ∧ (∀ j z, j∉R 23 j z) ∧
    (∀ j z, quota 23 j z ≤
      (4*avoidedCount (p 23) ((positions 23 j).val+1) (avoidedPositions (positions 23) (R 23 j z))+2-
        (24-1-(R 23 j z).card))/3) ∧
    (∀ j, loss 23 j ≤ (∑ z, (quota 23 j z : ℚ)*α 23 j z)-
      penaltySum (p 23) ((positions 23 j).val+1) (fun z => avoidedPositions (positions 23) (R 23 j z)) (α 23 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 23) (k.val+1) true)
      (min (CachedRows.cachedA (p 23) (k.val+1) false) (CachedRows.cachedC (p 23) (k.val+1)-centerLoss (positions 23) (loss 23) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_24 : Numeric.validProfile (p 24) 34 ∧ (p 24).emptyPairCap=none ∧
    (∀ j, (positions 24 j).val+1∈(p 24).correctionCenters) ∧
    (∀ j z, 0≤α 24 j z) ∧ (∀ j z, j∉R 24 j z) ∧
    (∀ j z, quota 24 j z ≤
      (4*avoidedCount (p 24) ((positions 24 j).val+1) (avoidedPositions (positions 24) (R 24 j z))+2-
        (24-1-(R 24 j z).card))/3) ∧
    (∀ j, loss 24 j ≤ (∑ z, (quota 24 j z : ℚ)*α 24 j z)-
      penaltySum (p 24) ((positions 24 j).val+1) (fun z => avoidedPositions (positions 24) (R 24 j z)) (α 24 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 24) (k.val+1) true)
      (min (CachedRows.cachedA (p 24) (k.val+1) false) (CachedRows.cachedC (p 24) (k.val+1)-centerLoss (positions 24) (loss 24) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_25 : Numeric.validProfile (p 25) 34 ∧ (p 25).emptyPairCap=none ∧
    (∀ j, (positions 25 j).val+1∈(p 25).correctionCenters) ∧
    (∀ j z, 0≤α 25 j z) ∧ (∀ j z, j∉R 25 j z) ∧
    (∀ j z, quota 25 j z ≤
      (4*avoidedCount (p 25) ((positions 25 j).val+1) (avoidedPositions (positions 25) (R 25 j z))+2-
        (24-1-(R 25 j z).card))/3) ∧
    (∀ j, loss 25 j ≤ (∑ z, (quota 25 j z : ℚ)*α 25 j z)-
      penaltySum (p 25) ((positions 25 j).val+1) (fun z => avoidedPositions (positions 25) (R 25 j z)) (α 25 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 25) (k.val+1) true)
      (min (CachedRows.cachedA (p 25) (k.val+1) false) (CachedRows.cachedC (p 25) (k.val+1)-centerLoss (positions 25) (loss 25) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_26 : Numeric.validProfile (p 26) 34 ∧ (p 26).emptyPairCap=none ∧
    (∀ j, (positions 26 j).val+1∈(p 26).correctionCenters) ∧
    (∀ j z, 0≤α 26 j z) ∧ (∀ j z, j∉R 26 j z) ∧
    (∀ j z, quota 26 j z ≤
      (4*avoidedCount (p 26) ((positions 26 j).val+1) (avoidedPositions (positions 26) (R 26 j z))+2-
        (24-1-(R 26 j z).card))/3) ∧
    (∀ j, loss 26 j ≤ (∑ z, (quota 26 j z : ℚ)*α 26 j z)-
      penaltySum (p 26) ((positions 26 j).val+1) (fun z => avoidedPositions (positions 26) (R 26 j z)) (α 26 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 26) (k.val+1) true)
      (min (CachedRows.cachedA (p 26) (k.val+1) false) (CachedRows.cachedC (p 26) (k.val+1)-centerLoss (positions 26) (loss 26) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_27 : Numeric.validProfile (p 27) 34 ∧ (p 27).emptyPairCap=none ∧
    (∀ j, (positions 27 j).val+1∈(p 27).correctionCenters) ∧
    (∀ j z, 0≤α 27 j z) ∧ (∀ j z, j∉R 27 j z) ∧
    (∀ j z, quota 27 j z ≤
      (4*avoidedCount (p 27) ((positions 27 j).val+1) (avoidedPositions (positions 27) (R 27 j z))+2-
        (24-1-(R 27 j z).card))/3) ∧
    (∀ j, loss 27 j ≤ (∑ z, (quota 27 j z : ℚ)*α 27 j z)-
      penaltySum (p 27) ((positions 27 j).val+1) (fun z => avoidedPositions (positions 27) (R 27 j z)) (α 27 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 27) (k.val+1) true)
      (min (CachedRows.cachedA (p 27) (k.val+1) false) (CachedRows.cachedC (p 27) (k.val+1)-centerLoss (positions 27) (loss 27) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_28 : Numeric.validProfile (p 28) 34 ∧ (p 28).emptyPairCap=none ∧
    (∀ j, (positions 28 j).val+1∈(p 28).correctionCenters) ∧
    (∀ j z, 0≤α 28 j z) ∧ (∀ j z, j∉R 28 j z) ∧
    (∀ j z, quota 28 j z ≤
      (4*avoidedCount (p 28) ((positions 28 j).val+1) (avoidedPositions (positions 28) (R 28 j z))+2-
        (24-1-(R 28 j z).card))/3) ∧
    (∀ j, loss 28 j ≤ (∑ z, (quota 28 j z : ℚ)*α 28 j z)-
      penaltySum (p 28) ((positions 28 j).val+1) (fun z => avoidedPositions (positions 28) (R 28 j z)) (α 28 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 28) (k.val+1) true)
      (min (CachedRows.cachedA (p 28) (k.val+1) false) (CachedRows.cachedC (p 28) (k.val+1)-centerLoss (positions 28) (loss 28) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_29 : Numeric.validProfile (p 29) 34 ∧ (p 29).emptyPairCap=none ∧
    (∀ j, (positions 29 j).val+1∈(p 29).correctionCenters) ∧
    (∀ j z, 0≤α 29 j z) ∧ (∀ j z, j∉R 29 j z) ∧
    (∀ j z, quota 29 j z ≤
      (4*avoidedCount (p 29) ((positions 29 j).val+1) (avoidedPositions (positions 29) (R 29 j z))+2-
        (24-1-(R 29 j z).card))/3) ∧
    (∀ j, loss 29 j ≤ (∑ z, (quota 29 j z : ℚ)*α 29 j z)-
      penaltySum (p 29) ((positions 29 j).val+1) (fun z => avoidedPositions (positions 29) (R 29 j z)) (α 29 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 29) (k.val+1) true)
      (min (CachedRows.cachedA (p 29) (k.val+1) false) (CachedRows.cachedC (p 29) (k.val+1)-centerLoss (positions 29) (loss 29) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
