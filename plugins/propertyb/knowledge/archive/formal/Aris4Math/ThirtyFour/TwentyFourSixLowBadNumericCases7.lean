import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_70 : Numeric.validProfile (p 70) 34 ∧ (p 70).emptyPairCap=none ∧
    (∀ j, (positions 70 j).val+1∈(p 70).correctionCenters) ∧
    (∀ j z, 0≤α 70 j z) ∧ (∀ j z, j∉R 70 j z) ∧
    (∀ j z, quota 70 j z ≤
      (4*avoidedCount (p 70) ((positions 70 j).val+1) (avoidedPositions (positions 70) (R 70 j z))+2-
        (24-1-(R 70 j z).card))/3) ∧
    (∀ j, loss 70 j ≤ (∑ z, (quota 70 j z : ℚ)*α 70 j z)-
      penaltySum (p 70) ((positions 70 j).val+1) (fun z => avoidedPositions (positions 70) (R 70 j z)) (α 70 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 70) (k.val+1) true)
      (min (CachedRows.cachedA (p 70) (k.val+1) false) (CachedRows.cachedC (p 70) (k.val+1)-centerLoss (positions 70) (loss 70) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_71 : Numeric.validProfile (p 71) 34 ∧ (p 71).emptyPairCap=none ∧
    (∀ j, (positions 71 j).val+1∈(p 71).correctionCenters) ∧
    (∀ j z, 0≤α 71 j z) ∧ (∀ j z, j∉R 71 j z) ∧
    (∀ j z, quota 71 j z ≤
      (4*avoidedCount (p 71) ((positions 71 j).val+1) (avoidedPositions (positions 71) (R 71 j z))+2-
        (24-1-(R 71 j z).card))/3) ∧
    (∀ j, loss 71 j ≤ (∑ z, (quota 71 j z : ℚ)*α 71 j z)-
      penaltySum (p 71) ((positions 71 j).val+1) (fun z => avoidedPositions (positions 71) (R 71 j z)) (α 71 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 71) (k.val+1) true)
      (min (CachedRows.cachedA (p 71) (k.val+1) false) (CachedRows.cachedC (p 71) (k.val+1)-centerLoss (positions 71) (loss 71) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_72 : Numeric.validProfile (p 72) 34 ∧ (p 72).emptyPairCap=none ∧
    (∀ j, (positions 72 j).val+1∈(p 72).correctionCenters) ∧
    (∀ j z, 0≤α 72 j z) ∧ (∀ j z, j∉R 72 j z) ∧
    (∀ j z, quota 72 j z ≤
      (4*avoidedCount (p 72) ((positions 72 j).val+1) (avoidedPositions (positions 72) (R 72 j z))+2-
        (24-1-(R 72 j z).card))/3) ∧
    (∀ j, loss 72 j ≤ (∑ z, (quota 72 j z : ℚ)*α 72 j z)-
      penaltySum (p 72) ((positions 72 j).val+1) (fun z => avoidedPositions (positions 72) (R 72 j z)) (α 72 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 72) (k.val+1) true)
      (min (CachedRows.cachedA (p 72) (k.val+1) false) (CachedRows.cachedC (p 72) (k.val+1)-centerLoss (positions 72) (loss 72) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_73 : Numeric.validProfile (p 73) 34 ∧ (p 73).emptyPairCap=none ∧
    (∀ j, (positions 73 j).val+1∈(p 73).correctionCenters) ∧
    (∀ j z, 0≤α 73 j z) ∧ (∀ j z, j∉R 73 j z) ∧
    (∀ j z, quota 73 j z ≤
      (4*avoidedCount (p 73) ((positions 73 j).val+1) (avoidedPositions (positions 73) (R 73 j z))+2-
        (24-1-(R 73 j z).card))/3) ∧
    (∀ j, loss 73 j ≤ (∑ z, (quota 73 j z : ℚ)*α 73 j z)-
      penaltySum (p 73) ((positions 73 j).val+1) (fun z => avoidedPositions (positions 73) (R 73 j z)) (α 73 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 73) (k.val+1) true)
      (min (CachedRows.cachedA (p 73) (k.val+1) false) (CachedRows.cachedC (p 73) (k.val+1)-centerLoss (positions 73) (loss 73) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_74 : Numeric.validProfile (p 74) 34 ∧ (p 74).emptyPairCap=none ∧
    (∀ j, (positions 74 j).val+1∈(p 74).correctionCenters) ∧
    (∀ j z, 0≤α 74 j z) ∧ (∀ j z, j∉R 74 j z) ∧
    (∀ j z, quota 74 j z ≤
      (4*avoidedCount (p 74) ((positions 74 j).val+1) (avoidedPositions (positions 74) (R 74 j z))+2-
        (24-1-(R 74 j z).card))/3) ∧
    (∀ j, loss 74 j ≤ (∑ z, (quota 74 j z : ℚ)*α 74 j z)-
      penaltySum (p 74) ((positions 74 j).val+1) (fun z => avoidedPositions (positions 74) (R 74 j z)) (α 74 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 74) (k.val+1) true)
      (min (CachedRows.cachedA (p 74) (k.val+1) false) (CachedRows.cachedC (p 74) (k.val+1)-centerLoss (positions 74) (loss 74) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_75 : Numeric.validProfile (p 75) 34 ∧ (p 75).emptyPairCap=none ∧
    (∀ j, (positions 75 j).val+1∈(p 75).correctionCenters) ∧
    (∀ j z, 0≤α 75 j z) ∧ (∀ j z, j∉R 75 j z) ∧
    (∀ j z, quota 75 j z ≤
      (4*avoidedCount (p 75) ((positions 75 j).val+1) (avoidedPositions (positions 75) (R 75 j z))+2-
        (24-1-(R 75 j z).card))/3) ∧
    (∀ j, loss 75 j ≤ (∑ z, (quota 75 j z : ℚ)*α 75 j z)-
      penaltySum (p 75) ((positions 75 j).val+1) (fun z => avoidedPositions (positions 75) (R 75 j z)) (α 75 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 75) (k.val+1) true)
      (min (CachedRows.cachedA (p 75) (k.val+1) false) (CachedRows.cachedC (p 75) (k.val+1)-centerLoss (positions 75) (loss 75) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_76 : Numeric.validProfile (p 76) 34 ∧ (p 76).emptyPairCap=none ∧
    (∀ j, (positions 76 j).val+1∈(p 76).correctionCenters) ∧
    (∀ j z, 0≤α 76 j z) ∧ (∀ j z, j∉R 76 j z) ∧
    (∀ j z, quota 76 j z ≤
      (4*avoidedCount (p 76) ((positions 76 j).val+1) (avoidedPositions (positions 76) (R 76 j z))+2-
        (24-1-(R 76 j z).card))/3) ∧
    (∀ j, loss 76 j ≤ (∑ z, (quota 76 j z : ℚ)*α 76 j z)-
      penaltySum (p 76) ((positions 76 j).val+1) (fun z => avoidedPositions (positions 76) (R 76 j z)) (α 76 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 76) (k.val+1) true)
      (min (CachedRows.cachedA (p 76) (k.val+1) false) (CachedRows.cachedC (p 76) (k.val+1)-centerLoss (positions 76) (loss 76) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_77 : Numeric.validProfile (p 77) 34 ∧ (p 77).emptyPairCap=none ∧
    (∀ j, (positions 77 j).val+1∈(p 77).correctionCenters) ∧
    (∀ j z, 0≤α 77 j z) ∧ (∀ j z, j∉R 77 j z) ∧
    (∀ j z, quota 77 j z ≤
      (4*avoidedCount (p 77) ((positions 77 j).val+1) (avoidedPositions (positions 77) (R 77 j z))+2-
        (24-1-(R 77 j z).card))/3) ∧
    (∀ j, loss 77 j ≤ (∑ z, (quota 77 j z : ℚ)*α 77 j z)-
      penaltySum (p 77) ((positions 77 j).val+1) (fun z => avoidedPositions (positions 77) (R 77 j z)) (α 77 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 77) (k.val+1) true)
      (min (CachedRows.cachedA (p 77) (k.val+1) false) (CachedRows.cachedC (p 77) (k.val+1)-centerLoss (positions 77) (loss 77) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_78 : Numeric.validProfile (p 78) 34 ∧ (p 78).emptyPairCap=none ∧
    (∀ j, (positions 78 j).val+1∈(p 78).correctionCenters) ∧
    (∀ j z, 0≤α 78 j z) ∧ (∀ j z, j∉R 78 j z) ∧
    (∀ j z, quota 78 j z ≤
      (4*avoidedCount (p 78) ((positions 78 j).val+1) (avoidedPositions (positions 78) (R 78 j z))+2-
        (24-1-(R 78 j z).card))/3) ∧
    (∀ j, loss 78 j ≤ (∑ z, (quota 78 j z : ℚ)*α 78 j z)-
      penaltySum (p 78) ((positions 78 j).val+1) (fun z => avoidedPositions (positions 78) (R 78 j z)) (α 78 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 78) (k.val+1) true)
      (min (CachedRows.cachedA (p 78) (k.val+1) false) (CachedRows.cachedC (p 78) (k.val+1)-centerLoss (positions 78) (loss 78) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_79 : Numeric.validProfile (p 79) 34 ∧ (p 79).emptyPairCap=none ∧
    (∀ j, (positions 79 j).val+1∈(p 79).correctionCenters) ∧
    (∀ j z, 0≤α 79 j z) ∧ (∀ j z, j∉R 79 j z) ∧
    (∀ j z, quota 79 j z ≤
      (4*avoidedCount (p 79) ((positions 79 j).val+1) (avoidedPositions (positions 79) (R 79 j z))+2-
        (24-1-(R 79 j z).card))/3) ∧
    (∀ j, loss 79 j ≤ (∑ z, (quota 79 j z : ℚ)*α 79 j z)-
      penaltySum (p 79) ((positions 79 j).val+1) (fun z => avoidedPositions (positions 79) (R 79 j z)) (α 79 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 79) (k.val+1) true)
      (min (CachedRows.cachedA (p 79) (k.val+1) false) (CachedRows.cachedC (p 79) (k.val+1)-centerLoss (positions 79) (loss 79) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
