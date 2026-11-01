import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_110 : Numeric.validProfile (p 110) 34 ∧ (p 110).emptyPairCap=none ∧
    (∀ j, (positions 110 j).val+1∈(p 110).correctionCenters) ∧
    (∀ j z, 0≤α 110 j z) ∧ (∀ j z, j∉R 110 j z) ∧
    (∀ j z, quota 110 j z ≤
      (4*avoidedCount (p 110) ((positions 110 j).val+1) (avoidedPositions (positions 110) (R 110 j z))+2-
        (24-1-(R 110 j z).card))/3) ∧
    (∀ j, loss 110 j ≤ (∑ z, (quota 110 j z : ℚ)*α 110 j z)-
      penaltySum (p 110) ((positions 110 j).val+1) (fun z => avoidedPositions (positions 110) (R 110 j z)) (α 110 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 110) (k.val+1) true)
      (min (CachedRows.cachedA (p 110) (k.val+1) false) (CachedRows.cachedC (p 110) (k.val+1)-centerLoss (positions 110) (loss 110) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_111 : Numeric.validProfile (p 111) 34 ∧ (p 111).emptyPairCap=none ∧
    (∀ j, (positions 111 j).val+1∈(p 111).correctionCenters) ∧
    (∀ j z, 0≤α 111 j z) ∧ (∀ j z, j∉R 111 j z) ∧
    (∀ j z, quota 111 j z ≤
      (4*avoidedCount (p 111) ((positions 111 j).val+1) (avoidedPositions (positions 111) (R 111 j z))+2-
        (24-1-(R 111 j z).card))/3) ∧
    (∀ j, loss 111 j ≤ (∑ z, (quota 111 j z : ℚ)*α 111 j z)-
      penaltySum (p 111) ((positions 111 j).val+1) (fun z => avoidedPositions (positions 111) (R 111 j z)) (α 111 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 111) (k.val+1) true)
      (min (CachedRows.cachedA (p 111) (k.val+1) false) (CachedRows.cachedC (p 111) (k.val+1)-centerLoss (positions 111) (loss 111) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_112 : Numeric.validProfile (p 112) 34 ∧ (p 112).emptyPairCap=none ∧
    (∀ j, (positions 112 j).val+1∈(p 112).correctionCenters) ∧
    (∀ j z, 0≤α 112 j z) ∧ (∀ j z, j∉R 112 j z) ∧
    (∀ j z, quota 112 j z ≤
      (4*avoidedCount (p 112) ((positions 112 j).val+1) (avoidedPositions (positions 112) (R 112 j z))+2-
        (24-1-(R 112 j z).card))/3) ∧
    (∀ j, loss 112 j ≤ (∑ z, (quota 112 j z : ℚ)*α 112 j z)-
      penaltySum (p 112) ((positions 112 j).val+1) (fun z => avoidedPositions (positions 112) (R 112 j z)) (α 112 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 112) (k.val+1) true)
      (min (CachedRows.cachedA (p 112) (k.val+1) false) (CachedRows.cachedC (p 112) (k.val+1)-centerLoss (positions 112) (loss 112) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_113 : Numeric.validProfile (p 113) 34 ∧ (p 113).emptyPairCap=none ∧
    (∀ j, (positions 113 j).val+1∈(p 113).correctionCenters) ∧
    (∀ j z, 0≤α 113 j z) ∧ (∀ j z, j∉R 113 j z) ∧
    (∀ j z, quota 113 j z ≤
      (4*avoidedCount (p 113) ((positions 113 j).val+1) (avoidedPositions (positions 113) (R 113 j z))+2-
        (24-1-(R 113 j z).card))/3) ∧
    (∀ j, loss 113 j ≤ (∑ z, (quota 113 j z : ℚ)*α 113 j z)-
      penaltySum (p 113) ((positions 113 j).val+1) (fun z => avoidedPositions (positions 113) (R 113 j z)) (α 113 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 113) (k.val+1) true)
      (min (CachedRows.cachedA (p 113) (k.val+1) false) (CachedRows.cachedC (p 113) (k.val+1)-centerLoss (positions 113) (loss 113) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_114 : Numeric.validProfile (p 114) 34 ∧ (p 114).emptyPairCap=none ∧
    (∀ j, (positions 114 j).val+1∈(p 114).correctionCenters) ∧
    (∀ j z, 0≤α 114 j z) ∧ (∀ j z, j∉R 114 j z) ∧
    (∀ j z, quota 114 j z ≤
      (4*avoidedCount (p 114) ((positions 114 j).val+1) (avoidedPositions (positions 114) (R 114 j z))+2-
        (24-1-(R 114 j z).card))/3) ∧
    (∀ j, loss 114 j ≤ (∑ z, (quota 114 j z : ℚ)*α 114 j z)-
      penaltySum (p 114) ((positions 114 j).val+1) (fun z => avoidedPositions (positions 114) (R 114 j z)) (α 114 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 114) (k.val+1) true)
      (min (CachedRows.cachedA (p 114) (k.val+1) false) (CachedRows.cachedC (p 114) (k.val+1)-centerLoss (positions 114) (loss 114) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_115 : Numeric.validProfile (p 115) 34 ∧ (p 115).emptyPairCap=none ∧
    (∀ j, (positions 115 j).val+1∈(p 115).correctionCenters) ∧
    (∀ j z, 0≤α 115 j z) ∧ (∀ j z, j∉R 115 j z) ∧
    (∀ j z, quota 115 j z ≤
      (4*avoidedCount (p 115) ((positions 115 j).val+1) (avoidedPositions (positions 115) (R 115 j z))+2-
        (24-1-(R 115 j z).card))/3) ∧
    (∀ j, loss 115 j ≤ (∑ z, (quota 115 j z : ℚ)*α 115 j z)-
      penaltySum (p 115) ((positions 115 j).val+1) (fun z => avoidedPositions (positions 115) (R 115 j z)) (α 115 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 115) (k.val+1) true)
      (min (CachedRows.cachedA (p 115) (k.val+1) false) (CachedRows.cachedC (p 115) (k.val+1)-centerLoss (positions 115) (loss 115) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_116 : Numeric.validProfile (p 116) 34 ∧ (p 116).emptyPairCap=none ∧
    (∀ j, (positions 116 j).val+1∈(p 116).correctionCenters) ∧
    (∀ j z, 0≤α 116 j z) ∧ (∀ j z, j∉R 116 j z) ∧
    (∀ j z, quota 116 j z ≤
      (4*avoidedCount (p 116) ((positions 116 j).val+1) (avoidedPositions (positions 116) (R 116 j z))+2-
        (24-1-(R 116 j z).card))/3) ∧
    (∀ j, loss 116 j ≤ (∑ z, (quota 116 j z : ℚ)*α 116 j z)-
      penaltySum (p 116) ((positions 116 j).val+1) (fun z => avoidedPositions (positions 116) (R 116 j z)) (α 116 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 116) (k.val+1) true)
      (min (CachedRows.cachedA (p 116) (k.val+1) false) (CachedRows.cachedC (p 116) (k.val+1)-centerLoss (positions 116) (loss 116) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_117 : Numeric.validProfile (p 117) 34 ∧ (p 117).emptyPairCap=none ∧
    (∀ j, (positions 117 j).val+1∈(p 117).correctionCenters) ∧
    (∀ j z, 0≤α 117 j z) ∧ (∀ j z, j∉R 117 j z) ∧
    (∀ j z, quota 117 j z ≤
      (4*avoidedCount (p 117) ((positions 117 j).val+1) (avoidedPositions (positions 117) (R 117 j z))+2-
        (24-1-(R 117 j z).card))/3) ∧
    (∀ j, loss 117 j ≤ (∑ z, (quota 117 j z : ℚ)*α 117 j z)-
      penaltySum (p 117) ((positions 117 j).val+1) (fun z => avoidedPositions (positions 117) (R 117 j z)) (α 117 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 117) (k.val+1) true)
      (min (CachedRows.cachedA (p 117) (k.val+1) false) (CachedRows.cachedC (p 117) (k.val+1)-centerLoss (positions 117) (loss 117) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_118 : Numeric.validProfile (p 118) 34 ∧ (p 118).emptyPairCap=none ∧
    (∀ j, (positions 118 j).val+1∈(p 118).correctionCenters) ∧
    (∀ j z, 0≤α 118 j z) ∧ (∀ j z, j∉R 118 j z) ∧
    (∀ j z, quota 118 j z ≤
      (4*avoidedCount (p 118) ((positions 118 j).val+1) (avoidedPositions (positions 118) (R 118 j z))+2-
        (24-1-(R 118 j z).card))/3) ∧
    (∀ j, loss 118 j ≤ (∑ z, (quota 118 j z : ℚ)*α 118 j z)-
      penaltySum (p 118) ((positions 118 j).val+1) (fun z => avoidedPositions (positions 118) (R 118 j z)) (α 118 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 118) (k.val+1) true)
      (min (CachedRows.cachedA (p 118) (k.val+1) false) (CachedRows.cachedC (p 118) (k.val+1)-centerLoss (positions 118) (loss 118) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_119 : Numeric.validProfile (p 119) 34 ∧ (p 119).emptyPairCap=none ∧
    (∀ j, (positions 119 j).val+1∈(p 119).correctionCenters) ∧
    (∀ j z, 0≤α 119 j z) ∧ (∀ j z, j∉R 119 j z) ∧
    (∀ j z, quota 119 j z ≤
      (4*avoidedCount (p 119) ((positions 119 j).val+1) (avoidedPositions (positions 119) (R 119 j z))+2-
        (24-1-(R 119 j z).card))/3) ∧
    (∀ j, loss 119 j ≤ (∑ z, (quota 119 j z : ℚ)*α 119 j z)-
      penaltySum (p 119) ((positions 119 j).val+1) (fun z => avoidedPositions (positions 119) (R 119 j z)) (α 119 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 119) (k.val+1) true)
      (min (CachedRows.cachedA (p 119) (k.val+1) false) (CachedRows.cachedC (p 119) (k.val+1)-centerLoss (positions 119) (loss 119) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
