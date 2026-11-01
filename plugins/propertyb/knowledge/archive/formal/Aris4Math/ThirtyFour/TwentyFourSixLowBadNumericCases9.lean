import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_90 : Numeric.validProfile (p 90) 34 ∧ (p 90).emptyPairCap=none ∧
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
theorem cached_case_91 : Numeric.validProfile (p 91) 34 ∧ (p 91).emptyPairCap=none ∧
    (∀ j, (positions 91 j).val+1∈(p 91).correctionCenters) ∧
    (∀ j z, 0≤α 91 j z) ∧ (∀ j z, j∉R 91 j z) ∧
    (∀ j z, quota 91 j z ≤
      (4*avoidedCount (p 91) ((positions 91 j).val+1) (avoidedPositions (positions 91) (R 91 j z))+2-
        (24-1-(R 91 j z).card))/3) ∧
    (∀ j, loss 91 j ≤ (∑ z, (quota 91 j z : ℚ)*α 91 j z)-
      penaltySum (p 91) ((positions 91 j).val+1) (fun z => avoidedPositions (positions 91) (R 91 j z)) (α 91 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 91) (k.val+1) true)
      (min (CachedRows.cachedA (p 91) (k.val+1) false) (CachedRows.cachedC (p 91) (k.val+1)-centerLoss (positions 91) (loss 91) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_92 : Numeric.validProfile (p 92) 34 ∧ (p 92).emptyPairCap=none ∧
    (∀ j, (positions 92 j).val+1∈(p 92).correctionCenters) ∧
    (∀ j z, 0≤α 92 j z) ∧ (∀ j z, j∉R 92 j z) ∧
    (∀ j z, quota 92 j z ≤
      (4*avoidedCount (p 92) ((positions 92 j).val+1) (avoidedPositions (positions 92) (R 92 j z))+2-
        (24-1-(R 92 j z).card))/3) ∧
    (∀ j, loss 92 j ≤ (∑ z, (quota 92 j z : ℚ)*α 92 j z)-
      penaltySum (p 92) ((positions 92 j).val+1) (fun z => avoidedPositions (positions 92) (R 92 j z)) (α 92 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 92) (k.val+1) true)
      (min (CachedRows.cachedA (p 92) (k.val+1) false) (CachedRows.cachedC (p 92) (k.val+1)-centerLoss (positions 92) (loss 92) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_93 : Numeric.validProfile (p 93) 34 ∧ (p 93).emptyPairCap=none ∧
    (∀ j, (positions 93 j).val+1∈(p 93).correctionCenters) ∧
    (∀ j z, 0≤α 93 j z) ∧ (∀ j z, j∉R 93 j z) ∧
    (∀ j z, quota 93 j z ≤
      (4*avoidedCount (p 93) ((positions 93 j).val+1) (avoidedPositions (positions 93) (R 93 j z))+2-
        (24-1-(R 93 j z).card))/3) ∧
    (∀ j, loss 93 j ≤ (∑ z, (quota 93 j z : ℚ)*α 93 j z)-
      penaltySum (p 93) ((positions 93 j).val+1) (fun z => avoidedPositions (positions 93) (R 93 j z)) (α 93 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 93) (k.val+1) true)
      (min (CachedRows.cachedA (p 93) (k.val+1) false) (CachedRows.cachedC (p 93) (k.val+1)-centerLoss (positions 93) (loss 93) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_94 : Numeric.validProfile (p 94) 34 ∧ (p 94).emptyPairCap=none ∧
    (∀ j, (positions 94 j).val+1∈(p 94).correctionCenters) ∧
    (∀ j z, 0≤α 94 j z) ∧ (∀ j z, j∉R 94 j z) ∧
    (∀ j z, quota 94 j z ≤
      (4*avoidedCount (p 94) ((positions 94 j).val+1) (avoidedPositions (positions 94) (R 94 j z))+2-
        (24-1-(R 94 j z).card))/3) ∧
    (∀ j, loss 94 j ≤ (∑ z, (quota 94 j z : ℚ)*α 94 j z)-
      penaltySum (p 94) ((positions 94 j).val+1) (fun z => avoidedPositions (positions 94) (R 94 j z)) (α 94 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 94) (k.val+1) true)
      (min (CachedRows.cachedA (p 94) (k.val+1) false) (CachedRows.cachedC (p 94) (k.val+1)-centerLoss (positions 94) (loss 94) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_95 : Numeric.validProfile (p 95) 34 ∧ (p 95).emptyPairCap=none ∧
    (∀ j, (positions 95 j).val+1∈(p 95).correctionCenters) ∧
    (∀ j z, 0≤α 95 j z) ∧ (∀ j z, j∉R 95 j z) ∧
    (∀ j z, quota 95 j z ≤
      (4*avoidedCount (p 95) ((positions 95 j).val+1) (avoidedPositions (positions 95) (R 95 j z))+2-
        (24-1-(R 95 j z).card))/3) ∧
    (∀ j, loss 95 j ≤ (∑ z, (quota 95 j z : ℚ)*α 95 j z)-
      penaltySum (p 95) ((positions 95 j).val+1) (fun z => avoidedPositions (positions 95) (R 95 j z)) (α 95 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 95) (k.val+1) true)
      (min (CachedRows.cachedA (p 95) (k.val+1) false) (CachedRows.cachedC (p 95) (k.val+1)-centerLoss (positions 95) (loss 95) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_96 : Numeric.validProfile (p 96) 34 ∧ (p 96).emptyPairCap=none ∧
    (∀ j, (positions 96 j).val+1∈(p 96).correctionCenters) ∧
    (∀ j z, 0≤α 96 j z) ∧ (∀ j z, j∉R 96 j z) ∧
    (∀ j z, quota 96 j z ≤
      (4*avoidedCount (p 96) ((positions 96 j).val+1) (avoidedPositions (positions 96) (R 96 j z))+2-
        (24-1-(R 96 j z).card))/3) ∧
    (∀ j, loss 96 j ≤ (∑ z, (quota 96 j z : ℚ)*α 96 j z)-
      penaltySum (p 96) ((positions 96 j).val+1) (fun z => avoidedPositions (positions 96) (R 96 j z)) (α 96 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 96) (k.val+1) true)
      (min (CachedRows.cachedA (p 96) (k.val+1) false) (CachedRows.cachedC (p 96) (k.val+1)-centerLoss (positions 96) (loss 96) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_97 : Numeric.validProfile (p 97) 34 ∧ (p 97).emptyPairCap=none ∧
    (∀ j, (positions 97 j).val+1∈(p 97).correctionCenters) ∧
    (∀ j z, 0≤α 97 j z) ∧ (∀ j z, j∉R 97 j z) ∧
    (∀ j z, quota 97 j z ≤
      (4*avoidedCount (p 97) ((positions 97 j).val+1) (avoidedPositions (positions 97) (R 97 j z))+2-
        (24-1-(R 97 j z).card))/3) ∧
    (∀ j, loss 97 j ≤ (∑ z, (quota 97 j z : ℚ)*α 97 j z)-
      penaltySum (p 97) ((positions 97 j).val+1) (fun z => avoidedPositions (positions 97) (R 97 j z)) (α 97 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 97) (k.val+1) true)
      (min (CachedRows.cachedA (p 97) (k.val+1) false) (CachedRows.cachedC (p 97) (k.val+1)-centerLoss (positions 97) (loss 97) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_98 : Numeric.validProfile (p 98) 34 ∧ (p 98).emptyPairCap=none ∧
    (∀ j, (positions 98 j).val+1∈(p 98).correctionCenters) ∧
    (∀ j z, 0≤α 98 j z) ∧ (∀ j z, j∉R 98 j z) ∧
    (∀ j z, quota 98 j z ≤
      (4*avoidedCount (p 98) ((positions 98 j).val+1) (avoidedPositions (positions 98) (R 98 j z))+2-
        (24-1-(R 98 j z).card))/3) ∧
    (∀ j, loss 98 j ≤ (∑ z, (quota 98 j z : ℚ)*α 98 j z)-
      penaltySum (p 98) ((positions 98 j).val+1) (fun z => avoidedPositions (positions 98) (R 98 j z)) (α 98 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 98) (k.val+1) true)
      (min (CachedRows.cachedA (p 98) (k.val+1) false) (CachedRows.cachedC (p 98) (k.val+1)-centerLoss (positions 98) (loss 98) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_99 : Numeric.validProfile (p 99) 34 ∧ (p 99).emptyPairCap=none ∧
    (∀ j, (positions 99 j).val+1∈(p 99).correctionCenters) ∧
    (∀ j z, 0≤α 99 j z) ∧ (∀ j z, j∉R 99 j z) ∧
    (∀ j z, quota 99 j z ≤
      (4*avoidedCount (p 99) ((positions 99 j).val+1) (avoidedPositions (positions 99) (R 99 j z))+2-
        (24-1-(R 99 j z).card))/3) ∧
    (∀ j, loss 99 j ≤ (∑ z, (quota 99 j z : ℚ)*α 99 j z)-
      penaltySum (p 99) ((positions 99 j).val+1) (fun z => avoidedPositions (positions 99) (R 99 j z)) (α 99 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 99) (k.val+1) true)
      (min (CachedRows.cachedA (p 99) (k.val+1) false) (CachedRows.cachedC (p 99) (k.val+1)-centerLoss (positions 99) (loss 99) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
