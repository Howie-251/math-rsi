import Aris4Math.General.RS.OrderCounting

open Equiv
open Aris4Math.General.RS

/-- A caller states the event literally on global vertex positions. -/
theorem actual_position_caller {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    (Fintype.card {σ : Perm (Fin n) //
      (∀ a ∈ A, σ a < σ x) ∧ (∀ b ∈ B, σ x < σ b)} : ℝ) /
        n.factorial =
      ((A.card.factorial : ℝ) * B.card.factorial) /
        (A.card+B.card+1).factorial := by
  have hc : Fintype.card {σ : Perm (Fin n) //
      (∀ a ∈ A, σ a < σ x) ∧ (∀ b ∈ B, σ x < σ b)} =
      Fintype.card {σ : Perm (Fin n) // BeforeAfter A B x σ} := by
    exact @Fintype.card_congr _ _ _ _ (Equiv.refl _)
  rw [hc]
  simpa only [Fintype.card_perm, Fintype.card_fin] using
    beforeAfter_ratio A B x hAB hxA hxB

#check Aris4Math.General.RS.beforeAfter_ratio
#print axioms actual_position_caller
#print axioms Aris4Math.General.RS.card_beforeAfter
