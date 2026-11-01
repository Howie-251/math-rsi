import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_80 : Numeric.validProfile (p 80) 34 ∧ (p 80).emptyPairCap=none ∧
    (∀ j, (positions 80 j).val+1∈(p 80).correctionCenters) ∧
    (∀ j z, 0≤α 80 j z) ∧ (∀ j z, j∉R 80 j z) ∧
    (∀ j z, quota 80 j z ≤
      (4*avoidedCount (p 80) ((positions 80 j).val+1) (avoidedPositions (positions 80) (R 80 j z))+2-
        (24-1-(R 80 j z).card))/3) ∧
    (∀ j, loss 80 j ≤ (∑ z, (quota 80 j z : ℚ)*α 80 j z)-
      penaltySum (p 80) ((positions 80 j).val+1) (fun z => avoidedPositions (positions 80) (R 80 j z)) (α 80 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 80) (k.val+1) true)
      (min (CachedRows.cachedA (p 80) (k.val+1) false) (CachedRows.cachedC (p 80) (k.val+1)-centerLoss (positions 80) (loss 80) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_81 : Numeric.validProfile (p 81) 34 ∧ (p 81).emptyPairCap=none ∧
    (∀ j, (positions 81 j).val+1∈(p 81).correctionCenters) ∧
    (∀ j z, 0≤α 81 j z) ∧ (∀ j z, j∉R 81 j z) ∧
    (∀ j z, quota 81 j z ≤
      (4*avoidedCount (p 81) ((positions 81 j).val+1) (avoidedPositions (positions 81) (R 81 j z))+2-
        (24-1-(R 81 j z).card))/3) ∧
    (∀ j, loss 81 j ≤ (∑ z, (quota 81 j z : ℚ)*α 81 j z)-
      penaltySum (p 81) ((positions 81 j).val+1) (fun z => avoidedPositions (positions 81) (R 81 j z)) (α 81 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 81) (k.val+1) true)
      (min (CachedRows.cachedA (p 81) (k.val+1) false) (CachedRows.cachedC (p 81) (k.val+1)-centerLoss (positions 81) (loss 81) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_82 : Numeric.validProfile (p 82) 34 ∧ (p 82).emptyPairCap=none ∧
    (∀ j, (positions 82 j).val+1∈(p 82).correctionCenters) ∧
    (∀ j z, 0≤α 82 j z) ∧ (∀ j z, j∉R 82 j z) ∧
    (∀ j z, quota 82 j z ≤
      (4*avoidedCount (p 82) ((positions 82 j).val+1) (avoidedPositions (positions 82) (R 82 j z))+2-
        (24-1-(R 82 j z).card))/3) ∧
    (∀ j, loss 82 j ≤ (∑ z, (quota 82 j z : ℚ)*α 82 j z)-
      penaltySum (p 82) ((positions 82 j).val+1) (fun z => avoidedPositions (positions 82) (R 82 j z)) (α 82 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 82) (k.val+1) true)
      (min (CachedRows.cachedA (p 82) (k.val+1) false) (CachedRows.cachedC (p 82) (k.val+1)-centerLoss (positions 82) (loss 82) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_83 : Numeric.validProfile (p 83) 34 ∧ (p 83).emptyPairCap=none ∧
    (∀ j, (positions 83 j).val+1∈(p 83).correctionCenters) ∧
    (∀ j z, 0≤α 83 j z) ∧ (∀ j z, j∉R 83 j z) ∧
    (∀ j z, quota 83 j z ≤
      (4*avoidedCount (p 83) ((positions 83 j).val+1) (avoidedPositions (positions 83) (R 83 j z))+2-
        (24-1-(R 83 j z).card))/3) ∧
    (∀ j, loss 83 j ≤ (∑ z, (quota 83 j z : ℚ)*α 83 j z)-
      penaltySum (p 83) ((positions 83 j).val+1) (fun z => avoidedPositions (positions 83) (R 83 j z)) (α 83 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 83) (k.val+1) true)
      (min (CachedRows.cachedA (p 83) (k.val+1) false) (CachedRows.cachedC (p 83) (k.val+1)-centerLoss (positions 83) (loss 83) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_84 : Numeric.validProfile (p 84) 34 ∧ (p 84).emptyPairCap=none ∧
    (∀ j, (positions 84 j).val+1∈(p 84).correctionCenters) ∧
    (∀ j z, 0≤α 84 j z) ∧ (∀ j z, j∉R 84 j z) ∧
    (∀ j z, quota 84 j z ≤
      (4*avoidedCount (p 84) ((positions 84 j).val+1) (avoidedPositions (positions 84) (R 84 j z))+2-
        (24-1-(R 84 j z).card))/3) ∧
    (∀ j, loss 84 j ≤ (∑ z, (quota 84 j z : ℚ)*α 84 j z)-
      penaltySum (p 84) ((positions 84 j).val+1) (fun z => avoidedPositions (positions 84) (R 84 j z)) (α 84 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 84) (k.val+1) true)
      (min (CachedRows.cachedA (p 84) (k.val+1) false) (CachedRows.cachedC (p 84) (k.val+1)-centerLoss (positions 84) (loss 84) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_85 : Numeric.validProfile (p 85) 34 ∧ (p 85).emptyPairCap=none ∧
    (∀ j, (positions 85 j).val+1∈(p 85).correctionCenters) ∧
    (∀ j z, 0≤α 85 j z) ∧ (∀ j z, j∉R 85 j z) ∧
    (∀ j z, quota 85 j z ≤
      (4*avoidedCount (p 85) ((positions 85 j).val+1) (avoidedPositions (positions 85) (R 85 j z))+2-
        (24-1-(R 85 j z).card))/3) ∧
    (∀ j, loss 85 j ≤ (∑ z, (quota 85 j z : ℚ)*α 85 j z)-
      penaltySum (p 85) ((positions 85 j).val+1) (fun z => avoidedPositions (positions 85) (R 85 j z)) (α 85 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 85) (k.val+1) true)
      (min (CachedRows.cachedA (p 85) (k.val+1) false) (CachedRows.cachedC (p 85) (k.val+1)-centerLoss (positions 85) (loss 85) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_86 : Numeric.validProfile (p 86) 34 ∧ (p 86).emptyPairCap=none ∧
    (∀ j, (positions 86 j).val+1∈(p 86).correctionCenters) ∧
    (∀ j z, 0≤α 86 j z) ∧ (∀ j z, j∉R 86 j z) ∧
    (∀ j z, quota 86 j z ≤
      (4*avoidedCount (p 86) ((positions 86 j).val+1) (avoidedPositions (positions 86) (R 86 j z))+2-
        (24-1-(R 86 j z).card))/3) ∧
    (∀ j, loss 86 j ≤ (∑ z, (quota 86 j z : ℚ)*α 86 j z)-
      penaltySum (p 86) ((positions 86 j).val+1) (fun z => avoidedPositions (positions 86) (R 86 j z)) (α 86 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 86) (k.val+1) true)
      (min (CachedRows.cachedA (p 86) (k.val+1) false) (CachedRows.cachedC (p 86) (k.val+1)-centerLoss (positions 86) (loss 86) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_87 : Numeric.validProfile (p 87) 34 ∧ (p 87).emptyPairCap=none ∧
    (∀ j, (positions 87 j).val+1∈(p 87).correctionCenters) ∧
    (∀ j z, 0≤α 87 j z) ∧ (∀ j z, j∉R 87 j z) ∧
    (∀ j z, quota 87 j z ≤
      (4*avoidedCount (p 87) ((positions 87 j).val+1) (avoidedPositions (positions 87) (R 87 j z))+2-
        (24-1-(R 87 j z).card))/3) ∧
    (∀ j, loss 87 j ≤ (∑ z, (quota 87 j z : ℚ)*α 87 j z)-
      penaltySum (p 87) ((positions 87 j).val+1) (fun z => avoidedPositions (positions 87) (R 87 j z)) (α 87 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 87) (k.val+1) true)
      (min (CachedRows.cachedA (p 87) (k.val+1) false) (CachedRows.cachedC (p 87) (k.val+1)-centerLoss (positions 87) (loss 87) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_88 : Numeric.validProfile (p 88) 34 ∧ (p 88).emptyPairCap=none ∧
    (∀ j, (positions 88 j).val+1∈(p 88).correctionCenters) ∧
    (∀ j z, 0≤α 88 j z) ∧ (∀ j z, j∉R 88 j z) ∧
    (∀ j z, quota 88 j z ≤
      (4*avoidedCount (p 88) ((positions 88 j).val+1) (avoidedPositions (positions 88) (R 88 j z))+2-
        (24-1-(R 88 j z).card))/3) ∧
    (∀ j, loss 88 j ≤ (∑ z, (quota 88 j z : ℚ)*α 88 j z)-
      penaltySum (p 88) ((positions 88 j).val+1) (fun z => avoidedPositions (positions 88) (R 88 j z)) (α 88 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 88) (k.val+1) true)
      (min (CachedRows.cachedA (p 88) (k.val+1) false) (CachedRows.cachedC (p 88) (k.val+1)-centerLoss (positions 88) (loss 88) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_89 : Numeric.validProfile (p 89) 34 ∧ (p 89).emptyPairCap=none ∧
    (∀ j, (positions 89 j).val+1∈(p 89).correctionCenters) ∧
    (∀ j z, 0≤α 89 j z) ∧ (∀ j z, j∉R 89 j z) ∧
    (∀ j z, quota 89 j z ≤
      (4*avoidedCount (p 89) ((positions 89 j).val+1) (avoidedPositions (positions 89) (R 89 j z))+2-
        (24-1-(R 89 j z).card))/3) ∧
    (∀ j, loss 89 j ≤ (∑ z, (quota 89 j z : ℚ)*α 89 j z)-
      penaltySum (p 89) ((positions 89 j).val+1) (fun z => avoidedPositions (positions 89) (R 89 j z)) (α 89 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 89) (k.val+1) true)
      (min (CachedRows.cachedA (p 89) (k.val+1) false) (CachedRows.cachedC (p 89) (k.val+1)-centerLoss (positions 89) (loss 89) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
