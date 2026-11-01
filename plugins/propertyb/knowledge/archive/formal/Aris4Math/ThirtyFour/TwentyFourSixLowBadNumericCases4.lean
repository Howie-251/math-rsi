import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_40 : Numeric.validProfile (p 40) 34 ∧ (p 40).emptyPairCap=none ∧
    (∀ j, (positions 40 j).val+1∈(p 40).correctionCenters) ∧
    (∀ j z, 0≤α 40 j z) ∧ (∀ j z, j∉R 40 j z) ∧
    (∀ j z, quota 40 j z ≤
      (4*avoidedCount (p 40) ((positions 40 j).val+1) (avoidedPositions (positions 40) (R 40 j z))+2-
        (24-1-(R 40 j z).card))/3) ∧
    (∀ j, loss 40 j ≤ (∑ z, (quota 40 j z : ℚ)*α 40 j z)-
      penaltySum (p 40) ((positions 40 j).val+1) (fun z => avoidedPositions (positions 40) (R 40 j z)) (α 40 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 40) (k.val+1) true)
      (min (CachedRows.cachedA (p 40) (k.val+1) false) (CachedRows.cachedC (p 40) (k.val+1)-centerLoss (positions 40) (loss 40) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_41 : Numeric.validProfile (p 41) 34 ∧ (p 41).emptyPairCap=none ∧
    (∀ j, (positions 41 j).val+1∈(p 41).correctionCenters) ∧
    (∀ j z, 0≤α 41 j z) ∧ (∀ j z, j∉R 41 j z) ∧
    (∀ j z, quota 41 j z ≤
      (4*avoidedCount (p 41) ((positions 41 j).val+1) (avoidedPositions (positions 41) (R 41 j z))+2-
        (24-1-(R 41 j z).card))/3) ∧
    (∀ j, loss 41 j ≤ (∑ z, (quota 41 j z : ℚ)*α 41 j z)-
      penaltySum (p 41) ((positions 41 j).val+1) (fun z => avoidedPositions (positions 41) (R 41 j z)) (α 41 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 41) (k.val+1) true)
      (min (CachedRows.cachedA (p 41) (k.val+1) false) (CachedRows.cachedC (p 41) (k.val+1)-centerLoss (positions 41) (loss 41) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_42 : Numeric.validProfile (p 42) 34 ∧ (p 42).emptyPairCap=none ∧
    (∀ j, (positions 42 j).val+1∈(p 42).correctionCenters) ∧
    (∀ j z, 0≤α 42 j z) ∧ (∀ j z, j∉R 42 j z) ∧
    (∀ j z, quota 42 j z ≤
      (4*avoidedCount (p 42) ((positions 42 j).val+1) (avoidedPositions (positions 42) (R 42 j z))+2-
        (24-1-(R 42 j z).card))/3) ∧
    (∀ j, loss 42 j ≤ (∑ z, (quota 42 j z : ℚ)*α 42 j z)-
      penaltySum (p 42) ((positions 42 j).val+1) (fun z => avoidedPositions (positions 42) (R 42 j z)) (α 42 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 42) (k.val+1) true)
      (min (CachedRows.cachedA (p 42) (k.val+1) false) (CachedRows.cachedC (p 42) (k.val+1)-centerLoss (positions 42) (loss 42) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_43 : Numeric.validProfile (p 43) 34 ∧ (p 43).emptyPairCap=none ∧
    (∀ j, (positions 43 j).val+1∈(p 43).correctionCenters) ∧
    (∀ j z, 0≤α 43 j z) ∧ (∀ j z, j∉R 43 j z) ∧
    (∀ j z, quota 43 j z ≤
      (4*avoidedCount (p 43) ((positions 43 j).val+1) (avoidedPositions (positions 43) (R 43 j z))+2-
        (24-1-(R 43 j z).card))/3) ∧
    (∀ j, loss 43 j ≤ (∑ z, (quota 43 j z : ℚ)*α 43 j z)-
      penaltySum (p 43) ((positions 43 j).val+1) (fun z => avoidedPositions (positions 43) (R 43 j z)) (α 43 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 43) (k.val+1) true)
      (min (CachedRows.cachedA (p 43) (k.val+1) false) (CachedRows.cachedC (p 43) (k.val+1)-centerLoss (positions 43) (loss 43) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_44 : Numeric.validProfile (p 44) 34 ∧ (p 44).emptyPairCap=none ∧
    (∀ j, (positions 44 j).val+1∈(p 44).correctionCenters) ∧
    (∀ j z, 0≤α 44 j z) ∧ (∀ j z, j∉R 44 j z) ∧
    (∀ j z, quota 44 j z ≤
      (4*avoidedCount (p 44) ((positions 44 j).val+1) (avoidedPositions (positions 44) (R 44 j z))+2-
        (24-1-(R 44 j z).card))/3) ∧
    (∀ j, loss 44 j ≤ (∑ z, (quota 44 j z : ℚ)*α 44 j z)-
      penaltySum (p 44) ((positions 44 j).val+1) (fun z => avoidedPositions (positions 44) (R 44 j z)) (α 44 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 44) (k.val+1) true)
      (min (CachedRows.cachedA (p 44) (k.val+1) false) (CachedRows.cachedC (p 44) (k.val+1)-centerLoss (positions 44) (loss 44) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_45 : Numeric.validProfile (p 45) 34 ∧ (p 45).emptyPairCap=none ∧
    (∀ j, (positions 45 j).val+1∈(p 45).correctionCenters) ∧
    (∀ j z, 0≤α 45 j z) ∧ (∀ j z, j∉R 45 j z) ∧
    (∀ j z, quota 45 j z ≤
      (4*avoidedCount (p 45) ((positions 45 j).val+1) (avoidedPositions (positions 45) (R 45 j z))+2-
        (24-1-(R 45 j z).card))/3) ∧
    (∀ j, loss 45 j ≤ (∑ z, (quota 45 j z : ℚ)*α 45 j z)-
      penaltySum (p 45) ((positions 45 j).val+1) (fun z => avoidedPositions (positions 45) (R 45 j z)) (α 45 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 45) (k.val+1) true)
      (min (CachedRows.cachedA (p 45) (k.val+1) false) (CachedRows.cachedC (p 45) (k.val+1)-centerLoss (positions 45) (loss 45) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_46 : Numeric.validProfile (p 46) 34 ∧ (p 46).emptyPairCap=none ∧
    (∀ j, (positions 46 j).val+1∈(p 46).correctionCenters) ∧
    (∀ j z, 0≤α 46 j z) ∧ (∀ j z, j∉R 46 j z) ∧
    (∀ j z, quota 46 j z ≤
      (4*avoidedCount (p 46) ((positions 46 j).val+1) (avoidedPositions (positions 46) (R 46 j z))+2-
        (24-1-(R 46 j z).card))/3) ∧
    (∀ j, loss 46 j ≤ (∑ z, (quota 46 j z : ℚ)*α 46 j z)-
      penaltySum (p 46) ((positions 46 j).val+1) (fun z => avoidedPositions (positions 46) (R 46 j z)) (α 46 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 46) (k.val+1) true)
      (min (CachedRows.cachedA (p 46) (k.val+1) false) (CachedRows.cachedC (p 46) (k.val+1)-centerLoss (positions 46) (loss 46) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_47 : Numeric.validProfile (p 47) 34 ∧ (p 47).emptyPairCap=none ∧
    (∀ j, (positions 47 j).val+1∈(p 47).correctionCenters) ∧
    (∀ j z, 0≤α 47 j z) ∧ (∀ j z, j∉R 47 j z) ∧
    (∀ j z, quota 47 j z ≤
      (4*avoidedCount (p 47) ((positions 47 j).val+1) (avoidedPositions (positions 47) (R 47 j z))+2-
        (24-1-(R 47 j z).card))/3) ∧
    (∀ j, loss 47 j ≤ (∑ z, (quota 47 j z : ℚ)*α 47 j z)-
      penaltySum (p 47) ((positions 47 j).val+1) (fun z => avoidedPositions (positions 47) (R 47 j z)) (α 47 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 47) (k.val+1) true)
      (min (CachedRows.cachedA (p 47) (k.val+1) false) (CachedRows.cachedC (p 47) (k.val+1)-centerLoss (positions 47) (loss 47) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_48 : Numeric.validProfile (p 48) 34 ∧ (p 48).emptyPairCap=none ∧
    (∀ j, (positions 48 j).val+1∈(p 48).correctionCenters) ∧
    (∀ j z, 0≤α 48 j z) ∧ (∀ j z, j∉R 48 j z) ∧
    (∀ j z, quota 48 j z ≤
      (4*avoidedCount (p 48) ((positions 48 j).val+1) (avoidedPositions (positions 48) (R 48 j z))+2-
        (24-1-(R 48 j z).card))/3) ∧
    (∀ j, loss 48 j ≤ (∑ z, (quota 48 j z : ℚ)*α 48 j z)-
      penaltySum (p 48) ((positions 48 j).val+1) (fun z => avoidedPositions (positions 48) (R 48 j z)) (α 48 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 48) (k.val+1) true)
      (min (CachedRows.cachedA (p 48) (k.val+1) false) (CachedRows.cachedC (p 48) (k.val+1)-centerLoss (positions 48) (loss 48) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_49 : Numeric.validProfile (p 49) 34 ∧ (p 49).emptyPairCap=none ∧
    (∀ j, (positions 49 j).val+1∈(p 49).correctionCenters) ∧
    (∀ j z, 0≤α 49 j z) ∧ (∀ j z, j∉R 49 j z) ∧
    (∀ j z, quota 49 j z ≤
      (4*avoidedCount (p 49) ((positions 49 j).val+1) (avoidedPositions (positions 49) (R 49 j z))+2-
        (24-1-(R 49 j z).card))/3) ∧
    (∀ j, loss 49 j ≤ (∑ z, (quota 49 j z : ℚ)*α 49 j z)-
      penaltySum (p 49) ((positions 49 j).val+1) (fun z => avoidedPositions (positions 49) (R 49 j z)) (α 49 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 49) (k.val+1) true)
      (min (CachedRows.cachedA (p 49) (k.val+1) false) (CachedRows.cachedC (p 49) (k.val+1)-centerLoss (positions 49) (loss 49) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
