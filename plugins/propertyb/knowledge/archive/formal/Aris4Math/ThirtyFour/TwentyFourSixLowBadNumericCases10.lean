import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_100 : Numeric.validProfile (p 100) 34 ∧ (p 100).emptyPairCap=none ∧
    (∀ j, (positions 100 j).val+1∈(p 100).correctionCenters) ∧
    (∀ j z, 0≤α 100 j z) ∧ (∀ j z, j∉R 100 j z) ∧
    (∀ j z, quota 100 j z ≤
      (4*avoidedCount (p 100) ((positions 100 j).val+1) (avoidedPositions (positions 100) (R 100 j z))+2-
        (24-1-(R 100 j z).card))/3) ∧
    (∀ j, loss 100 j ≤ (∑ z, (quota 100 j z : ℚ)*α 100 j z)-
      penaltySum (p 100) ((positions 100 j).val+1) (fun z => avoidedPositions (positions 100) (R 100 j z)) (α 100 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 100) (k.val+1) true)
      (min (CachedRows.cachedA (p 100) (k.val+1) false) (CachedRows.cachedC (p 100) (k.val+1)-centerLoss (positions 100) (loss 100) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_101 : Numeric.validProfile (p 101) 34 ∧ (p 101).emptyPairCap=none ∧
    (∀ j, (positions 101 j).val+1∈(p 101).correctionCenters) ∧
    (∀ j z, 0≤α 101 j z) ∧ (∀ j z, j∉R 101 j z) ∧
    (∀ j z, quota 101 j z ≤
      (4*avoidedCount (p 101) ((positions 101 j).val+1) (avoidedPositions (positions 101) (R 101 j z))+2-
        (24-1-(R 101 j z).card))/3) ∧
    (∀ j, loss 101 j ≤ (∑ z, (quota 101 j z : ℚ)*α 101 j z)-
      penaltySum (p 101) ((positions 101 j).val+1) (fun z => avoidedPositions (positions 101) (R 101 j z)) (α 101 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 101) (k.val+1) true)
      (min (CachedRows.cachedA (p 101) (k.val+1) false) (CachedRows.cachedC (p 101) (k.val+1)-centerLoss (positions 101) (loss 101) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_102 : Numeric.validProfile (p 102) 34 ∧ (p 102).emptyPairCap=none ∧
    (∀ j, (positions 102 j).val+1∈(p 102).correctionCenters) ∧
    (∀ j z, 0≤α 102 j z) ∧ (∀ j z, j∉R 102 j z) ∧
    (∀ j z, quota 102 j z ≤
      (4*avoidedCount (p 102) ((positions 102 j).val+1) (avoidedPositions (positions 102) (R 102 j z))+2-
        (24-1-(R 102 j z).card))/3) ∧
    (∀ j, loss 102 j ≤ (∑ z, (quota 102 j z : ℚ)*α 102 j z)-
      penaltySum (p 102) ((positions 102 j).val+1) (fun z => avoidedPositions (positions 102) (R 102 j z)) (α 102 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 102) (k.val+1) true)
      (min (CachedRows.cachedA (p 102) (k.val+1) false) (CachedRows.cachedC (p 102) (k.val+1)-centerLoss (positions 102) (loss 102) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_103 : Numeric.validProfile (p 103) 34 ∧ (p 103).emptyPairCap=none ∧
    (∀ j, (positions 103 j).val+1∈(p 103).correctionCenters) ∧
    (∀ j z, 0≤α 103 j z) ∧ (∀ j z, j∉R 103 j z) ∧
    (∀ j z, quota 103 j z ≤
      (4*avoidedCount (p 103) ((positions 103 j).val+1) (avoidedPositions (positions 103) (R 103 j z))+2-
        (24-1-(R 103 j z).card))/3) ∧
    (∀ j, loss 103 j ≤ (∑ z, (quota 103 j z : ℚ)*α 103 j z)-
      penaltySum (p 103) ((positions 103 j).val+1) (fun z => avoidedPositions (positions 103) (R 103 j z)) (α 103 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 103) (k.val+1) true)
      (min (CachedRows.cachedA (p 103) (k.val+1) false) (CachedRows.cachedC (p 103) (k.val+1)-centerLoss (positions 103) (loss 103) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_104 : Numeric.validProfile (p 104) 34 ∧ (p 104).emptyPairCap=none ∧
    (∀ j, (positions 104 j).val+1∈(p 104).correctionCenters) ∧
    (∀ j z, 0≤α 104 j z) ∧ (∀ j z, j∉R 104 j z) ∧
    (∀ j z, quota 104 j z ≤
      (4*avoidedCount (p 104) ((positions 104 j).val+1) (avoidedPositions (positions 104) (R 104 j z))+2-
        (24-1-(R 104 j z).card))/3) ∧
    (∀ j, loss 104 j ≤ (∑ z, (quota 104 j z : ℚ)*α 104 j z)-
      penaltySum (p 104) ((positions 104 j).val+1) (fun z => avoidedPositions (positions 104) (R 104 j z)) (α 104 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 104) (k.val+1) true)
      (min (CachedRows.cachedA (p 104) (k.val+1) false) (CachedRows.cachedC (p 104) (k.val+1)-centerLoss (positions 104) (loss 104) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_105 : Numeric.validProfile (p 105) 34 ∧ (p 105).emptyPairCap=none ∧
    (∀ j, (positions 105 j).val+1∈(p 105).correctionCenters) ∧
    (∀ j z, 0≤α 105 j z) ∧ (∀ j z, j∉R 105 j z) ∧
    (∀ j z, quota 105 j z ≤
      (4*avoidedCount (p 105) ((positions 105 j).val+1) (avoidedPositions (positions 105) (R 105 j z))+2-
        (24-1-(R 105 j z).card))/3) ∧
    (∀ j, loss 105 j ≤ (∑ z, (quota 105 j z : ℚ)*α 105 j z)-
      penaltySum (p 105) ((positions 105 j).val+1) (fun z => avoidedPositions (positions 105) (R 105 j z)) (α 105 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 105) (k.val+1) true)
      (min (CachedRows.cachedA (p 105) (k.val+1) false) (CachedRows.cachedC (p 105) (k.val+1)-centerLoss (positions 105) (loss 105) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_106 : Numeric.validProfile (p 106) 34 ∧ (p 106).emptyPairCap=none ∧
    (∀ j, (positions 106 j).val+1∈(p 106).correctionCenters) ∧
    (∀ j z, 0≤α 106 j z) ∧ (∀ j z, j∉R 106 j z) ∧
    (∀ j z, quota 106 j z ≤
      (4*avoidedCount (p 106) ((positions 106 j).val+1) (avoidedPositions (positions 106) (R 106 j z))+2-
        (24-1-(R 106 j z).card))/3) ∧
    (∀ j, loss 106 j ≤ (∑ z, (quota 106 j z : ℚ)*α 106 j z)-
      penaltySum (p 106) ((positions 106 j).val+1) (fun z => avoidedPositions (positions 106) (R 106 j z)) (α 106 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 106) (k.val+1) true)
      (min (CachedRows.cachedA (p 106) (k.val+1) false) (CachedRows.cachedC (p 106) (k.val+1)-centerLoss (positions 106) (loss 106) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_107 : Numeric.validProfile (p 107) 34 ∧ (p 107).emptyPairCap=none ∧
    (∀ j, (positions 107 j).val+1∈(p 107).correctionCenters) ∧
    (∀ j z, 0≤α 107 j z) ∧ (∀ j z, j∉R 107 j z) ∧
    (∀ j z, quota 107 j z ≤
      (4*avoidedCount (p 107) ((positions 107 j).val+1) (avoidedPositions (positions 107) (R 107 j z))+2-
        (24-1-(R 107 j z).card))/3) ∧
    (∀ j, loss 107 j ≤ (∑ z, (quota 107 j z : ℚ)*α 107 j z)-
      penaltySum (p 107) ((positions 107 j).val+1) (fun z => avoidedPositions (positions 107) (R 107 j z)) (α 107 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 107) (k.val+1) true)
      (min (CachedRows.cachedA (p 107) (k.val+1) false) (CachedRows.cachedC (p 107) (k.val+1)-centerLoss (positions 107) (loss 107) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_108 : Numeric.validProfile (p 108) 34 ∧ (p 108).emptyPairCap=none ∧
    (∀ j, (positions 108 j).val+1∈(p 108).correctionCenters) ∧
    (∀ j z, 0≤α 108 j z) ∧ (∀ j z, j∉R 108 j z) ∧
    (∀ j z, quota 108 j z ≤
      (4*avoidedCount (p 108) ((positions 108 j).val+1) (avoidedPositions (positions 108) (R 108 j z))+2-
        (24-1-(R 108 j z).card))/3) ∧
    (∀ j, loss 108 j ≤ (∑ z, (quota 108 j z : ℚ)*α 108 j z)-
      penaltySum (p 108) ((positions 108 j).val+1) (fun z => avoidedPositions (positions 108) (R 108 j z)) (α 108 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 108) (k.val+1) true)
      (min (CachedRows.cachedA (p 108) (k.val+1) false) (CachedRows.cachedC (p 108) (k.val+1)-centerLoss (positions 108) (loss 108) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_109 : Numeric.validProfile (p 109) 34 ∧ (p 109).emptyPairCap=none ∧
    (∀ j, (positions 109 j).val+1∈(p 109).correctionCenters) ∧
    (∀ j z, 0≤α 109 j z) ∧ (∀ j z, j∉R 109 j z) ∧
    (∀ j z, quota 109 j z ≤
      (4*avoidedCount (p 109) ((positions 109 j).val+1) (avoidedPositions (positions 109) (R 109 j z))+2-
        (24-1-(R 109 j z).card))/3) ∧
    (∀ j, loss 109 j ≤ (∑ z, (quota 109 j z : ℚ)*α 109 j z)-
      penaltySum (p 109) ((positions 109 j).val+1) (fun z => avoidedPositions (positions 109) (R 109 j z)) (α 109 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 109) (k.val+1) true)
      (min (CachedRows.cachedA (p 109) (k.val+1) false) (CachedRows.cachedC (p 109) (k.val+1)-centerLoss (positions 109) (loss 109) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
