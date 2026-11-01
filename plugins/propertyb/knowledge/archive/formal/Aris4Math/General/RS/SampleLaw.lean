import Aris4Math.General.RS.Sample

namespace Aris4Math.General.RS
open scoped BigOperators
noncomputable section
attribute [local instance] Classical.propDecidable
variable {n : ℕ}

/-- The actual joint mass of the initial colors, eligibility mask, and scan order. -/
def sampleWeight (p : ℝ) (c b : Fin n → Bool) (_σ : Equiv.Perm (Fin n)) : ℝ :=
  bernoulliWeight (1/2 : ℝ) c * bernoulliWeight p b /
    (Fintype.card (Equiv.Perm (Fin n)) : ℝ)

theorem sampleWeight_nonneg {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) : 0 ≤ sampleWeight p c b σ := by
  exact div_nonneg (mul_nonneg (bernoulliWeight_nonneg (by norm_num) (by norm_num) c)
    (bernoulliWeight_nonneg hp hp1 b)) (le_of_lt permCard_pos)

theorem sampleExpect_eq_sum (p : ℝ)
    (f : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → ℝ) :
    sampleExpect p f = ∑ c, ∑ b, ∑ σ, sampleWeight p c b σ * f c b σ := by
  unfold sampleExpect bernoulliExpect permExpect sampleWeight
  simp_rw [div_eq_mul_inv, Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr (by ext c; simp) ?_
  intro c _
  refine Finset.sum_congr (by ext b; simp) ?_
  intro b _
  simp_rw [Finset.mul_sum]
  refine Finset.sum_congr (by ext σ; simp) ?_
  intro σ _
  ring

@[simp] theorem sum_sampleWeight (p : ℝ) :
    (∑ c : Fin n → Bool, ∑ b : Fin n → Bool, ∑ σ : Equiv.Perm (Fin n),
      sampleWeight p c b σ) = 1 := by
  have h := sampleExpect_eq_sum (n := n) p (fun _ _ _ => 1)
  simpa only [sampleExpect_const, mul_one] using h.symm

end
end Aris4Math.General.RS
