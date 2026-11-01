import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.SingleLayoutApplication
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.RefinedDeletion
open Aris4Math.ThirtyFour.MixedLayoutApplication (centerLoss loss_at)
variable {n v m : ℕ} {Q : Type*} [Fintype Q]

theorem propertyB_of_single_layout (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p m) (nocap : p.emptyPairCap=none)
    (centers : ∀ j, (positions j).val+1∈p.correctionCenters)
    (R : Fin n → Q → Finset (Fin n)) (α : Fin n → Q → ℚ) (q : Fin n → Q → ℕ)
    (loss : Fin n → ℚ)
    (nonneg : ∀ j z, 0≤α j z) (avoids : ∀ j z, j∉R j z)
    (quotas : ∀ j z, q j z ≤
      (4*avoidedCount p ((positions j).val+1) (avoidedPositions positions (R j z))+2-
        (v-1-(R j z).card))/3)
    (deduction : ∀ j, loss j ≤ (∑ z, (q j z : ℚ)*α j z)-
      penaltySum p ((positions j).val+1) (fun z => avoidedPositions positions (R j z)) (α j))
    (strict : (∑ k : Fin v, min (Numeric.boundA p (k.val+1))
      (min (Numeric.boundB p (k.val+1))
        (Numeric.boundC p (k.val+1)-centerLoss positions loss (k.val+1))))<1) : PropertyB H := by
  apply ThirtyThree.CustomDeletion.propertyB_of_custom_deletion H vertices positions p real nocap
    (centerLoss positions loss)
  · intro j _
    rw [loss_at]
    exact realized_refined_deduction H vertices positions p real j (R j) (α j) (q j)
      (loss j) (nonneg j) (avoids j) (quotas j) (deduction j)
  · intro k absent
    apply Finset.sum_eq_zero
    intro j _
    have ne : (positions j).val+1≠k := by intro eq; exact absent (eq ▸ centers j)
    simp only [centerLoss,if_neg ne]
  · exact strict
end Aris4Math.ThirtyFour.SingleLayoutApplication
