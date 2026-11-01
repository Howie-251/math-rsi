import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cachedCertificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (24-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p i) (k.val+1) true)
      (min (CachedRows.cachedA (p i) (k.val+1) false) (CachedRows.cachedC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel

theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (24-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := cachedCertificates i
  refine ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,?_⟩
  have eq : (∑k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1)))) =
      ∑k : Fin 24, min (CachedRows.cachedA (p i) (k.val+1) true)
      (min (CachedRows.cachedA (p i) (k.val+1) false) (CachedRows.cachedC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))) := by
    apply Finset.sum_congr rfl
    intro k _
    obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p i) 34 (k.val+1) valid nocap
    rw [ha,hb,hc]
  rw [eq]
  exact strict
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric.certificates
