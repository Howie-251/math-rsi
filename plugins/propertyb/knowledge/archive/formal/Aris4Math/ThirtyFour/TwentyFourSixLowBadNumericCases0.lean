import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_0 : Numeric.validProfile (p 0) 34 ∧ (p 0).emptyPairCap=none ∧
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
theorem cached_case_1 : Numeric.validProfile (p 1) 34 ∧ (p 1).emptyPairCap=none ∧
    (∀ j, (positions 1 j).val+1∈(p 1).correctionCenters) ∧
    (∀ j z, 0≤α 1 j z) ∧ (∀ j z, j∉R 1 j z) ∧
    (∀ j z, quota 1 j z ≤
      (4*avoidedCount (p 1) ((positions 1 j).val+1) (avoidedPositions (positions 1) (R 1 j z))+2-
        (24-1-(R 1 j z).card))/3) ∧
    (∀ j, loss 1 j ≤ (∑ z, (quota 1 j z : ℚ)*α 1 j z)-
      penaltySum (p 1) ((positions 1 j).val+1) (fun z => avoidedPositions (positions 1) (R 1 j z)) (α 1 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 1) (k.val+1) true)
      (min (CachedRows.cachedA (p 1) (k.val+1) false) (CachedRows.cachedC (p 1) (k.val+1)-centerLoss (positions 1) (loss 1) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_2 : Numeric.validProfile (p 2) 34 ∧ (p 2).emptyPairCap=none ∧
    (∀ j, (positions 2 j).val+1∈(p 2).correctionCenters) ∧
    (∀ j z, 0≤α 2 j z) ∧ (∀ j z, j∉R 2 j z) ∧
    (∀ j z, quota 2 j z ≤
      (4*avoidedCount (p 2) ((positions 2 j).val+1) (avoidedPositions (positions 2) (R 2 j z))+2-
        (24-1-(R 2 j z).card))/3) ∧
    (∀ j, loss 2 j ≤ (∑ z, (quota 2 j z : ℚ)*α 2 j z)-
      penaltySum (p 2) ((positions 2 j).val+1) (fun z => avoidedPositions (positions 2) (R 2 j z)) (α 2 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 2) (k.val+1) true)
      (min (CachedRows.cachedA (p 2) (k.val+1) false) (CachedRows.cachedC (p 2) (k.val+1)-centerLoss (positions 2) (loss 2) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_3 : Numeric.validProfile (p 3) 34 ∧ (p 3).emptyPairCap=none ∧
    (∀ j, (positions 3 j).val+1∈(p 3).correctionCenters) ∧
    (∀ j z, 0≤α 3 j z) ∧ (∀ j z, j∉R 3 j z) ∧
    (∀ j z, quota 3 j z ≤
      (4*avoidedCount (p 3) ((positions 3 j).val+1) (avoidedPositions (positions 3) (R 3 j z))+2-
        (24-1-(R 3 j z).card))/3) ∧
    (∀ j, loss 3 j ≤ (∑ z, (quota 3 j z : ℚ)*α 3 j z)-
      penaltySum (p 3) ((positions 3 j).val+1) (fun z => avoidedPositions (positions 3) (R 3 j z)) (α 3 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 3) (k.val+1) true)
      (min (CachedRows.cachedA (p 3) (k.val+1) false) (CachedRows.cachedC (p 3) (k.val+1)-centerLoss (positions 3) (loss 3) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_4 : Numeric.validProfile (p 4) 34 ∧ (p 4).emptyPairCap=none ∧
    (∀ j, (positions 4 j).val+1∈(p 4).correctionCenters) ∧
    (∀ j z, 0≤α 4 j z) ∧ (∀ j z, j∉R 4 j z) ∧
    (∀ j z, quota 4 j z ≤
      (4*avoidedCount (p 4) ((positions 4 j).val+1) (avoidedPositions (positions 4) (R 4 j z))+2-
        (24-1-(R 4 j z).card))/3) ∧
    (∀ j, loss 4 j ≤ (∑ z, (quota 4 j z : ℚ)*α 4 j z)-
      penaltySum (p 4) ((positions 4 j).val+1) (fun z => avoidedPositions (positions 4) (R 4 j z)) (α 4 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 4) (k.val+1) true)
      (min (CachedRows.cachedA (p 4) (k.val+1) false) (CachedRows.cachedC (p 4) (k.val+1)-centerLoss (positions 4) (loss 4) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_5 : Numeric.validProfile (p 5) 34 ∧ (p 5).emptyPairCap=none ∧
    (∀ j, (positions 5 j).val+1∈(p 5).correctionCenters) ∧
    (∀ j z, 0≤α 5 j z) ∧ (∀ j z, j∉R 5 j z) ∧
    (∀ j z, quota 5 j z ≤
      (4*avoidedCount (p 5) ((positions 5 j).val+1) (avoidedPositions (positions 5) (R 5 j z))+2-
        (24-1-(R 5 j z).card))/3) ∧
    (∀ j, loss 5 j ≤ (∑ z, (quota 5 j z : ℚ)*α 5 j z)-
      penaltySum (p 5) ((positions 5 j).val+1) (fun z => avoidedPositions (positions 5) (R 5 j z)) (α 5 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 5) (k.val+1) true)
      (min (CachedRows.cachedA (p 5) (k.val+1) false) (CachedRows.cachedC (p 5) (k.val+1)-centerLoss (positions 5) (loss 5) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_6 : Numeric.validProfile (p 6) 34 ∧ (p 6).emptyPairCap=none ∧
    (∀ j, (positions 6 j).val+1∈(p 6).correctionCenters) ∧
    (∀ j z, 0≤α 6 j z) ∧ (∀ j z, j∉R 6 j z) ∧
    (∀ j z, quota 6 j z ≤
      (4*avoidedCount (p 6) ((positions 6 j).val+1) (avoidedPositions (positions 6) (R 6 j z))+2-
        (24-1-(R 6 j z).card))/3) ∧
    (∀ j, loss 6 j ≤ (∑ z, (quota 6 j z : ℚ)*α 6 j z)-
      penaltySum (p 6) ((positions 6 j).val+1) (fun z => avoidedPositions (positions 6) (R 6 j z)) (α 6 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 6) (k.val+1) true)
      (min (CachedRows.cachedA (p 6) (k.val+1) false) (CachedRows.cachedC (p 6) (k.val+1)-centerLoss (positions 6) (loss 6) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_7 : Numeric.validProfile (p 7) 34 ∧ (p 7).emptyPairCap=none ∧
    (∀ j, (positions 7 j).val+1∈(p 7).correctionCenters) ∧
    (∀ j z, 0≤α 7 j z) ∧ (∀ j z, j∉R 7 j z) ∧
    (∀ j z, quota 7 j z ≤
      (4*avoidedCount (p 7) ((positions 7 j).val+1) (avoidedPositions (positions 7) (R 7 j z))+2-
        (24-1-(R 7 j z).card))/3) ∧
    (∀ j, loss 7 j ≤ (∑ z, (quota 7 j z : ℚ)*α 7 j z)-
      penaltySum (p 7) ((positions 7 j).val+1) (fun z => avoidedPositions (positions 7) (R 7 j z)) (α 7 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 7) (k.val+1) true)
      (min (CachedRows.cachedA (p 7) (k.val+1) false) (CachedRows.cachedC (p 7) (k.val+1)-centerLoss (positions 7) (loss 7) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_8 : Numeric.validProfile (p 8) 34 ∧ (p 8).emptyPairCap=none ∧
    (∀ j, (positions 8 j).val+1∈(p 8).correctionCenters) ∧
    (∀ j z, 0≤α 8 j z) ∧ (∀ j z, j∉R 8 j z) ∧
    (∀ j z, quota 8 j z ≤
      (4*avoidedCount (p 8) ((positions 8 j).val+1) (avoidedPositions (positions 8) (R 8 j z))+2-
        (24-1-(R 8 j z).card))/3) ∧
    (∀ j, loss 8 j ≤ (∑ z, (quota 8 j z : ℚ)*α 8 j z)-
      penaltySum (p 8) ((positions 8 j).val+1) (fun z => avoidedPositions (positions 8) (R 8 j z)) (α 8 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 8) (k.val+1) true)
      (min (CachedRows.cachedA (p 8) (k.val+1) false) (CachedRows.cachedC (p 8) (k.val+1)-centerLoss (positions 8) (loss 8) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_9 : Numeric.validProfile (p 9) 34 ∧ (p 9).emptyPairCap=none ∧
    (∀ j, (positions 9 j).val+1∈(p 9).correctionCenters) ∧
    (∀ j z, 0≤α 9 j z) ∧ (∀ j z, j∉R 9 j z) ∧
    (∀ j z, quota 9 j z ≤
      (4*avoidedCount (p 9) ((positions 9 j).val+1) (avoidedPositions (positions 9) (R 9 j z))+2-
        (24-1-(R 9 j z).card))/3) ∧
    (∀ j, loss 9 j ≤ (∑ z, (quota 9 j z : ℚ)*α 9 j z)-
      penaltySum (p 9) ((positions 9 j).val+1) (fun z => avoidedPositions (positions 9) (R 9 j z)) (α 9 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 9) (k.val+1) true)
      (min (CachedRows.cachedA (p 9) (k.val+1) false) (CachedRows.cachedC (p 9) (k.val+1)-centerLoss (positions 9) (loss 9) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
